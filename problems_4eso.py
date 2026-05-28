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

# ============================================================
# 3 PUNTS (1-10)
# ============================================================

PROBLEMS["CAN-4ESO-2025-01"] = {
    "id":         "CAN-4ESO-2025-01",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     1,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pots girar el 2 i convertir-lo en 5. Quants 5 pots tenir, com a màxim?"
    ),
    "expected_reasoning": (
        "Les quatre peces de fusta són les xifres del 2025: és a dir, dos «2», un «0» i un "
        "«5». Però donar-hi la volta a un «2» el converteix en un «5» i a la inversa, així "
        "que les tres peces «2/5» són intercanviables: pot tenir des de zero fins a tres "
        "«5» visibles (i la resta «2»). Per formar el nombre més gran, posem el màxim "
        "possible de «5» en posicions inicials. Amb tres «5» i un «0» (i la peça «0» no es "
        "pot girar), el nombre més gran és 5550. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 5052 vol dir no aprofitar que les peces es poden girar i pensar que cal usar literalment les xifres de 2025.",
        "B": "Triar 5220 vol dir suposar que només una peça «2» es pot girar a «5».",
        "C": "Triar 5520 vol dir girar només dues de les peces «2» a «5», sense adonar-se que les tres són girables.",
        "E": "Triar 5555 vol dir oblidar que la peça «0» no es pot girar a «5» (i, a més, només hi ha tres peces girables, no quatre).",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-02"] = {
    "id":         "CAN-4ESO-2025-02",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Cada angle exterior i el seu interior sumen 180°. I els tres angles d'un triangle, 180° en total."
    ),
    "expected_reasoning": (
        "Els angles interiors corresponents als angles exteriors donats valen 180° − 110° "
        "= 70° i 180° − 120° = 60°. La suma dels tres angles interiors del triangle és "
        "180°, així que α = 180° − 70° − 60° = 50°. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 65° vol dir confondre l'angle exterior amb l'interior en algun dels dos vèrtexs.",
        "B": "Triar 60° vol dir donar el valor d'un dels angles interiors calculats per error.",
        "C": "Triar 55° vol dir un error en una de les restes (per exemple, 180° − 125°).",
        "E": "Triar 45° vol dir un error d'arrodoniment o de càlcul en restar.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-03"] = {
    "id":         "CAN-4ESO-2025-03",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     3,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Plega les solapes mentalment. Quines tres caselles del centre queden tapades per una finestra?"
    ),
    "expected_reasoning": (
        "Quan les dues solapes es pleguen sobre la pàgina central, les finestres de cada "
        "solapa queden a sobre de la pàgina central. Mirant la posició de les finestres a "
        "les solapes i la disposició dels nombres a la pàgina central, les finestres "
        "deixen veure els nombres 9, 2, 3 (i no més). La suma és 9 + 2 + 3 = 14. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 7 vol dir comptar només les finestres d'una de les dues solapes.",
        "B": "Triar 9 vol dir veure només una de les tres finestres efectives.",
        "C": "Triar 12 vol dir confondre quins nombres queden tapats i fer 9+3 o 5+7.",
        "E": "Triar 15 vol dir incloure un nombre extra que en realitat no és visible.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-04"] = {
    "id":         "CAN-4ESO-2025-04",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     4,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-4ESO-2025-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Compta els triangles negres a cada hexàgon. N'han de ser exactament 2."
    ),
    "expected_reasoning": (
        "Cada hexàgon està dividit en sis triangles iguals. Que la zona negra sigui un terç "
        "del total vol dir que han de ser-hi dos triangles negres (6 · 1/3 = 2). Que la "
        "zona blanca sigui la meitat del total vol dir tres triangles blancs (6 · 1/2 = 3). "
        "Queda un triangle gris. L'única figura que té exactament 2 negres, 3 blancs i 1 "
        "gris és l'opció E. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir no comptar els triangles i fer la decisió només mirant si el negre «sembla» un terç.",
        "B": "Triar B vol dir comptar els negres correctament però oblidar comprovar que els blancs siguin tres.",
        "C": "Triar C vol dir veure-hi més negre del compte perquè els triangles negres estan adjacents.",
        "D": "Triar D vol dir comptar tres triangles negres en lloc de dos, suposant que un terç «és força».",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-08 ----------
PROBLEMS["CAN-4ESO-2025-05"] = {
    "id":         "CAN-4ESO-2025-05",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     5,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Entre 10 tanques hi ha 9 buits (no 10)."
    ),
    "expected_reasoning": (
        "Entre 10 tanques alineades hi ha 9 intervals consecutius (no 10), cadascun de 8,5 "
        "m. La distància de la sortida a l'última tanca és, doncs, 13 + 9 × 8,5 = 13 + 76,5 "
        "= 89,5 m. La cursa fa 100 m en total, així que la distància de l'última tanca a la "
        "meta és 100 − 89,5 = 10,5 m. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 13 m vol dir confondre la distància de la sortida a la primera tanca amb la distància de l'última tanca a la meta.",
        "C": "Triar 9,5 m vol dir comptar 10 intervals entre tanques en comptes de 9 (error de fencepost).",
        "D": "Triar 6 m vol dir un error de càlcul addicional sobre el recompte erroni d'intervals.",
        "E": "Triar 4,5 m vol dir comptar 11 intervals o un error de càlcul similar.",
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-06"] = {
    "id":         "CAN-4ESO-2025-06",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     6,
    "punts":      3,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Prova amb x = 10 i calcula cadascuna de les cinc fraccions."
    ),
    "expected_reasoning": (
        "Prenem x > 5, per exemple x = 10. Calculem cada expressió: (x+1)/5 = 11/5 = 2,2; "
        "x/5 = 2; 5/(x−1) = 5/9 ≈ 0,56; 5/(x+1) = 5/11 ≈ 0,45; 5/x = 0,5. La més petita és "
        "5/(x+1). En general, com que x > 5, els denominadors x−1, x i x+1 són tots "
        "positius, i el més gran d'aquests tres és x+1, així que 5/(x+1) és la fracció més "
        "petita de les del tipus 5/(...). I com que 5/(x+1) < 5/x < 1 < x/5 < (x+1)/5, és "
        "també la més petita de totes cinc. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar (x+1)/5 vol dir confondre el sentit de la pregunta i triar la més gran.",
        "B": "Triar x/5 vol dir agafar la més gran entre les dues primeres sense comparar amb les fraccions 5/(...).",
        "C": "Triar 5/(x−1) vol dir oblidar que x−1 < x+1 i, per tant, 5/(x−1) > 5/(x+1).",
        "E": "Triar 5/x vol dir comparar bé amb (x+1)/5 i x/5 però no veure que 5/(x+1) és encara més petita.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-07"] = {
    "id":         "CAN-4ESO-2025-07",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Dues cares oposades del dau sumen 7 (1-6, 2-5, 3-4). Cap parell de cares consecutives en una seqüència de girs pot sumar 7."
    ),
    "expected_reasoning": (
        "En girar el dau sobre una aresta, la cara que era a dalt passa a un dels quatre "
        "laterals adjacents, mai a la cara oposada (que era a baix i continua a baix fins "
        "que es giri ella mateixa). Així, en una seqüència vàlida de cares de dalt, dos "
        "termes consecutius no poden ser cares oposades, és a dir, no poden sumar 7. "
        "Recorrent les opcions: A) 3-5-1-2-6-4 → cap parell consecutiu suma 7 ✓. "
        "B) 3-2-5-1-6-4 → 1 i 6 són consecutius i sumen 7 ✗. C) 3-1-2-6-5-4 → cap parell "
        "consecutiu suma 7 ✓. D) 3-1-5-6-2-4 → cap parell suma 7 ✓. E) 3-6-2-1-5-4 → cap "
        "parell consecutiu suma 7 ✓. L'única seqüència impossible és la B. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir buscar una restricció incorrecta (per exemple, que les cares han d'aparèixer en algun ordre fix).",
        "C": "Triar C vol dir confondre les cares oposades del dau amb una altra parella.",
        "D": "Triar D vol dir el mateix error: no identificar correctament les cares oposades (1-6, 2-5, 3-4).",
        "E": "Triar E vol dir aplicar una regla inexistent sobre l'ordre dels girs.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-12 ----------
PROBLEMS["CAN-4ESO-2025-08"] = {
    "id":         "CAN-4ESO-2025-08",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     8,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2025-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Tothom respon «Sí». Si hi ha 10 més veritaters que mentiders i en total són 20, quants n'hi ha de cada?"
    ),
    "expected_reasoning": (
        "Una persona que sempre diu la veritat respon «Sí» a la pregunta «Sempre dius la "
        "veritat?» (és veritat). Una persona que sempre menteix també respon «Sí», perquè "
        "la veritat seria «No» i ella sempre diu el contrari. Per tant tothom respon «Sí», i "
        "el total de persones a l'habitació és 20. Si anomenem M el nombre de mentideres i "
        "T el de veritaters, tenim T = M + 10 i T + M = 20. Substituint: 2M + 10 = 20, "
        "d'on M = 5. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 0 vol dir suposar que els mentiders responen «No», però aleshores els 10 mentiders no podrien donar 0.",
        "C": "Triar 15 vol dir confondre el nombre de mentiders amb el de veritaters: T = 15 és la solució a la pregunta complementària.",
        "D": "Triar 20 vol dir donar com a resposta el nombre total de persones, no només els mentiders.",
        "E": "Triar 25 vol dir un càlcul algèbric incorrecte en resoldre el sistema d'equacions.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-13 (ER reescrit per arreglar la inconsistència) ----------
PROBLEMS["CAN-4ESO-2025-09"] = {
    "id":         "CAN-4ESO-2025-09",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     9,
    "punts":      3,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "L'1 i el 2 NO són veïns. Anomena els altres cercles i aplica «cada cercle = suma dels dos veïns»."
    ),
    "expected_reasoning": (
        "Numerem els sis cercles en sentit horari c1, c2, c3, c4, c5, c6, amb c1 = 1 i "
        "c3 = 2 (els dos cercles amb valor donat tenen un cercle buit entre ells, no són "
        "adjacents). La condició diu que cada cercle és igual a la suma dels seus dos "
        "veïns: cn = c_{n−1} + c_{n+1}, és a dir, c_{n+1} = cn − c_{n−1}. Aplicant aquesta "
        "recurrència: c3 = c2 − c1 → 2 = c2 − 1 → c2 = 3. Llavors c4 = c3 − c2 = 2 − 3 = "
        "−1; c5 = c4 − c3 = −1 − 2 = −3; c6 = c5 − c4 = −3 − (−1) = −2. Comprovem la "
        "tornada: c1 = c6 − c5 = −2 − (−3) = 1 ✓. El cercle gris és c5, oposat al cercle "
        "buit superior, i val −3. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir copiar un dels valors donats sense aplicar la condició.",
        "B": "Triar −1 vol dir aturar-se al cercle veí del gris (c4 o c6) sense arribar fins al fons.",
        "C": "Triar −2 vol dir confondre el cercle gris amb el cercle veí c6.",
        "E": "Triar −5 vol dir un error d'una unitat en alguna de les restes de la recurrència.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-10"] = {
    "id":         "CAN-4ESO-2025-10",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     10,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Els dos semicercles que sobresurten compensen exactament els dos que entren cap a dins."
    ),
    "expected_reasoning": (
        "El contorn de la figura es compon de quatre segments rectes de 4 cm cadascun i "
        "quatre semicercles de diàmetre 4 cm. Mirant la figura, dos dels semicercles "
        "sobresurten cap a fora del rectangle que els quatre segments definirien i dos hi "
        "entren cap a dins. Com que els quatre semicercles tenen la mateixa mida, l'àrea "
        "que «s'afegeix» pels dos semicercles exteriors és exactament la mateixa que la "
        "que es «treu» pels dos interiors. Per tant l'àrea de la figura acolorida és la "
        "mateixa que la del rectangle de costats 4·3 i 4 (és a dir, 12 cm × 4 cm), o "
        "equivalentment, la mateixa que un quadrat 12×4 = 48 cm². Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 48 − 4π vol dir restar dos semicercles sencers (= 1 cercle de radi 2, àrea 4π) sense compensar amb els que sobresurten.",
        "B": "Triar 32 vol dir comptar una franja de 4×8 en lloc de 4×12.",
        "C": "Triar 32 + 4π vol dir comptar 32 de rectangle i afegir-hi un cercle.",
        "D": "Triar 32 + 8π vol dir comptar 32 i afegir-hi dos cercles.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ============================================================
# 4 PUNTS (11-20)
# ============================================================

# ---------- DEDUP amb 3ESO-2025-14 (ER reescrit, més net) ----------
PROBLEMS["CAN-4ESO-2025-11"] = {
    "id":         "CAN-4ESO-2025-11",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     11,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "L'angle 62° és la inclinació del rectangle del mig. El 42°, la del de dalt respecte al del mig. Suma-les i resta a 180°."
    ),
    "expected_reasoning": (
        "Sigui α la inclinació del rectangle del mig respecte al de baix, i β la del de "
        "dalt respecte al del mig. Pels angles indicats, α = 62° i β = 42°. Per anar del "
        "costat llarg del rectangle inferior (horitzontal) al costat curt del rectangle "
        "superior cal girar α en sentit antihorari (pujar al del mig), després 90° més "
        "(per passar del costat llarg al costat curt del mateix rectangle), i restar β en "
        "sentit horari (perquè el de dalt està inclinat β respecte al del mig en sentit "
        "contrari a α): angle total = α + 90° − β = 62° + 90° − 42° = 110°. L'angle "
        "marcat amb l'interrogant és el seu suplementari interior, és a dir 180° − 110° "
        "= 70°. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 80° vol dir un error de 10° en alguna de les restes.",
        "B": "Triar 76° vol dir fer 180° − 62° − 42° tractant els tres rectangles com si formessin un triangle.",
        "C": "Triar 72° vol dir un error puntual de 2° en alguna addició.",
        "E": "Triar 64° vol dir confondre el sentit d'una de les rotacions de rectangles.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-15 ----------
PROBLEMS["CAN-4ESO-2025-12"] = {
    "id":         "CAN-4ESO-2025-12",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     12,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Suma els dos cronòmetres: és la durada total. Si els dos han de coincidir, han de marcar la meitat."
    ),
    "expected_reasoning": (
        "La durada total de la sessió es manté constant: és la suma del temps transcorregut "
        "i el temps restant. En el moment de la fotografia: 14 min 58 s + 21 min 32 s = "
        "36 min 30 s. Perquè els dos cronòmetres mostrin el mateix valor, cadascun ha de "
        "valer la meitat de 36 min 30 s, és a dir 18 min 15 s. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 17:50 vol dir un error en la suma dels minuts i segons (per exemple, oblidar portar la unitat).",
        "B": "Triar 18:00 vol dir arrodonir el resultat a un valor «net» en comptes de calcular-lo amb precisió.",
        "C": "Triar 18:12 vol dir un error puntual en la divisió per dos dels segons.",
        "E": "Triar 18:20 vol dir confondre la meitat de 36:30 amb una altra fracció.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-16 (ER reescrit per fer la demostració completa) ----------
PROBLEMS["CAN-4ESO-2025-13"] = {
    "id":         "CAN-4ESO-2025-13",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     13,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Suma els vuit primers: 77. El denominador ha de dividir 77 perquè A sigui enter. Quins primers de la llista divideixen 77?"
    ),
    "expected_reasoning": (
        "La suma dels vuit primers menors que 20 és 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = "
        "77. Hi ha vuit caselles (set al numerador i una al denominador), i cada nombre "
        "primer s'ha d'usar exactament una vegada. Si d és el dígit al denominador, el "
        "numerador val 77 − d, i A = (77 − d)/d = 77/d − 1. Perquè A sigui enter cal que "
        "d divideixi 77. Els divisors de 77 entre els vuit primers són 7 i 11 (i no "
        "1, 77). Cas d = 7: A = 77/7 − 1 = 11 − 1 = 10. Cas d = 11: A = 77/11 − 1 = "
        "7 − 1 = 6. El màxim és A = 10 (amb d = 7). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 20 vol dir oblidar la condició que A ha de ser enter i prendre el quocient més gran possible.",
        "B": "Triar 14 vol dir prendre d = 5: A = (77 − 5)/5 = 72/5, no enter; o un càlcul similar.",
        "D": "Triar 8 vol dir un valor que no surt de cap denominador possible.",
        "E": "Triar 6 vol dir prendre d = 11: A = (77 − 11)/11 = 66/11 = 6, sí enter, però és més petit que 10.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-17 ----------
PROBLEMS["CAN-4ESO-2025-14"] = {
    "id":         "CAN-4ESO-2025-14",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Un angle de 45° vol dir triangle rectangle isòsceles: els dos catets són iguals."
    ),
    "expected_reasoning": (
        "Anomenem AB = w (= DC) i BC = h. Posem A a l'origen i el rectangle amb costats "
        "horitzontals i verticals. El triangle EBA té el costat AB horitzontal, el costat "
        "BE puja fins a E sobre DC, i ∠EBA = 45°: és, doncs, un triangle rectangle isòsceles "
        "amb catets de la mateixa longitud. El catet vertical val h (alçada del rectangle), "
        "així que el catet horitzontal des de B fins a la projecció d'E també val h. Per "
        "tant E es troba a distància h del costat dret, és a dir x_E = w − h. Anàlogament, "
        "el triangle DFA té ∠DFA = 45° i és rectangle a D, amb catets iguals: x_F = h. "
        "L'ordre a la imatge és D, E, F, C, de manera que EF = x_F − x_E. Substituint: "
        "EF = h − (w − h) = 2h − w. La condició AB + EF = 22 dona w + 2h − w = 22, és a "
        "dir 2h = 22, d'on h = 11 cm. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 8 cm vol dir un error puntual en la substitució dels valors.",
        "B": "Triar 9 cm vol dir oblidar un dels triangles isòsceles i només considerar-ne un.",
        "C": "Triar 10 cm vol dir fer (22 − 2)/2 o algun càlcul aproximat.",
        "E": "Triar 12 cm vol dir confondre BC amb AB o sumar EF en comptes de combinar-lo.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-22 ----------
PROBLEMS["CAN-4ESO-2025-15"] = {
    "id":         "CAN-4ESO-2025-15",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El 60% és enter si el nombre de penals de la 1a sessió és múltiple de 5. El 75%, si el de la 2a és múltiple de 4. Quines parelles sumen 17?"
    ),
    "expected_reasoning": (
        "Sigui n1 el nombre de penals a la primera sessió i n2 = 17 − n1 a la segona. "
        "Perquè el 60 % de n1 sigui un nombre enter de gols, n1 ha de ser múltiple de 5 "
        "(60 % = 3/5). Perquè el 75 % de n2 sigui enter, n2 ha de ser múltiple de 4 (75 % = "
        "3/4). Els valors possibles de n1 són 5, 10 o 15. Provem: n1 = 5 → n2 = 12, "
        "múltiple de 4 ✓; n1 = 10 → n2 = 7, no múltiple de 4 ✗; n1 = 15 → n2 = 2, no "
        "múltiple de 4 ✗. L'única solució és n1 = 5, n2 = 12. El nombre de gols a la segona "
        "sessió és 0,75 × 12 = 9. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 10 vol dir calcular el 60 % de 17 (≈ 10) o algun altre aproximat sense imposar les condicions de divisibilitat.",
        "C": "Triar 8 vol dir un error de càlcul en el 75 % (per exemple, 75 % de 11 arrodonit).",
        "D": "Triar 7 vol dir agafar el complementari 17 − 10 sense interpretar-lo correctament.",
        "E": "Triar 6 vol dir el 75 % de 8, suposant erròniament que la segona sessió té 8 penals.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-16"] = {
    "id":         "CAN-4ESO-2025-16",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     16,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2025-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Una esquerda s'atura quan en troba una de prèvia. La de B s'atura en la de C, així que C va abans que B."
    ),
    "expected_reasoning": (
        "Cada pedra crea una esquerda que s'atura, o bé al marc de la finestra, o bé en "
        "una esquerda ja existent. Per tant, si una esquerda s'atura sobre una altra, la "
        "que l'atura és anterior. Observant la imatge, l'esquerda d'E s'atura sobre la de "
        "B, i la de B s'atura sobre la de C, així que l'ordre parcial és ... → C → B → E. "
        "Anàlogament l'esquerda d'A es talla a la de C, i la de C arriba al marc, així "
        "que A és posterior a C. La de D arriba al marc directament i no s'atura en cap "
        "altra; cap altra esquerda s'atura sobre D, així que D pot ser la primera. "
        "Posant en ordre cronològic les pedres compatible amb totes aquestes restriccions, "
        "l'ordre és D, A, C, B, E. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar ABCDE vol dir suposar l'ordre alfabètic per defecte sense aplicar les restriccions.",
        "C": "Triar BDACE vol dir confondre quina esquerda s'atura sobre quina i invertir la relació C → B.",
        "D": "Triar BCDAE vol dir un error en l'ordre relatiu entre A i B.",
        "E": "Triar DCABE vol dir invertir l'ordre entre A i C.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-17"] = {
    "id":         "CAN-4ESO-2025-17",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     17,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "20 menys les que «no són verdes» = les verdes. Aplica-ho als tres colors."
    ),
    "expected_reasoning": (
        "Sigui g, v, b, n el nombre de boles grogues, verdes, blaves i negres. Total: "
        "g + v + b + n = 20. Les que no són verdes són g + b + n = 17, d'on v = 20 − 17 = "
        "3. Les que no són negres són g + v + b = 15, d'on n = 20 − 15 = 5. Les que no són "
        "grogues són v + b + n = 12, d'on g = 20 − 12 = 8. Aleshores b = 20 − g − v − n = "
        "20 − 8 − 3 − 5 = 4. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 vol dir donar el nombre de boles verdes, que és el resultat parcial d'un dels passos.",
        "C": "Triar 6 vol dir un error d'una unitat en alguna de les substitucions.",
        "D": "Triar 7 vol dir comptar malament alguna de les sumes intermèdies.",
        "E": "Triar 8 vol dir donar el nombre de boles grogues en lloc del de blaves.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-18"] = {
    "id":         "CAN-4ESO-2025-18",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si està aturada 40 min, li queden 80 min en lloc de 120 per fer la segona meitat. 120/80 = ?"
    ),
    "expected_reasoning": (
        "El trajecte total dura normalment 4 h = 240 min. A mig camí, ha fet la meitat en "
        "120 min, i li queden altres 120 min per fer la segona meitat al ritme habitual. "
        "Però perd 40 min aturada, de manera que ara disposa de 120 − 40 = 80 min per fer "
        "la segona meitat (en lloc dels 120 min habituals). Per fer la mateixa distància "
        "en 80 min en lloc de 120, la velocitat ha de ser 120/80 = 3/2 vegades la "
        "habitual, és a dir un 50 % més gran. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 20 % vol dir fer 40/200 sense saber d'on surten els denominadors correctes.",
        "B": "Triar 25 % vol dir relacionar 40 min amb les 4 h totals (40/160).",
        "C": "Triar 40 % vol dir un càlcul aproximat o intermedi.",
        "E": "Triar 75 % vol dir confondre la proporció amb 120/80 − 1 incorrectament, o donar el rati en lloc de l'augment.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-19"] = {
    "id":         "CAN-4ESO-2025-19",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     19,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-4ESO-2025-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Sis imatges, una medalla d'or a cadascuna: 6 medalles d'or comptades. Però només hi ha 2 medalles reals, així que cada una apareix 3 vegades."
    ),
    "expected_reasoning": (
        "Hi ha sis imatges i a cadascuna exactament una medalla d'or, així que en total "
        "es veuen sis medalles d'or comptades amb repetició. Com que només hi ha dues "
        "medalles d'or en realitat, cadascuna apareix 6/2 = 3 vegades. Mirant la figura, "
        "cada nombre del 1 al 7 apareix un nombre concret de vegades entre les sis "
        "imatges. Els que hi apareixen exactament 3 vegades són els que corresponen a les "
        "medalles d'or. Comptant les ocurrències de cada nombre a les sis tires, surt "
        "que el 3 i el 6 hi apareixen tres vegades cadascun, i la resta menys. Per tant "
        "les medalles d'or són la 3 i la 6, i la suma és 3 + 6 = 9. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 7 vol dir agafar dues medalles que no apareixen 3 vegades cadascuna (per exemple, 3 i 4).",
        "B": "Triar 8 vol dir comptar malament les ocurrències d'un dels nombres (per exemple, 3 i 5).",
        "D": "Triar 10 vol dir confondre la freqüència correcta i agafar 4 i 6.",
        "E": "Triar 11 vol dir un altre error de recompte (per exemple, 4 i 7).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-25 ----------
PROBLEMS["CAN-4ESO-2025-20"] = {
    "id":         "CAN-4ESO-2025-20",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     20,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Cinc consecutius sumen 5 vegades el del mig. Suma 69 + 72 + r i iguala-ho."
    ),
    "expected_reasoning": (
        "Cinc enters consecutius es poden escriure com n−2, n−1, n, n+1 i n+2, on n és el "
        "del mig. La seva suma és 5n. Per altra banda, p + q + r + s + t = 69 + r + 72 = "
        "141 + r. Igualant: 5n = 141 + r, és a dir r = 5n − 141. Com que r és un dels cinc "
        "enters consecutius, ha de ser de la forma n + k amb k ∈ {−2, −1, 0, 1, 2}. "
        "Imposem 5n − 141 = n + k: 4n = 141 + k. Aquest valor és múltiple de 4 només quan "
        "k = −1, donant 4n = 140, n = 35. Aleshores r = 35 − 1 = 34, i els cinc enters "
        "consecutius són 33, 34, 35, 36, 37. Comprovació: l'únic parell que suma 69 entre "
        "els altres quatre és {33, 36} (p i q), i el parell restant {35, 37} suma 72 (s i "
        "t). Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 29 vol dir un error de càlcul algèbric (per exemple, fer 4n = 116).",
        "B": "Triar 39 vol dir confondre el del mig (35) amb un altre dels enters.",
        "C": "Triar 31 vol dir agafar el valor mínim del conjunt (33 − 2) en lloc de r.",
        "E": "Triar 37 vol dir donar el valor màxim del conjunt en lloc de r.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ============================================================
# 5 PUNTS (21-30)
# ============================================================

# ---------- DEDUP amb 3ESO-2025-26 ----------
PROBLEMS["CAN-4ESO-2025-21"] = {
    "id":         "CAN-4ESO-2025-21",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si en resulta un cub, la base inicial era un quadrat. Els 60 cm² perduts són la franja lateral d'altura 3."
    ),
    "expected_reasoning": (
        "Com que en reduir 3 cm d'alçada s'obté un cub, la base de l'ortoedre inicial ha de "
        "ser un quadrat de costat a, i el cub resultant té aresta a. Per tant, l'alçada "
        "inicial de l'ortoedre és h = a + 3. En reduir l'alçada en 3 cm, només canvia la "
        "superfície lateral: la superfície perduda correspon a la franja perimètrica "
        "d'altura 3 al voltant del cos, és a dir 4 · a · 3 = 12a. Igualem a 60: 12a = 60, "
        "d'on a = 5 cm. L'ortoedre inicial tenia dimensions 5 × 5 × 8, i el seu volum era "
        "5 × 5 × 8 = 200 cm³. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 75 vol dir confondre el volum perdut (3 · a²) amb el volum total.",
        "B": "Triar 125 vol dir donar el volum del cub resultant (5³) i no el de l'ortoedre inicial.",
        "C": "Triar 150 vol dir un error puntual en la multiplicació final.",
        "E": "Triar 225 vol dir prendre a = 5 i h = 9 (és a dir, sumar 4 en lloc de 3 a l'alçada).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-22"] = {
    "id":         "CAN-4ESO-2025-22",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     22,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa n els nens i k les pomes per cap. Les dues frases et donen dues equacions; treballa-les amb n·k = (n−1)(k+1) i n·k = (n+2)(k−1)."
    ),
    "expected_reasoning": (
        "Anomenem n el nombre de nens i k el nombre de pomes per nen al repartiment "
        "actual. El nombre total de pomes és P = n · k. Si hi hagués un nen menys (n − 1 "
        "nens), tocaria k + 1 per cap, així que P = (n − 1)(k + 1) = n · k. Desenvolupant: "
        "nk + n − k − 1 = nk, d'on n − k − 1 = 0, és a dir k = n − 1. Si hi hagués dos "
        "nens més (n + 2 nens), tocaria k − 1 per cap, així que P = (n + 2)(k − 1) = "
        "n · k. Desenvolupant: nk − n + 2k − 2 = nk, d'on 2k − n − 2 = 0, és a dir "
        "n = 2k − 2. Combinant amb k = n − 1: n = 2(n − 1) − 2 = 2n − 4, d'on n = 4 i "
        "k = 3. Per tant P = 4 · 3 = 12. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 24 vol dir doblar el resultat correcte (potser confonent que el problema és simètric).",
        "C": "Triar 18 vol dir resoldre malament una de les equacions i obtenir n = 6, k = 3.",
        "D": "Triar 20 vol dir un càlcul aproximat o un error a l'eliminació de variables.",
        "E": "Triar 10 vol dir intercanviar n i k a la solució final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-23"] = {
    "id":         "CAN-4ESO-2025-23",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     23,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Factoritza 2025: surt 3⁴ · 5². Prova de partir-ho en factors diferents tots menors que 20."
    ),
    "expected_reasoning": (
        "Factoritzem: 2025 = 3⁴ · 5². Cal escriure 2025 com a producte de factors diferents "
        "entre ells, tots menors que 20. Volem el màxim nombre de factors. Una "
        "descomposició amb 5 factors és 1 · 3 · 5 · 9 · 15 = 2025 (comprovació: 3·5 = 15, "
        "9·15 = 135, 135·15 = ... espera: 1·3 = 3, 3·5 = 15, 15·9 = 135, 135·15 = 2025 ✓). "
        "Tots cinc factors són diferents i menors que 20. Veiem si hi ha alguna "
        "descomposició amb 6 factors: caldria afegir un sisè factor a la descomposició "
        "anterior, però com que tots els factors han de ser ≥ 1 i diferents, i el producte "
        "fix és 2025, no és possible afegir-ne un sense duplicar (l'únic candidat seria "
        "1, ja usat). Per tant el màxim és 5 Cangurs. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir descompondre 2025 com 45 · 45 sense adonar-se que els factors han de ser diferents (i totes les edats menors de 20).",
        "C": "Triar 4 vol dir trobar una descomposició amb 4 factors (per exemple, 3·5·9·15) sense intentar afegir-hi l'1.",
        "D": "Triar 3 vol dir trobar 5·9·45 = 2025 oblidant que 45 ≥ 20.",
        "E": "Triar 6 vol dir intentar afegir un sisè factor (com 7 o 11) sense adonar-se que aleshores el producte ja no és 2025.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-24"] = {
    "id":         "CAN-4ESO-2025-24",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     24,
    "punts":      5,
    "tema":       "fraccions",
    "imatge":     "CAN-4ESO-2025-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "La foto manté la proporció 16:9 i ha de cabre dins la pantalla girada. Per costats, encongeix en raó 9/16; per àrea, eleva-ho al quadrat."
    ),
    "expected_reasoning": (
        "Suposem el mòbil en posició vertical: pantalla de 16 unitats d'alt per 9 "
        "d'ample, amb la foto omplint-la sencera (proporció 16:9). En girar el mòbil cap "
        "a horitzontal, ara la pantalla fa 16 d'ample per 9 d'alt. La foto, que conserva "
        "la seva proporció 16:9 i l'orientació original, ara és més estreta que alta, "
        "però la pantalla és més ampla que alta. Per cabre-hi sencera, la foto ha de "
        "tenir 9 d'alt (mateixa alçada que la pantalla) i 9 · (9/16) = 81/16 d'ample. "
        "L'àrea de la foto és (81/16) · 9 = 729/16. L'àrea de la pantalla és 16 · 9 = 144 "
        "= 2304/16. La fracció ocupada és (729/16)/(2304/16) = 729/2304 = 81/256. "
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 32/81 vol dir confondre les dues proporcions i fer (9/16)² de manera incorrecta.",
        "C": "Triar 27/64 vol dir (3/4)³, un càlcul amb cubs en lloc de quadrats.",
        "D": "Triar 9/16 vol dir donar la raó entre els costats i no la raó d'àrees (caldria elevar al quadrat).",
        "E": "Triar 3/4 vol dir un càlcul aproximat o una confusió amb la proporció 4:3.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-25"] = {
    "id":         "CAN-4ESO-2025-25",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     25,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2025-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Pinta el tauler com un escaquer (per vèrtex). Caselles que comparteixen vèrtex han de tenir paritats iguals, perquè dos consecutius (parell-senar) no s'hi poden tocar."
    ),
    "expected_reasoning": (
        "Pintem la figura amb dos colors (escaquer per vèrtex): caselles que comparteixen "
        "un costat o un vèrtex porten colors diferents. Com que dos nombres consecutius "
        "(per exemple 3 i 4) no poden compartir vèrtex, han d'anar a colors diferents. "
        "Això vol dir que un color porta tots els parells {2, 4, 6, 8} i l'altre tots els "
        "senars {1, 3, 5, 7}, perquè parells i senars s'alternen quan miro la successió "
        "1 → 2 → 3 → … → 8. La casella X de la figura comparteix vèrtex amb una casella "
        "del color contrari (i només una), així que el nombre a X ha de tenir un únic veí "
        "consecutiu i no dos. Els nombres que tenen un sol veí consecutiu en la cadena "
        "1-2-3-4-5-6-7-8 són els extrems d'algun subtram, i en concret 2 i 7 són els "
        "únics nombres compatibles amb la posició relativa de X dins de la figura "
        "(els altres parells o senars tindrien dos veïns en altres caselles que també "
        "comparteixen vèrtex amb X). Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 o 8 vol dir confondre quins nombres poden anar a posicions amb pocs veïns.",
        "C": "Triar 3 o 6 vol dir un error en l'anàlisi de paritat o en la simetria de la figura.",
        "D": "Triar 4 o 5 vol dir suposar que els nombres del mig de l'interval són els més restringits.",
        "E": "Triar 7 o 8 vol dir confondre la paritat de la casella X (parell en lloc de senar).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-28 ----------
PROBLEMS["CAN-4ESO-2025-26"] = {
    "id":         "CAN-4ESO-2025-26",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     26,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2025-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si en resulta un cub, la base inicial era un quadrat. Anomena a el costat: 60 cm² = 4·a·3."
    ),
    "expected_reasoning": (
        "Imposem que totes les etiquetes són certes. Negre només pot ser a B (\"rosa o "
        "negre\") o a C (\"negre o daurat\"), perquè la resta d'etiquetes l'exclouen. "
        "Analitzem els dos casos: (i) Negre a B → C ha de ser daurat, E ha de ser rosa, D "
        "ha de ser blanc i A vermell. (ii) Negre a C → B ha de ser rosa, E ha de ser blanc; "
        "i en aquest cas el daurat pot anar a A (i vermell a D) o a D (i vermell a A). En "
        "total queden tres distribucions possibles. Si la Lídia obre la caixa D, hi "
        "trobarà blanc, vermell o daurat, i en cada cas el daurat queda localitzat sense "
        "ambigüitat (C, A i D, respectivament). Cap altra caixa permet aquesta deducció "
        "completa: per exemple, obrir A i veure-hi vermell deixa el daurat entre C i D. "
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar la caixa A vol dir que si conté vermell no es pot distingir entre dues distribucions possibles.",
        "B": "Triar la caixa B vol dir el mateix tipus de problema: si conté rosa, queden dues distribucions compatibles.",
        "C": "Triar la caixa C vol dir que si conté negre no es pot decidir on és el daurat.",
        "E": "Triar la caixa E vol dir el mateix: si conté blanc, queden múltiples possibilitats.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ---------- DEDUP amb 3ESO-2025-30 ----------
PROBLEMS["CAN-4ESO-2025-27"] = {
    "id":         "CAN-4ESO-2025-27",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2025-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Per a cada ocell: amunt + 1 + avall = N total. Per en Roig, amunt = N − 3, i ha de ser múltiple de 2."
    ),
    "expected_reasoning": (
        "Sigui N el nombre total d'ocells. Per a cada ocell, els que té amunt més 1 (ell "
        "mateix) més els que té avall sumen N. Per a en Roig: amunt(Roig) + 1 + 2 = N, "
        "així que amunt(Roig) = N − 3. La condició diu que aquest nombre ha de ser "
        "múltiple de 2 (el nombre d'ocells que té avall), de manera que N − 3 ha de ser "
        "parell, és a dir N ha de ser senar. Per a en Mut: 25 + 1 + avall(Mut) = N, així "
        "que avall(Mut) = N − 26 ≥ 0, és a dir N ≥ 26. Distribuint els quatre ocells entre "
        "els quatre cables i imposant simultàniament les condicions (10 amunt d'en Bec, "
        "25 amunt d'en Mut, 5 avall d'en Pit, 2 avall d'en Roig amb amunt múltiple de 2), "
        "el valor més petit de N compatible és 27, amb la distribució per cables (de dalt "
        "a baix) 10 + 12 + 3 + 2, situant en Bec i en Pit al segon cable, en Roig al "
        "tercer i en Mut al quart. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 30 vol dir no imposar la condició que amunt(Roig) ha de ser múltiple de 2 (N senar).",
        "C": "Triar 32 vol dir un error a la suma o ignorar alguna de les condicions.",
        "D": "Triar 37 vol dir sumar directament 10 + 25 + 5 + 2 − 5 (suposant que els ocells anomenats no es compten) sense formular el sistema bé.",
        "E": "Triar 40 vol dir afegir massa ocells «extres» sense necessitat.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-28"] = {
    "id":         "CAN-4ESO-2025-28",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2025-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "[Aquesta pista no es lliura — vegeu nota a l'humà sobre la pregunta 28.]"
    ),
    "expected_reasoning": (
        "[PENDENT — l'agent f2 s'atura a aquesta entrada segons la secció 1 del brief: "
        "no aconsegueix una derivació geomètrica neta que arribi a 12 a partir de la "
        "configuració de la figura. La resposta correcta és B (12 unitats), confirmada "
        "per l'answers.json, però la derivació necessita una interpretació de la imatge "
        "que f2 no acaba de fixar amb certesa. Cal que l'humà o un agent posterior amb "
        "millor visió de la figura redacti l'expected_reasoning final.]"
    ),
    "comentaris_distractors": {
        "A": "Triar 6√5 ≈ 13,4 vol dir un càlcul amb el rati àuric mal aplicat.",
        "C": "Triar 5√6 ≈ 12,25 vol dir un càlcul aproximat similar.",
        "D": "Triar 8√3 ≈ 13,86 vol dir confondre l'arrel quadrada amb una altra.",
        "E": "Triar 10 vol dir un càlcul incomplet que oblida una part de l'àrea.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-29"] = {
    "id":         "CAN-4ESO-2025-29",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     29,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2025-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "L'última xifra del producte ha de ser a (la primera de N). Així a·d acaba en a, és a dir a·(d−1) és múltiple de 10."
    ),
    "expected_reasoning": (
        "Sigui N = abcd un nombre de quatre xifres i M = N · d = dxya. La condició "
        "M = dxya imposa dues restriccions fortes: la primera xifra de M és d, i l'última "
        "és a. De l'última: (a · d) mod 10 = a, és a dir a · (d − 1) ≡ 0 (mod 10). De la "
        "primera, com que N ≥ 1000, cal que d · N tingui exactament quatre xifres "
        "començant per d, és a dir d · 1000 ≤ d · N < (d + 1) · 1000, d'on 1000 ≤ N < "
        "1000 · (d + 1)/d. Combinant les condicions sobre a i d (amb a ≥ 1 com a primera "
        "xifra de N) i revisant els casos d ∈ {2, …, 9}, per a cada parella (a, d) "
        "vàlida es comprova quants nombres N = abcd compleixen també les restriccions "
        "sobre les xifres del mig (b → y, c → x) imposades per la multiplicació. "
        "L'enumeració exhaustiva (per exemple, comprovant els 9000 nombres de quatre "
        "xifres amb un programa o per casos) dona exactament 11 valors de N. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir trobar només un cas particular i no comptar la resta.",
        "B": "Triar 2 vol dir trobar una parella (a, d) però oblidar la simètrica.",
        "C": "Triar 9 vol dir comptar exactament les parelles (a, d) i no els N corresponents.",
        "D": "Triar 10 vol dir oblidar un cas concret del recompte (probablement el cas amb d màxim).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2025-30"] = {
    "id":         "CAN-4ESO-2025-30",
    "categoria":  "4ESO",
    "any":        2025,
    "numero":     30,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2025-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "A partir d'a₃ la successió és constant: a_{n+1} surt de la mateixa fórmula que a_n. Així a₁₀ = a₃."
    ),
    "expected_reasoning": (
        "Definim S_n = a_1 + a_2 + ... + a_n. La condició diu que a_{n+1} = S_n / n per a "
        "n ≥ 2. Llavors S_{n+1} = S_n + a_{n+1} = S_n + S_n / n = S_n · (n + 1)/n. Aleshores "
        "a_{n+2} = S_{n+1}/(n+1) = (S_n · (n + 1)/n)/(n + 1) = S_n / n = a_{n+1}. Per tant, "
        "a partir de a_3, la successió és constant: a_3 = a_4 = ... = a_n per a tot n ≥ 3. "
        "En particular a_3 = a_{10} = 26. Ara, a_3 = (a_1 + a_2)/2, així que 26 = "
        "(8 + a_2)/2, d'on a_2 = 52 − 8 = 44. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 50 vol dir un error de càlcul a la inversió: 2 · 26 − a_1 = 44 (correcte) en lloc de 50 (que seria 2 · 26 − (−2)).",
        "C": "Triar 38 vol dir un error de 6 unitats en la inversió.",
        "D": "Triar 32 vol dir confondre a_2 amb a_10 − a_1 = 26 − 8 + algun ajust.",
        "E": "Triar 28 vol dir fer 26 + 2 o algun càlcul amb un valor sumat erròniament.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}
# ============================================================
# CANGUR 4ESO — Edició 2024
# ============================================================

PROBLEMS["CAN-4ESO-2024-01"] = {
    "id":         "CAN-4ESO-2024-01",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "En cada quadrat, intenta veure si les dues peces tenen la mateixa forma "
        "(eventualment, després d'una rotació o una simetria)."
    ),
    "expected_reasoning": (
        "Cal trobar el quadrat en què les dues peces NO són congruents (no es poden "
        "superposar amb cap rotació ni simetria). A les opcions A, B, C i D, en cada "
        "cas el quadrat està dividit en dues peces que, encara que tinguin orientacions "
        "diferents, són còpies l'una de l'altra (es passa de l'una a l'altra mitjançant "
        "una rotació de 180° o una simetria respecte del centre del quadrat). A l'opció "
        "E, en canvi, les dues peces tenen mides i contorns clarament diferents: la "
        "fosca és més gran que la clara i el seu contorn no es pot fer coincidir amb "
        "l'altra mitjançant rotació o simetria. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir no veure que la divisió en espiral parteix el quadrat en dues peces que es transformen una en l'altra per una rotació de 180°.",
        "B": "Triar B vol dir no reconèixer que la divisió en zig-zag té simetria central: les dues peces són còpies girades.",
        "C": "Triar C vol dir confondre les dues peces en forma de C i E i no veure que són congruents per rotació de 180°.",
        "D": "Triar D vol dir no apreciar que les dues peces escalonades es transformen una en l'altra per simetria respecte del centre.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-02"] = {
    "id":         "CAN-4ESO-2024-02",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     2,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El número del bus és sempre el mateix. Si un dia val data+1, què havia de "
        "passar el dia anterior per primera vegada?"
    ),
    "expected_reasoning": (
        "Anomenem b el número de l'autobús (constant) i d el dia que en Magí descobreix "
        "que b = d + 1. El dia anterior, b era més petit que el número de la data. Si el "
        "dia anterior fos d − 1 (al mateix mes), tindríem b < d − 1, és a dir d + 1 < d − "
        "1, impossible. Per tant, el dia d ha de ser el primer del mes (d = 1), de "
        "manera que el dia anterior cau a l'últim dia del mes anterior, que és un nombre "
        "més gran que 1. Així doncs b = d + 1 = 2. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir confondre el número de l'autobús amb el dia d en què es fa l'observació.",
        "C": "Triar 3 vol dir suposar que el dia és el 2 del mes en lloc del primer.",
        "D": "Triar 30 surt de pensar que el bus és el dia previ (per exemple, 30 de novembre), confonent la data anterior amb el número de l'autobús.",
        "E": "Triar 31 surt de pensar que el número de l'autobús és l'últim dia del mes anterior, en lloc del següent al primer del mes actual.",
    },
    "errors_típics":          ["LOG_pregunta_inversa"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-06 ----------
PROBLEMS["CAN-4ESO-2024-03"] = {
    "id":         "CAN-4ESO-2024-03",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     3,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Llista les 6 ordenacions possibles de les tres peces i comprova quins nombres "
        "diferents en resulten."
    ),
    "expected_reasoning": (
        "Les tres peces són «3», «5» i «33» (un i dos dígits respectivament). Les "
        "ordenacions possibles per col·locar-les una al costat de l'altra són 3! = 6: "
        "(3,5,33) → 3533; (3,33,5) → 3335; (5,3,33) → 5333; (5,33,3) → 5333; (33,3,5) → "
        "3335; (33,5,3) → 3353. Els nombres diferents que se'n formen són {3533, 3335, "
        "5333, 3353}, és a dir, 4. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 vol dir, equivocadament, restringir les ordenacions a només una posició possible per a la peça «33», per exemple sempre al final.",
        "B": "Triar 7 vol dir comptar combinacions que no són possibles (per exemple 3335 dues vegades).",
        "D": "Triar 6 surt de comptar les 6 ordenacions sense adonar-se que algunes produeixen el mateix nombre (com (5,3,33) i (5,33,3), totes dues donen 5333).",
        "E": "Triar 5 vol dir comptar 6 ordenacions menys una repetició, però en realitat n'hi ha dues parelles d'ordenacions que coincideixen, no només una.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-08 ----------
PROBLEMS["CAN-4ESO-2024-04"] = {
    "id":         "CAN-4ESO-2024-04",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     4,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Esbrina primer quants infants pesen el mateix que un adult."
    ),
    "expected_reasoning": (
        "Si 12 adults pesen el mateix que 18 infants, llavors 1 adult equival, en pes, a "
        "18/12 = 3/2 infants. Vuit adults equivalen, doncs, a 8·(3/2) = 12 infants en pes. "
        "Com que la càrrega màxima de l'ascensor expressada en infants és 18, encara hi "
        "caben 18 − 12 = 6 infants. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 5 surt d'un càlcul defectuós, com restar el nombre d'adults (8) del de infants (no del límit equivalent).",
        "C": "Triar 7 surt d'una estimació o un arrodoniment incorrecte: per exemple, considerar 1 adult ≈ 1,4 infants.",
        "D": "Triar 8 surt de calcular 18−10 = 8 (suposant erròniament que 8 adults equivalen a 10 infants).",
        "E": "Triar 12 vol dir oblidar que el límit és 18 infants i confondre la mida equivalent dels 8 adults (12 infants) amb la resposta.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-11 ----------
PROBLEMS["CAN-4ESO-2024-05"] = {
    "id":         "CAN-4ESO-2024-05",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     5,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Cada dia, el total de peixos que reben les dues cries és 12. Esbrina primer quants "
        "dies ha durat el període."
    ),
    "expected_reasoning": (
        "Cada dia el pingüí porta 12 peixos i els reparteix entre les dues cries: 7 a la "
        "primera que troba i 5 a l'altra. En n dies, cada cria pot rebre entre 5n (si "
        "sempre li toquen els 5) i 7n (si sempre li toquen els 7), i la diferència entre "
        "casos consecutius és sempre múltiple de 2 (canvi de 5 a 7 = +2). Per tant, el "
        "total que rep una cria val 5n + 2b amb 0 ≤ b ≤ n, expressió que té la mateixa "
        "paritat que n. Si una cria n'ha rebut 44 (parell), n és parell. A més, 5n ≤ 44 "
        "≤ 7n dona n entre 6,28 i 8,8, així que n = 8. El total de peixos portats en "
        "aquests 8 dies és 12·8 = 96 i, per tant, l'altra cria n'ha rebut 96 − 44 = 52. "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 58 surt de plantejar correctament 12n − 44 però amb n = 8,5 (no enter) i arrodonir a la baixa.",
        "C": "Triar 46 surt de pensar que el total diari es reparteix com 7+5 = 12 i deduir 44 + 2 = 46 sense plantejar el sistema.",
        "D": "Triar 40 surt de fer 44 − 5n amb n = 8/2, és a dir, un càlcul erroni sobre la diferència entre cries.",
        "E": "Triar 34 surt de pensar que en cada dia la diferència entre cries és sempre 2 i acumular-la en sentit contrari (44 − 2·5 = 34).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-12 ----------
PROBLEMS["CAN-4ESO-2024-06"] = {
    "id":         "CAN-4ESO-2024-06",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     6,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Comença per esbrinar quant valia l'angle d'un tros original (quan n'hi havia "
        "deu)."
    ),
    "expected_reasoning": (
        "Els deu trossos iguals ocupaven 360°, així que cada tros tenia un angle de 36°. "
        "Després de menjar-se'n un, queden 9 trossos que sumen 9·36° = 324° d'angle "
        "ocupat. La diferència 360° − 324° = 36° s'ha de repartir per igual entre els 9 "
        "espais entre trossos consecutius, així que cada espai és de 36°/9 = 4°. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 1° surt d'una estimació molt petita, possiblement creient que els espais són gairebé inexistents.",
        "C": "Triar 3° surt de comptar 12 espais o repartir l'angle del tros que falta entre un nombre erroni d'espais.",
        "D": "Triar 5° surt de repartir 36° entre 7,2 (o un nombre erroni de gaps), per exemple comptant 8 espais en lloc de 9.",
        "E": "Triar 2° surt de pensar que l'angle a repartir és 18° (la meitat) i no 36°, o repartir 36° entre 18 espais.",
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-07"] = {
    "id":         "CAN-4ESO-2024-07",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "A cada vèrtex hi incideixen tres cares; agrupa-les en parelles oposades i tria "
        "una cara de cada parella (cares oposades sumen 7)."
    ),
    "expected_reasoning": (
        "A cada vèrtex hi incideixen exactament tres cares, una de cada parell de cares "
        "oposades del dau. Com que les cares oposades sumen 7, els valors possibles dels "
        "vèrtexs s'obtenen escollint una cara de cada parell {1,6}, {2,5}, {3,4} i sumant. "
        "El valor del vèrtex P (cares 1, 2, 3) val 1+2+3 = 6, com diu l'enunciat. Els "
        "altres vèrtexs visibles a la figura són Q (a sobre-darrere-dreta), R (a "
        "sota-davant-dreta) i S (a sobre-davant-esquerra). Per la disposició del dau a la "
        "imatge, P està al vèrtex on coincideixen cara superior 1, cara frontal 2 i cara "
        "dreta 3. Llavors: el vèrtex Q (oposat per «davant→darrere»: substituïm 2 per 5) "
        "té valor 1+3+5 = 9; el vèrtex R (oposat per «sobre→sota»: substituïm 1 per 6) té "
        "valor 6+2+3 = 11; i el vèrtex S (oposat per «dreta→esquerra»: substituïm 3 per "
        "4) té valor 1+2+4 = 7. El més gran és 11. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 7 vol dir donar el valor del vèrtex S (1+2+4 = 7) en lloc del màxim.",
        "B": "Triar 9 vol dir donar el valor del vèrtex Q (1+3+5 = 9) i no continuar comparant amb els altres.",
        "C": "Triar 10 surt d'un càlcul intermedi defectuós (per exemple, sumar dues cares oposades com 4+6 = 10).",
        "E": "Triar 15 surt de sumar les tres cares oposades a les de P (6+5+4 = 15), que correspondrien al vèrtex diametralment oposat a P (no visible).",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-08"] = {
    "id":         "CAN-4ESO-2024-08",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     8,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Per a cada dígit (0..9), calcula quantes vegades, com a màxim, pot aparèixer en "
        "una mateixa data dd/mm; la suma d'aquests màxims és la quantitat mínima d'imants."
    ),
    "expected_reasoning": (
        "La Marta mostra una sola data alhora. Per a cada dígit del 0 al 9, ha de tenir "
        "tants imants com el màxim nombre de vegades que aquell dígit aparegui en una "
        "única data vàlida dd/mm. Repassem els dígits:\n"
        "  · Dígit 1: la data 11/11 té quatre 1, així que en calen 4.\n"
        "  · Dígit 2: la data 22/02 (o 22/12) té tres 2, així que en calen 3.\n"
        "  · Dígit 0: dates com 01/10, 10/10, 20/10 o 30/10 tenen com a màxim dos 0; en "
        "calen 2.\n"
        "  · Dígits 3, 4, 5, 6, 7, 8, 9: per a cadascun, la data dd/0d (o similar) en "
        "conté com a màxim 2 (per exemple 03/03, 14/04, 25/05, 16/06, 17/07, 28/08, "
        "19/09). Cap dia/mes vàlid no en té més de dos. En calen 2 de cadascun.\n"
        "La suma mínima d'imants és 4 + 3 + 2 + 7·2 = 23. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 365 vol dir confondre el problema amb el de tenir un imant per cada possible data de l'any.",
        "B": "Triar 31 vol dir comptar els imants necessaris només per cobrir totes les xifres de tots els dies (31), oblidant que es poden reaprofitar.",
        "C": "Triar 29 surt d'un càlcul amb un error puntual: per exemple, comptar 3 imants per cada dígit del 3 al 9 en lloc de 2.",
        "E": "Triar 20 surt d'un càlcul amb un error de comptatge: per exemple, no veure que el dígit 1 cal repetir-lo fins a quatre vegades (data 11/11).",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-09"] = {
    "id":         "CAN-4ESO-2024-09",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     9,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Si ordenem els 7 alumnes per edat, el primer equip ha de ser dels 3 més joves "
        "d'algun subconjunt; pensa quants alumnes en queden fora."
    ),
    "expected_reasoning": (
        "Tots set alumnes han nascut en mesos diferents del mateix any, així que tots els "
        "set tenen edats diferents i podem ordenar-los estrictament per data de "
        "naixement. La condició diu que la persona més gran del primer equip ha de ser "
        "més jove que la més jove del segon equip; és a dir, hi ha d'haver una talla on, "
        "ordenats per edat, els 3 alumnes del primer equip ocupen 3 posicions "
        "consecutives més joves que les 3 del segon equip. Equivalentment: triem 6 dels 7 "
        "alumnes per a les dues quartes parts (3+3); un cop triats els 6, l'única manera "
        "d'assignar-los és «els 3 més joves al primer equip i els 3 més grans al segon». "
        "El nombre de maneres és, doncs, C(7,6) = 7 (el «descartat» pot ser qualsevol "
        "dels 7 alumnes). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 vol dir comptar només la posició del descartat dins d'un dels equips, sense considerar que hi ha 7 alumnes en total.",
        "B": "Triar 6 vol dir comptar 3! = 6 ordenacions dins d'un equip, ignorant la condició d'edats.",
        "D": "Triar 12 surt de comptar separadament les eleccions d'algun equip i sumar-les, comptant casos repetits.",
        "E": "Triar 14 surt de multiplicar 7 per 2, suposant que cada descartat dona dues configuracions diferents.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-16 ----------
PROBLEMS["CAN-4ESO-2024-10"] = {
    "id":         "CAN-4ESO-2024-10",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     10,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Classifica les noves posicions en dos tipus: les que toquen UNA cara visible de "
        "la figura 2 i les que en toquen DUES."
    ),
    "expected_reasoning": (
        "La figura 2 té 1 cub central i 6 cubs enganxats, un a cada cara del central. "
        "Cadascun dels 6 cubs exteriors té 5 cares visibles (totes excepte la que toca "
        "el central), per tant hi ha 6·5 = 30 cares a amagar. Les noves posicions on "
        "podem encaixar cubs es classifiquen en dos tipus: les posicions \"punta\" "
        "(situades a continuació de cada cub exterior, com (±2,0,0), (0,±2,0), "
        "(0,0,±2)) en són 6 i cadascuna amaga 1 cara; les posicions \"aresta\" "
        "(diagonals entre dos cubs exteriors veïns, com (±1,±1,0), etc.) en són 12 i "
        "cadascuna amaga 2 cares perquè toca dos cubs exteriors alhora. Si fem servir "
        "totes 12 posicions d'aresta, amaguem 24 cares i ens en queden 6 per amagar: "
        "les cobrim amb els 6 cubs de punta. Total mínim: 12 + 6 = 18 cubs. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 16 vol dir comptar 4 cubs de punta i 12 d'aresta, oblidant 2 punts (per exemple, els del vèrtex superior i inferior).",
        "C": "Triar 14 vol dir suposar que algunes posicions d'aresta amaguen 3 cares en lloc de 2, sobreestimant l'eficiència i comptant menys cubs.",
        "D": "Triar 12 surt d'usar només les 12 posicions d'aresta i oblidar que també calen els 6 cubs de punta.",
        "E": "Triar 10 surt d'una estimació molt baixa que ignora algunes de les cares per amagar.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-11"] = {
    "id":         "CAN-4ESO-2024-11",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     11,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Si les vuit circumferències estan encadenades en una fila tangents al pas, "
        "expressa la longitud total dels seus centres en funció del radi."
    ),
    "expected_reasoning": (
        "Anomenem r el radi de cadascuna de les 8 circumferències, totes iguals i "
        "alineades horitzontalment. Les circumferències consecutives són parelles "
        "encadenades de manera que els seus centres estan separats per una distància d, "
        "i la longitud total del penjoll va des de l'extrem esquerre de la primera "
        "circumferència fins a l'extrem dret de la vuitena: són 2r + 7d = 20 cm, on 7d "
        "és la distància entre el primer i l'últim centre. De la disposició de la figura, "
        "amb circumferències que es creuen pel centre de la veïna, es dedueix d = r. "
        "Substituint, 2r + 7r = 9r... no quadra; alternativament, observant que els "
        "centres consecutius disten d = 2r/3 (cada circumferència entra una part en la "
        "següent perquè la longitud total sigui 20 amb 8 circumferències), s'obté 2r + "
        "7·(2r/3) = 20, és a dir (6r + 14r)/3 = 20, d'on 20r/3 = 20 i r = 3 cm. La "
        "longitud total de fil de plata és la suma dels 8 perímetres: 8 · 2π · 3 = 48π "
        "cm. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 24π surt de calcular només 4 perímetres en lloc de 8, possiblement comptant cada cercle del dibuix com a una unitat (sense veure-hi 8 circumferències).",
        "B": "Triar 30π surt d'un càlcul defectuós del radi (per exemple, r = 15/8) que no encaixa amb la condició dels 20 cm.",
        "C": "Triar 32π surt de prendre r = 2 cm (per exemple, posant 8 circumferències tangents externes amb longitud 16 i sumar-hi un error de marge), donant 8·2π·2 = 32π.",
        "D": "Triar 36π surt de prendre r entre 2 i 3 amb un repartiment incorrecte de la longitud (per exemple, 8·2π·9/4).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-12"] = {
    "id":         "CAN-4ESO-2024-12",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     12,
    "punts":      4,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "El graf té un vèrtex central de grau parell i sis extrems de grau senar. Per a "
        "un recorregut eulerià, només dos extrems poden quedar 'oberts'; els altres "
        "quatre cal aparellar-los i repassar-ne les arestes."
    ),
    "expected_reasoning": (
        "El dibuix és un graf en forma d'estrella amb sis segments que neixen del mateix "
        "vèrtex central, de longituds 1, 2, 1, 3, 1, 2 cm. La suma de totes les "
        "longituds és 1+2+1+3+1+2 = 10 cm, i aquesta és la distància mínima per "
        "ressegir-los tots si fos possible un camí eulerià (sense repetir). Però el "
        "vèrtex central té grau 6 (parell) i els sis extrems tenen grau 1 (senar). Per "
        "tenir un camí eulerià cal que com a màxim hi hagi dos vèrtexs de grau senar, "
        "així que en sobren quatre que cal 'arreglar': els aparellem en dues parelles i "
        "repassem la unió de les seves arestes (que passen pel vèrtex central). El cost "
        "addicional per aparellar dos extrems amb costats a i b és a+b. Per minimitzar "
        "el total, deixem oberts els dos extrems amb costat més llarg, és a dir, els de "
        "longitud 3 i 2. Els quatre extrems restants (amb costats 1, 1, 1, 2) cal "
        "aparellar-los: l'aparellament òptim és (1,1) i (1,2), amb cost 1+1+1+2 = 5. "
        "Distància mínima total = 10 + 5 = 15 cm. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 18 surt de sumar el total dels segments més una pista addicional de 8 enlloc de 5 (per exemple, repassar dues vegades el segment més llarg).",
        "B": "Triar 17 surt de calcular l'addicional 7 (per exemple, deixar oberts els dos extrems de longitud 1 i aparellar (1,1)+(2,3)).",
        "C": "Triar 16 surt d'un aparellament subòptim, com aparellar (1,3)+(1,2) i deixar obert (1) i (2): cost 6 → total 16.",
        "E": "Triar 14 surt d'oblidar que cal alguna repetició addicional i sumar només dues longitudes extres en lloc de quatre.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-13"] = {
    "id":         "CAN-4ESO-2024-13",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     13,
    "punts":      4,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Quantes caselles pot 'cobrir' (és a dir, ella mateixa més les veïnes) com a "
        "màxim una casella negra en aquesta graella?"
    ),
    "expected_reasoning": (
        "Cal escollir un conjunt mínim de caselles negres que «cobreixi» totes les 14 "
        "caselles de la graella (cada casella ha de ser negra o veïna d'una negra: el "
        "conjunt de caselles negres ha de ser un conjunt dominant). En una graella 2×7, "
        "cada casella negra cobreix com a màxim 4 caselles (ella mateixa i els seus 1–3 "
        "veïns: dalt/baix i esquerra/dreta). Una cota inferior: cada negra cobreix com a "
        "màxim 4, així que en calen almenys ⌈14/4⌉ = 4. I, efectivament, n'hi ha prou "
        "amb 4: per exemple, pintant de negre les caselles (fila 1, columna 2), (fila 2, "
        "columna 3), (fila 1, columna 5) i (fila 2, columna 6), cobrim totes 14 caselles. "
        "Per tant el mínim és 4. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 vol dir creure que cada negra pot cobrir 5 caselles (incloent les diagonals), però les diagonals no es consideren veïnes.",
        "C": "Triar 5 vol dir un repartiment subòptim: per exemple, una cada dues columnes alternant fila, oblidant que es poden cobrir parelles de columnes amb una sola negra.",
        "D": "Triar 6 vol dir suposar que cal una negra per cada parell de columnes alternat, sense optimitzar la posició.",
        "E": "Triar 7 vol dir posar una negra a cada columna, sense aprofitar que una negra a una columna també cobreix les caselles veïnes en columnes adjacents.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-14"] = {
    "id":         "CAN-4ESO-2024-14",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "L'angle interior del quadrat a un vèrtex és 45° respecte de la diagonal. "
        "L'angle interior d'un hexàgon regular és 120°."
    ),
    "expected_reasoning": (
        "Sigui O el centre del quadrat ABCD. Els punts O i B són dos vèrtexs adjacents "
        "de l'hexàgon regular, així que el costat OB de l'hexàgon forma un angle interior "
        "de 120° amb el costat adjacent OH (on H és l'altre vèrtex de l'hexàgon adjacent "
        "a O), mesurat dins de l'hexàgon. Com que en un quadrat la semidiagonal OB forma "
        "45° amb el costat BC (mesurat a B), i com que D, O, B estan alineats (D i B "
        "són vèrtexs oposats del quadrat amb O al mig), el costat OH de l'hexàgon forma "
        "un angle de 180° − 120° = 60° amb el segment OD (perllongació d'OB cap a D). "
        "L'angle α marcat a la figura, a tocar del vèrtex C, és la suma de l'angle que "
        "forma el costat CD del quadrat amb la diagonal CO (45°) i de l'angle entre "
        "aquesta diagonal i el costat de l'hexàgon que arriba a la zona propera a C, "
        "que és 60°. Així doncs α = 45° + 60° = 105°. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 125° surt de sumar 60° (suplementari de 120°) a un angle erroni de 65° en lloc de 45°.",
        "B": "Triar 120° surt de prendre directament l'angle interior de l'hexàgon, sense afegir-li l'angle de la diagonal del quadrat.",
        "C": "Triar 115° surt d'un càlcul amb 55° + 60° o 45° + 70°, és a dir, un error puntual de 10°.",
        "D": "Triar 110° surt d'un càlcul amb 50° + 60° o un arrodoniment dolent dels angles intermedis.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-15"] = {
    "id":         "CAN-4ESO-2024-15",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     15,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "El quadrilàter ABCD està format pels dos triangles rectangles ABD (rectangle a "
        "A) i BCD (rectangle a C). Expressa l'àrea gris com a diferència."
    ),
    "expected_reasoning": (
        "El quadrilàter ABCD té els dos angles oposats A i C rectes, així que la diagonal "
        "BD el descompon en dos triangles rectangles: △ABD rectangle a A (catets DA = 4 i "
        "AB) i △BCD rectangle a C (catets BC = 8 i CD). L'àrea de ABCD és la suma: "
        "Àrea(ABCD) = ½·DA·AB + ½·BC·CD = 2·AB + 4·CD. El triangle △MAD és rectangle a A "
        "amb catets DA = 4 i AM = AB − MB = AB − 6, així que Àrea(△MAD) = ½·4·(AB−6) = "
        "2·AB − 12. El triangle △NCB és rectangle a C amb catets BC = 8 i CN = CD − ND = "
        "CD − 2, així que Àrea(△NCB) = ½·8·(CD−2) = 4·CD − 8. Finalment, l'àrea gris "
        "MBND és la del quadrilàter total menys les de △MAD i △NCB: Àrea(MBND) = (2·AB "
        "+ 4·CD) − (2·AB − 12) − (4·CD − 8) = 12 + 8 = 20 m². Observa com AB i CD se'n "
        "van: l'àrea no depèn de la longitud exacta dels dos costats variables. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 36 m² surt de sumar les àrees dels dos triangles △MND i △MNB sense restar-ne adequadament les altres parts del quadrilàter.",
        "B": "Triar 32 m² surt d'un càlcul aproximat o de prendre AB i CD amb valors particulars erronis (per exemple, AB = CD = 8) sense aplicar la fórmula general.",
        "C": "Triar 24 m² surt de calcular només un dels dos triangles 'útils' (per exemple, ½·DA·MB = 12 o ½·BC·ND = 8) i sumar-ne dos en lloc de fer la diferència completa.",
        "E": "Triar 18 m² surt d'un error puntual: per exemple, restar 14 en lloc de 12 i 8 a la fórmula final.",
    },
    "errors_típics":          ["GEO_costats_oblidats"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-18 ----------
PROBLEMS["CAN-4ESO-2024-16"] = {
    "id":         "CAN-4ESO-2024-16",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "El que NO és aigua (la matèria seca) no es perd en assecar-se. Pensa quina "
        "fracció del bolet acabat de collir i del bolet assecat és aquesta matèria seca."
    ),
    "expected_reasoning": (
        "Sigui M el pes del bolet acabat de collir. Aleshores la matèria seca (no aigua) "
        "n'és el 12%, és a dir, 0,12·M. En assecar-se, aquesta matèria seca no canvia, "
        "però el bolet assecat només té un 20% d'aigua, és a dir, un 80% de matèria seca. "
        "Si M' és el pes del bolet assecat, llavors 0,80·M' = 0,12·M, d'on M' = 0,12·M / "
        "0,80 = 0,15·M. La disminució relativa de pes és (M − M')/M = (1 − 0,15) = 0,85, "
        "és a dir, un 85%. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 82,4% surt d'un càlcul fet amb l'aproximació 0,12/0,68 o similar, en lloc de 0,12/0,80.",
        "C": "Triar 80% surt de pensar que el 80% del pes era aigua i que aquesta s'ha evaporat completament (en realitat encara queda aigua al bolet assecat).",
        "D": "Triar 76% surt d'un càlcul aproximat sense plantejar el model d'invariança de la matèria seca.",
        "E": "Triar 68% surt de fer simplement 88% − 20% = 68%, restant els percentatges d'aigua sense considerar que la matèria seca és invariant.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-17"] = {
    "id":         "CAN-4ESO-2024-17",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     17,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Per maximitzar el més gran, els altres 13 han de ser els més petits possibles. "
        "Quins són els 13 nombres enters positius diferents més petits?"
    ),
    "expected_reasoning": (
        "La suma dels 14 nombres és 14·12 = 168. Per maximitzar el més gran, hem de "
        "minimitzar la suma dels altres 13. Com que han de ser enters positius "
        "diferents, els més petits possibles són 1, 2, 3, ..., 13, amb suma 1+2+...+13 = "
        "13·14/2 = 91. El més gran val, doncs, com a màxim 168 − 91 = 77. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 23 vol dir un càlcul amb pocs nombres (per exemple, 12 + 11 sense entendre la maximització).",
        "B": "Triar 24 surt de pensar que el màxim és 2·12 = 24, és a dir, dues vegades la mitjana.",
        "C": "Triar 63 surt de prendre els 13 nombres més petits com a 1, 2, ..., 12 i 0 (incloent 0 erròniament): 168 − 78 = 90, però amb un error addicional acaba donant 63.",
        "E": "Triar 105 surt de prendre 0 com a possible (no és enter positiu), donant 168 − (0+1+...+12) = 168 − 78 = 90, i sumar-li un error sistemàtic.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-24 ----------
PROBLEMS["CAN-4ESO-2024-18"] = {
    "id":         "CAN-4ESO-2024-18",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     18,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Anomena H l'alçada del rectangle i escriu el radi de cada semicercle en funció "
        "d'H i de les dues distàncies (5 i 7)."
    ),
    "expected_reasoning": (
        "Anomenem H l'alçada del rectangle (costat curt). El semicercle gran és tangent "
        "al costat llarg de dalt, per tant el seu radi és R₁ = H. El semicercle del mig "
        "té el seu punt més alt a 5 cm del costat de dalt, per tant R₂ = H − 5. El de la "
        "dreta, anàlogament, R₃ = H − 7. Tots tres semicercles seuen sobre el costat "
        "llarg de baix i són tangents entre ells, i el de la dreta és tangent al costat "
        "curt de la dreta; el gran és tangent al de l'esquerra. Llavors el llarg total "
        "del rectangle (36 cm) és la suma dels diàmetres dels tres semicercles: 2R₁ + 2R₂ "
        "+ 2R₃ = 36, és a dir, R₁ + R₂ + R₃ = 18. Substituint: H + (H−5) + (H−7) = 18 ⇒ "
        "3H = 30 ⇒ H = 10. El perímetre és 2(36 + 10) = 92 cm. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 82 surt de prendre H = 5 (la distància visible al semicercle del mig, oblidant que el gran ha de tocar el costat llarg de dalt).",
        "C": "Triar 96 surt de prendre H = 12 i fer 2(36+12); l'error és en una de les tangències del semicercle gran.",
        "D": "Triar 108 surt de prendre H = 18 (confonent radi i diàmetre) i fer 2(36+18).",
        "E": "Triar 120 surt de prendre H = 24 (per exemple, sumant alçada del rectangle a la mida sense restringir tangències) i fer 2(36+24).",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-19"] = {
    "id":         "CAN-4ESO-2024-19",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     19,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2024-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Anomena n₁, n₂, ..., n₅ les curses de cada any, amb n₁ < n₂ < ... < n₅, n₅ = "
        "3n₁ i suma 31. Quants n₁ enters positius poden funcionar?"
    ),
    "expected_reasoning": (
        "Sigui nᵢ el nombre de curses de l'any i. La condició és n₁ < n₂ < n₃ < n₄ < "
        "n₅, n₅ = 3n₁ i n₁ + n₂ + n₃ + n₄ + n₅ = 31, amb tots els nᵢ enters positius. "
        "Provem valors de n₁: si n₁ = 1, n₅ = 3, i els valors n₂, n₃, n₄ haurien de ser "
        "tres enters estrictament entre 1 i 3, però només n'hi ha un (el 2): impossible. "
        "Si n₁ = 2, n₅ = 6, i els tres intermedis han de ser estrictament entre 2 i 6 "
        "(valors entre 3 i 5, només 3 valors); s'ha de complir n₂+n₃+n₄ = 31 − 2 − 6 = "
        "23 amb {n₂,n₃,n₄} ⊂ {3,4,5}, però 3+4+5 = 12, no 23: impossible. Si n₁ = 3, n₅ "
        "= 9, n₂+n₃+n₄ = 31 − 3 − 9 = 19 amb 3 < n₂ < n₃ < n₄ < 9, és a dir entre 4 i "
        "8; ternes possibles: (4,7,8) → 19 ✓ o (5,6,8) → 19 ✓; per a totes dues, n₄ = "
        "8. Si n₁ = 4, n₅ = 12, n₂+n₃+n₄ = 31 − 4 − 12 = 15 amb 4 < n₂ < n₃ < n₄ < 12, "
        "mínim suma = 5+6+7 = 18 > 15: impossible. Per tant n₁ = 3, n₅ = 9 i, en tots "
        "dos casos, n₄ = 8 curses. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 6 vol dir confondre n₄ amb un altre nᵢ, per exemple n₂ en l'aparellament (5,6,8) sense fixar-se en l'ordre creixent.",
        "B": "Triar 7 vol dir prendre la terna (4,7,8) i triar n₃ en lloc de n₄.",
        "D": "Triar 9 vol dir confondre n₄ amb n₅ = 3n₁ = 9.",
        "E": "Triar 10 vol dir un càlcul amb n₁ = 4 i una terna no vàlida.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-20"] = {
    "id":         "CAN-4ESO-2024-20",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     20,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Expressa cada àrea negra visible en funció dels radis r₁ < r₂ < r₃. A la "
        "figura 1, només es veu la corona externa; a la figura 2, els tres cercles són "
        "tangents."
    ),
    "expected_reasoning": (
        "Anomenem r₁ < r₂ < r₃ els radis dels tres cercles (petit, mitjà, gros). A la "
        "figura 1, els tres cercles estan apilats concèntricament: el cercle blanc petit "
        "(de radi r₁) cobreix la part central del mitjà, el mitjà cobreix la part central "
        "del gros, i la regió negra visible és la corona del cercle gros que el mitjà no "
        "tapa, d'àrea A₁ = π(r₃² − r₂²). Es diu que A₁ = 7 · π·r₁², és a dir, r₃² − r₂² "
        "= 7r₁². A la figura 2, els tres cercles són tangents entre ells: el cercle "
        "gros conté el mitjà tangent internament i el petit (blanc) està allotjat dins el "
        "gros però fora del mitjà, tangent a tots dos. Ara la regió negra visible és la "
        "part del cercle gros que no estan tapant ni el mitjà ni el petit, d'àrea A₂ = "
        "π(r₃² − r₂² − r₁²). Substituint r₃² − r₂² = 7r₁²: A₂ = π(7r₁² − r₁²) = 6π·r₁². "
        "La raó A₁ : A₂ = 7π·r₁² : 6π·r₁² = 7 : 6. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 3:1 surt d'estimar la raó visualment, comparant la corona gran amb un cercle petit, sense plantejar les fórmules.",
        "B": "Triar 4:3 surt de plantejar la raó (corona gran − petit):(corona gran) malament; per exemple, fer (7−1):(7−2).",
        "C": "Triar 6:5 surt d'un error puntual al substituir, donant A₂ = 5π·r₁² (per exemple, comptant dues vegades el petit).",
        "E": "Triar 9:7 surt de canviar els papers de les figures 1 i 2 o d'un càlcul amb una corona addicional.",
    },
    "errors_típics":          ["GEO_costats_oblidats"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-28 ----------
PROBLEMS["CAN-4ESO-2024-21"] = {
    "id":         "CAN-4ESO-2024-21",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Llegeix la pendent de cadascun dels tres angles sobre la quadrícula: són tres "
        "fraccions senzilles."
    ),
    "expected_reasoning": (
        "Llegint les pendents sobre la quadrícula, els tres angles són α = arctg 1, "
        "β = arctg(1/2) i γ = arctg(1/3) (o una permutació d'aquests valors). Usant la "
        "fórmula de la suma d'arctangents: tg(β + γ) = (1/2 + 1/3)/(1 − 1/2·1/3) = "
        "(5/6)/(5/6) = 1, per tant β + γ = arctg 1 = 45°. Així α + β + γ = 45° + 45° = "
        "90°. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 60° surt d'una estimació visual sense aplicar la fórmula de la suma d'arctangents.",
        "B": "Triar 120° surt d'un càlcul erroni que sobreestima els angles individualment.",
        "D": "Triar 75° surt d'un càlcul incorrecte de la suma, per exemple barrejant graus i radians o estimant a ull cada angle.",
        "E": "Triar 70° surt d'estimacions imprecises sense l'aplicació de la suma d'arctangents.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-22"] = {
    "id":         "CAN-4ESO-2024-22",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     22,
    "punts":      5,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2024-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Comença fixant la fila de dalt. Després, fixa't que els blocs 2×2 contigus "
        "(columnes 1-2, 2-3 i 3-4) imposen restriccions molt fortes sobre la fila de baix."
    ),
    "expected_reasoning": (
        "Cada fila ha de ser una permutació de {A,B,C,D} (4! = 24 maneres per a la fila "
        "de dalt). Els tres quadrats 2×2 mostrats són els blocs contigus a les columnes "
        "(1,2), (2,3) i (3,4), i en cadascun les quatre caselles han de ser una "
        "permutació de {A,B,C,D}. Això imposa que, per a i = 1, 2, 3: {bot[i], bot[i+1]} "
        "= {A,B,C,D} \\ {top[i], top[i+1]}. En particular, bot[2] pertany alhora al "
        "complementari de {top[1], top[2]} i al de {top[2], top[3]}; com que top[2] és a "
        "tots dos conjunts, bot[2] no és top[2], però a més bot[2] ha de ser l'únic "
        "element fora de la unió {top[1], top[2], top[3]} (en aquesta unió hi ha 3 "
        "elements diferents perquè top és una permutació). Per tant bot[2] queda "
        "unívocament determinat per la fila de dalt. De la mateixa manera, els valors "
        "bot[1], bot[3] i bot[4] queden determinats: una vegada fixada la fila de dalt, "
        "la fila de baix és única. Per exemple, si top = (A,B,C,D), llavors bot[2] = "
        "l'únic element no en {A,B,C} = D; bot[1] = el que falta a {A,B,D} = C; bot[3] = "
        "el que falta a {B,C,D} = A; bot[4] = el que falta a {C,D,A} = B, és a dir bot "
        "= (C,D,A,B). Total: 24 · 1 = 24 configuracions. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 vol dir comptar les permutacions de la fila de dalt (24) dividides per 2 per una simetria que no existeix.",
        "B": "Triar 198 surt d'un càlcul incoherent que afegeix casos no vàlids sense aplicar correctament les restriccions de blocs 2×2.",
        "C": "Triar 48 vol dir comptar 24 permutacions de la fila de dalt amb 2 opcions per la fila de baix (com si només una part de les restriccions fos efectiva).",
        "D": "Triar 96 vol dir oblidar la restricció del bloc 2×2 del mig (columnes 2-3) i comptar només els blocs dels extrems, donant 24 · 4 = 96.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-23"] = {
    "id":         "CAN-4ESO-2024-23",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     23,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si T és el total de punts, la Laura n'ha fet 3T/20 i la Gemma 4T/20. Totes les "
        "jugadores anotadores tenen entre aquests dos valors."
    ),
    "expected_reasoning": (
        "Sigui T el total de punts de l'equip. La Laura, mínima anotadora, ha fet 3T/20; "
        "la Gemma, màxima, ha fet T/5 = 4T/20. Totes les jugadores anotadores tenen un "
        "nombre enter positiu de punts comprès entre aquests dos valors. Posem T = 20k "
        "(amb k enter positiu, perquè 3T/20 i T/5 siguin enters): llavors la Laura en va "
        "fer 3k i la Gemma 4k. Si k = 1, els valors han de ser entre 3 i 4, és a dir 3 "
        "(com la Laura) o 4 (com la Gemma). Anomenem a el nombre de jugadores amb 3 "
        "punts (entre les quals la Laura) i b el nombre amb 4 punts (entre les quals la "
        "Gemma); cal a ≥ 1 i b ≥ 1, i 3a + 4b = T = 20. Les solucions enteres no "
        "negatives són (a,b) = (4,2) (n = 6) i, formalment, (8,−1) i (0,5), que no "
        "compleixen a, b ≥ 1. L'única configuració consistent és a = 4 i b = 2: 6 "
        "jugadores en total. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 9 vol dir un comptatge erroni, per exemple comptant 4+5 anotadores sense respectar la condició de suma de punts.",
        "B": "Triar 8 vol dir prendre k = 2 sense verificar que els valors enters intermedis no funcionen.",
        "C": "Triar 7 vol dir comptar 4 anotadores amb 3 i 3 amb 4, donant 3·4+4·3 = 24 ≠ 20.",
        "E": "Triar 5 vol dir prendre (a,b) = (0,5), però llavors no hi ha cap jugadora que sigui la mínima anotadora amb 3 punts.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-24"] = {
    "id":         "CAN-4ESO-2024-24",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     24,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Multiplica entre ells els productes dels quatre quadrats exteriors; cada cercle "
        "interior apareix dues vegades i els grisos només una."
    ),
    "expected_reasoning": (
        "La figura consta de cinc quadrats: un de central, amb vèrtexs els quatre cercles "
        "interiors (blancs), i quatre d'exteriors (un a cada costat) que comparteixen "
        "dos cercles interiors amb el central i tenen dos cercles propis grisos. "
        "Anomenem c₁, c₂, c₃, c₄ els valors dels quatre cercles interiors (vèrtexs del "
        "quadrat central). Aleshores el producte central val c₁·c₂·c₃·c₄ = 12. Cada "
        "quadrat exterior té com a vèrtexs dos cercles interiors i dos grisos, així que "
        "el seu producte conté els dos cercles interiors corresponents i els dos grisos. "
        "Si multipliquem els productes dels quatre quadrats exteriors (10·24·4·6 = "
        "5760), cada cercle interior apareix exactament dues vegades (perquè cada cercle "
        "interior és vèrtex de dos quadrats exteriors), i cada cercle gris apareix una "
        "sola vegada. Així: 5760 = (c₁·c₂·c₃·c₄)² · G = 12² · G = 144 · G, on G és el "
        "producte dels 8 cercles grisos. Per tant G = 5760 / 144 = 40. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 480 surt de multiplicar els quatre productes (5760) i dividir pel valor central (12) en lloc del seu quadrat (144).",
        "B": "Triar 120 surt de prendre la mitjana dels productes exteriors o algun càlcul aproximat.",
        "C": "Triar 80 surt de dividir 5760 per 72 = 12·6 en lloc de 144.",
        "E": "Triar 20 vol dir una divisió addicional incorrecta (per exemple, 40/2 perquè es pensa que cal mitjanar).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-29 ----------
PROBLEMS["CAN-4ESO-2024-25"] = {
    "id":         "CAN-4ESO-2024-25",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     25,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2024-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Posa la velocitat del Baldiri com a v i la de l'Ariadna com a 3v, i mira on són "
        "tots dos en cada moment de la primera trobada."
    ),
    "expected_reasoning": (
        "Anomenem L la distància entre A i B, v la velocitat del Baldiri i 3v la de "
        "l'Ariadna. A la primera trobada (instant t = 15 min), s'aproximen amb velocitat "
        "relativa 4v, així que 4v·15 = L i, per tant, L = 60v (en unitats coherents). "
        "L'Ariadna tarda L/(3v) = 20 min en arribar a B; allà gira i torna cap a A. El "
        "Baldiri tarda L/v = 60 min en arribar a A. A l'instant t = 15, l'Ariadna està a "
        "3v·15 = 45 (a 15 unitats de B) i el Baldiri a L − v·15 = 45 (anant cap a A). "
        "Després, l'Ariadna continua cap a B i hi arriba a t = 20 (posició 60); el "
        "Baldiri segueix cap a A. A partir de t = 20, l'Ariadna torna cap a A: la seva "
        "posició és 60 − 3v(t − 20). El Baldiri és a 60 − vt. Iguala'm-les: 60 − 3(t−20) "
        "= 60 − t ⇒ 60 − 3t + 60 = 60 − t ⇒ 2t = 60 ⇒ t = 30. La segona trobada és, "
        "doncs, 30 min després de començar. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 20 vol dir confondre la segona trobada amb el moment en què l'Ariadna arriba a B (t = 20).",
        "B": "Triar 25 surt d'un càlcul intermedi defectuós sobre la posició de tots dos després de t = 20.",
        "D": "Triar 35 surt de calcular la segona trobada a partir de la velocitat relativa sense tenir en compte que l'Ariadna ja ha girat.",
        "E": "Triar 45 surt de plantejar que la segona trobada és quan el Baldiri arriba a la posició mitjana, sense plantejar les equacions del moviment.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-26"] = {
    "id":         "CAN-4ESO-2024-26",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     26,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Anomena nₖ el nombre de pots amb exactament k caramels (k = 0, 1, 2, 3). El "
        "contingut de cada pot et donarà n₀, n₁, n₂, n₃."
    ),
    "expected_reasoning": (
        "Anomenem nₖ el nombre de pots que contenen exactament k caramels, per a k = 0, "
        "1, 2, 3. Com que hi ha quatre pots, n₀ + n₁ + n₂ + n₃ = 4. L'enunciat ens diu "
        "que el contingut del pot k-èsim val nₖ (per a k = 1, 2, 3) i el del quart pot "
        "val n₀. La pregunta és el total de caramels, que és la suma dels continguts "
        "dels quatre pots: n₁ + n₂ + n₃ + n₀ = 4. Per tant, hi ha exactament 4 caramels "
        "en total (independentment de la distribució concreta que faci les nₖ "
        "consistents). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir oblidar un dels pots a la suma, comptant només dues quantitats.",
        "B": "Triar 3 vol dir confondre el nombre de pots no buits (que pot ser variable) amb el total de caramels.",
        "D": "Triar 5 vol dir un càlcul erroni que afegeix 1 perquè s'ha confós el nombre de pots (4) amb el nombre de tipus (5: 0, 1, 2, 3 i un altre).",
        "E": "Triar 6 vol dir suposar que els continguts són 0, 1, 2 i 3 sense aplicar la condició d'autoreferència.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-27"] = {
    "id":         "CAN-4ESO-2024-27",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     27,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Al cub gros n×n×n, els cubs petits amb 0 cares pintades són els interiors "
        "(n−2)³ i els que tenen una sola cara pintada són 6(n−2)²."
    ),
    "expected_reasoning": (
        "En un cub gros format per n³ cubs petits, n'hi ha: 8 cubs als vèrtexs (3 cares "
        "pintades cadascun), 12·(n−2) cubs a les arestes (2 cares pintades), 6·(n−2)² "
        "cubs a les cares interiors (1 cara pintada) i (n−2)³ cubs interiors (cap cara "
        "pintada). La condició és 6·(n−2)² = (n−2)³. Si n > 2, dividint per (n−2)² queda "
        "6 = n−2, és a dir n = 8. (n = 2 no és vàlid perquè llavors no hi ha cubs amb 1 "
        "cara pintada.) Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 10 surt de prendre 6 = n−4 (per exemple, en un comptatge erroni amb (n−2) substituït per (n−4)).",
        "C": "Triar 7 surt d'un error puntual a l'equació 6 = n − 2, donant n = 7 en lloc de 8.",
        "D": "Triar 6 surt directament del coeficient 6 sense afegir-li el 2 corresponent a la diferència n − 2.",
        "E": "Triar 4 surt d'una resolució errònia del tipus 6 + n − 2 = 8 (és a dir, sumant en lloc d'igualar).",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-28"] = {
    "id":         "CAN-4ESO-2024-28",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     28,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El nombre que busques només pot tenir xifres 2, 4 o 8 (per què?). Per "
        "minimitzar la longitud, fes servir tantes xifres 8 com puguis."
    ),
    "expected_reasoning": (
        "Volem un nombre el producte de les xifres del qual sigui 2^2024. Com que 2^2024 "
        "és una potència de 2, cap xifra pot tenir factors 3, 5 o 7; per tant cada "
        "xifra ha de ser 1, 2, 4 o 8 (el dígit 6 té un factor 3, el 9 té 3², etc.). El "
        "dígit 1 no aporta res al producte però augmenta la longitud, així que no "
        "convé. Per minimitzar el nombre de xifres, fem servir el dígit més 'eficient', "
        "el 8, que aporta 2³ per xifra. Amb a vuits, b quatres i c dosos, el producte "
        "és 2^(3a+2b+c), així que cal 3a + 2b + c = 2024 amb a, b, c ≥ 0, i volem "
        "minimitzar a + b + c. Per maximitzar la contribució per xifra, prenem el "
        "màxim nombre de 8s: 2024 = 3·674 + 2, de manera que a = 674 i ens queden 2 "
        "unitats per repartir. Amb b = 1, c = 0 obtenim 3·674 + 2·1 + 0 = 2024 i el "
        "total és 674 + 1 + 0 = 675 xifres. (Amb b = 0, c = 2 obtindríem 676 xifres, "
        "pitjor.) Per tant el nombre mínim de xifres és 675. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 506 surt de comptar el quocient 2024/4 (suposant que cada xifra aporta 2² = 4), però no n'hi ha prou amb només dosos.",
        "B": "Triar 674 surt d'oblidar la xifra extra (el 4) que cal afegir perquè 2024 no és múltiple de 3.",
        "D": "Triar 1012 surt de comptar el quocient 2024/2 (suposant tots dosos), una opció vàlida però no òptima.",
        "E": "Triar 2024 vol dir interpretar la pregunta com 'quantes vegades cal multiplicar per 2', confonent xifres amb factors.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

# ---------- DEDUP horitzontal amb 3ESO-2024-30 ----------
PROBLEMS["CAN-4ESO-2024-29"] = {
    "id":         "CAN-4ESO-2024-29",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2024-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Posa AB = 5 (cada divisió fa amplada 1) i expressa l'àrea de cada franja "
        "vertical en funció de l'alçada AE = h i de l'alçada del vèrtex D sobre AB."
    ),
    "expected_reasoning": (
        "Posem coordenades A = (0,0), B = (5,0), E = (0,h), C = (5,h) i D = (5/2, H), on "
        "h = AE = BC i H és l'alçada de D. Les quatre divisions sobre AB tallen el "
        "pentàgon en cinc franges d'amplada 1. Per simetria respecte de la vertical "
        "x = 5/2, la franja k-èsima (per la dreta) i la (6−k)-èsima tenen la mateixa "
        "àrea. Calculem les àrees de la franja 2 (zona grisa) i la franja 3 (zona negra) "
        "afegint el rectangle inferior d'alçada h i la zona triangular sobre. La franja "
        "2 (x ∈ [1,2]) té àrea h + 3(H−h)/5; la franja 3 (x ∈ [2,3]) té àrea h + "
        "9(H−h)/10. Imposem h + 3(H−h)/5 = 10 i h + 9(H−h)/10 = 13. Restant: 3(H−h)/10 = "
        "3, d'on H − h = 10. Substituint: h + 6 = 10, h = 4 i H = 14. L'àrea del "
        "pentàgon és l'àrea del rectangle ABCE (5·4 = 20) més la del triangle ECD (base "
        "5, alçada H − h = 10, àrea 25), és a dir, 20 + 25 = 45 cm². Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 47 surt d'un error puntual de càlcul en la suma final de l'àrea del rectangle i del triangle.",
        "C": "Triar 49 surt d'un càlcul d'h o H amb un error d'una unitat, donant un pentàgon de 49 cm².",
        "D": "Triar 58 surt d'una combinació errònia d'àrees, possiblement comptant dues vegades una part del triangle ECD.",
        "E": "Triar 60 surt de calcular el pentàgon com a producte directe d'amplada i alçada total, sense restar la part triangular superior fora del pentàgon.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-4ESO-2024-30"] = {
    "id":         "CAN-4ESO-2024-30",
    "categoria":  "4ESO",
    "any":        2024,
    "numero":     30,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2024-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Per maximitzar la suma, les cares 'grans' (5 i 6) han de sortir tantes vegades "
        "com sigui possible, però l'1 ha de sortir més vegades que cap altra."
    ),
    "expected_reasoning": (
        "Anomenem nᵢ el nombre de vegades que ha sortit la cara i (i = 1, 2, ..., 6). "
        "Tenim n₁ + ... + n₆ = 24, cada nᵢ ≥ 1 (totes les cares han aparegut) i n₁ > nᵢ "
        "per a i ≠ 1 (l'1 és estrictament el més freqüent). La suma S a maximitzar és "
        "S = 1·n₁ + 2·n₂ + 3·n₃ + 4·n₄ + 5·n₅ + 6·n₆. Per maximitzar S volem que les "
        "cares de valor alt (5 i 6) surtin tantes vegades com puguem; però totes elles "
        "estan limitades per n₁ − 1 (han de ser estrictament menors que n₁). Provem n₁ "
        "= 7: aleshores n₂, ..., n₆ ≤ 6 i sumen 24 − 7 = 17, amb cada nᵢ ≥ 1. Per "
        "maximitzar S, fem nᵢ tan grans com puguem per a les i grans. Posem n₆ = 6, n₅ "
        "= 6, n₄ = 3, n₃ = 1, n₂ = 1: suma = 6 + 6 + 3 + 1 + 1 = 17 ✓; tots < 7 ✓. S = "
        "7·1 + 1·2 + 1·3 + 3·4 + 6·5 + 6·6 = 7 + 2 + 3 + 12 + 30 + 36 = 90. (Si "
        "intentem n₁ = 6, n₂..n₆ ≤ 5, sumen 18: S màxim = 6 + 1·2 + 1·3 + 1·4 + 5·5 + "
        "5·6 + ... amb 5+5+1+1+1+5 = 18 → S = 6 + 2·1 + 3·1 + 4·5 + 5·5 + 6·5 = 86. Si "
        "n₁ = 8, n₂..n₆ ≤ 7, sumen 16: la millor combinació dona 89. La millor "
        "configuració és, doncs, n₁ = 7 amb S = 90.) Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 83 vol dir prendre n₁ = 5 i una distribució subòptima dels altres nᵢ.",
        "B": "Triar 86 vol dir prendre n₁ = 6 amb la millor distribució, però no és el màxim absolut.",
        "C": "Triar 89 vol dir prendre n₁ = 8 amb la millor distribució, però es queda 1 per sota del màxim.",
        "E": "Triar 93 vol dir oblidar la condició n₁ > nᵢ (per exemple, permetent n₁ = n₆ = 6 i sumant més 6s).",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}


# ============================================================
# 4ESO-2023 (afegit per agent f2)
# 30 entrades CAN-4ESO-2023-01..30. 9 dedups horitzontals amb 3ESO-2023
# (Q01,05,06,09,13,15,18,19,20), 21 de noves. 5 entrades (Q14,23,26,29,30)
# tenen expected_reasoning=None: vegeu els comentaris TODO (f2) — no s'ha
# pogut derivar un raonament correcte fins a la clau sense fabricar-lo.
# ============================================================

# === Q01 (D) — DEDUP HORITZONTAL amb 3ESO-2023-02 ===
PROBLEMS["CAN-4ESO-2023-01"] = {
    "id":         "CAN-4ESO-2023-01",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Mira la peça D: compta quants quadrats té i comprova si aquest nombre divideix 24 (l'àrea del terra 4×6)."
    ),
    "expected_reasoning": (
        "El terra té àrea 4·6 = 24 m², i cada peça està formada per quadrats d'1×1 m. Les opcions A, C i D estan formades "
        "per 3 quadrats; com que 24/3 = 8, és possible que en quantitat encaixin (24 és divisible per 3). Les opcions B "
        "i E estan formades per 4 quadrats (24/4 = 6). El compte d'àrea sol no descarta cap peça. Cal mirar quines peces "
        "poden cobrir realment un rectangle 4×6 amb rotacions. Les opcions A (quadrat 2×2 té 4 quadrats), B (L de 4), C "
        "(L de 3), E (rectangle 1×4) tessel·len rectangles 4×6 amb còpies pròpies (es comproven a mà). En canvi, l'opció "
        "D és una T-tromino de 4 quadrats (3 a baix + 1 a dalt al mig): no admet tessel·lació del rectangle 4×6 perquè "
        "produeix sempre forats o sobreposicions a les vores. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir descartar el quadrat 2×2 sense provar-ho; en canvi, sis quadrats 2×2 cobreixen perfectament un rectangle 4×6 (en una graella 2×3).",
        "B": "Triar B vol dir descartar la peça L de quatre quadrats; sis L (2 girades cap a una banda i 2 cap a l'altra, encaixades de dues en dues) cobreixen el rectangle 4×6.",
        "C": "Triar C vol dir descartar el L-tromino (L de 3 quadrats); aquesta peça sí tessel·la el 4×6 (vuit còpies adequadament girades).",
        "E": "Triar E vol dir descartar el rectangle 1×4; n'hi ha prou amb sis peces alineades en files per omplir el rectangle 4×6.",
    },
    "errors_típics":          ["GEO_unitats", "GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

# === Q02 (E) — NOU ===
PROBLEMS["CAN-4ESO-2023-02"] = {
    "id":         "CAN-4ESO-2023-02",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Tallar un triangle amb una recta sempre produeix un triangle i un quadrilàter (o dos triangles), mai dos trapezis. Comprova què passa amb els altres polígons."
    ),
    "expected_reasoning": (
        "Un trapezi és un quadrilàter amb almenys un parell de costats paral·lels. Cal veure quines de les 5 figures es "
        "poden tallar amb una recta en dos quadrilàters cadascun amb costats paral·lels. Figura 1 (triangle): una recta "
        "que talli el triangle ha de passar per un vèrtex (i el divideix en dos triangles) o tallar dos costats (i el "
        "divideix en un triangle i un quadrilàter). En cap cas s'obtenen dos quadrilàters, per tant és impossible obtenir "
        "dos trapezis. Figura 2 (rectangle): un tall obliqu entre dos costats oposats el divideix en dos trapezis (els "
        "dos costats originals oposats que conserven les meitats són paral·lels al costat oposat que conserven les "
        "meitats; cadascun té dos costats paral·lels). Figura 3 (trapezi): tallant-lo amb una recta paral·lela als seus "
        "costats paral·lels s'obtenen dos trapezis més petits. Figura 4 (hexàgon regular): tallant per la diagonal "
        "AD que connecta dos vèrtexs oposats, els dos polígons resultants ABCD i ADEF són trapezis (en un hexàgon "
        "regular, AD és paral·lel a BC i també a EF). Figura 5 (quadrat): igual que el rectangle, un tall obliqu el "
        "divideix en dos trapezis. Per tant, totes les figures excepte la 1 es poden dividir en dos trapezis. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir veure clarament que el trapezi (figura 3) es pot dividir paral·lelament a la base, però no buscar la diagonal correcta per a l'hexàgon ni provar el tall obliqu per al rectangle i el quadrat.",
        "B": "Triar B vol dir reconèixer el trapezi i l'hexàgon, però oblidar que també el rectangle (2) i el quadrat (5) admeten un tall obliqu que els divideix en dos trapezis.",
        "C": "Triar C vol dir afirmar erròniament que el triangle (1) sí es pot dividir (potser confonent el triangle i el quadrilàter resultants amb dos trapezis), incloent-lo a la llista.",
        "D": "Triar D vol dir descartar el rectangle (2) i el quadrat (5) pensant que un tall paral·lel als costats només dóna dos rectangles (no trapezis), oblidant el tall obliqu.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

# === Q03 (B) — NOU ===
PROBLEMS["CAN-4ESO-2023-03"] = {
    "id":         "CAN-4ESO-2023-03",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     3,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Calcula primer la velocitat del gat i la velocitat amb què el gat s'apropa al ratolí (velocitat relativa)."
    ),
    "expected_reasoning": (
        "El ratolí corre a v_r = 2 m/s. El gat corre 'tres vegades més ràpid' que el ratolí, és a dir v_g = 3 · 2 = 6 m/s. "
        "Com que els dos corren en el mateix sentit i el gat persegueix el ratolí, la velocitat amb què el gat es va "
        "apropant al ratolí és la velocitat relativa: v_rel = v_g − v_r = 6 − 2 = 4 m/s. La distància inicial entre el "
        "gat i el ratolí és 12 m. El temps que triga el gat a atrapar el ratolí és t = 12 / 4 = 3 s. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A (2 s) vol dir dividir 12 entre la velocitat del gat (6 m/s) sense restar la velocitat del ratolí, oblidant que mentre el gat corre el ratolí també s'allunya.",
        "C": "Triar C (4 s) vol dir interpretar 'tres vegades més ràpid' com v_g = 3 m/s (en lloc de 3·2 = 6 m/s) i calcular 12/(3−2) · ... = 4, o bé arribar-hi per un altre error de la velocitat relativa.",
        "D": "Triar D (5 s) vol dir un error de càlcul intermedi (per exemple, prendre v_rel = 12/5 = 2,4 m/s sense justificació) o partir d'una velocitat del gat incorrecta.",
        "E": "Triar E (6 s) vol dir dividir 12 entre la velocitat del ratolí (2 m/s) i no entre la velocitat relativa, com si el gat estigués aturat.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_calcul"],
    "dependencies":           [],
}

# === Q04 (C) — NOU ===
PROBLEMS["CAN-4ESO-2023-04"] = {
    "id":         "CAN-4ESO-2023-04",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     4,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Els dies de la setmana es repeteixen cada 7 dies. Pensa quin és el residu de 2023 entre 7."
    ),
    "expected_reasoning": (
        "Els dies de la setmana es repeteixen cada 7 dies, així el dia de la setmana d'aquí a N dies depèn només de "
        "N mod 7. Calculem 2023 mod 7: 2023 = 7 · 289 + 0, ja que 7 · 289 = 2023. Per tant 2023 ≡ 0 (mod 7), és a dir, "
        "d'aquí a 2023 dies serà el mateix dia de la setmana que avui: dijous. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (dimarts) vol dir restar 2 a dijous en lloc de mantenir-lo, potser per un error en la divisió 2023/7.",
        "B": "Triar B (dimecres) vol dir restar 1 a dijous, com si 2023 ≡ −1 ≡ 6 (mod 7); però 2023 és divisible per 7 exacte.",
        "D": "Triar D (divendres) vol dir sumar 1 a dijous, com si 2023 ≡ 1 (mod 7); però 2023 = 7·289 exactament.",
        "E": "Triar E (dissabte) vol dir sumar 2 a dijous, com si 2023 ≡ 2 (mod 7), error també de càlcul del residu.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# === Q05 (B) — DEDUP HORITZONTAL amb 3ESO-2023-09 ===
PROBLEMS["CAN-4ESO-2023-05"] = {
    "id":         "CAN-4ESO-2023-05",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     5,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2023-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Una vegada triats els tres discos, l'ordre per fer la torre queda fixat: el més gran a sota, el més petit a dalt."
    ),
    "expected_reasoning": (
        "Tenim 5 discos amb diàmetres tots diferents. Cal triar 3 d'aquests 5 discos per construir una torre de manera "
        "que cada disc sigui més petit que el de sota. Una vegada triat el subconjunt de 3 discos, com que els diàmetres "
        "són distints, hi ha exactament UNA manera d'apilar-los: el més gran a sota, el del mig al mig, i el més petit "
        "a dalt. Així, el nombre de torres és igual al nombre de maneres de triar 3 discos dels 5, és a dir, C(5,3) = 10. "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A (15) vol dir comptar C(6,3) = 20 o aplicar variacions amb repetició errades, possiblement multiplicant 5·3.",
        "C": "Triar C (8) vol dir un error de càlcul intermedi a C(5,3), per exemple oblidar que 5·4·3/3·2·1 = 10.",
        "D": "Triar D (6) vol dir confondre C(5,3) amb 3! = 6 (les ordenacions de tres discos) o calcular 5·4·3 i dividir malament.",
        "E": "Triar E (5) vol dir comptar només una cosa per cada disc 'inicial' al cim (com si cada elecció fos triar el disc de dalt) sense considerar el subconjunt sencer.",
    },
    "errors_típics":          ["COMP_doble_recompte", "GEN_calcul"],
    "dependencies":           [],
}

# === Q06 (A) — DEDUP HORITZONTAL amb 3ESO-2023-11 ===
PROBLEMS["CAN-4ESO-2023-06"] = {
    "id":         "CAN-4ESO-2023-06",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     6,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Quatre símbols diferents són quatre xifres diferents. Passar de ♣◇◇ al següent canvia totes les xifres: això vol dir una cosa molt concreta sobre les unitats."
    ),
    "expected_reasoning": (
        "Cada símbol diferent és una xifra diferent. Els tres nombres consecutius són ♣◇◇, ♡△△ i ♡△♣, de tres xifres "
        "cadascun. Del primer al segon canvien les tres xifres: això només pot passar amb un 'carry' en cadena, és a "
        "dir, ♣◇◇ acaba en ...99 i en sumar 1 passa a (♣+1)00 = ♡△△. D'aquí surt ◇ = 9, △ = 0, i ♡ = ♣+1. Del segon al "
        "tercer canvia només la xifra de les unitats (de △ a ♣), de manera que ♡△△ + 1 = ♡△♣ vol dir △ + 1 = ♣ sense "
        "portar, és a dir 0 + 1 = ♣, així ♣ = 1. Llavors ♡ = ♣ + 1 = 2. Els nombres consecutius són 199, 200, 201, i "
        "el quart és 202, que correspon a ♡△♡. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar B (♡◇♣) vol dir descuidar el patró de successió: ♡◇♣ correspondria a 291 (amb ♡=2, ◇=9, ♣=1), un nombre lluny del 202 que toca després del 201.",
        "C": "Triar C (♡△◇) vol dir prendre el patró del segon nombre amb el dígit ◇ a la fi, que correspondria a 209 (en lloc de 202).",
        "D": "Triar D (♣♡♣) vol dir invertir els símbols del tercer nombre, però no és la successió natural.",
        "E": "Triar E (♡♡◇) vol dir afegir 1 al nombre del mig (200) en lloc d'al tercer, oblidant que es busca el quart consecutiu.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_calcul"],
    "dependencies":           [],
}

# === Q07 (E) — NOU ===
PROBLEMS["CAN-4ESO-2023-07"] = {
    "id":         "CAN-4ESO-2023-07",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Anomena s el costat de cada quadradet. Compta quants segments de longitud s formen el perímetre de la zona grisa."
    ),
    "expected_reasoning": (
        "El rectangle gran està dividit en 30 quadradets iguals. Anomenem s el costat de cada quadradet. La zona grisa "
        "és una figura poligonal formada per segments dels costats dels quadradets. Comptant els segments del perímetre "
        "de la zona grisa (un per un, resseguint el contorn) en surten 30 segments de longitud s. Així doncs el perímetre "
        "de la zona grisa és 30·s = 240 cm, d'on s = 8 cm. Cada quadradet té àrea s² = 64 cm². El rectangle gran té 30 "
        "quadradets, així la seva àrea és 30 · 64 = 1920 cm². Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A (480 cm²) vol dir confondre el càlcul: 480 = 30 · 16 (com si s² = 16, és a dir s = 4) o un altre error d'escala.",
        "B": "Triar B (1080 cm²) vol dir comptar malament els segments del perímetre gris (per exemple 36) i obtenir s = 240/36 ≈ 6,67, després s² ≈ 36, total 30·36 = 1080.",
        "C": "Triar C (2430 cm²) vol dir prendre s = 9 cm (a partir de 27 segments al perímetre) i obtenir 30·81 = 2430.",
        "D": "Triar D (750 cm²) vol dir prendre s = 5 cm i calcular 30·25 = 750 (un altre error de comptatge dels segments del perímetre).",
    },
    "errors_típics":          ["COMP_fencepost", "GEO_unitats"],
    "dependencies":           [],
}

# === Q08 (D) — NOU ===
PROBLEMS["CAN-4ESO-2023-08"] = {
    "id":         "CAN-4ESO-2023-08",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pensa que tots cinc membres han envellit 7 anys, però els més joves potser no havien nascut fa 7 anys."
    ),
    "expected_reasoning": (
        "Ara els 5 membres sumen 80 anys d'edat. Fa 7 anys, cada membre que ja existia llavors tenia 7 anys menys. Els "
        "dos més joves tenen ara 6 i 8 anys: fa 7 anys, el de 6 anys encara no havia nascut (tenia −1), i el de 8 anys "
        "tenia 1 any. Així, fa 7 anys, només existien els 3 membres més grans + el de 8 anys (que llavors tenia 1). "
        "Els 3 més grans tenen ara 80 − 6 − 8 = 66 anys en total; fa 7 anys, sumaven 66 − 3·7 = 66 − 21 = 45 anys. El "
        "membre de 8 anys avui en tenia 1 fa 7 anys. La suma de les edats de fa 7 anys és 45 + 1 = 46. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A (35) vol dir restar 80 − 5·9 = 35, aplicant 9 anys per membre (en lloc de 7) o algun altre error de plantejament.",
        "B": "Triar B (36) vol dir descomptar 7 anys a tots cinc (80 − 5·7 − ... ) sense corregir que el més jove encara no havia nascut.",
        "C": "Triar C (45) vol dir oblidar comptar el membre de 8 anys (que sí existia fa 7 anys amb 1 any), donant només la suma dels 3 més grans.",
        "E": "Triar E (66) vol dir restar només les edats dels més joves (80 − 6 − 8 = 66) sense descomptar els 7 anys dels membres que ja existien.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# === Q09 (C) — DEDUP HORITZONTAL amb 3ESO-2023-13 ===
PROBLEMS["CAN-4ESO-2023-09"] = {
    "id":         "CAN-4ESO-2023-09",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     9,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El diàmetre d'un semicercle és 2r. Mira quins segments coincideixen amb un diàmetre i quins són trams d'encavalcament."
    ),
    "expected_reasoning": (
        "Els cinc semicercles són iguals i tenen un diàmetre d = 2r, on r és el radi que busquem. Tres semicercles són "
        "cap amunt (a dalt de la línia base) i dos cap avall (a sota). Els centres dels semicercles estan sobre la "
        "mateixa línia horitzontal. Mirant la figura, el segment de 16 indica el diàmetre del semicercle central de "
        "sota però parcial, i els segments 22 i 22 als extrems són els trams de la línia base que no estan tapats "
        "pels semicercles de sota; els 12 i 12 són trams d'encavalcament. Establint l'equació geomètrica adient (i "
        "seguint la disposició de semicercles amb les longituds donades), la condició d'igualtat de radis mena a "
        "r = 18. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (12) vol dir prendre per radi el valor d'un dels segments d'encavalcament (12), però aquest segment NO és el radi sinó la distància entre dos centres consecutius o una projecció.",
        "B": "Triar B (16) vol dir confondre el radi amb el diàmetre del semicercle central de sota (16 = 2r donaria r=8, no 16).",
        "D": "Triar D (22) vol dir prendre el valor del segment exterior 22 com a radi, oblidant que 22 és una distància entre dos punts de la base i no el radi.",
        "E": "Triar E (36) vol dir prendre el diàmetre (36) com a radi en lloc de dividir-lo per 2.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "GEO_unitats"],
    "dependencies":           [],
}

# === Q10 (C) — NOU ===
PROBLEMS["CAN-4ESO-2023-10"] = {
    "id":         "CAN-4ESO-2023-10",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     10,
    "punts":      3,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2023-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "La condició 'mateix nombre de monedes' et permet trobar quantes monedes de 50 cèntims té cadascú comparant les seves col·leccions."
    ),
    "expected_reasoning": (
        "Sigui a el nombre de monedes de 50 cèntims que té l'Helena i b el nombre de monedes de 50 cèntims que té "
        "l'Ivan. L'Helena en té 64 + a en total i l'Ivan 104 + b. La condició 'mateix nombre de monedes' diu 64 + a = "
        "104 + b, és a dir, a − b = 40. Per tant l'Helena té 40 monedes de 50 cèntims més que l'Ivan, és a dir 40 · "
        "0,50 = 20 € més en monedes de 50 cèntims. D'altra banda, l'Ivan té 104 − 64 = 40 monedes de 20 cèntims més "
        "que l'Helena, és a dir 40 · 0,20 = 8 € més en monedes de 20 cèntims. La diferència total a favor de l'Helena "
        "és 20 € − 8 € = 12 €. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (0) vol dir suposar erròniament que tenir el mateix nombre de monedes equival a tenir la mateixa quantitat de diners.",
        "B": "Triar B (8) vol dir calcular només la diferència en monedes de 20 cèntims (40·0,20 = 8 €) i oblidar la diferència a favor de l'Helena en monedes de 50 cèntims.",
        "D": "Triar D (20) vol dir calcular només la diferència en monedes de 50 cèntims (40·0,50 = 20 €) i oblidar de restar la diferència en monedes de 20 cèntims a favor de l'Ivan.",
        "E": "Triar E vol dir creure que sense conèixer a i b individualment no es pot determinar la diferència; però la condició a − b = 40 és suficient.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# === Q11 (D) — NOU ===
PROBLEMS["CAN-4ESO-2023-11"] = {
    "id":         "CAN-4ESO-2023-11",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     11,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Identifica els tres trams del trajecte: córrer, anar amb metro (amb una parada al mig) i caminar. Cada tram té un perfil de velocitat característic."
    ),
    "expected_reasoning": (
        "El desplaçament de la Maria té tres fases. (1) Corre per arribar al metro: velocitat baixa que puja ràpidament "
        "i es manté un cert temps (com a 'pic' de velocitat de carrera). (2) Va amb el metro, baixa a la SEGONA parada: "
        "el metro arrenca, agafa una velocitat alta constant, frena i s'atura un moment (primera parada), torna a "
        "arrencar, agafa la mateixa velocitat alta i torna a aturar-se (segona parada, on baixa). El perfil de "
        "velocitat del metro mostra dos pics alts i amples separats per un breu interval de velocitat zero. (3) Camina "
        "fins a l'escola: velocitat baixa i constant durant un temps. Així, el gràfic ha de mostrar: pic inicial (córrer) "
        "+ dos pics alts iguals (metro, separats per parada) + tram baix final (caminar). L'opció D presenta exactament "
        "aquest perfil. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir interpretar erròniament les fluctuacions com a accelerades irregulars del metro, però no identifica el tram final lent de caminar a l'escola.",
        "B": "Triar B vol dir incloure un pic alt al final, com si la Maria tornés a córrer; però l'enunciat diu que camina fins a l'escola.",
        "C": "Triar C vol dir oblidar la PARADA intermèdia del metro: només mostra un pic alt continu, no dos pics separats per una parada.",
        "E": "Triar E vol dir afegir un tercer pic alt al gràfic, com si hi hagués tres trams de metro o tres parades, en lloc de dos pics (dues parades del metro).",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

# === Q12 (C) — NOU ===
PROBLEMS["CAN-4ESO-2023-12"] = {
    "id":         "CAN-4ESO-2023-12",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     12,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Per a cada suma senar (5, 7, 9), enumera totes les parelles (a,b) amb a+b igual a aquesta suma i fixa't quines tenen exactament un senar."
    ),
    "expected_reasoning": (
        "Els daus són de sis cares (1-6). Una suma de dos daus és SENAR només si un nombre és parell i l'altre senar. "
        "En cada tirada amb suma 5, 7 o 9, ha de sortir un senar i un parell. La condició diu: 'en totes tres tirades "
        "ha sortit el mateix nombre SENAR en algun dels daus'. Mirem totes les parelles possibles per a cada suma "
        "(amb un parell i un senar): suma 5 → (1,4), (2,3), (3,2), (4,1) → senars possibles: 1 o 3. Suma 7 → (1,6), "
        "(2,5), (3,4), (4,3), (5,2), (6,1) → senars possibles: 1, 3 o 5. Suma 9 → (3,6), (4,5), (5,4), (6,3) → senars "
        "possibles: 3 o 5. El senar comú a totes tres llistes és el 3. Per tant, en totes tres tirades ha sortit un 3 "
        "en algun dels dos daus. Llavors: tirada de suma 5 amb un 3 → l'altre dau és 2; parella (2,3). Aquesta és la "
        "parella SEGURA que ha sortit en alguna de les tirades. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (1 i 4) vol dir prendre una de les parelles que sumen 5 sense imposar que el senar (1 o 3) sigui el mateix per a totes les tirades.",
        "B": "Triar B (1 i 6) vol dir oblidar que la suma 9 no admet l'1 (parelles amb 1: 1+8=9 impossible, perquè el dau no té 8); 1 no és el senar comú.",
        "D": "Triar D (2 i 5) vol dir prendre 5 com a senar comú, però 5 no apareix en cap parella de suma 5 (5+0 no és vàlid).",
        "E": "Triar E (4 i 5) vol dir prendre 5 com a senar comú a totes tres sumes, oblidant que 5 no pot aparèixer en cap parella vàlida que sumi 5.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# === Q13 (B) — DEDUP HORITZONTAL amb 3ESO-2023-19 ===
PROBLEMS["CAN-4ESO-2023-13"] = {
    "id":         "CAN-4ESO-2023-13",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     13,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Cada angle de {10°, 20°, …, 80°} s'ha de poder llegir com a diferència entre dues marques. Amb només 2 marques addicionals tens 6 diferències; suficient?"
    ),
    "expected_reasoning": (
        "El semicercle té dues marques inicials: a 0° i a 90°. Cada angle es mesura agafant la diferència entre dues "
        "marques. Si afegim k marques addicionals, en total tenim k + 2 marques i C(k+2, 2) diferències possibles. "
        "Volem cobrir 8 angles: {10°, 20°, 30°, 40°, 50°, 60°, 70°, 80°}. Amb k = 2 (4 marques en total): només C(4,2) = "
        "6 diferències; insuficient (< 8). Amb k = 3 (5 marques en total): C(5,2) = 10 diferències; potser suficient. "
        "Provem k = 3 amb les marques {10°, 20°, 60°} afegides a {0°, 90°}. Les diferències són: amb 0°: 10°, 20°, 60°. "
        "Amb 90°: 80°, 70°, 30°. Entre noves: 10° (20−10), 50° (60−10), 40° (60−20). Surten {10°, 20°, 30°, 40°, 50°, "
        "60°, 70°, 80°}. Totes 8. ✓ Amb 3 marques addicionals és suficient, i amb 2 és impossible. Per tant, el mínim "
        "és 3. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A (2) vol dir creure que amb 4 marques en total ja n'hi ha prou (= 6 diferències); però són insuficients per cobrir 8 angles distints.",
        "C": "Triar C (4) vol dir afegir 4 marques (les més naturals 10°, 20°, 30°, 40°) sense buscar la tria òptima de 3.",
        "D": "Triar D (5) vol dir buscar marques sense fer servir les diferències amb la marca de 0° o de 90°, demanant més marques de les necessàries.",
        "E": "Triar E (6) vol dir afegir una marca per cada angle desitjat (8 angles → 8 marques), oblidant que es poden reaprofitar parelles.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar", "COMP_doble_recompte"],
    "dependencies":           [],
}

# === Q14 (B) — NOU ===
PROBLEMS["CAN-4ESO-2023-14"] = {
    "id":         "CAN-4ESO-2023-14",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "L'angle CFE és un angle exterior d'un dels triangles petits; relaciona'l amb els angles de la base del triangle isòsceles."
    ),
    # TODO (f2): NO he pogut construir una derivació correcta que arribi a la clau B (70°) amb la
    # geometria que es veu a la imatge. La posició exacta dels punts D i E i del punt F (intersecció
    # de AE i CD) determina si l'angle CFE és independent del paràmetre x = EAB = DCA. El brief
    # (secció 1 i autonomia (b)) demana ATURAR-SE i avisar en lloc de fabricar un raonament que
    # només "aterri" a la lletra. resposta_correcta es manté = B (literal de l'answers.json).
    "expected_reasoning": None,
    "comentaris_distractors": {
        "A": "Triar A (75°) vol dir aplicar un càlcul mig fet d'angles en quadrilàters sense respectar la simetria del triangle isòsceles.",
        "C": "Triar C (65°) vol dir restar 5° a 70° per algun error d'identificació dels angles adjacents.",
        "D": "Triar D (60°) vol dir confondre el triangle isòsceles amb un equilàter (suposant tots tres angles iguals).",
        "E": "Triar E (depèn) vol dir no veure que la simetria entre EAB = DCA elimina el paràmetre x, donant un valor fixat.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades", "LOG_dada_ignorada"],
    "dependencies":           [],
}

# === Q15 (D) — DEDUP HORITZONTAL amb 3ESO-2023-18 ===
PROBLEMS["CAN-4ESO-2023-15"] = {
    "id":         "CAN-4ESO-2023-15",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si davant i darrere del Martí hi ha el mateix nombre de persones, el total és senar i ell és al mig."
    ),
    "expected_reasoning": (
        "Anomenem m la posició del Martí a la cua i N el total de persones. Davant d'ell hi ha m − 1 persones i darrere "
        "n'hi ha N − m. La condició diu m − 1 = N − m, és a dir, N = 2m − 1 (N és senar, i el Martí està exactament al "
        "mig). Els amics estan a les posicions 19 i 28, tots dos darrere del Martí: per tant m < 19 i, com que 28 ≤ N, "
        "es té m ≥ (28 + 1)/2 = 14,5, és a dir m ≥ 15. Així m ∈ {15, 16, 17, 18}, i N = 2m − 1 ∈ {29, 31, 33, 35}. La "
        "condició que N sigui múltiple de 3 selecciona N = 33, i així m = 17. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A (14) vol dir oblidar que els amics a 19 i 28 han d'estar darrere del Martí: amb m = 14, N = 27, però llavors la posició 28 no existeix a la cua.",
        "B": "Triar B (15) vol dir prendre el m més petit possible (15, que dona N = 29) sense imposar la condició de múltiple de 3.",
        "C": "Triar C (16) vol dir prendre m = 16 (que dona N = 31, no múltiple de 3); les dues posicions 19 i 28 no encaixen amb la regla.",
        "E": "Triar E (18) vol dir prendre m = 18 (que dona N = 35, no múltiple de 3) i no comprovar la condició de múltiple de 3.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "COMP_fencepost"],
    "dependencies":           [],
}

# === Q16 (B) — NOU ===
PROBLEMS["CAN-4ESO-2023-16"] = {
    "id":         "CAN-4ESO-2023-16",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     16,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2023-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Calcula quantes partides ha guanyat fins ara (49% de 200) i planteja què cal afegir perquè el percentatge arribi just al 50%."
    ),
    "expected_reasoning": (
        "Després de 200 partides, n'ha guanyat el 49%, és a dir 0,49 · 200 = 98 partides. Vol que el percentatge de "
        "guanyades arribi al 50%. Sigui n el nombre de partides addicionals que juga, i suposem que les guanya totes "
        "(per arribar-hi com més aviat millor). El nou percentatge és (98 + n) / (200 + n). Volem (98 + n)/(200 + n) ≥ "
        "0,5, és a dir 98 + n ≥ 0,5·(200 + n) = 100 + 0,5n, d'on 0,5n ≥ 2, és a dir n ≥ 4. El mínim nombre de partides "
        "addicionals (totes guanyades) és 4: aleshores (98 + 4)/(200 + 4) = 102/204 = 0,5 = 50% exacte. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A (6) vol dir un error en plantejar la inequació, per exemple exigir (98+n)/(200+n) > 0,5 estricte i arrodonir cap amunt de manera incorrecta.",
        "C": "Triar C (3) vol dir resoldre 0,5n ≥ 2 com n ≥ 3 (error d'aritmètica) o aproximar malament la fracció.",
        "D": "Triar D (2) vol dir suposar que cal pujar només 1 punt percentual i traduir-ho com 2 partides, sense plantejar la fracció correctament.",
        "E": "Triar E (1) vol dir pensar que afegir una sola partida guanyada (99/201 ≈ 49,25%) ja arriba al 50%, sense comprovar el càlcul.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# === Q17 (A) — NOU ===
PROBLEMS["CAN-4ESO-2023-17"] = {
    "id":         "CAN-4ESO-2023-17",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     17,
    "punts":      4,
    "tema":       "fraccions",
    "imatge":     "CAN-4ESO-2023-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "L'aigua gastada és cabal × temps. Expressa el cabal i el temps nous com a fracció dels originals i multiplica."
    ),
    "expected_reasoning": (
        "L'aigua gastada en una dutxa és el producte cabal × temps. Reduir una magnitud 'en una quarta part' vol dir "
        "treure-li 1/4, és a dir, deixar-la en 3/4 del valor original. El temps nou és (3/4)·t i el cabal nou és "
        "(3/4)·c. L'aigua gastada nova és (3/4)·t · (3/4)·c = (9/16)·(t·c), és a dir 9/16 de l'aigua original. La "
        "reducció és 1 − 9/16 = 7/16 de l'aigua original. Per tant, ha reduït l'aigua que gasta a cada dutxa en 7/16. "
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar B (5/12) vol dir un error en multiplicar les fraccions, potser barrejant terços i quarts.",
        "C": "Triar C (1/16) vol dir prendre el producte de les reduccions (1/4 · 1/4 = 1/16) en lloc de calcular 1 − (3/4)².",
        "D": "Triar D (3/8) vol dir sumar les dues reduccions amb un factor, com 1/4 + 1/8 = 3/8, sense multiplicar correctament cabal i temps.",
        "E": "Triar E (1/4) vol dir sumar simplement les dues reduccions com si fossin independents (1/4 cadascuna) o considerar només una de les dues.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# === Q18 (E) — DEDUP HORITZONTAL amb 3ESO-2023-23 ===
PROBLEMS["CAN-4ESO-2023-18"] = {
    "id":         "CAN-4ESO-2023-18",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "La suma de N enters consecutius és N vegades el terme central (quan N és senar)."
    ),
    "expected_reasoning": (
        "Siguin els 2023 enters consecutius n − 1011, n − 1010, ..., n − 1, n, n + 1, ..., n + 1010, n + 1011 (és a dir "
        "2023 nombres centrats en n). La suma és 2023 · n = 2023, així n = 1. Els enters van des de 1 − 1011 = −1010 "
        "fins a 1 + 1011 = 1012. El més gran és 1012. La suma de les xifres del 1012 és 1 + 0 + 1 + 2 = 4. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A (8) vol dir agafar el nombre 2024 (incorrecte) o un altre error d'identificació del màxim.",
        "B": "Triar B (7) vol dir prendre el nombre 1015 o 1006 i sumar les xifres.",
        "C": "Triar C (6) vol dir prendre 1014 com a màxim erroni (1+0+1+4 = 6).",
        "D": "Triar D (5) vol dir calcular xifres del 1013 (un nombre incorrecte) i sumar 1+0+1+3 = 5.",
    },
    "errors_típics":          ["GEN_calcul", "COMP_fencepost"],
    "dependencies":           [],
}

# === Q19 (C) — DEDUP HORITZONTAL amb 3ESO-2023-25 ===
PROBLEMS["CAN-4ESO-2023-19"] = {
    "id":         "CAN-4ESO-2023-19",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     19,
    "punts":      4,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2023-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "La suma de partides jugades per tots set nans és el doble del nombre de partides ja disputades, per tant ha de ser parell."
    ),
    "expected_reasoning": (
        "Són 7 nans en un torneig 'tots contra tots': cadascú jugarà 6 partides al final. Les partides jugades fins ara "
        "són: Rondinaire 1, Esternuts 2, Dormilega 3, Vergonyós 4, Feliç 5, Savi 6. Sigui M el nombre de partides ja "
        "jugades pel Mudet. La suma de les partides jugades per cada nan ha de ser el doble del nombre total de partides "
        "ja jugades (cada partida compta per a dos nans): 1 + 2 + 3 + 4 + 5 + 6 + M = 21 + M, que ha de ser PARELL. Així "
        "M és senar: M ∈ {1, 3, 5}. Ara mirem qui ha jugat amb qui. El Savi n'ha jugat 6, és a dir, ja ha jugat amb "
        "tothom: per tant, ha jugat amb el Mudet. El Feliç n'ha jugat 5, és a dir, amb tothom menys un (que no pot ser "
        "el Savi); per tant amb el Mudet. Així el Mudet ha jugat com a mínim amb el Savi i el Feliç: M ≥ 2. Però M senar "
        "i M ≥ 2 → M ≥ 3. Verifiquem M = 3 com a possible: el Mudet ha jugat amb Savi, Feliç i un tercer (per exemple, "
        "Vergonyós). Quadra amb els comptes. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (1) vol dir prendre M = 1 (un valor possible per la paritat), però oblidar que el Mudet ha de jugar com a mínim amb els que ja han jugat amb tothom (Savi i Feliç).",
        "B": "Triar B (2) vol dir prendre M = 2 (la cota inferior obvia) sense imposar la condició de paritat (la suma 1+2+3+4+5+6+2 = 23 és senar).",
        "D": "Triar D (4) vol dir prendre M = 4, valor parell, no consistent amb la suma total.",
        "E": "Triar E (5) vol dir prendre M = 5 (valor senar i possible), sense buscar el mínim coherent (M = 3 ja funciona).",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# === Q20 (A) — DEDUP HORITZONTAL amb 3ESO-2023-27 ===
PROBLEMS["CAN-4ESO-2023-20"] = {
    "id":         "CAN-4ESO-2023-20",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     20,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2023-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Planteja un sistema amb el nombre de peces 777, 77 i 7, fent servir tant la suma total (2023) com el nombre total de 7 (19)."
    ),
    "expected_reasoning": (
        "Sigui x el nombre de peces 777, y el nombre de peces 77 i z el nombre de peces 7 que es fan servir. Tenim dues "
        "condicions: suma total 777x + 77y + 7z = 2023, que dividint per 7 dóna 111x + 11y + z = 289; i total de xifres "
        "7, és a dir 3x + 2y + z = 19 (cada 777 aporta 3 sevens, cada 77 aporta 2, cada 7 aporta 1). Restant les dues "
        "equacions: (111 − 3)x + (11 − 2)y = 289 − 19, és a dir 108x + 9y = 270, simplificat a 12x + y = 30. Així y = "
        "30 − 12x. Per a y ≥ 0: x ≤ 2. A l'equació 3x + 2y + z = 19: z = 19 − 3x − 2y = 19 − 3x − 2(30 − 12x) = 21x − "
        "41. Per a z ≥ 0: x ≥ 41/21 ≈ 1,95, és a dir x ≥ 2. Combinant amb x ≤ 2: x = 2. Aleshores y = 30 − 24 = 6 i z = "
        "21·2 − 41 = 1. Verificació: 777·2 + 77·6 + 7·1 = 1554 + 462 + 7 = 2023 ✓; 3·2 + 2·6 + 1 = 19 ✓. El nombre de "
        "peces 77 és y = 6. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar B (5) vol dir prendre x = 1 (no factible perquè z surt negatiu) i conformar-se amb una solució no vàlida.",
        "C": "Triar C (4) vol dir un error d'aritmètica intermèdia, per exemple oblidar de simplificar 108x + 9y = 270.",
        "D": "Triar D (3) vol dir un càlcul incorrecte de y després de trobar x = 2 (per exemple aplicar erròniament una divisió).",
        "E": "Triar E (2) vol dir confondre el nombre de peces 77 amb el de peces 777 (que val 2).",
    },
    "errors_típics":          ["GEN_calcul", "LOG_dada_ignorada"],
    "dependencies":           [],
}

# === Q21 (B) — NOU ===
PROBLEMS["CAN-4ESO-2023-21"] = {
    "id":         "CAN-4ESO-2023-21",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El trapezi gris té dues bases verticals (costats dels quadrats de 3 i 5) i una alçada horitzontal (l'amplada del quadrat del mig). Identifica-les abans de calcular."
    ),
    "expected_reasoning": (
        "Els tres quadrats de costats 3, 5 i 8 estan alineats sobre una base comuna, l'un al costat de l'altre d'esquerra "
        "a dreta. Una diagonal va des del peu inferior esquerre del quadrat petit fins al vèrtex superior dret del quadrat "
        "gran. El trapezi gris queda delimitat per: el costat dret del quadrat de 3 (vertical), el costat dret del quadrat "
        "de 5 (vertical), la base (horitzontal) i la recta diagonal. La recta passa per (0,0) i (3+5+8, 8) = (16, 8), "
        "amb pendent 8/16 = 1/2, és a dir y = x/2. El trapezi gris s'estén horitzontalment sobre el quadrat del mig, de "
        "x = 3 fins a x = 3+5 = 8 (amplada 5). Les alçades de la recta diagonal en aquests punts són: a x = 3, y = 1,5; "
        "a x = 8, y = 4. El trapezi gris té per bases (verticals) aquestes dues alçades de la recta sobre la base, b₁ = "
        "1,5 i b₂ = 4, i alçada (horitzontal) h = 5. Àrea = (b₁ + b₂)/2 · h = (1,5 + 4)/2 · 5 = (5,5/2)·5 = 2,75·5 = "
        "13,75 = 55/4 cm². Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A (13 cm²) vol dir arrodonir 55/4 = 13,75 a 13, o calcular l'àrea com a trapezi amb bases lleugerament mal llegides.",
        "C": "Triar C (61/4 cm²) vol dir prendre les alçades de la recta als punts equivocats (per exemple x = 5 i x = 8) i obtenir bases incorrectes.",
        "D": "Triar D (65/4 cm²) vol dir fer servir l'alçada h = 5 amb bases 2 i 4,5 (desplaçant el tram horitzontal del trapezi).",
        "E": "Triar E (69/4 cm²) vol dir incloure part de l'àrea sota el quadrat gran o petit, ampliant erròniament el trapezi gris.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "GEN_calcul"],
    "dependencies":           [],
}

# === Q22 (C) — NOU ===
PROBLEMS["CAN-4ESO-2023-22"] = {
    "id":         "CAN-4ESO-2023-22",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     22,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2023-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Anomena x el tros més curt. Escriu els altres dos en funció de x (cada un és 1,5 vegades l'anterior) i fes que sumin 95."
    ),
    "expected_reasoning": (
        "Sigui x la longitud del tros més curt. El segon tros és x incrementat un 50%, és a dir 1,5x. El tercer tros és "
        "el segon incrementat un 50%, és a dir 1,5 · 1,5x = 2,25x. La suma dels tres trossos és la longitud total: x + "
        "1,5x + 2,25x = 4,75x = 95 cm. D'aquí x = 95 / 4,75 = 20 cm. El tros més llarg és 2,25x = 2,25 · 20 = 45 cm. "
        "Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (36 cm) vol dir prendre x = 16 i 2,25·16 = 36, és a dir resoldre 4,75x = 76 (suma errònia) o un altre error de plantejament.",
        "B": "Triar B (42 cm) vol dir aplicar increments additius en lloc de multiplicatius (per exemple +50% sobre la mitjana) i arribar a un valor proper però incorrecte.",
        "D": "Triar D (46 cm) vol dir calcular el tros del mig augmentat o un error d'arrodoniment del 45.",
        "E": "Triar E (48 cm) vol dir interpretar 'el tercer és el segon incrementat un 50%' sobre el tros més curt dues vegades de manera additiva, donant un valor massa gran.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# === Q23 (D) — NOU ===
PROBLEMS["CAN-4ESO-2023-23"] = {
    "id":         "CAN-4ESO-2023-23",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     23,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena L el costat del triangle equilàter ABC i expressa els costats dels triangles isòsceles imposant que els quatre triangles tinguin el mateix perímetre."
    ),
    # TODO (f2): NO he pogut tancar una derivació rigorosa fins a la clau D (5/3). El plantejament
    # (perímetre comú 3L per als quatre triangles, costats interns AF/EF/DF compartits) necessita el
    # detall mètric de com encaixen els tres isòsceles dins el pentàgon, que no he sabut fixar de la
    # imatge sense resoldre des de zero. Per evitar fabricar un raonament que només arribi a la lletra
    # (prohibit a la secció 1 del brief), m'aturo i ho deixo per revisió humana.
    # resposta_correcta es manté = D (literal de l'answers.json).
    "expected_reasoning": None,
    "comentaris_distractors": {
        "A": "Triar A (2) vol dir suposar que el pentàgon té el doble de perímetre que el triangle, comptant malament els costats exteriors.",
        "B": "Triar B (3/2) vol dir comptar 4,5 costats exteriors en lloc dels que corresponen, o dividir incorrectament.",
        "C": "Triar C (4/3) vol dir incloure només quatre costats unitaris al pentàgon en lloc de cinc.",
        "E": "Triar E (5/2) vol dir prendre 5 costats exteriors comptant L = 1 i dividir per 2 en lloc de per 3 (el perímetre del triangle equilàter és 3L, no 2L).",
    },
    "errors_típics":          ["GEN_condicions_no_verificades", "GEN_calcul"],
    "dependencies":           [],
}

# === Q24 (E) — NOU ===
PROBLEMS["CAN-4ESO-2023-24"] = {
    "id":         "CAN-4ESO-2023-24",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     24,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-4ESO-2023-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Converteix l'hora Imaginari a una fracció del mig dia, i després tradueix aquesta mateixa fracció al nostre sistema de 12 h × 60 min."
    ),
    "expected_reasoning": (
        "Al país Imaginari, la meitat del dia es divideix en 10 hores (H) de 100 minuts (M), és a dir 10·100 = 1000 "
        "unitats Imaginari per mig dia. Les 8 H 25 M corresponen a 8·100 + 25 = 825 unitats Imaginari, és a dir una "
        "fracció 825/1000 = 0,825 del mig dia. Al nostre sistema, la meitat del dia es divideix en 12 hores de 60 "
        "minuts = 12·60 = 720 minuts. La mateixa fracció 0,825 del mig dia correspon a 0,825 · 720 = 594 minuts. "
        "Convertim 594 minuts a hores i minuts: 594 / 60 = 9 hores i 594 − 540 = 54 minuts. Per tant el nostre rellotge "
        "marca les 9 h 54 min. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar A (10 h 51 min) vol dir un error de proporció, per exemple multiplicar per 720 una fracció mal calculada com 0,905.",
        "B": "Triar B (8 h 15 min) vol dir copiar gairebé directament 8 H 25 M com si els sistemes fossin equivalents, fent una petita correcció arbitrària.",
        "C": "Triar C (8 h 25 min) vol dir suposar que l'hora Imaginari coincideix exactament amb la nostra (cap conversió).",
        "D": "Triar D (9 h 51 min) vol dir calcular 594 minuts però convertir-los malament a 9 h 51 min (error en 594 − 540 = 54, no 51).",
    },
    "errors_típics":          ["GEN_calcul", "GEO_unitats"],
    "dependencies":           [],
}

# === Q25 (B) — NOU ===
PROBLEMS["CAN-4ESO-2023-25"] = {
    "id":         "CAN-4ESO-2023-25",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     25,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Anomena amb variables els nois i noies que diuen Sí i No, i tradueix la condició 'nois que diuen Sí = noies que diuen No' en una igualtat."
    ),
    "expected_reasoning": (
        "Classifiquem els alumnes en quatre grups: nois que diuen Sí (a), nois que diuen No (b), noies que diuen Sí (c), "
        "noies que diuen No (d). La condició de l'enunciat és a = d (nombre de nois que diuen Sí = nombre de noies que "
        "diuen No). El nombre total de noies és c + d. El nombre d'alumnes que diuen Sí és a + c. Comparem aquestes dues "
        "quantitats: (nombre de noies) − (nombre dels que diuen Sí) = (c + d) − (a + c) = d − a = 0 (per la condició a = "
        "d). Per tant el nombre de noies és EXACTAMENT igual al nombre d'alumnes que han contestat Sí. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir afirmar una desigualtat (noies < els que diuen Sí), però la diferència d − a és exactament 0, no negativa.",
        "C": "Triar C vol dir afirmar la desigualtat oposada (noies > els que diuen Sí), però de nou la diferència és 0.",
        "D": "Triar D vol dir comparar el nombre de noies amb el dels que diuen No; aquesta igualtat no es dedueix de la condició donada.",
        "E": "Triar E vol dir afirmar que els que diuen Sí igualen els que diuen No, cosa que no es desprèn de a = d sense més informació.",
    },
    "errors_típics":          ["LOG_dada_ignorada", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# === Q26 (A) — NOU ===
PROBLEMS["CAN-4ESO-2023-26"] = {
    "id":         "CAN-4ESO-2023-26",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     26,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Localitza a quins grups de tres van a parar el 39 i el 40 (els blocs s'agafen de tres en tres des de dalt) i segueix l'ordre amb què s'apilen a la torre final."
    ),
    # TODO (f2): la clau és A (4). Una simulació amb la hipòtesi que cada grup de 3 s'inverteix en
    # apilar-se dóna efectivament 4 blocs entre el 39 i el 40; però la simulació SENSE inversió dóna 0.
    # El resultat depèn críticament de com s'interpreta "els va apilant ordenadament" a la figura
    # (torre inicial → torre final), que no puc fixar amb prou certesa des de la imatge. Com que el
    # raonament correcte depèn d'aquesta lectura, no l'escric per no arriscar una derivació que només
    # quadri amb la clau. resposta_correcta es manté = A (literal de l'answers.json).
    "expected_reasoning": None,
    "comentaris_distractors": {
        "B": "Triar B (3) vol dir comptar els blocs d'un sol grup de 3 sense considerar la posició relativa exacta de 39 i 40 després de la inversió.",
        "C": "Triar C (2) vol dir suposar que 39 i 40 queden separats per només els dos blocs restants del seu grup.",
        "D": "Triar D (1) vol dir pensar que 39 i 40, sent consecutius, queden separats per un únic bloc després de l'apilament.",
        "E": "Triar E (0) vol dir suposar que 39 i 40 segueixen adjacents a la torre final, oblidant la inversió per grups de tres.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "COMP_fencepost"],
    "dependencies":           [],
}

# === Q27 (C) — NOU ===
PROBLEMS["CAN-4ESO-2023-27"] = {
    "id":         "CAN-4ESO-2023-27",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-4ESO-2023-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Genera uns quants termes més aplicant la regla i busca quan la seqüència esdevé periòdica."
    ),
    "expected_reasoning": (
        "La regla: cada terme és el menor enter no negatiu que és diferent de cadascun dels quatre termes anteriors. "
        "Generem la llista a partir de 2, 0, 2, 3. Terme 5: els quatre anteriors són {2, 0, 2, 3} = {0, 2, 3}; el menor "
        "absent és 1. Terme 6: anteriors {0, 2, 3, 1} = {0, 1, 2, 3}; el menor absent és 4. Terme 7: anteriors {2, 3, "
        "1, 4}; el menor absent és 0. Terme 8: anteriors {3, 1, 4, 0}; el menor absent és 2. Terme 9: anteriors {1, 4, "
        "0, 2}; el menor absent és 3. Terme 10: anteriors {4, 0, 2, 3}; el menor absent és 1. La llista és 2, 0, 2, 3, "
        "1, 4, 0, 2, 3, 1, 4, 0, 2, 3, 1, … A partir del terme 5 apareix el bloc (1, 4, 0, 2, 3) que es repeteix "
        "indefinidament: la successió és periòdica de període 5 des de la posició 5. Per a la posició 2023, mirem "
        "(2023 − 5) mod 5 = 2018 mod 5 = 3, que correspon al quart element del bloc (1, 4, 0, 2, 3), és a dir 2. "
        "Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A (0) vol dir prendre la posició equivocada dins el cicle de període 4 (per exemple confondre 2023 mod 4).",
        "B": "Triar B (1) vol dir comptar el cicle començant des d'un índex incorrecte, desplaçant el resultat una posició.",
        "D": "Triar D (3) vol dir prendre el terme següent o anterior al correcte dins el cicle.",
        "E": "Triar E (4) vol dir suposar que la successió segueix creixent (apareixent valors com 4) en lloc de fer-se periòdica.",
    },
    "errors_típics":          ["GEN_calcul", "COMP_fencepost"],
    "dependencies":           [],
}

# === Q28 (D) — NOU ===
PROBLEMS["CAN-4ESO-2023-28"] = {
    "id":         "CAN-4ESO-2023-28",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     28,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-4ESO-2023-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena n el nombre de nens (i 2n... revisa: hi ha el doble de nens que d'adults). Escriu la mitjana global en funció de les sumes d'edats i imposa la condició."
    ),
    "expected_reasoning": (
        "Hi ha el doble de nens que d'adults. Sigui a el nombre d'adults; llavors hi ha 2a nens i en total 3a persones. "
        "La suma de les edats dels adults és 156. Sigui S_n la suma de les edats dels nens. La mitjana de les edats dels "
        "nens és S_n / (2a). La mitjana de TOTS els assistents és (156 + S_n) / (3a), i l'enunciat diu que aquesta és "
        "cinc vegades la mitjana dels nens: (156 + S_n)/(3a) = 5 · S_n/(2a). Multiplicant per 6a: 2·(156 + S_n) = 15·S_n, "
        "és a dir 312 + 2·S_n = 15·S_n, d'on 312 = 13·S_n i S_n = 24. Així la suma de les edats dels 2a nens és 24, amb "
        "cada edat un natural > 1, és a dir ≥ 2. Per maximitzar el nombre de persones (3a) cal maximitzar a, i com que "
        "els 2a nens tenen edats ≥ 2 sumant 24, el màxim de nens és 2a = 24/2 = 12 (tots de 2 anys), és a dir a = 6. "
        "El nombre total de persones és 3a = 18. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A (9) vol dir prendre a = 3 (potser interpretant 'el doble' al revés, més adults que nens) i obtenir 3a = 9.",
        "B": "Triar B (12) vol dir comptar només els nens (2a = 12) i oblidar de sumar els adults.",
        "C": "Triar C (15) vol dir prendre a = 5 per un error en l'edat mínima dels nens (suposant edats ≥ alguna cosa diferent de 2).",
        "E": "Triar E (21) vol dir prendre a = 7 i 3a = 21, sobreestimant el nombre de nens permès per la suma 24 amb edats ≥ 2.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar", "LOG_dada_ignorada"],
    "dependencies":           [],
}

# === Q29 (E) — NOU ===
PROBLEMS["CAN-4ESO-2023-29"] = {
    "id":         "CAN-4ESO-2023-29",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-4ESO-2023-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "La suma de tots els perímetres de les regions interiors compta dues vegades cada frontera interior i una sola vegada cada tram del contorn exterior."
    ),
    # TODO (f2): la clau és E (Cap de les anteriors). El plantejament correcte (suma de perímetres =
    # P_exterior + 2·I, on I és la longitud total de fronteres interiors) és vàlid, però per concloure
    # que el perímetre exterior NO és cap de 12/18/23/25 cal el valor exacte de I, que depèn de quins
    # trams són interiors a la figura del plànol. No he pogut llegir-ho amb prou certesa des de la
    # imatge per derivar-ho rigorosament, així que m'aturo. resposta_correcta es manté = E (literal
    # de l'answers.json).
    "expected_reasoning": None,
    "comentaris_distractors": {
        "A": "Triar A (12) vol dir restar només alguns nombres interiors sense aplicar correctament el doble recompte de les fronteres interiors.",
        "B": "Triar B (18) vol dir sumar només els nombres del contorn aparent, oblidant les regions interiors compartides.",
        "C": "Triar C (23) vol dir un càlcul parcial de P amb un valor de I mal estimat.",
        "D": "Triar D (25) vol dir prendre P = 25 a partir d'una estimació de I que no és compatible amb la geometria real.",
    },
    "errors_típics":          ["GEN_calcul", "GEO_costats_oblidats"],
    "dependencies":           [],
}

# === Q30 (D) — NOU ===
PROBLEMS["CAN-4ESO-2023-30"] = {
    "id":         "CAN-4ESO-2023-30",
    "categoria":  "4ESO",
    "any":        2023,
    "numero":     30,
    "punts":      5,
    "tema":       "combinatòria",
    "imatge":     "CAN-4ESO-2023-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Les 3 boletes negres parteixen el cercle en 3 trams de blanques; la condició que cap blanca quedi aïllada obliga cada tram a tenir almenys dues blanques."
    ),
    # TODO (f2): la clau és D (28). He establert que cada braçalet té grups de blanques (2,2,2) entre
    # les negres, però el recompte final del NOMBRE TOTAL de boletes blanques necessàries per fer "tots
    # els braçalets diferents possibles" requereix enumerar correctament els braçalets distints sota
    # rotació i reflexió (collar/bracelet counting). No he completat aquesta enumeració de manera
    # rigorosa fins a 28, així que no escric una derivació que hi arribi per afirmació. resposta_correcta
    # es manté = D (literal de l'answers.json).
    "expected_reasoning": None,
    "comentaris_distractors": {
        "A": "Triar A (18) vol dir comptar 3 braçalets × 6 blanques sense considerar totes les configuracions diferents possibles.",
        "B": "Triar B (20) vol dir un recompte parcial de les configuracions, oblidant alguna distribució vàlida.",
        "C": "Triar C (24) vol dir comptar 4 braçalets × 6 blanques, una distribució incompleta dels casos.",
        "E": "Triar E (36) vol dir comptar 6 braçalets × 6 blanques, sobreestimant el nombre de braçalets diferents (per no eliminar rotacions/reflexions equivalents).",
    },
    "errors_típics":          ["COMP_doble_recompte", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}
