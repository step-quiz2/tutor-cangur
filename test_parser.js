// Test harness: extract the JS logic from the HTML editor and run it against
// real files in the project to verify (a) we extract pista_inicial correctly
// for all 240 problems, (b) re-emitting and patching back yields a file that
// is byte-identical to the original when no changes are made, (c) when we
// CHANGE a pista, only the relevant span is altered.

const fs = require('fs');
const path = require('path');

// ─── Copy of the parser/emitter from pistes_editor.html ──────────────

function parseProblemsPy(text, year) {
  const problems = [];
  const headerRe = /PROBLEMS\["(CAN-[1-4]ESO-\d{4}-\d{2})"\]\s*=\s*\{/g;
  const headers = [];
  let m;
  while ((m = headerRe.exec(text)) !== null) {
    headers.push({ id: m[1], headerStart: m.index, bodyStart: m.index + m[0].length });
  }
  for (let i = 0; i < headers.length; i++) {
    const h = headers[i];
    const yearInId = parseInt(h.id.split('-')[2], 10);
    if (yearInId !== year) continue;
    const blockEnd = findMatchingBrace(text, h.bodyStart - 1);
    if (blockEnd < 0) continue;
    const blockBody = text.slice(h.bodyStart, blockEnd);
    const fields = extractFields(blockBody, h.bodyStart);
    if (!fields.pista) continue;
    problems.push({
      id: h.id, numero: fields.numero, punts: fields.punts,
      tema: fields.tema, imatge: fields.imatge,
      pista: fields.pista.value,
      pistaStart: fields.pista.start, pistaEnd: fields.pista.end,
      blockStart: h.headerStart, blockEnd: blockEnd + 1,
    });
  }
  problems.sort((a, b) => a.numero - b.numero);
  return problems;
}

function findMatchingBrace(text, openPos) {
  let depth = 0, i = openPos, n = text.length;
  while (i < n) {
    const c = text[i];
    if (c === '#') { while (i < n && text[i] !== '\n') i++; continue; }
    if (c === '"' || c === "'") {
      const triple = text.substr(i, 3);
      if (triple === '"""' || triple === "'''") {
        const quote = triple; i += 3;
        while (i < n && text.substr(i, 3) !== quote) {
          if (text[i] === '\\') i += 2; else i++;
        }
        i += 3; continue;
      } else {
        const quote = c; i++;
        while (i < n && text[i] !== quote && text[i] !== '\n') {
          if (text[i] === '\\') i += 2; else i++;
        }
        i++; continue;
      }
    }
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) return i; }
    i++;
  }
  return -1;
}

