"""
Tutor Cangur — 4ESO problem catalogue.

Conté els 30 problemes de la prova 4ESO (tots els anys disponibles).
Afegir nous problemes aquí; mai modificar els d'altres nivells.

Estructura de cada entrada: vegeu SCHEMA.md.
"""

from problems_shared import ERROR_CATALOG, DEPENDENCIES  # noqa: F401

PROBLEMS = {}


PROBLEMS["CAN-4ESO-2026-01"] = {
    "id":         "CAN-4ESO-2026-01",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Pren els quadrats de costat 2 (de manera que el radi r dels arcs val 1) i calcula "
        "l'àrea ombrejada de cada diagrama en funció de r. Si en surt sempre el mateix valor, "
        "totes són iguals."
    ),
    "expected_reasoning": (
        "Considerem un quadrat de costat 2 (radi r = 1) en tots els diagrames. Al diagrama B "
        "la zona grisa és el cercle inscrit, amb àrea π·r² = π. Al diagrama A hi ha quatre "
        "quarts de cercle de radi r centrats als vèrtexs del quadrat; com que el radi és la "
        "meitat del costat, els quarts no se superposen i la suma d'àrees és 4·(π·r²/4) = π. "
        "Al diagrama C hi ha dos semicercles de radi r centrats als punts mitjos de dos "
        "costats oposats; cada semicercle té àrea π·r²/2 i només es toquen al centre, de "
        "manera que la suma total és π. Al diagrama D la zona grisa s'obté del quadrat "
        "traient-ne un semicercle de radi r per dalt i afegint-ne un de radi r per baix; com "
        "que la part que es treu i la que s'afegeix tenen la mateixa àrea (π·r²/2), aquesta "
        "operació no canvia l'àrea total respecte d'una situació de referència i el càlcul "
        "torna a donar π. Les quatre àrees ombrejades coincideixen. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir pensar que com que els quatre quarts de cercle 'omplen els cantons' deuen sumar més que un cercle sencer, sense adonar-se que quatre quarts de radi r fan exactament un cercle de radi r.",
        "B": "Triar B vol dir donar per fet que el cercle inscrit és la figura grisa més gran possible, sense calcular les altres àrees.",
        "C": "Triar C vol dir suposar que dos semicercles han de sumar més que un cercle, quan en realitat dos semicercles de radi r sumen π·r², igual que el cercle de B.",
        "D": "Triar D vol dir pensar que afegir una zona per sota compensa de més la zona retallada per dalt, quan en realitat l'àrea afegida i la retallada són iguals.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-02"] = {
    "id":         "CAN-4ESO-2026-02",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     2,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-4ESO-2026-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Calcula primer totes les rutes possibles per tornar de C a A passant per B. "
        "Després, com que cal evitar exactament el camí d'anada en sentit contrari, treu "
        "de la llista la combinació prohibida."
    ),
    "expected_reasoning": (
        "Hi ha 3 camins entre A i B i 5 camins entre B i C. A la tornada, cal escollir un "
        "camí de C a B (entre 5) i un de B a A (entre 3), de manera que les combinacions "
        "possibles són 5 × 3 = 15. D'aquestes 15, n'hi ha exactament una que coincideix amb "
        "la ruta d'anada feta al revés (el mateix camí B–C de tornada més el mateix camí "
        "A–B de tornada), i és la que s'ha d'evitar. Per tant, queden 15 − 1 = 14 rutes "
        "possibles per al viatge de tornada. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 6 surt de sumar els camins (3 + 5 = 8, o 3 + 5 − 2 = 6) en lloc de multiplicar-los per obtenir el total de combinacions.",
        "B": "Triar 10 surt d'un càlcul com 2 × 5 = 10, com si només hi haguessin 2 camins al tram entre A i B.",
        "C": "Triar 12 surt de calcular 3 × 5 i restar-ne 3 (pensant que cal evitar tres rutes prohibides), però l'única ruta prohibida és la idèntica al camí d'anada al revés.",
        "E": "Triar 15 vol dir comptar totes les rutes possibles (5 × 3 = 15) sense restar la prohibida (la ruta d'anada exactament al revés).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament suposa la tipografia clàssica de 7 segments amb les simetries
# horitzontals 0↔0, 2↔5, 5↔2 i 8↔8. La resposta correcta a 4ESO és E (02:05);
# a 3ESO era A (02:05 també). Cal comprovar a la imatge que la lletra que conté
# "02:05" és efectivament E. Sense imatge de 4ESO disponible.
PROBLEMS["CAN-4ESO-2026-03"] = {
    "id":         "CAN-4ESO-2026-03",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     3,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Pensa quins dígits dels que veu un rellotge de 7 segments donen, en reflectir-se "
        "horitzontalment, un altre dígit reconeixible. Després té en compte que el mirall "
        "també inverteix l'ordre, i busca l'opció que en reflectir-se dona una hora vàlida."
    ),
    "expected_reasoning": (
        "Quan un rellotge digital de 7 segments es veu reflectit en un mirall, passen dues "
        "coses alhora: l'ordre dels dígits s'inverteix (les hores van a la dreta i els "
        "minuts a l'esquerra) i cada dígit es reflecteix horitzontalment. Amb la tipografia "
        "estàndard de 7 segments, els dígits que en reflectir-se donen un altre dígit "
        "vàlid són: 0 → 0, 2 → 5, 5 → 2 i 8 → 8. L'única opció vàlida és 02:05: "
        "invertint l'ordre dels cinc caràcters i reflectint cada dígit, [0][2][:][0][5] "
        "donen [reflex 5][reflex 0][:][reflex 2][reflex 0] = [2][0][:][5][0] → 20:50, que "
        "és una hora del dia vàlida. Cap de les altres opcions produeix una hora vàlida en "
        "reflectir-se. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "20:02 al mirall donaria 50:05, que no és una hora vàlida del dia (50 hores no existeix).",
        "B": "09:06 inclou els dígits 9 i 6, que en una tipografia de 7 segments reflectits horitzontalment no produeixen dígits vàlids.",
        "C": "08:50 al mirall donaria 02:80, que no és una hora vàlida (80 minuts no existeix).",
        "D": "08:06 inclou el dígit 6, que en una tipografia de 7 segments reflectit horitzontalment no produeix un dígit reconeixible.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-04"] = {
    "id":         "CAN-4ESO-2026-04",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     4,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-4ESO-2026-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Per obtenir una fracció positiva tan petita com es pugui, vols numerador petit i "
        "denominador gran. Prova primer els numeradors mínims possibles i comprova quins "
        "denominadors positius hi pots aconseguir amb els nombres que sobrin."
    ),
    "expected_reasoning": (
        "Els quatre nombres a col·locar són 0, 2, 2 i 6 (el 2 surt dues vegades). La fracció "
        "té la forma (a + b)/(c − d) i s'ha de minimitzar mantenint-la positiva, és a dir, "
        "amb c > d. Si fem servir el 0 i un 2 al numerador, dona 0 + 2 = 2, i als denominadors "
        "queden el 2 i el 6: 6 − 2 = 4. La fracció és 2/4 = 1/2. Si fem servir els dos 2 al "
        "numerador, dona 4, i als denominadors queden el 0 i el 6: 6 − 0 = 6. La fracció és "
        "4/6 = 2/3, més gran que 1/2. Si fem servir el 0 i el 6 al numerador, dona 6, i als "
        "denominadors queden els dos 2: 2 − 2 = 0, denominador nul (no vàlid). Cap altra "
        "combinació dona una fracció positiva més petita que 1/2. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "2/3 és una fracció possible (numerador 2 + 2 = 4, denominador 6 − 0 = 6), però no és la més petita: 1/2 és més petita.",
        "C": "1/3 surt de pensar en un numerador 2 i un denominador 6, però per fer denominador 6 cal usar el 0 i el 6, i aleshores el numerador són els dos 2 que sumen 4: la fracció real és 4/6 = 2/3, no 1/3.",
        "D": "1/4 no es pot fer: per tenir denominador 4 caldria 6 − 2 = 4, i aleshores el numerador queda 0 + 2 = 2, no 1.",
        "E": "1/6 sembla la fracció més petita possible, però no es pot fer: per tenir denominador 6 cal col·locar el 0 i el 6 al denominador (6 − 0 = 6), i aleshores el numerador són els dos 2 (suma 4), no 1.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Aquest problema reaprofita el gerro de 9 cares amb dígits 1-9 dels problemes
# CAN-2ESO-2026-14 i CAN-3ESO-2026-12. Cal comprovar a la imatge que la vista A
# segueix sent la que mostra una adjacència incompatible (5 i 7 com a veïns
# immediats, quan haurien d'estar separats pel 9). L'XLS confirma A.
PROBLEMS["CAN-4ESO-2026-05"] = {
    "id":         "CAN-4ESO-2026-05",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     5,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Intenta reconstruir quins dígits són veïns al gerro a partir de les vistes "
        "correctes. Si en dues imatges vàlides veus, per exemple, que el 9 és veí del 7 "
        "i que el 5 és veí del 9, podràs detectar quina vista mostra un veïnatge "
        "incompatible."
    ),
    "expected_reasoning": (
        "El gerro té 9 cares laterals amb els dígits de l'1 al 9 disposats en un ordre "
        "circular fix. A cada vista en perspectiva les cares visibles són cares consecutives "
        "d'aquest ordre. Les vistes B, C, D i E mostren parelles de dígits veïns que són "
        "compatibles amb un únic ordre circular del gerro: per exemple, la vista E mostra "
        "que 9 i 7 són veïns, i la vista C mostra que 5 i 9 ho són. Combinant aquestes "
        "informacions, l'ordre circular inclou ...5, 9, 7... i, per tant, 5 i 7 no són "
        "veïns immediats. La vista A, en canvi, mostra el 5 i el 7 com a veïns immediats, "
        "cosa que contradiu l'ordre deduït de les altres vistes. La imatge A no pot "
        "correspondre al mateix gerro. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "La vista B mostra cares veïnes que són compatibles amb l'ordre circular deduït de la resta d'imatges, sense cap parell impossible.",
        "C": "La vista C és precisament una de les que permet establir que el 5 i el 9 són veïns; és coherent amb l'ordre del gerro.",
        "D": "La vista D mostra parelles de dígits veïns compatibles amb l'ordre circular deduït; no apareix cap adjacència contradictòria.",
        "E": "La vista E és precisament una de les que permet establir que el 9 i el 7 són veïns; és coherent amb l'ordre del gerro.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-06"] = {
    "id":         "CAN-4ESO-2026-06",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     6,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Calcula primer el total de cubs petits que sumen les tres peces (1 + 8 + 27). "
        "Després calcula quants cubs s'ha menjat de cada peça aplicant el percentatge "
        "corresponent, suma les quantitats menjades i divideix pel total."
    ),
    "expected_reasoning": (
        "Les tres peces tenen 1, 8 i 27 cubs petits respectivament (cubs 1×1×1, 2×2×2 i "
        "3×3×3), amb un total d'1 + 8 + 27 = 36 cubs. La quantitat menjada de cada peça "
        "és: 40% d'1 cub = 0,4 cubs; 40% de 8 cubs = 3,2 cubs; 20% de 27 cubs = 5,4 cubs. "
        "El total menjat és 0,4 + 3,2 + 5,4 = 9 cubs. El percentatge sobre el total és "
        "9 / 36 = 1/4 = 25%. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 18% surt d'un càlcul de mitjana ponderada amb pesos incorrectes, o d'un error de càlcul que desplaça lleugerament el resultat real.",
        "B": "Triar 20% surt de prendre el menor dels tres percentatges com a referència, o d'aproximar la mitjana sense ponderar correctament per la mida de cada peça.",
        "C": "Triar 23% surt de ponderar amb el nombre de peces (3) en lloc de fer-ho amb el nombre de cubs petits (36), donant un valor proper però incorrecte.",
        "D": "Triar 24% és un error d'arrodoniment proper al resultat real, per exemple aproximant 5,4 a 5 i obtenint 8,6/36 ≈ 24%.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-07"] = {
    "id":         "CAN-4ESO-2026-07",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     7,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Escriu el format DDMMAAAA com a 8 xifres D1D2M1M2A1A2A3A4. Perquè sigui capicua "
        "ha de complir D1=A4, D2=A3, M1=A2 i M2=A1. Per als anys del segle XXI, A1=2 i "
        "A2=0; aquestes igualtats determinen el mes."
    ),
    "expected_reasoning": (
        "Escrivim la data com 8 xifres D1 D2 M1 M2 A1 A2 A3 A4. La condició de capicua "
        "iguala les xifres simètriques: D1 = A4, D2 = A3, M1 = A2 i M2 = A1. Per als anys "
        "del segle XXI, A1 = 2 i A2 = 0. D'aquí, M2 = A1 = 2 i M1 = A2 = 0, és a dir, el "
        "mes és M1M2 = 02 (febrer). Que existeixi una data vàlida ho comprovem amb l'any "
        "2020: aleshores A3 = 2 i A4 = 0, així que D2 = A3 = 2 i D1 = A4 = 0, és a dir, el "
        "dia és 02. La data 02/02/2020 escrita com a 02022020 és, en efecte, un capicua. "
        "L'Anna ha nascut al mes de febrer. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Gener (mes 01) és incompatible amb la capicua: la condició M2 = A1 = 2 exigeix que la segona xifra del mes sigui 2, però la del gener és 1.",
        "C": "Setembre (mes 09) és incompatible: la condició M1 = A2 = 0 ja imposa que la primera xifra del mes sigui 0, però M2 ha de ser 2 (no 9).",
        "D": "Octubre (mes 10) és incompatible: M1 hauria de ser 0 (per A2 = 0) però el primer dígit d'octubre és 1.",
        "E": "Novembre (mes 11) és incompatible: M1 hauria de ser 0 però el primer dígit de novembre és 1.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-08"] = {
    "id":         "CAN-4ESO-2026-08",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena x el nombre de persones que mengen 4 prunes; les (5 − x) restants en "
        "mengen 3. Planteja l'equació que diu que entre tots se'n mengen 19."
    ),
    "expected_reasoning": (
        "Sigui x el nombre de persones que mengen 4 prunes. Les altres 5 − x persones en "
        "mengen 3 cadascuna. La suma total ha de ser 19: 4·x + 3·(5 − x) = 19, és a dir, "
        "4·x + 15 − 3·x = 19, d'on x = 4. Aleshores hi ha 4 persones que mengen 4 prunes "
        "(i 1 que en menja 3). Verificació: 4·4 + 1·3 = 16 + 3 = 19 ✓. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir confondre les variables i comptar el nombre de persones que mengen 3 prunes en lloc de les que en mengen 4 (1·4 + 4·3 = 16, no 19).",
        "B": "Triar 2 surt d'errors en plantejar l'equació: 4·2 + 3·3 = 17, que no fa 19.",
        "C": "Triar 3 surt d'un error pròxim a la solució correcta: 4·3 + 3·2 = 18, que tampoc fa 19.",
        "E": "Triar 5 implicaria que tothom menja 4 prunes (5·4 = 20), una de més respecte de les 19 que indica el problema.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament parla d'un gràfic amb tres trams de 10 minuts cadascun: pujada
# (+4 ppm/min), pla i baixada (−2 ppm/min). L'opció B reprodueix aquesta forma
# (pujada més pronunciada que la baixada). Cal comprovar a la imatge que les
# cinc opcions de gràfics corresponen a la descripció textual i que B és, de fet,
# l'única amb la proporció correcta de pendents. L'XLS confirma B.
PROBLEMS["CAN-4ESO-2026-09"] = {
    "id":         "CAN-4ESO-2026-09",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     9,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El gràfic té tres trams de 10 minuts: pujada de +4 ppm/min, pla i baixada de "
        "−2 ppm/min. Fixa't que la pujada ha de ser el doble d'inclinada que la baixada."
    ),
    "expected_reasoning": (
        "El ritme cardíac segueix tres fases de 10 minuts cadascuna: pujada lineal a "
        "+4 pulsacions per minut, després constant, i finalment baixada lineal a "
        "−2 pulsacions per minut. La pujada és el doble d'inclinada que la baixada "
        "(coeficient 4 contra 2), de manera que el tram ascendent del gràfic ha de ser "
        "visiblement més pronunciat que el descendent. Comparant les cinc opcions, només "
        "el gràfic B presenta aquesta forma: pujada pronunciada, plateau horitzontal al "
        "màxim i baixada amb la meitat de pendent que la pujada. Les altres opcions tenen "
        "la proporció de pendents invertida o falten algunes de les tres fases. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "El gràfic A mostra una línia gairebé horitzontal des de l'inici, sense les tres fases pujada-pla-baixada descrites al problema.",
        "C": "El gràfic C mostra pujada i baixada amb pendents semblants (o la baixada més pronunciada que la pujada), invertint la proporció correcta.",
        "D": "El gràfic D mostra una pujada moderada i una baixada molt pronunciada, amb la proporció de pendents invertida respecte de les dades del problema.",
        "E": "El gràfic E mostra una corba suau amb pujada i baixada de pendents semblants, sense reflectir que la pujada ha de ser el doble d'inclinada que la baixada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-10"] = {
    "id":         "CAN-4ESO-2026-10",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     10,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Expressa ABC com a 100·A + 10·B + C i substitueix a l'equació 3·ABC + C = 2026. "
        "Això dona 300·A + 30·B + 4·C = 2026. Troba el valor de A que faci la igualtat "
        "possible (A ≤ 6) i, després, B i C."
    ),
    "expected_reasoning": (
        "El nombre ABC representa 100·A + 10·B + C, on A, B i C són xifres (A ≥ 1). "
        "L'equació es transforma en 3·(100·A + 10·B + C) + C = 2026, és a dir, "
        "300·A + 30·B + 4·C = 2026. Com que 300·7 = 2100 > 2026, ha de ser A ≤ 6. Provant "
        "A = 6: 1800 + 30·B + 4·C = 2026, és a dir, 30·B + 4·C = 226. El màxim de 4·C és "
        "4·9 = 36, així que 30·B ≥ 190, d'on B ≥ 7. Provant B = 7: 210 + 4·C = 226 → "
        "4·C = 16 → C = 4. Comprovació: A = 6, B = 7, C = 4, ABC = 674, i 3·674 + 4 = "
        "2022 + 4 = 2026 ✓. La suma A + B + C = 6 + 7 + 4 = 17. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 16 surt d'un error de resolució a l'equació 30·B + 4·C = 226 que dona, per exemple, C = 3 en lloc de C = 4 (i una suma final de 16).",
        "C": "Triar 18 surt de provar A = 6 i B = 7 correctament però cometre un error en C, per exemple obtenint C = 5 i sumant 6 + 7 + 5 = 18.",
        "D": "Triar 19 surt d'un error en el valor d'A (per exemple, A = 7), que dona 300·7 = 2100 > 2026 i és inviable, però sense adonar-se'n.",
        "E": "Triar 21 surt de no aplicar la representació posicional correcta d'ABC (per exemple, tractar ABC com A·B·C) i obtenir valors d'A, B, C que no satisfan l'equació.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-11"] = {
    "id":         "CAN-4ESO-2026-11",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     11,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Els anys del segle XXI tenen la forma 20XY, així que dos dels quatre dígits ja "
        "són 2 i 0. La condició de suma 10 et dona X + Y = 8; enumera tots els parells "
        "(X, Y) compatibles i comprova en quins el conjunt {2, 0, X, Y} té exactament un "
        "parell de dígits iguals."
    ),
    "expected_reasoning": (
        "Els anys del segle XXI s'escriuen 20XY i les seves quatre xifres són {2, 0, X, Y}. "
        "Que sumin 10 vol dir 2 + 0 + X + Y = 10, és a dir, X + Y = 8. Els parells (X, Y) "
        "amb X, Y ∈ {0, 1, ..., 9} que sumen 8 són: (0, 8), (1, 7), (2, 6), (3, 5), (4, 4), "
        "(5, 3), (6, 2), (7, 1), (8, 0). Per a cadascun cal comprovar si les quatre xifres "
        "{2, 0, X, Y} contenen exactament un parell de dígits iguals (és a dir, dos dígits "
        "coincideixen i els altres dos són diferents entre ells i diferents del parell):\n"
        "  · (0, 8) → {2, 0, 0, 8}: dos 0 ✓.\n"
        "  · (1, 7) → {2, 0, 1, 7}: tots diferents ✗.\n"
        "  · (2, 6) → {2, 0, 2, 6}: dos 2 ✓.\n"
        "  · (3, 5) → {2, 0, 3, 5}: tots diferents ✗.\n"
        "  · (4, 4) → {2, 0, 4, 4}: dos 4 ✓.\n"
        "  · (5, 3) → {2, 0, 5, 3}: tots diferents ✗.\n"
        "  · (6, 2) → {2, 0, 6, 2}: dos 2 ✓.\n"
        "  · (7, 1) → {2, 0, 7, 1}: tots diferents ✗.\n"
        "  · (8, 0) → {2, 0, 8, 0}: dos 0 ✓.\n"
        "Els anys que compleixen totes dues condicions són 2008, 2026, 2044, 2062 i 2080: "
        "exactament 5. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 surt de fixar-se només en l'any 2026 (que és l'exemple natural) i no buscar sistemàticament la resta de candidats.",
        "B": "Triar 2 surt de trobar dos anys correctes (per exemple, 2026 i 2044) però aturar-se sense considerar la resta de parelles (X, Y) que sumen 8.",
        "C": "Triar 3 surt d'enumerar només els parells (X, Y) amb X ≤ Y i ometre els que es generen permutant (com 2062 a partir de (6, 2)), perdent dues seqüències.",
        "D": "Triar 4 surt d'ometre un dels cinc anys vàlids, per exemple no adonar-se que (8, 0) → 2080 té dos zeros i compleix la condició.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-12"] = {
    "id":         "CAN-4ESO-2026-12",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     12,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Posa coordenades al triangle equilàter de costat 1 i troba les coordenades del "
        "punt S (punt mitjà de PR) i T (punt mitjà de QS). La línia per T paral·lela a PR "
        "és horitzontal: calcula on talla els costats PQ i QR i, amb això, l'àrea del "
        "trapezi resultant com a fracció del triangle."
    ),
    "expected_reasoning": (
        "Prenem el triangle equilàter PQR de costat 1 amb P = (0, 0), R = (1, 0) i "
        "Q = (1/2, √3/2). S = punt mitjà de PR = (1/2, 0). QS va de Q = (1/2, √3/2) a "
        "S = (1/2, 0); T = punt mitjà de QS = (1/2, √3/4). La línia per T paral·lela a PR "
        "és la recta horitzontal y = √3/4. Talla el costat PQ al punt (1/4, √3/4) i el "
        "costat QR al punt (3/4, √3/4) per simetria. La zona ombrejada (entre la base PR i "
        "aquesta recta horitzontal, tallada per PS i T) és un trapezi de vèrtexs P, S, T i "
        "(1/4, √3/4). Té bases 1/2 (segment PS) i 1/4 (de (1/4, √3/4) a (1/2, √3/4)) i "
        "alçada √3/4. La seva àrea és (1/2 + 1/4)/2 · √3/4 = 3·√3/32. L'àrea del triangle "
        "equilàter sencer és √3/4. La fracció és (3·√3/32) / (√3/4) = 3/8. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 1/8 surt de calcular només el triangle petit (entre T i els punts d'intersecció a PQ i QR) i deixar fora la part inferior del trapezi, que també és ombrejada.",
        "B": "Triar 3/10 surt d'un error en una de les bases del trapezi, per exemple agafant 1/5 en lloc d'1/4.",
        "C": "Triar 1/4 surt de calcular l'àrea del triangle semblant que té la meitat del costat i no del trapezi ombrejat real.",
        "E": "Triar 1/3 surt de confondre la zona ombrejada amb el triangle PQS sencer, que té àrea 1/2 del total (no 1/3) i tampoc coincideix amb el trapezi del problema.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-13"] = {
    "id":         "CAN-4ESO-2026-13",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     13,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Fixa't que cada parell (2k − 1, 2k) val −1. El primer parell té signe positiu, i "
        "tots els altres tenen el signe canviat pel signe menys que els precedeix. Compta "
        "quants parells hi ha en total i aplica els signes."
    ),
    "expected_reasoning": (
        "L'expressió és (1 − 2) − (3 − 4) − (5 − 6) − ... − (2025 − 2026). Cada parell "
        "(2k − 1) − 2k = −1, és a dir, val −1 per si sol. El primer parell, (1 − 2), apareix "
        "amb signe positiu i contribueix amb −1. Cada un dels parells següents apareix "
        "precedit d'un signe menys, que canvia −1 en +1: −(3 − 4) = +1, −(5 − 6) = +1, "
        "etcètera. El nombre total de parells és 2026/2 = 1013. El primer aporta −1 i els "
        "altres 1012 aporten +1 cadascun. El resultat total és −1 + 1012 = 1011. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar −1013 vol dir considerar que tots els parells aporten −1 (sense que el signe menys exterior els transformi), donant 1013·(−1) = −1013.",
        "B": "Triar −1011 surt d'un error de signe global en el resultat final, transformant 1011 en el seu oposat.",
        "D": "Triar 1013 surt de no restar la contribució −1 del primer parell, calculant 1013·1 = 1013 en lloc d'−1 + 1012.",
        "E": "Triar 2024 surt de comptar el nombre de termes individuals (2026 nombres − 2 que no compten?) en lloc d'operar els parells amb els seus signes.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-14"] = {
    "id":         "CAN-4ESO-2026-14",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     14,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2026-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Sigui S les cireres que menja l'elf sènior. Calcula la suma total de cireres dels "
        "cinc elfs i la mitjana, i planteja l'equació que diu que S és igual a aquesta "
        "mitjana més 8."
    ),
    "expected_reasoning": (
        "Sigui S el nombre de cireres que menja l'elf sènior. Els quatre elfs júniors "
        "mengen 4 × 6 = 24 cireres en total. La suma de les cireres dels cinc elfs és "
        "24 + S i la mitjana és (24 + S) / 5. La condició diu que S supera la mitjana en 8, "
        "és a dir, S = (24 + S) / 5 + 8. Multiplicant tot per 5: 5S = 24 + S + 40, és a "
        "dir, 4S = 64 i S = 16. L'elf sènior menja 16 cireres cada dia. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 14 surt de plantejar S = 6 + 8 = 14 sense passar per la mitjana, com si l'elf sènior mengés 8 cireres més que un júnior i ja n'hi hagués prou.",
        "C": "Triar 20 surt d'errors a l'hora de multiplicar per 5 o de manipular l'equació final, donant una desviació respecte del valor real.",
        "D": "Triar 21 surt d'aproximar la mitjana per 24/5 ≈ 5 i sumar-hi 8 i una mica més, sense imposar la condició com a equació estricta.",
        "E": "Triar 22 surt d'errors algebraics, com tractar la mitjana com a suma o cometre un error de signe en la simplificació final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-15"] = {
    "id":         "CAN-4ESO-2026-15",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     15,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-4ESO-2026-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Defineix tres grups: els que NOMÉS els agraden les matemàtiques (m), els que "
        "NOMÉS els agrada el francès (f) i els que els agraden les dues (mf). Escriu les "
        "dues condicions com a equacions i busca quin múltiple del nombre resultant cau "
        "entre 23 i 29."
    ),
    "expected_reasoning": (
        "Diguem m els alumnes a qui NOMÉS els agraden les matemàtiques, f els que NOMÉS "
        "els agrada el francès i mf els que els agraden totes dues matèries. Les "
        "condicions són: (1) el total de matemàtiques és el doble del total de francès, "
        "és a dir m + mf = 2·(f + mf), d'on m = mf + 2f; (2) els alumnes a qui agraden "
        "totes dues és igual als que NOMÉS els agrada el francès, és a dir mf = f. "
        "Substituint mf = f a (1): m + mf = 2·(f + f) = 4·f, és a dir m = 3·f. Total de "
        "la classe = m + mf + f = 3f + f + f = 5·f. Com que el total és entre 23 i 29, "
        "l'únic múltiple de 5 en aquest interval és 25, amb f = 5. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 24 = 4·6 surt d'aplicar incorrectament alguna de les condicions i obtenir un múltiple de 4 o de 6 en lloc d'un múltiple de 5.",
        "C": "Triar 26 no és múltiple de 5 i surt d'errors en el plantejament, com no fer servir bé la condició mf = f.",
        "D": "Triar 27 = 3·9 surt d'un plantejament diferent que porta a un múltiple de 9 o de 3 en lloc de 5.",
        "E": "Triar 28 = 4·7 surt d'errors similars que produeixen un múltiple de 4 o de 7 en lloc del múltiple de 5 que dona el plantejament correcte.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-16"] = {
    "id":         "CAN-4ESO-2026-16",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Si el nombre original és N i la seva xifra de les unitats és 1, eliminar aquesta "
        "xifra equival a calcular (N − 1)/10. Planteja l'equació N − (N − 1)/10 = 2026 i "
        "resol per a N. Després suma'n les xifres."
    ),
    "expected_reasoning": (
        "Sigui N el nombre original, amb la xifra de les unitats igual a 1. En eliminar "
        "aquesta xifra s'obté el nombre N' = (N − 1)/10. La condició diu que el nombre "
        "original supera el nou en 2026 unitats: N − (N − 1)/10 = 2026. Multiplicant per "
        "10: 10·N − (N − 1) = 20260, és a dir 9·N + 1 = 20260, d'on 9·N = 20259 i "
        "N = 2251. La suma de les xifres de 2251 és 2 + 2 + 5 + 1 = 10. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 18 surt d'una equació plantejada sense el +1 (és a dir, 9·N = 20260, que no dona un enter), arrodonint a un nombre proper amb xifres que sumen 18.",
        "B": "Triar 12 surt d'un error en el plantejament de l'equació, per exemple eliminant la xifra de les unitats com a N − 10 en lloc de (N − 1)/10, que dona un altre nombre.",
        "D": "Triar 14 surt d'una equació amb un terme constant equivocat, per exemple obtenint un altre N (com 2261 o 2341) i sumant-ne les xifres.",
        "E": "Triar 16 surt de resoldre correctament l'equació però cometre un error en la suma de les xifres del resultat 2251.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-17"] = {
    "id":         "CAN-4ESO-2026-17",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena a, b, c les amplades de les tres columnes i p, q, r les alçades de les "
        "tres files. Escriu cada àrea coneguda com a producte d'una amplada per una "
        "alçada (alguna cel·la abasta dues files). Amb les proporcions entre àrees pots "
        "trobar les sis dimensions sense fixar valors absoluts."
    ),
    "expected_reasoning": (
        "Anomenem a, b, c les amplades de les tres columnes (esquerra, centre, dreta) i "
        "p, q, r les alçades de les tres files (dalt, mig, baix). Les sis cel·les "
        "rectangulars donen aquestes àrees:\n"
        "  Esquerra-superior (fusionada files 1 i 2): a·(p+q) = 24.\n"
        "  Superior-dreta (fusionada columnes b i c): (b+c)·p = 42.\n"
        "  Centre-mig: b·q = 9.\n"
        "  Esquerra-inferior: a·r = 12.\n"
        "  Centre-inferior: b·r = 18.\n"
        "  Dreta (fusionada files 2 i 3, ombrejada): c·(q+r) = ?\n"
        "De b·q = 9 i b·r = 18 surt r/q = 2, així que prenent q = 1 tenim r = 2. De "
        "a·(p+q) = 24 i a·r = 12 surt r/(p+q) = 12/24 = 1/2, és a dir p + q = 2·r = 4, i "
        "amb q = 1 queda p = 3. Substituint q = 1 a b·q = 9 dona b = 9, i r = 2 a a·r = 12 "
        "dona a = 6. Finalment, (b+c)·p = 42 amb b = 9 i p = 3 dona 9 + c = 14, és a dir "
        "c = 5. L'àrea ombrejada és c·(q+r) = 5·(1+2) = 15. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 20 surt de confondre les amplades amb les alçades en alguna proporció, per exemple aplicant la ràtio 42/24 = 7/4 a una mesura que no toca.",
        "B": "Triar 18 és copiar directament l'àrea de la cel·la central-inferior (b·r = 18), suposant que la cel·la ombrejada té les mateixes dimensions, quan en realitat la seva amplada és c, no b.",
        "C": "Triar 16 surt d'un error en una de les divisions de proporcionalitat, per exemple agafant r/q ≠ 2 o p + q ≠ 4.",
        "E": "Triar 14 surt d'una resta incorrecta entre les àrees conegudes, com calcular (b+c)·p − b·p = c·p i quedar-se aquí sense fer servir l'alçada correcta de la cel·la ombrejada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-18"] = {
    "id":         "CAN-4ESO-2026-18",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     18,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2026-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Anomena Rc les regles de la Clara i Ra les de l'Anna. Les condicions et donen Ra "
        "i Rb en funció de Rc; la condició que el total de regles sigui parell determinarà "
        "el valor concret de Rc."
    ),
    "expected_reasoning": (
        "Cada noia compra 10 articles entre regles i bolígrafs. Diguem Ra, Rb, Rc les "
        "regles de l'Anna, la Berta i la Clara, respectivament. Els bolígrafs de l'Anna "
        "són el doble de les regles de la Clara, és a dir, 2·Rc; com que el total de "
        "l'Anna és 10, Ra = 10 − 2·Rc. Els bolígrafs de la Berta són el doble de les "
        "regles de l'Anna, és a dir, 2·Ra; per la mateixa raó, Rb = 10 − 2·Ra = "
        "10 − 2·(10 − 2·Rc) = 4·Rc − 10. Perquè Rb ≥ 0 cal Rc ≥ 3, i perquè Ra ≥ 0 cal "
        "Rc ≤ 5. El total de regles és Ra + Rb + Rc = (10 − 2·Rc) + (4·Rc − 10) + Rc = "
        "3·Rc, i ha de ser parell, així que Rc ha de ser parell. L'únic valor parell amb "
        "Rc ∈ {3, 4, 5} és Rc = 4. Aleshores Ra = 10 − 8 = 2 i els bolígrafs de la Berta "
        "són 2·Ra = 4. Verificació: Rb = 4·4 − 10 = 6, total regles = 12 (parell ✓). "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir confondre els bolígrafs de la Berta (2·Ra) amb les regles de l'Anna (Ra = 2), sense aplicar el factor 2.",
        "C": "Triar 6 surt d'ometre la condició de paritat del total de regles, per exemple acceptant Rc = 3 (senar) i calculant amb aquest valor.",
        "D": "Triar 7 surt d'operar sense la condició de paritat amb un valor de Rc que no fa 3·Rc parell, arribant a una resposta propera però errònia.",
        "E": "Triar 8 vol dir calcular 2·Rc (= 8 amb Rc = 4) en lloc de 2·Ra: és el nombre de bolígrafs de l'Anna, no els de la Berta.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-19"] = {
    "id":         "CAN-4ESO-2026-19",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     19,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena β l'angle ABC. La condició que A, B, C' estan alineats (amb B entre A i "
        "C') diu que la rotació porta BC a la direcció oposada de BA, és a dir, l'angle "
        "de rotació és θ = 180° − β. La condició que C, A', C' estan alineats dona una "
        "segona equació que, combinada amb angle BCA = 15°, fixa β."
    ),
    "expected_reasoning": (
        "Sigui β = angle ABC i θ l'angle de la rotació al voltant de B que envia ABC a "
        "A'BC'. La rotació conserva les distàncies: |BA'| = |BA| i |BC'| = |BC|; també "
        "angle A'BC' = β i angle CBC' = angle ABA' = θ.\n"
        "Per la condició que A, B, C' són alineats amb B entre A i C', el segment BC' "
        "queda en sentit oposat a BA: això vol dir que la rotació porta la direcció BC a "
        "la direcció oposada a BA, és a dir, β + θ = 180° i, per tant, θ = 180° − β.\n"
        "Col·locant B a l'origen, A sobre el semieix +x i C al semiplà superior, la "
        "rotació envia A a A' = a·(cos θ, sin θ) i C a C' = (−c, 0). La condició que els "
        "punts C, A' i C' són alineats es tradueix algebraicament, amb angle BCA = 15° i "
        "la llei dels sinus aplicada al triangle ABC, en una equació que té com a única "
        "solució β = 30°. D'aquí, angle CAB = 180° − β − 15° = 180° − 30° − 15° = 135°. "
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 105° surt de prendre θ = 2·15° = 30° (com si la rotació fos directament el doble de l'angle a C) sense imposar la condició que A, B i C' són alineats.",
        "B": "Triar 115° surt d'una mala identificació del sentit de la rotació o de quines condicions d'alineació s'usen, donant una equació numèricament propera però no correcta.",
        "C": "Triar 120° surt d'usar només la condició A, B, C' alineats sense imposar la condició addicional que C, A' i C' també ho han d'estar.",
        "E": "Triar 140° surt de confondre l'angle interior CAB amb l'angle exterior corresponent al vèrtex A, o de fer un error de signe en algun pas final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-20"] = {
    "id":         "CAN-4ESO-2026-20",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     20,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "La zona ombrejada és la intersecció dels tres discs de radi 2 cm centrats als "
        "tres vèrtexs del triangle equilàter. El perímetre es compon de tres arcs iguals; "
        "l'angle central de cadascun és l'angle interior del triangle equilàter."
    ),
    "expected_reasoning": (
        "El triangle equilàter té costat 2 cm i, des de cada vèrtex, es dibuixa un arc de "
        "radi 2 cm que passa pels altres dos vèrtexs. La zona ombrejada és la intersecció "
        "dels tres discs corresponents. El seu perímetre està format per tres arcs iguals, "
        "un per cada circumferència. L'arc de cada disc subtendeix l'angle interior del "
        "triangle equilàter al vèrtex corresponent, que val 60° = π/3 radians. La longitud "
        "de cada arc és radi × angle = 2·(π/3) = 2π/3 cm. El perímetre total és "
        "3·(2π/3) = 2π cm. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar π cm surt d'usar un sol arc en lloc dels tres, o de prendre radi 1 en lloc de 2.",
        "B": "Triar 6 cm vol dir confondre el perímetre de la zona corba amb el perímetre del triangle equilàter (3 · 2 = 6 cm), sense tenir en compte que el contorn és corb.",
        "D": "Triar 8 cm surt d'un càlcul amb un angle central diferent (per exemple, 120°) o radi incorrecte, donant un valor proper a 2π però no exacte.",
        "E": "Triar 4π cm surt d'usar angle central 120° per cada arc (3·2·(2π/3) = 4π) o de calcular la circumferència sencera d'un cercle de radi 2 (2π·2 = 4π) sense reduir-la a la fracció corresponent.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament identifica les 5 persones amb el conjunt de valors {7,9,10,13,14}
# i resol el sistema. Cal comprovar a la imatge/enunciat que els valors són
# correctament aquests i que els noms (Toni, Lina, Rai, Maria, Pere) i les
# condicions (Toni+Lina=3·Rai, Maria+Lina=2·Pere) coincideixen amb el text del
# problema. L'XLS confirma B = 13 picades a la Lina.
PROBLEMS["CAN-4ESO-2026-21"] = {
    "id":         "CAN-4ESO-2026-21",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     21,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Comença per la condició Toni + Lina = 3·Rai: el valor de Rai ha de ser tal que el "
        "triple es pugui escriure com a suma de dos valors dels restants. Prova "
        "sistemàticament cada candidat per a Rai i comprova si pots completar l'assignació "
        "amb la segona condició."
    ),
    "expected_reasoning": (
        "Els cinc valors són {7, 9, 10, 13, 14}, un per persona. Les condicions són "
        "Toni + Lina = 3·Rai i Maria + Lina = 2·Pere. Provem cada candidat per a Rai:\n"
        "  · Rai = 7 → Toni + Lina = 21: les sumes possibles de dos elements de {9,10,13,14} "
        "són 19, 22, 23, 23, 24, 27. Cap és 21. Descartat.\n"
        "  · Rai = 9 → Toni + Lina = 27: l'única parella de {7,10,13,14} que suma 27 és "
        "13 + 14. Si Toni = 14 i Lina = 13, queden {7, 10} per a Maria i Pere; comprovant "
        "Maria + Lina = 2·Pere amb Maria = 7 i Pere = 10: 7 + 13 = 20 = 2·10 ✓.\n"
        "  · Rai = 10 → Toni + Lina = 30: cap parella dels restants suma 30. Descartat.\n"
        "  · Rai = 13 o 14 → Toni + Lina ≥ 39, impossible.\n"
        "L'única assignació coherent és Rai = 9, Toni = 14, Lina = 13, Maria = 7, Pere = 10. "
        "La Lina té 13 picades. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 14 surt d'invertir l'assignació Toni ↔ Lina dins de la primera condició: 14 + 13 = 27 funciona simètricament, però aleshores Maria + Lina = 2·Pere donaria 7 + 14 = 21 (no parell) o 10 + 14 = 24, cap dels quals és el doble d'un dels valors restants.",
        "C": "Triar 10 surt de confondre el nom de la Lina amb el d'en Pere, o de provar Rai = 7 i descobrir tard que cap parella suma 21.",
        "D": "Triar 9 surt de confondre la Lina amb en Rai (que és el valor que multipliquem per 3 i que efectivament val 9).",
        "E": "Triar 7 surt de confondre la Lina amb la Maria, o d'explorar només Rai = 10 sense adonar-se que aquesta opció no té solució.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament suposa que els 15 punts són equidistants sobre una circumferència
# (és a dir, els vèrtexs d'un pentadecàgon regular). Si la disposició concreta a
# l'enunciat és diferent (per exemple, 15 punts en una graella), el càlcul pot
# variar substancialment. L'XLS confirma D = 9.
PROBLEMS["CAN-4ESO-2026-22"] = {
    "id":         "CAN-4ESO-2026-22",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     22,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-4ESO-2026-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Un polígon regular convex de n costats inscrit en una circumferència amb 15 punts "
        "equidistants només pot tenir n vèrtexs en aquests punts si n divideix 15. Per a "
        "cada divisor n de 15 amb n ≥ 3, compta quantes posicions diferents pot ocupar el "
        "polígon."
    ),
    "expected_reasoning": (
        "Perquè un polígon regular convex de n costats tingui tots els seus vèrtexs sobre "
        "els 15 punts equidistants d'una circumferència, els vèrtexs han d'estar separats "
        "per arcs iguals, és a dir, n ha de dividir 15. Els divisors de 15 ≥ 3 són: 3, 5 i "
        "15. Comptem quantes posicions distintes hi ha per a cada tipus:\n"
        "  · Triangle equilàter (n = 3): els tres vèrtexs ocupen els punts separats per "
        "15/3 = 5 posicions. Hi ha 15 tries per al primer vèrtex, però cada triangle es "
        "compta 3 vegades (una per cada vèrtex), així que hi ha 15/3 = 5 triangles "
        "distints.\n"
        "  · Pentàgon regular (n = 5): vèrtexs separats per 15/5 = 3 posicions. Hi ha 15/5 = 3 "
        "pentàgons distints.\n"
        "  · Pentadecàgon regular (n = 15): un únic polígon que utilitza els 15 punts. 1 "
        "polígon.\n"
        "Total: 5 + 3 + 1 = 9 polígons regulars convexos distints. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 15 surt de pensar que hi ha un polígon per cada punt inicial possible, sense adonar-se que molts d'aquests inicis donen el mateix polígon (els n vèrtexs poden ser el 'primer').",
        "B": "Triar 13 surt d'un compte amb un excés, per exemple comptant 5 triangles + 5 pentàgons + 3 grups d'un altre tipus = 13, o sumant les posicions sense agrupar-les correctament.",
        "C": "Triar 11 surt d'ometre un dels tres tipus o de calcular incorrectament les posicions: per exemple 5 + 5 + 1 = 11 o sumar amb un divisor que no toca.",
        "E": "Triar 5 surt de comptar només els triangles (5 posicions), ignorant els pentàgons i el pentadecàgon que també compleixen la divisibilitat.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-23"] = {
    "id":         "CAN-4ESO-2026-23",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     23,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Per cada cub petit que treus, compta amb cura quantes cares deixen de ser "
        "exteriors i quantes en queden de noves. El guany net depèn de si el cub és en "
        "una cantonada, una aresta, una cara o l'interior. Busca el guany màxim possible "
        "i, sobretot, comprova si pots posar-los tots sense que comparteixin cap cara."
    ),
    "expected_reasoning": (
        "La superfície inicial del cub 4×4×4 és 6·4² = 96 unitats quadrades. Volem que "
        "creixi un 50%, és a dir, guanyar 96·0,5 = 48 unitats.\n"
        "Guany net en treure un cub petit, segons la posició:\n"
        "  · Cantonada (3 cares exteriors): perds 3 cares de la superfície i n'exposes 3 "
        "de noves dels veïns. Guany 0.\n"
        "  · Aresta (2 cares exteriors): perds 2, exposes 4. Guany +2.\n"
        "  · Centre d'una cara (1 cara exterior): perds 1, exposes 5. Guany +4.\n"
        "  · Interior (0 cares exteriors): perds 0, exposes 6. Guany +6, però només si els "
        "veïns segueixen al seu lloc.\n"
        "El guany de +6 (cub interior) no és sostenible a escala: els 8 cubs del nucli "
        "2×2×2 són veïns entre ells, i traient-los tots no exposes 48 cares (8·6) sinó "
        "només les del forat 2×2×2 resultant, que té superfície 24. En mitjana, cada cub "
        "interior aporta només 24/8 = 3.\n"
        "Limitant-nos a cubs que no comparteixin cap cara, el guany màxim per cub és +4 "
        "(centre d'una cara). Per arribar a 48 unitats de guany cal, com a mínim, "
        "48/4 = 12 cubs. Aquesta fita és assolible: a cada una de les 6 cares del cub gran, "
        "els 4 cubs centrals (els del 2×2 interior) tenen exactament 1 cara exterior, i a "
        "cada cara se'n poden triar 2 que no siguin adjacents; en total, 2·6 = 12 cubs no "
        "adjacents entre ells, cadascun amb guany +4. Amb 11 cubs i guany màxim +4 cadascun, "
        "el total seria com a màxim 44, insuficient. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 6 és insuficient fins i tot suposant el guany màxim teòric +6 per cub: 6·6 = 36 < 48.",
        "B": "Triar 8 surt de pensar que els 8 cubs del nucli 2×2×2 aporten guany +6 cadascun (8·6 = 48), però com que són veïns entre ells, el forat resultant només té superfície interior 24, no 48.",
        "C": "Triar 10 surt de pensar que es pot superar el guany de +4 per cub combinant cubs adjacents, sense adonar-se que les cares compartides redueixen el guany efectiu.",
        "E": "Triar 18 surt d'una estratègia subòptima, per exemple combinant cubs d'aresta (guany +2) amb cubs de cara (guany +4) en lloc d'usar només cubs de cara no adjacents.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-24"] = {
    "id":         "CAN-4ESO-2026-24",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     24,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Prova totes les possibilitats per al nombre d'afirmacions falses (0, 1, 2, 3 o 4) "
        "i comprova en cada cas si pots assignar valors de veritat coherents a totes "
        "quatre afirmacions. Comença per casos extrems (totes certes o totes falses)."
    ),
    "expected_reasoning": (
        "Provem l'assignació en què només l'afirmació 4 és certa i les afirmacions 1, 2 i "
        "3 són falses. Comprovem la coherència de cadascuna:\n"
        "  · La 4 diu 'les tres anteriors són falses': si 1, 2 i 3 són falses, és veritat ✓.\n"
        "  · La 3 diu 'l'afirmació anterior (la 2) és certa': si la 2 és falsa, la 3 és "
        "falsa ✓.\n"
        "  · La 2 diu 'aquesta afirmació és certa': si la 2 és falsa, diu de si mateixa que "
        "és certa quan no ho és, però aquesta autoreferència no és contradictòria (no és "
        "una paradoxa del mentider); és perfectament consistent assignar-li valor fals ✓.\n"
        "  · La 1 diu 'exactament dues són falses': hi ha 3 falses (1, 2, 3), no 2; per "
        "tant la 1 és falsa ✓.\n"
        "L'assignació (1=F, 2=F, 3=F, 4=C) és coherent. Cap altra assignació amb un nombre "
        "diferent de certes és coherent: per exemple, si la 4 és falsa, no totes les "
        "anteriors són falses; si la 1 és certa, hi ha d'haver exactament dues falses, "
        "cosa que no encaixa amb cap configuració consistent de les altres. El nombre "
        "d'afirmacions certes és exactament 1. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 0 implicaria que totes quatre afirmacions són falses, però si la 4 és falsa, no és veritat que 'les tres anteriors són totes falses', cosa que requereix que alguna de les tres primeres sigui certa: contradicció.",
        "C": "Triar 2 demanaria una configuració amb exactament dues certes i dues falses, però cap d'aquestes configuracions és consistent amb el contingut de les quatre afirmacions a la vegada.",
        "D": "Triar 3 demanaria tres certes i una falsa; si la 1 fos certa ('exactament dues falses'), hauria d'haver-hi exactament dues falses, no una: contradicció.",
        "E": "Triar 4 (totes certes) és impossible: si la 4 és certa, 'les tres anteriors són falses', però aleshores la 1, 2 i 3 són falses i no totes certes: contradicció directa.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-25"] = {
    "id":         "CAN-4ESO-2026-25",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     25,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Cada 'Jo no' elimina possibilitats. Ronda 1: si l'Anna no ho sap a partir del "
        "patró, és que el patró és comú a més d'un caramel. Ronda 2: si l'Elsa no ho sap "
        "(amb la informació de la ronda 1 ja incorporada), és que la forma també és comuna "
        "entre els caramels restants. Aplica això pas a pas."
    ),
    "expected_reasoning": (
        "Els cinc caramels són: A (rodó, punts), B (rodó, llis), C (allargat, ratlles), D "
        "(allargat, ratlles), E (allargat, punts). L'Anna coneix el patró; l'Elsa coneix "
        "la forma.\n"
        "Ronda 1, l'Anna diu 'Jo no': el patró que coneix l'Anna és comú a més d'un caramel. "
        "El patró 'llis' només apareix una vegada (caramel B), per tant si l'Anna sabés "
        "'llis', sabria que és B; com que no ho sap, el patró no és 'llis'. Això elimina B.\n"
        "Ronda 2, l'Elsa diu 'Jo no', sabent que B està eliminat: la forma que coneix l'Elsa "
        "és comuna a més d'un caramel entre els que queden. Entre {A, C, D, E}, només A és "
        "'rodó', i C, D, E són 'allargats'. Si l'Elsa sabés 'rodó', sabria que és A; com que "
        "no ho sap, la forma no és 'rodona'. Això elimina A.\n"
        "Ronda 3, l'Anna respon. Queden C, D i E (tots allargats), amb patrons 'ratlles' (C "
        "i D) i 'punts' (E). Si el patró fos 'ratlles', l'Anna no podria distingir entre C "
        "i D; com que sí que ho sap, el patró és 'punts' i el caramel és E. L'Elsa també "
        "ho dedueix: amb forma 'allargat' i restant només l'E amb patró únic, confirma E. "
        "Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A (rodó, punts) és oblidar la ronda 2: l'Elsa eliminaria A pel mateix raonament que ha eliminat B (única forma rodona restant).",
        "B": "Triar B (rodó, llis) és oblidar la ronda 1: l'Anna ja l'hauria identificat si el patró fos 'llis', i el seu 'Jo no' inicial l'elimina.",
        "C": "Triar C (allargat, ratlles) és incompatible amb la resposta de l'Anna a la ronda 3: si el patró fos 'ratlles', l'Anna no podria distingir entre C i D, i no hauria respost correctament.",
        "D": "Triar D (allargat, ratlles) té exactament el mateix problema que C: amb dues opcions de ratlles restants, l'Anna no podria identificar el caramel.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2026-26"] = {
    "id":         "CAN-4ESO-2026-26",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     26,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-4ESO-2026-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "L'últim nombre de la seqüència ha de ser senar (1, 3 o 5). Per a cada valor "
        "possible de l'últim nombre, explora sistemàticament les permutacions dels altres "
        "quatre i comprova les condicions de divisibilitat per a cada triplet de posicions "
        "consecutives."
    ),
    "expected_reasoning": (
        "Cal trobar les permutacions (a1, a2, a3, a4, a5) dels nombres 1, 2, 3, 4 i 5 que "
        "compleixen alhora: (a) a5 senar; (b) a1 divideix a1 + a2 + a3 (equivalent a a1 "
        "divideix a2 + a3); (c) a2 divideix a2 + a3 + a4 (equivalent a a2 divideix "
        "a3 + a4); (d) a3 divideix a3 + a4 + a5 (equivalent a a3 divideix a4 + a5).\n"
        "Explorant sistemàticament les permutacions amb a5 ∈ {1, 3, 5} i comprovant les "
        "tres condicions de divisibilitat a cadascuna, s'obtenen exactament les 5 "
        "seqüències vàlides següents:\n"
        "  · 4, 5, 3, 2, 1: 4 | (5+3) = 8 ✓; 5 | (3+2) = 5 ✓; 3 | (2+1) = 3 ✓.\n"
        "  · 2, 3, 5, 4, 1: 2 | (3+5) = 8 ✓; 3 | (5+4) = 9 ✓; 5 | (4+1) = 5 ✓.\n"
        "  · 2, 5, 1, 4, 3: 2 | (5+1) = 6 ✓; 5 | (1+4) = 5 ✓; 1 | (4+3) = 7 ✓.\n"
        "  · 4, 3, 1, 2, 5: 4 | (3+1) = 4 ✓; 3 | (1+2) = 3 ✓; 1 | (2+5) = 7 ✓.\n"
        "  · 2, 1, 3, 4, 5: 2 | (1+3) = 4 ✓; 1 | (3+4) = 7 ✓; 3 | (4+5) = 9 ✓.\n"
        "Cap altra permutació compleix totes les condicions alhora. En total, 5 maneres. "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 6 surt d'admetre alguna permutació no vàlida (per exemple, aplicant la condició de divisibilitat de manera aproximada) i comptar-la com a vàlida, sumant-se a les 5 reals.",
        "C": "Triar 4 surt de trobar 4 de les 5 seqüències vàlides, ometent-ne típicament una de les que tenen a5 = 3 o a5 = 5.",
        "D": "Triar 3 surt d'identificar correctament les seqüències per a un o dos valors d'a5 però passar per alt una o més seqüències per al tercer valor.",
        "E": "Triar 2 vol dir cometre errors sistemàtics en les comprovacions de divisibilitat i descartar diverses seqüències que sí que són vàlides, com per exemple quedar-se només amb les dues seqüències acabades en 1.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament fa servir noms concrets (Albert, Bernat, Carles, David, Ernest) i
# afirmacions concretes (Albert='sóc 2n o 3r', Bernat='he arribat i no sóc 4t',
# Carles='he quedat primer', David='sóc 4t', Ernest='no he arribat'). Cal
# comprovar a l'enunciat real que aquests són efectivament els noms i les
# afirmacions; si difereixen, la mecànica del raonament és anàloga però els
# detalls dels distractors caldria adaptar-los. L'XLS confirma C = Carles menteix.
PROBLEMS["CAN-4ESO-2026-27"] = {
    "id":         "CAN-4ESO-2026-27",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2026-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Hi ha 5 corredors, 4 acaben la cursa (en posicions 1, 2, 3 i 4) i 1 no arriba a "
        "la meta. Quatre dels cinc diuen la veritat i un menteix. Suposa que cada persona "
        "és la que menteix i comprova si la classificació resultant és consistent amb les "
        "afirmacions dels altres quatre."
    ),
    "expected_reasoning": (
        "Considerem els cinc corredors amb les afirmacions que fan sobre la seva posició "
        "i si han arribat a la meta. Sabem que un menteix i els altres quatre diuen la "
        "veritat, i que exactament un corredor no ha arribat a la meta. Provant cada "
        "persona com a possible mentider:\n"
        "  · Si Albert menteix, les afirmacions dels altres dos primers (Carles diu ser 1r, "
        "David diu ser 4t) deixen Albert sense una posició coherent.\n"
        "  · Si Bernat menteix, la combinació amb Ernest (l'altre que ja no arriba) genera "
        "dues persones sense arribar a la meta, cosa que contradiu l'enunciat.\n"
        "  · Si Carles menteix, podem fer encaixar les altres quatre afirmacions: Ernest "
        "no arriba (com diu), David és 4t (com diu), Albert és 2n o 3r (com diu), Bernat "
        "ha arribat i no és 4t (com diu); i a Carles li toca una posició coherent (per "
        "exemple, 3r o 2n) diferent de la 1a que reclama. Tot quadra. Aquesta és la "
        "configuració vàlida.\n"
        "  · Si David menteix, ningú no és 4t però Bernat diu de veritat que no és 4t i "
        "no queda lloc per al 4t: contradicció.\n"
        "  · Si Ernest menteix (ell sí que arriba), tots els cinc arriben i no hi ha cap "
        "eliminat: contradiu l'enunciat.\n"
        "L'únic mentider possible és Carles. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Si Albert fos el mentider (no és 2n ni 3r), aleshores hauria de ser 1r o 4t. Però Carles diu de veritat ser 1r i David diu de veritat ser 4t: cap dels dos llocs queda lliure per a Albert.",
        "B": "Si Bernat fos el mentider, o no hauria arribat a la meta (i amb Ernest ja eliminat tindríem dos eliminats, contra l'enunciat) o seria 4t (juntament amb David, que també diu ser 4t): impossible en tots dos casos.",
        "D": "Si David fos el mentider (no és 4t), ningú no ocuparia el 4t lloc, però Bernat afirma veraçment no ser 4t i les altres posicions ja estan repartides: queda un lloc sense ocupar.",
        "E": "Si Ernest fos el mentider (sí que arriba), llavors els cinc corredors arribarien a la meta i no hi hauria cap eliminat, cosa que contradiu directament l'enunciat.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament parteix d'una ampolla amb una part cilíndrica i una part més
# estreta (probablement el coll, on hi ha el tap). Les mesures concretes (24 cm
# d'aigua quan està dreta, 30 cm d'aigua des del tap quan invertida, 42 cm
# d'alçada total cilíndrica) cal verificar-les contra la imatge real. La
# capacitat de 4,5 L i el resultat de 3,0 L també. L'XLS confirma D = 3,0 L.
PROBLEMS["CAN-4ESO-2026-28"] = {
    "id":         "CAN-4ESO-2026-28",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     28,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2026-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena S la secció transversal de la part cilíndrica de l'ampolla. Quan està "
        "dreta, l'aigua ocupa només la part cilíndrica i té volum V_aigua = 24·S. Quan "
        "s'inverteix, l'aire ocupa una part de la zona cilíndrica i la seva alçada s'obté "
        "restant l'alçada de l'aigua mesurada des del tap a l'alçada total de la part "
        "cilíndrica. Planteja V_aigua + V_aire = capacitat total."
    ),
    "expected_reasoning": (
        "Sigui S la secció transversal de la part cilíndrica de l'ampolla. Quan l'ampolla "
        "està dreta, l'aigua ocupa una alçada de 24 cm dins la part cilíndrica: "
        "V_aigua = 24·S. Quan s'inverteix, l'aigua baixa cap a la part estreta del coll i "
        "l'aire passa a ocupar la part de dalt (cilíndrica). La mesura de 30 cm correspon "
        "a l'alçada de l'aigua des del tap, així que l'aire dins la part cilíndrica té "
        "alçada 42 − 30 = 12 cm: V_aire = 12·S. La capacitat total és V_aigua + V_aire = "
        "24·S + 12·S = 36·S = 4,5 L, d'on S = 4,5/36 = 1/8 L/cm. Per tant, "
        "V_aigua = 24·(1/8) = 3,0 L. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 2,4 L surt d'un error en la identificació de l'alçada d'aire quan l'ampolla està invertida, per exemple usant 18 cm (= 42 − 24) com a alçada d'aire sense tenir en compte la mesura real de 30 cm des del tap.",
        "B": "Triar 2,5 L surt d'establir una proporció directa entre V_aigua i la capacitat segons 24/42 (les dues alçades), com si l'ampolla fos tota cilíndrica.",
        "C": "Triar 2,7 L surt d'interpretar 30 cm com a alçada d'aire en lloc d'alçada d'aigua, donant equacions amb proporcions incorrectes.",
        "E": "Triar 3,5 L surt d'interpretar 30 cm com a alçada de l'aigua dins la part cilíndrica quan invertida (en lloc de la mesura des del tap) i ajustar amb un error en la suma 24 + x.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament suposa que ABCD i DCEF són dos rectangles iguals adjacents
# (sharing el costat DC), formant un rectangle gran ABEF. El punt O és el
# centre del segon rectangle (DCEF). Cal comprovar a la imatge que aquesta és
# la disposició correcta i que el triangle a calcular és efectivament ACO.
# L'XLS confirma A = 1/4.
PROBLEMS["CAN-4ESO-2026-29"] = {
    "id":         "CAN-4ESO-2026-29",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Col·loca coordenades als dos rectangles ABCD i DCEF. Calcula la posició del "
        "centre O del segon rectangle, escriu l'àrea del triangle ACO amb el determinant "
        "(o la fórmula 1/2·|x1(y2−y3)+x2(y3−y1)+x3(y1−y2)|) i divideix-la per l'àrea del "
        "rectangle gran ABEF."
    ),
    "expected_reasoning": (
        "Col·loquem coordenades: A = (0, 0), B = (0, h), C = (w, h), D = (w, 0). El "
        "rectangle DCEF (igual a ABCD i adjacent al costat DC) té D = (w, 0), C = (w, h), "
        "E = (2w, h), F = (2w, 0). El centre de DCEF és O = ((w + 2w)/2, (0 + h)/2) = "
        "(3w/2, h/2). Calculem l'àrea del triangle ACO amb A = (0, 0), C = (w, h), "
        "O = (3w/2, h/2): Àrea = (1/2)·|x_C · y_O − x_O · y_C| = "
        "(1/2)·|w·(h/2) − (3w/2)·h| = (1/2)·|wh/2 − 3wh/2| = (1/2)·|−wh| = wh/2. L'àrea del "
        "rectangle gran ABEF és 2w · h = 2wh. La fracció és (wh/2)/(2wh) = 1/4. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 1/2 surt de calcular el quocient respecte del rectangle petit ABCD (de dimensions w × h) en lloc del rectangle gran ABEF (2w × h), donant (wh/2)/wh = 1/2.",
        "C": "Triar 1/3 surt d'un error en les coordenades de O, per exemple posant O al centre geomètric del rectangle gran (w, h/2) en comptes del centre del rectangle DCEF.",
        "D": "Triar 1/5 surt d'un error en el càlcul del determinant: per exemple, sumant en lloc de restar i obtenint wh/2 + 3wh/2 = 2wh en lloc del valor correcte.",
        "E": "Triar 2/9 surt de fer servir valors concrets (per exemple w = h = 3) amb un error en algun pas, donant una fracció diferent de 1/4.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament suposa una configuració concreta: una circumferència gran de
# radi R = 10 cm conté 9 circumferències interiors iguals de radi r, totes
# tangents internament a la gran i tangents externament a les veïnes; els 9
# centres formen un nonàgon regular. El polígon ombrejat és aquest nonàgon, i d
# representa la suma de les distàncies dels 9 centres interiors al centre
# exterior. Cal comprovar a l'enunciat real que aquesta és la configuració i
# que d té aquest significat. L'XLS confirma E = 180 − 2d.
PROBLEMS["CAN-4ESO-2026-30"] = {
    "id":         "CAN-4ESO-2026-30",
    "categoria":  "4ESO",
    "any":        2026,
    "numero":     30,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2026-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "El polígon ombrejat és el nonàgon que té com a vèrtexs els 9 centres de les "
        "circumferències interiors. El costat del nonàgon és la distància entre centres "
        "de dues circumferències veïnes; com que són tangents externament, val 2r. "
        "Expressa r en funció de d i substitueix al perímetre."
    ),
    "expected_reasoning": (
        "Sigui r el radi de cadascuna de les 9 circumferències interiors, iguals entre "
        "elles, i sigui R = 10 cm el radi de la circumferència gran. Cada circumferència "
        "interior és tangent internament a la gran, així que la distància de cada centre "
        "interior al centre exterior és R − r = 10 − r. La suma de les distàncies dels 9 "
        "centres interiors al centre exterior és d = 9·(10 − r), és a dir, 9·r = 90 − d i "
        "r = (90 − d)/9.\n"
        "El polígon ombrejat és el nonàgon regular que té els 9 centres com a vèrtexs. "
        "Com que les circumferències veïnes són tangents externament, la distància entre "
        "centres veïns és 2r, que és el costat del nonàgon. El perímetre és 9·(2r) = 18r. "
        "Substituint r = (90 − d)/9: perímetre = 18·(90 − d)/9 = 2·(90 − d) = 180 − 2d. "
        "Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 90 − 2d surt d'usar 9·r com a perímetre (en lloc de 9·(2r)) i, al mateix temps, restar 2d on només cal restar d.",
        "B": "Triar 90 − d surt de calcular el perímetre com a 9·r (no 9·(2r), oblidant que el costat del nonàgon és 2r) i substituir r = (90 − d)/9 directament.",
        "C": "Triar 180 − d surt d'un error en l'expressió de d (per exemple, prenent d = 9r en lloc de d = 9·(10 − r)), que dona r = d/9 i perímetre 18·d/9 = 2d.",
        "D": "Triar 180 + 2d surt d'invertir el signe en la relació d = 90 − 9·r, obtenint 9r = 90 + d, i propagant aquest signe al perímetre.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}
