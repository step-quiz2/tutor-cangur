"""
Tutor Cangur — aggregator.

Importa els quatre fitxers de nivell i exposa un únic dict PROBLEMS
i les funcions helpers per a la resta del projecte.

Per afegir problemes nous: edita ÚNICAMENT el fitxer del nivell corresponent
(problems_1eso.py, problems_2eso.py, problems_3eso.py, problems_4eso.py).
Mai editar aquest fitxer per afegir problemes.
"""

from problems_shared import ERROR_CATALOG, DEPENDENCIES  # noqa: F401
import problems_1eso
import problems_2eso
import problems_3eso
import problems_4eso

PROBLEMS: dict = {}
PROBLEMS.update(problems_1eso.PROBLEMS)
PROBLEMS.update(problems_2eso.PROBLEMS)
PROBLEMS.update(problems_3eso.PROBLEMS)
PROBLEMS.update(problems_4eso.PROBLEMS)

# ============================================================
# Helpers públics
# ============================================================
def get_problem(problem_id: str) -> dict:
    """Recupera un problema pel seu id. Retorna None si no existeix."""
    return PROBLEMS.get(problem_id)


def get_available_problems() -> list:
    """
    Llista d'ids de problemes que estan REALMENT poblats (no placeholders).
    Un problema es considera disponible si té CONTINGUT (imatge o enunciat
    de text) + resposta correcta + les 5 claus d'opcions.

    Quan el contingut és una imatge, els valors de les opcions poden ser
    None o buits (les opcions ja apareixen a la imatge; la UI mostra
    només la lletra per al marcador d'eliminació).

    La UI usa aquesta llista per al selector del sidebar; els placeholders
    no apareixen fins que s'omplen.
    """
    available = []
    for pid, p in PROBLEMS.items():
        # Contingut: imatge (fitxer) o enunciat (text)
        if not p.get("imatge") and not p.get("enunciat"):
            continue
        # Resposta obligatòria
        if p.get("resposta_correcta") not in ("A", "B", "C", "D", "E"):
            continue
        # Les 5 claus d'opcions han d'existir (valors poden ser None si hi ha imatge)
        opts = p.get("opcions") or {}
        if set(opts.keys()) != {"A", "B", "C", "D", "E"}:
            continue
        available.append(pid)
    return sorted(available)


def get_problems_by_punts(punts: int) -> list:
    """Filtra problemes disponibles per dificultat (3/4/5 punts)."""
    return [
        pid for pid in get_available_problems()
        if PROBLEMS[pid].get("punts") == punts
    ]


# ============================================================
# Validació mínima del catàleg (al carregar el mòdul)
# ============================================================
# Comprovacions defensives que es disparen quan `import problems` per
# atrapar errors d'edició al catàleg. Si alguna asserció falla, el codi
# directament no carrega; preferim petar aviat que tenir bugs subtils a
# runtime.
def _validate_catalog():
    for pid, p in PROBLEMS.items():
        # Salta placeholders (sense contingut)
        has_content = p.get("imatge") or p.get("enunciat")
        if not has_content:
            continue
        # Si hi ha contingut, la resposta és obligatòria
        rc = p.get("resposta_correcta")
        assert rc in ("A", "B", "C", "D", "E"), (
            f"Problema {pid}: resposta_correcta ha de ser una lletra A-E (és {rc!r})."
        )
        # Les 5 claus d'opcions han d'existir sempre.
        # Els VALORS poden ser None/buits quan el contingut és una imatge
        # (les opcions ja apareixen a la imatge).
        opts = p.get("opcions") or {}
        assert set(opts.keys()) == {"A", "B", "C", "D", "E"}, (
            f"Problema {pid}: 'opcions' ha de tenir exactament les claus A-B-C-D-E."
        )
        # Si el contingut és text (sense imatge), les opcions han de tenir text.
        if p.get("enunciat") and not p.get("imatge"):
            for L in ("A", "B", "C", "D", "E"):
                assert opts.get(L), (
                    f"Problema {pid}: enunciat de text present però opció {L} buida."
                )
        # comentaris_distractors no pot incloure la lletra correcta.
        cd = p.get("comentaris_distractors") or {}
        assert rc not in cd, (
            f"Problema {pid}: comentaris_distractors NO ha de tenir la lletra correcta {rc}."
        )
        # Errors típics declarats han d'existir al catàleg.
        for err in p.get("errors_típics", []):
            assert err in ERROR_CATALOG, (
                f"Problema {pid}: error típic {err!r} no existeix a ERROR_CATALOG."
            )
        # pista_inicial, si està present, ha de ser una string no-buida o None.
        pi = p.get("pista_inicial")
        if pi is not None:
            assert isinstance(pi, str) and pi.strip(), (
                f"Problema {pid}: 'pista_inicial' ha de ser una string no-buida o None "
                f"(és {pi!r})."
            )


_validate_catalog()


if __name__ == "__main__":
    # Inspecció ràpida del catàleg: útil per veure quants problemes
    # estan poblats i quants encara són placeholders.
    available = get_available_problems()
    total = len(PROBLEMS)
    print(f"Problemes al catàleg: {total}")
    print(f"Problemes disponibles (poblats): {len(available)}")
    print(f"Placeholders pendents: {total - len(available)}")
    print()
    for pts in (3, 4, 5):
        ids = get_problems_by_punts(pts)
        print(f"  {pts} punts: {len(ids)} disponibles → {ids}")