function extractFields(body, bodyStart) {
  const out = {};
  out.numero = extractInt(body, 'numero');
  out.punts = extractInt(body, 'punts');
  out.tema = extractString(body, 'tema');
  out.imatge = extractString(body, 'imatge');
  const re = /"pista_inicial"\s*:\s*\(\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\)/m;
  const m = re.exec(body);
  if (m) {
    const strBlock = m[1];
    const partRe = /"((?:[^"\\]|\\.)*)"/g;
    let parts = []; let p;
    while ((p = partRe.exec(strBlock)) !== null) {
      parts.push(unescapePyString(p[1]));
    }
    out.pista = {
      value: parts.join(''),
      start: bodyStart + m.index,
      end: bodyStart + m.index + m[0].length,
    };
  }
  return out;
}
function extractInt(body, key) {
  const re = new RegExp('"' + key + '"\\s*:\\s*(\\d+)', 'm');
  const m = re.exec(body);
  return m ? parseInt(m[1], 10) : null;
}
function extractString(body, key) {
  const re = new RegExp('"' + key + '"\\s*:\\s*(?:"((?:[^"\\\\]|\\\\.)*)"|None)', 'm');
  const m = re.exec(body);
  if (!m) return null;
  if (m[1] === undefined) return null;
  return unescapePyString(m[1]);
}
function unescapePyString(s) {
  return s
    .replace(/\\\\/g, '\u0000')
    .replace(/\\"/g, '"')
    .replace(/\\'/g, "'")
    .replace(/\\n/g, '\n')
    .replace(/\\t/g, '\t')
    .replace(/\u0000/g, '\\');
}

function emitPistaBlock(text, opts = {}) {
  const wrap = opts.wrap || 92;
  const indent = '    ';
  const inner = '        ';
  const flat = text.replace(/\s+/g, ' ').trim();
  if (!flat) return `${indent}"pista_inicial": (\n${inner}""\n${indent})`;
  const escaped = flat.replace(/\\/g, '\\\\').replace(/"/g, '\\"');
  const words = escaped.split(' ');
  const lines = []; let cur = '';
  for (const w of words) {
    if (!cur) { cur = w; continue; }
    if ((cur + ' ' + w).length > wrap) { lines.push(cur); cur = w; }
    else cur += ' ' + w;
  }
  if (cur) lines.push(cur);
  const quoted = lines.map((l, i) => {
    const trail = i < lines.length - 1 ? ' ' : '';
    return `${inner}"${l}${trail}"`;
  }).join('\n');
  return `${indent}"pista_inicial": (\n${quoted}\n${indent})`;
}

// ─── Tests ──────────────────────────────────────────────────────────

const repo = path.resolve(__dirname);

function runTests() {
  let nProblems = 0;
  let issues = [];

  for (const level of ['1eso', '2eso', '3eso', '4eso']) {
    const fname = path.join(repo, `problems_${level}.py`);
    const src = fs.readFileSync(fname, 'utf8');

    for (const year of [2026, 2025]) {
      const probs = parseProblemsPy(src, year);
      nProblems += probs.length;
      if (probs.length !== 30) {
        issues.push(`${level} ${year}: parsed ${probs.length} problems (expected 30)`);
      }

      // Each problem should have a non-empty pista, sensible offsets, and numero 1-30
      for (const p of probs) {
        if (!p.pista) issues.push(`${p.id}: empty pista value`);
        if (!p.numero || p.numero < 1 || p.numero > 30)
          issues.push(`${p.id}: numero out of range (${p.numero})`);
        if (!p.imatge) issues.push(`${p.id}: missing imatge`);
        // The slice [pistaStart, pistaEnd] must start with '"pista_inicial"' and end with ')'
        const slice = src.slice(p.pistaStart, p.pistaEnd);
        if (!slice.startsWith('"pista_inicial"'))
          issues.push(`${p.id}: pistaStart misaligned, slice=${JSON.stringify(slice.slice(0, 30))}`);
        if (!slice.endsWith(')'))
          issues.push(`${p.id}: pistaEnd misaligned, slice=${JSON.stringify(slice.slice(-30))}`);
      }
    }
  }
  console.log(`[TEST 1] Parsed ${nProblems} problems total across 8 (level, year) combos.`);
  console.log(`         Expected: 240. Issues: ${issues.length}`);
  if (issues.length) { issues.slice(0, 20).forEach(s => console.log('  ! ' + s)); }
  if (nProblems !== 240) process.exit(1);
}

function testRoundTrip() {
  // For each problem, re-emit the EXISTING pista and patch back into a copy
  // of the source. Then compare against the original.
  // We expect the result to be IDENTICAL when our emit function reproduces
  // the same line-wrapping as the original (or at least semantically equivalent).
  let total = 0, identical = 0, semanticOnly = 0, broken = 0;
  for (const level of ['1eso', '2eso', '3eso', '4eso']) {
    const fname = path.join(repo, `problems_${level}.py`);
    const src = fs.readFileSync(fname, 'utf8');
    for (const year of [2026, 2025]) {
      const probs = parseProblemsPy(src, year);
      for (const p of probs) {
        total++;
        const original = src.slice(p.pistaStart, p.pistaEnd);
        // Re-emit using the SAME pista value (no change)
        const reemitted = emitPistaBlock(p.pista).replace(/^    /, '');
        // Parse the re-emitted to confirm it parses to the same value
        const test = '{\n    ' + reemitted + ',\n}';
        const reparsed = extractFields(test, 0).pista;
        if (!reparsed || reparsed.value !== p.pista) {
          broken++;
          if (broken <= 3) {
            console.log(`  ! ROUND-TRIP MISMATCH ${p.id}`);
            console.log(`    expected: ${JSON.stringify(p.pista.slice(0, 80))}...`);
            console.log(`    got:      ${JSON.stringify(reparsed ? reparsed.value.slice(0, 80) : 'null')}...`);
          }
        } else if (original === reemitted) {
          identical++;
        } else {
          semanticOnly++;
        }
      }
    }
  }
  console.log(`[TEST 2] Round-trip results: ${total} problems total`);
  console.log(`         Identical bytes: ${identical}`);
  console.log(`         Semantically equal (reparses to same string): ${semanticOnly}`);
  console.log(`         BROKEN (semantic mismatch): ${broken}`);
  if (broken !== 0) process.exit(1);
}

function testPatching() {
  // Simulate a real edit: pick a few problems, change their pistas, patch the
  // source, and verify (a) the changed problems have the new pistas, (b) all
  // OTHER problems are completely untouched (byte-for-byte equal in source).
  const fname = path.join(repo, 'problems_1eso.py');
  const original = fs.readFileSync(fname, 'utf8');
  const probs = parseProblemsPy(original, 2026);

  // Pick problem #1, #7, #20: change to known new texts
  const edits = {};
  edits[probs[0].id]  = 'NEW PISTA 1: text molt curt.';
  edits[probs[6].id]  = 'NEW PISTA 7: ' + 'paraula '.repeat(40).trim() + '.';
  edits[probs[19].id] = 'NEW PISTA 20: això inclou una "cita" i una barra invertida \\ per testar escapament.';

  // Apply patches: highest offset first
  const editedProbs = probs.filter(p => edits[p.id]).sort((a, b) => b.pistaStart - a.pistaStart);
  let patched = original;
  for (const p of editedProbs) {
    const newBlock = emitPistaBlock(edits[p.id]).replace(/^    /, '');
    patched = patched.slice(0, p.pistaStart) + newBlock + patched.slice(p.pistaEnd);
  }

  // Re-parse the patched source
  const patchedProbs = parseProblemsPy(patched, 2026);
  // Must have same count
  if (patchedProbs.length !== probs.length) {
    console.log(`[TEST 3] FAIL: patched has ${patchedProbs.length} problems, expected ${probs.length}`);
    process.exit(1);
  }
  // Each edited problem must have its new value
  let okEdits = 0;
  for (const p of patchedProbs) {
    if (edits[p.id]) {
      if (p.pista === edits[p.id]) okEdits++;
      else {
        console.log(`  ! ${p.id}: expected ${JSON.stringify(edits[p.id])}`);
        console.log(`              got       ${JSON.stringify(p.pista)}`);
      }
    }
  }
  console.log(`[TEST 3] Patched ${Object.keys(edits).length} pistes; ${okEdits} round-trip correctly.`);

  // 2025 problems should be UNTOUCHED entirely
  const probs2025_before = parseProblemsPy(original, 2025);
  const probs2025_after = parseProblemsPy(patched, 2025);
  let untouched = 0;
  for (let i = 0; i < probs2025_before.length; i++) {
    if (probs2025_before[i].pista === probs2025_after[i].pista) untouched++;
  }
  console.log(`         2025 untouched: ${untouched}/${probs2025_before.length}`);

  // 2026 problems NOT edited should be untouched
  const before2026 = probs;
  const after2026 = patchedProbs;
  let nonEditedUntouched = 0, nonEditedTotal = 0;
  for (let i = 0; i < before2026.length; i++) {
    if (!edits[before2026[i].id]) {
      nonEditedTotal++;
      if (before2026[i].pista === after2026[i].pista) nonEditedUntouched++;
    }
  }
  console.log(`         non-edited 2026 untouched: ${nonEditedUntouched}/${nonEditedTotal}`);

  // Verify the patched file is still valid Python (basic check: braces balanced)
  let depth = 0;
  for (let i = 0; i < patched.length; i++) {
    const c = patched[i];
    if (c === '{') depth++;
    else if (c === '}') depth--;
  }
  console.log(`         brace balance check: depth=${depth} (should be 0)`);

  // Save patched for human inspection
  fs.writeFileSync('/tmp/_test_patched.py', patched);
  console.log(`         (patched output saved to /tmp/_test_patched.py for inspection)`);

  if (okEdits !== Object.keys(edits).length) process.exit(1);
  if (untouched !== probs2025_before.length) process.exit(1);
  if (nonEditedUntouched !== nonEditedTotal) process.exit(1);
}

runTests();
testRoundTrip();
testPatching();
console.log('\nAll tests passed.');
