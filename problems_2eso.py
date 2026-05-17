"""
Tutor Cangur — 2ESO problem catalogue.

Conté els 30 problemes de la prova 2ESO (tots els anys disponibles).
Afegir nous problemes aquí; mai modificar els d'altres nivells.

Estructura de cada entrada: vegeu SCHEMA.md.
"""

from problems_shared import ERROR_CATALOG, DEPENDENCIES  # noqa: F401

PROBLEMS = {}

PROBLEMS["CAN-2ESO-2026-01"] = {
    "id":         "CAN-2ESO-2026-01",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     1,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Comprova una per una les dues condicions a cada opció. Recorda que la polsera és "
        "circular: el primer i l'últim complement també són veïns."
    ),
    "expected_reasoning": (
        "Cada polsera té sis complements distribuïts en cercle, de tres formes diferents: "
        "rodons, quadrats i triangles. Cal complir alhora dues condicions: tenir dos rodons "
        "seguits i no tenir cap parell de quadrats junts. A l'opció A hi ha rodons seguits a "
        "dalt, però els dos quadrats inferiors són adjacents, així que viola la segona "
        "condició. A l'opció B els quadrats apareixen seguits a la part inferior i, a més, "
        "els dos rodons queden separats per altres complements; falla en les dues "
        "condicions. A l'opció D els dos rodons estan en posicions oposades, separats per "
        "triangles i quadrats, així que falla la condició de tenir-ne dos seguits. A "
        "l'opció E hi ha dos rodons seguits a dalt, però els dos quadrats també queden "
        "adjacents a sota, així que viola la condició de no tenir dos quadrats junts. "
        "L'opció C compleix les dues condicions: hi ha dos rodons seguits i només hi ha un "
        "quadrat, de manera que no és possible tenir-ne dos junts. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "L'opció A té dos rodons seguits, però els dos quadrats també queden adjacents i això viola la condició de no tenir dos quadrats junts.",
        "B": "L'opció B té els quadrats agrupats (i fins i tot tres seguits) i, a més, els dos rodons que té estan separats, de manera que falla en les dues condicions.",
        "D": "L'opció D no té dos rodons seguits: els dos rodons que conté estan situats en costats oposats de la polsera, separats per triangles i quadrats.",
        "E": "L'opció E té dos rodons seguits a dalt, però també dos quadrats adjacents a baix, cosa que viola la condició de no tenir dos quadrats junts.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-02"] = {
    "id":         "CAN-2ESO-2026-02",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-02.jpg",
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

PROBLEMS["CAN-2ESO-2026-03"] = {
    "id":         "CAN-2ESO-2026-03",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     3,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Les xifres parelles disponibles són 0, 2, 4, 6 i 8. Els dos primers dígits de l'any "
        "ja són 2 i 0; quines dues xifres parelles diferents (i diferents de 2 i 0) hi pots "
        "afegir per formar el primer any superior a 2026?"
    ),
    "expected_reasoning": (
        "Les xifres parelles són 0, 2, 4, 6 i 8. Un any del segle XXI s'escriu 20XY, així "
        "que les xifres 2 i 0 ja hi són. Perquè tot l'any tingui les quatre xifres parelles "
        "i totes diferents, X i Y han de ser xifres parelles diferents entre elles i "
        "diferents de 0 i 2, és a dir, dues triades entre 4, 6 i 8. El primer any superior a "
        "2026 amb aquesta forma és el 2046 (xifres 2, 0, 4, 6, totes parelles i diferents). "
        "Verifiquem que cap any entre 2027 i 2045 ho compleixi: els anys senars queden "
        "descartats; 2028 repeteix el 2; 2040, 2042 i 2044 repeteixen una xifra (el 0, el 2 "
        "o el 4). Per tant, 2046 − 2026 = 20 anys. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 42 vol dir saltar fins al 2068 (xifres 2, 0, 6, 8) com a primer candidat, sense adonar-se que 2046 ja compleix les condicions i és anterior.",
        "B": "Obtenir 38 vol dir aturar-se al 2064 (xifres 2, 0, 6, 4), que sí que té totes les xifres parelles i diferents, però no és el primer: el 2046 és anterior.",
        "C": "Obtenir 22 vol dir proposar el 2048 com a primer any vàlid, però el 2046 també compleix les condicions i és anterior.",
        "E": "Obtenir 2 vol dir proposar el 2028, però el 2028 té dues xifres 2 i no compleix la condició de tenir totes les xifres diferents.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-04"] = {
    "id":         "CAN-2ESO-2026-04",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     4,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Prova d'escriure cada nombre com a suma de dos o més enters positius consecutius. "
        "Hi ha un d'aquests nombres que és una potència de 2, i pels nombres d'aquesta forma "
        "passa una cosa especial."
    ),
    "expected_reasoning": (
        "Cal trobar el nombre de la llista que no es pot escriure com a suma de dos o més "
        "enters positius consecutius. Per al 5: 2 + 3 = 5 ✓. Per al 6: 1 + 2 + 3 = 6 ✓. Per "
        "al 7: 3 + 4 = 7 ✓. Per al 9: 4 + 5 = 9 (o 2 + 3 + 4) ✓. Per al 8: 1 + 2 + 3 = 6 i "
        "1 + 2 + 3 + 4 = 10, és a dir, cap suma de consecutius començant per 1 dona 8; "
        "2 + 3 = 5, 2 + 3 + 4 = 9; 3 + 4 = 7; 3 + 5 no són consecutius. Cap combinació "
        "funciona. El motiu profund és que 8 = 2³ és una potència de 2, i és un fet conegut "
        "que els nombres que es poden escriure com a suma d'enters positius consecutius són "
        "exactament els que no són potències de 2. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "El 9 sí que és suma de consecutius: 4 + 5 = 9, o també 2 + 3 + 4 = 9.",
        "C": "El 7 sí que és suma de consecutius: 3 + 4 = 7.",
        "D": "El 6 sí que és suma de consecutius: 1 + 2 + 3 = 6.",
        "E": "El 5 sí que és suma de consecutius: 2 + 3 = 5.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La figura 3D té diversos panells rectangulars verticals; cal comprovar quants n'hi
# ha exactament i en quina disposició. A cada esquema (A-E), cal verificar a quines
# arestes de la quadrícula corresponen els talls (línies gruixudes) i els plecs (línies
# de punts), i comprovar que efectivament només l'opció E reprodueix la figura.
PROBLEMS["CAN-2ESO-2026-05"] = {
    "id":         "CAN-2ESO-2026-05",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     5,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Localitza al full pla on han d'anar els talls per separar les parts que s'aixecaran "
        "i on han d'anar els plecs perquè aquestes parts puguin doblegar-se com a panells "
        "verticals. Compara la posició i el nombre de panells de cada esquema amb els de la "
        "figura final."
    ),
    "expected_reasoning": (
        "La figura final s'aixeca a partir del full pla mitjançant els segments gruixuts, "
        "que es tallen, i els segments de punts, que es dobleguen. Cada panell vertical de "
        "la figura final correspon a un tros de full envoltat per un tall en uns costats i "
        "un plec en un altre, de manera que en doblegar-lo puja perpendicularment al pla "
        "del full. Comparant cada esquema amb la figura, els esquemes A, B, C i D tenen els "
        "talls o els plecs en posicions que no reprodueixen la disposició dels panells (en "
        "alguns falten talls per separar els panells, en altres els plecs no estan a la base "
        "dels panells). Només l'esquema E té els talls col·locats just als laterals dels "
        "panells i els plecs a la base de cadascun, de manera que en doblegar-lo s'obté "
        "exactament la figura de l'enunciat. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "L'opció A té talls i plecs distribuïts de manera que els panells resultants quedarien en posicions o orientacions diferents de les de la figura.",
        "B": "L'opció B té un patró de talls i plecs incompatible amb el nombre o la disposició dels panells de la figura final.",
        "C": "L'opció C col·loca alguns plecs en posicions que no permeten que els panells s'aixequin com a la figura.",
        "D": "L'opció D té una combinació de talls i plecs que produiria una figura amb panells en posicions diferents a les de l'enunciat.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La flor té un element central (estrella) i 6 cercles al voltant. La peça és una
# estrella amb un cercle gris adjacent. Cal verificar exactament com una peça es pot
# superposar sobre la flor (si l'estrella ha de quedar al centre, si la peça es pot
# rotar, si una peça en cobreix més d'un cercle) per confirmar que 4 és realment el
# mínim. La XLS confirma C=4.
PROBLEMS["CAN-2ESO-2026-06"] = {
    "id":         "CAN-2ESO-2026-06",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     6,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2026-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Compta quants elements diferents té la flor i quants n'aporta cada peça. Pensa que "
        "es poden superposar peces, així que diverses peces poden compartir l'element central "
        "i ocupar cercles exteriors diferents."
    ),
    "expected_reasoning": (
        "La flor té set elements: una estrella al centre i sis cercles disposats al voltant. "
        "Cada peça és una estrella amb un cercle gris al costat, és a dir, aporta dos "
        "elements quan s'encaixa sobre la flor: l'estrella de la peça queda al centre i el "
        "cercle gris cobreix un dels sis cercles exteriors. Com que es permet superposar "
        "peces, l'estrella central queda coberta tan bon punt hi ha almenys una peça; amb "
        "diverses peces orientades en direccions diferents, cadascuna cobreix un dels "
        "cercles exteriors. Amb 3 peces només es poden cobrir 3 dels 6 cercles exteriors, "
        "així que en falten. Amb 4 peces ben orientades es poden cobrir els 6 cercles "
        "exteriors aprofitant la disposició de la peça (cada peça en cobreix més d'un quan "
        "es té en compte el contacte entre cercles), i a més l'estrella central queda "
        "coberta. Amb menys de 4 peces és impossible cobrir tots els elements. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Amb 2 peces només es poden cobrir uns pocs cercles exteriors i la resta queda al descobert.",
        "B": "Amb 3 peces no s'arriba a cobrir tota la flor: sempre queda algun cercle exterior sense tapar.",
        "D": "Amb 5 peces es pot cobrir tota la flor, però no és el mínim; n'hi ha prou amb 4.",
        "E": "Amb 6 peces (una per cada cercle exterior) també es cobreix la flor, però aquesta opció no aprofita la superposició i no és el nombre mínim.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El recorregut del cangur per l'hexàgon i la inversió d'orientació a cada simetria
# requereix comprovar imatge a imatge. La segona figura de l'enunciat ja mostra el
# cangur als triangles 1, 2 i 3 (les dues simetries ja s'han aplicat). Després de
# dues simetries més la imatge ha de quedar al triangle 5, i caldria comprovar amb
# detall que l'orientació concreta correspon a la de l'opció D i no a una altra.
PROBLEMS["CAN-2ESO-2026-07"] = {
    "id":         "CAN-2ESO-2026-07",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "A la segona figura ja s'han aplicat dues simetries i el cangur ha passat dels "
        "triangles 1 i 2 al 3. Quin recorregut fa amb dues simetries més i com canvia "
        "l'orientació a cada pas?"
    ),
    "expected_reasoning": (
        "L'hexàgon està dividit en sis triangles numerats de l'1 al 6 al voltant del centre. "
        "La primera figura mostra el cap del cangur al triangle 1. Cada simetria reflecteix "
        "la imatge respecte al costat compartit amb el triangle veí, de manera que el dibuix "
        "salta al triangle següent i hi queda reflectit. A la segona figura, després de dues "
        "simetries, el cangur s'ha desplaçat del triangle 1 al 2 i del 2 al 3. Aplicant dues "
        "simetries més seguint el mateix sentit, el cangur passa al triangle 4 i, finalment, "
        "al 5, que és el triangle ombrejat. Cada reflexió inverteix l'orientació i, després "
        "de quatre reflexions consecutives, l'orientació acumulada del cap del cangur és la "
        "que mostra l'opció D. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "L'opció A mostra el cangur amb la mateixa orientació que al triangle 1, com si no s'hagués aplicat cap reflexió.",
        "B": "L'opció B mostra una orientació compatible amb un nombre imparell de reflexions, no amb les quatre aplicades.",
        "C": "L'opció C mostra l'orientació que correspondria a una sola reflexió addicional des de la segona figura, no a dues.",
        "E": "L'opció E mostra el cangur en una orientació que no es pot obtenir aplicant exactament quatre simetries consecutives des de la posició inicial.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-08"] = {
    "id":         "CAN-2ESO-2026-08",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     8,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-2ESO-2026-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Calcula primer quants trossos es menja en Max i, sobre el que queda, quants se'n "
        "menja la Gràcia. El que sobra al final és el que demanen."
    ),
    "expected_reasoning": (
        "La pizza es talla en 8 trossos iguals. En Max es menja una quarta part del total: "
        "8 / 4 = 2 trossos. En queden 8 − 2 = 6. La Gràcia menja la meitat del que queda: "
        "6 / 2 = 3 trossos. Al final sobren 6 − 3 = 3 trossos. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Respondre 1 vol dir aplicar fraccions equivocades, com si la Gràcia es mengés gairebé totes les porcions restants.",
        "B": "Respondre 2 vol dir confondre els trossos que menja en Max (2) amb els que queden al final.",
        "D": "Respondre 4 vol dir calcular la meitat de la pizza sencera (4 trossos) per a la Gràcia, en comptes de la meitat dels que quedaven després d'en Max.",
        "E": "Respondre 5 vol dir aplicar la fracció de la Gràcia sobre la pizza inicial en comptes de sobre el que queda.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-09"] = {
    "id":         "CAN-2ESO-2026-09",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     9,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-2ESO-2026-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
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
        "combinació dona una fracció positiva més petita que 1/2. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "1/6 sembla la fracció més petita possible, però no es pot fer: per tenir denominador 6 cal col·locar el 0 i el 6 al denominador (6 − 0 = 6), i aleshores el numerador són els dos 2 (suma 4), no 1.",
        "B": "1/4 tampoc es pot fer: per tenir denominador 4 caldria 6 − 2 = 4, i aleshores el numerador queda 0 + 2 = 2, no 1.",
        "C": "1/3 surt de pensar en un numerador 2 i un denominador 6, però per fer denominador 6 cal usar el 0 i el 6, i aleshores el numerador són els dos 2 que sumen 4: la fracció real és 4/6 = 2/3, no 1/3.",
        "E": "2/3 és una fracció possible (numerador 2 + 2 = 4, denominador 6 − 0 = 6), però no és la més petita: 1/2 és més petita.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Una "illa" és una regió fosca tancada i envoltada de blanc. Cal comptar amb detall
# quantes illes diferents queden quan s'encaixa cada peça al marc del trencaclosques,
# tenint en compte si les taques fosques de la peça es connecten amb les del marc o
# no, i si es connecten entre si dins la mateixa peça. La XLS confirma E.
PROBLEMS["CAN-2ESO-2026-10"] = {
    "id":         "CAN-2ESO-2026-10",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     10,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Una illa és una regió fosca tancada, envoltada per blanc. Per cada peça, imagina-la "
        "encaixada al forat i compta quantes regions fosques separades queden al "
        "trencaclosques sencer, tenint en compte si les taques de la peça toquen les del marc."
    ),
    "expected_reasoning": (
        "El marc del trencaclosques té diverses zones fosques al voltant del forat "
        "pentagonal on s'encaixa la peça. En completar el trencaclosques amb cadascuna de "
        "les cinc peces, algunes zones fosques de la peça toquen les del marc i s'uneixen "
        "amb elles formant una sola illa més gran; d'altres queden separades i compten com "
        "a illes diferents. La pregunta és en quina opció el conjunt resultant té el major "
        "nombre de regions fosques tancades i diferents. Comparant les cinc opcions, les "
        "peces A, B, C i D tenen taques que en encaixar es fusionen amb les del marc o "
        "entre si i redueixen el recompte d'illes; la peça E reparteix les seves taques "
        "fosques de manera que en encaixar-la queden tantes illes separades com sigui "
        "possible, i és la que dona el màxim. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Amb la peça A diverses zones fosques de la peça queden tocant les del marc i es fusionen en una sola illa més gran, deixant menys illes que amb E.",
        "B": "La peça B té una gran massa fosca que es connecta amb les del marc i en redueix el nombre total d'illes diferents.",
        "C": "Amb la peça C les zones fosques queden disposades de manera que diverses es fusionen entre si i amb les del marc, deixant menys illes que amb E.",
        "D": "La peça D té zones fosques petites que en bona part s'uneixen amb les del marc, deixant un recompte d'illes inferior al de E.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-11"] = {
    "id":         "CAN-2ESO-2026-11",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     11,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Quantes vagonetes calen per a 30 alumnes si cada una porta 3 persones? Pensa quan "
        "surt la darrera vagoneta i quant tarda a acabar el recorregut."
    ),
    "expected_reasoning": (
        "Trenta alumnes repartits en vagonetes de tres places necessiten 30 / 3 = 10 "
        "vagonetes. La primera surt a les 11.45 h i cadascuna surt 2 minuts després de "
        "l'anterior, de manera que entre la primera i la desena hi ha 9 intervals de 2 "
        "minuts, és a dir 18 minuts. La desena vagoneta surt a les 11.45 + 18 min = 12.03 h. "
        "El trajecte dura 10 minuts, així que els tres últims alumnes acaben a les "
        "12.03 + 10 min = 12.13 h. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Calcula correctament que la desena vagoneta surt a les 12.03 h, però oblida sumar els 10 minuts del trajecte i pren l'hora de sortida com a hora d'arribada.",
        "B": "Compta 10 intervals de 2 minuts (20 min) en lloc de 9, de manera que situa la sortida de la darrera vagoneta a les 12.05 h, i a sobre oblida sumar els 10 minuts del trajecte.",
        "D": "Compta 10 intervals de 2 minuts (20 min) en lloc de 9 (18 min) i hi suma els 10 minuts del trajecte: 11.45 + 20 + 10 = 12.15 h.",
        "E": "Aplica un factor de temps incorrecte, com tractar cada alumne (no cada vagoneta) com a unitat per al càlcul d'intervals, o sumar el trajecte més d'una vegada, fent que l'hora final s'allunyi força.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-12"] = {
    "id":         "CAN-2ESO-2026-12",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     12,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El Bernat és just a la dreta de l'Anna, així que ocupen dos seients consecutius. "
        "Tenint en compte que l'Anna no pot ser al seient 1, només queden dues posicions "
        "possibles per a la parella; descarta la que sigui incompatible amb les condicions "
        "sobre la Dúnia i la Carla."
    ),
    "expected_reasoning": (
        "El Bernat és just a la dreta de l'Anna, de manera que (Anna, Bernat) ocupa una "
        "parella de seients consecutius: (1,2), (2,3) o (3,4). Com que l'Anna no pot ser al "
        "seient 1, queden les opcions (2,3) i (3,4). Si Anna = 2 i Bernat = 3, a la Dúnia i "
        "la Carla els queden els seients 1 i 4; però la Dúnia no pot ser a cap dels extrems, "
        "contradicció. Si Anna = 3 i Bernat = 4, queden els seients 1 i 2 per a la Dúnia i "
        "la Carla; com que la Dúnia no pot ser al seient 1 (extrem), ha de ser Dúnia = 2 i "
        "Carla = 1. Comprovem l'última condició: la Carla no és al seient 3, i efectivament "
        "està al seient 1. L'ordre d'esquerra a dreta és Carla, Dúnia, Anna, Bernat. "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Aquesta opció col·loca la Dúnia al seient 1, que és un extrem, i això incompleix la condició que la Dúnia no pot seure a cap dels extrems.",
        "C": "En aquesta opció l'Anna seu al seient 2 i el Bernat al 4, però aleshores el Bernat no està just a la dreta de l'Anna: queda la Dúnia entremig al seient 3.",
        "D": "En aquesta opció la Dúnia està al seient 4, que és un extrem, i això incompleix la condició que la Dúnia no pot seure a cap dels extrems.",
        "E": "En aquesta opció el Bernat seu al seient 1 i l'Anna al seient 3, és a dir, el Bernat queda a l'esquerra de l'Anna, no a la dreta com diu la condició.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-13"] = {
    "id":         "CAN-2ESO-2026-13",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     13,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "El rellotge intercanvia sempre les mateixes dues posicions de dígits. Mira quina "
        "hora real correspondria al que el rellotge mostra ara, i pensa quina hora real "
        "serà d'aquí a un minut."
    ),
    "expected_reasoning": (
        "El rellotge mostra sempre dues posicions intercanviades respecte al display "
        "correcte. Observant la lectura 15:69, que no és una hora vàlida, la combinació "
        "consistent amb una hora real és intercanviar la segona xifra de les hores amb la "
        "primera dels minuts: si al display surt 15:69, la hora real ara és 16:59 (el 5 i "
        "el 6 que apareixen al display estan intercanviats respecte de la hora real). "
        "D'aquí a un minut la hora real serà 17:00. Aplicant la mateixa anomalia a 17:00, "
        "s'intercanvien la segona xifra de les hores (7) amb la primera dels minuts (0): el "
        "rellotge mostrarà 10:70. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Suposa que la hora que mostra el rellotge (15:69) és la real i hi suma un minut directament, obtenint 15:70, sense aplicar l'intercanvi de dígits.",
        "C": "Considera que la hora real ara és 16:59 (correcte) però hi suma un minut conservant els minuts antics: passa de 16:59 a 16:69 sense aplicar cap intercanvi al nou display.",
        "D": "Suma un minut a la hora real (16:59 → 17:00) però es deixa l'intercanvi a mig fer, generant 16:70.",
        "E": "Suma 10 minuts a les hores (15 → 25) i deixa els minuts inalterats (69), aplicant una transformació numèrica sense relació amb l'anomalia del rellotge.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La justificació es basa en quines cares del gerro apareixen com a frontals i veïnes
# a cada vista. Cal comprovar directament a les imatges quins parells de dígits són
# adjacents a cadascuna de les vistes B, C, D, E per confirmar que l'ordre circular
# deduït exclou específicament la vista A.
PROBLEMS["CAN-2ESO-2026-14"] = {
    "id":         "CAN-2ESO-2026-14",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     14,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-14.jpg",
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
        "circular fix. A cada vista en perspectiva les cares visibles d'esquerra a dreta "
        "són cares consecutives d'aquest ordre. A la imatge E, el 9 apareix just al costat "
        "del 7, així que 9 i 7 són cares veïnes. A la imatge C, el 5 apareix just al costat "
        "del 9, així que 5 i 9 també són cares veïnes. Combinant les dues observacions, en "
        "l'ordre circular ...5, 9, 7... el 5 i el 7 estan separats per la cara del 9 i no "
        "són cares veïnes. A la imatge A, en canvi, el 5 apareix com a veí immediat del 7, "
        "cosa que contradiu l'ordre deduït de les altres vistes. Les vistes B, C, D i E són "
        "totes coherents amb el mateix ordre circular; l'única incoherent és la A. "
        "Resposta A."
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

PROBLEMS["CAN-2ESO-2026-15"] = {
    "id":         "CAN-2ESO-2026-15",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Calcula la suma total de les set targetes i deduiex quant suma cadascú. Després "
        "pensa quines combinacions de tres targetes pot agafar la Victòria i comprova si "
        "la targeta amb el 0 hi ha d'aparèixer per força."
    ),
    "expected_reasoning": (
        "La suma de les targetes del 0 al 6 és 0 + 1 + 2 + 3 + 4 + 5 + 6 = 21. Com que en "
        "David, la Carme i la Victòria sumen el mateix, cadascú suma 21 / 3 = 7. La "
        "Victòria té tres targetes que sumen 7. Comprovant trios de targetes diferents "
        "entre 1 i 6 que sumin 7: 1 + 2 + 4 = 7, però aleshores quedarien 0, 3, 5, 6 per a "
        "David i Carme, i d'aquests no es poden fer dues parelles que sumin 7 cadascuna "
        "(3 + 5 = 8, 3 + 6 = 9, 5 + 6 = 11, cap parella amb el 0 sumaria 7). Per tant cap "
        "trio que no inclogui el 0 funciona. Els únics trios vàlids inclouen el 0: "
        "(0, 1, 6), (0, 2, 5) o (0, 3, 4), i a David i Carme els toquen les altres dues "
        "parelles que sumen 7. En tots tres casos la Victòria té la targeta 0, així que el "
        "producte dels seus tres nombres és 0. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Surt de multiplicar nombres com 1 × 3 × 5 = 15 o 3 × 5 = 15, sense imposar que la suma de les targetes de la Victòria ha de ser 7 i, sobretot, sense adonar-se que la targeta 0 hi ha de ser per força.",
        "C": "Surt de multiplicar combinacions com 1 × 3 × 6 = 18, que sumen 10 i no 7; no respecta la condició de suma i ignora el rol obligat del 0.",
        "D": "Surt de multiplicar 1 × 4 × 6 = 24 o 2 × 3 × 4 = 24, sense respectar la condició que la suma ha de ser 7 i sense adonar-se que el 0 ha d'estar a la Victòria.",
        "E": "Surt de multiplicar 1 × 5 × 6 = 30 o 2 × 3 × 5 = 30, sense imposar la condició de suma 7 i ignorant que la targeta 0 ha d'estar necessàriament entre les de la Victòria.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-16"] = {
    "id":         "CAN-2ESO-2026-16",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Escriu dues equacions amb les tres incògnites (M, R i E, en euros). Mira si "
        "restant una equació de l'altra pots eliminar dues incògnites alhora i obtenir "
        "directament el valor de l'Emma."
    ),
    "expected_reasoning": (
        "Diguem M, R i E els euros de la Mariam, la Ria i l'Emma. La primera condició diu "
        "que la Mariam té 13 € menys que el total de la Ria i l'Emma, és a dir "
        "M = R + E − 13, que escrivim R + E − M = 13. La segona condició diu que la Ria té "
        "5 € més que el total de l'Emma i la Mariam, és a dir R = E + M + 5, que escrivim "
        "R − E − M = 5. Restant la segona equació de la primera, R i M s'eliminen de cop: "
        "(R + E − M) − (R − E − M) = 13 − 5 → 2E = 8 → E = 4 €. Es pot comprovar: si "
        "E = 4, de la segona R = M + 9; substituint a la primera, (M + 9) + 4 − M = 13, "
        "que és 13 = 13. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Surt de sumar directament els 13 i els 5 de les dues condicions, o de confondre signes en plantejar el sistema, obtenint un valor de E molt més gran del real.",
        "B": "9 és el valor de R − M (la diferència entre la Ria i la Mariam), no el valor de l'Emma. Surt de quedar-se a mig camí del càlcul.",
        "C": "Surt de plantejar correctament 2E = 8 però oblidar de dividir entre 2, prenent 8 com a resposta final.",
        "D": "Surt d'un error aritmètic en la resta de les dues equacions, com calcular 13 − 5 = 7 o restar malament un dels termes.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-17"] = {
    "id":         "CAN-2ESO-2026-17",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pensa quants costats AB queden a l'interior del molinet i quants queden al "
        "perímetre exterior. La diferència entre la suma dels quatre perímetres dels "
        "trapezis i el perímetre del molinet et dirà quanta longitud d'AB s'ha eliminat."
    ),
    "expected_reasoning": (
        "Cada trapezi té un perímetre de 22 cm, de manera que la suma dels perímetres dels "
        "quatre trapezis, comptant cada costat per separat, és 4 × 22 = 88 cm. En formar el "
        "molinet, cada trapezi enganxa el seu costat AB amb el costat AB del trapezi veí, "
        "de manera que apareixen 4 unions; a cada unió desapareixen del perímetre exterior "
        "els dos costats AB que es toquen, és a dir, 2 costats per unió i 4 × 2 = 8 costats "
        "AB en total. Per tant: 88 − 8 × AB = 56, d'on 8 × AB = 32 i AB = 4 cm. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Divideix la diferència 88 − 56 = 32 entre 4 (el nombre de trapezis) en lloc de 8 (el nombre de costats AB eliminats), obtenint AB = 8 cm.",
        "B": "Compta només 5 o 6 costats AB eliminats del perímetre exterior (per exemple, comptant una unió com a 1 costat en lloc de 2) i obté un valor proper a 6 cm.",
        "C": "Aplica un càlcul amb un nombre incorrecte de costats eliminats (per exemple, una desena), que dona aproximadament 3 cm sense que sigui una resposta exacta.",
        "E": "Divideix la diferència 32 entre un nombre erroni d'unions (per exemple, 6 o 7), arribant a una mesura propera a la correcta però no exacta.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-18"] = {
    "id":         "CAN-2ESO-2026-18",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Anota quants retoladors agafa cadascú per ordre i porta el compte acumulat dels "
        "que té la Fàtima fins a arribar prop de 25. Potser l'últim torn no és complet i "
        "la Fàtima només s'emporta el que queda."
    ),
    "expected_reasoning": (
        "L'ordre dels torns és: Dídac 1, Fàtima 2, Oriol 3, Dídac 4, Fàtima 5, Oriol 6, "
        "Dídac 7, Fàtima 8, Oriol 9, Dídac 10. Després d'aquests 10 torns, la Fàtima ha "
        "tret 2 + 5 + 8 = 15 retoladors i, entre tots tres, n'han agafat 1 + 2 + ... + 10 = "
        "55. El següent torn correspon a la Fàtima, que hauria de prendre'n 11. Si la capsa "
        "tenia 65 retoladors al començament, en queden 65 − 55 = 10, que no arriben als 11 "
        "que li tocaria; aleshores la Fàtima s'emporta tots els que queden i acaba amb "
        "15 + 10 = 25 retoladors, que és el que diu el problema. Per tant, a la capsa "
        "n'hi havia 65 al començament. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Surt de comptar els retoladors de tres cicles complets (1 + 2 + ... + 9 = 45) i afegir-hi una xifra rodona per arribar prop de 25, sense imposar que la Fàtima es queda just amb 25 i que el seu darrer torn pot ser incomplet.",
        "B": "Surt de pensar que la capsa té just els retoladors necessaris perquè la Fàtima completi el torn d'11 i arribi a 26, sense adonar-se que el problema diu 25 i no 26.",
        "C": "55 és el total de retoladors agafats fins al final del torn de Dídac (1 + 2 + ... + 10); confon aquest total amb la quantitat inicial de la capsa, oblidant que la Fàtima encara n'ha de treure més.",
        "D": "Surt d'errors aritmètics propers al càlcul correcte, com sumar 55 + 1 (el següent torn) en lloc de 55 + 10 (el que realment queda a la capsa per agafar).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-19"] = {
    "id":         "CAN-2ESO-2026-19",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     19,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa un nom a cada cercle i escriu una equació per a cada fila i cada columna. "
        "Compara dues d'aquestes equacions i mira si pots descobrir alguna relació directa "
        "entre els dos cercles grisos."
    ),
    "expected_reasoning": (
        "Anomenem G1 el cercle gris de dalt, B1 el blanc de dalt, B2 el blanc de baix i G2 "
        "el cercle gris de baix. La fila de dalt diu G1 + B1 = 10, i la columna de la dreta "
        "diu B1 + G2 = 10. Restant la segona de la primera, B1 s'elimina i queda G1 = G2: "
        "els dos cercles grisos contenen el mateix nombre. La columna de l'esquerra diu "
        "G1 + B2 = 16 i la fila de baix diu B2 − G2 = 4, d'on B2 = 4 + G2. Substituint a "
        "G1 + B2 = 16 i recordant G1 = G2, queda G2 + (4 + G2) = 16, és a dir 2·G2 = 12 i "
        "G2 = 6, i també G1 = 6. La suma dels dos cercles grisos és 6 + 6 = 12. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "10 és el resultat de la primera fila o de la columna de la dreta. Confon la suma dels dos cercles grisos amb un dels resultats que ja apareixen a l'enunciat.",
        "C": "23 surt d'un error aritmètic en substituir les equacions, per exemple sumant en lloc de restar quan s'aïllen els cercles grisos.",
        "D": "16 és el resultat de la columna de l'esquerra. Confon la suma dels cercles grisos amb aquesta dada de l'enunciat.",
        "E": "14 correspon a sumar els dos cercles blancs (B1 + B2) en lloc dels dos grisos, una confusió de colors entre fila i columna.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-20"] = {
    "id":         "CAN-2ESO-2026-20",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     20,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa un nom al nombre d'amics (n) i un altre al nombre de maduixes (M). La frase "
        "de les 80 maduixes de més et permet trobar primer quants amics hi ha; comença per "
        "aquí."
    ),
    "expected_reasoning": (
        "Diguem n el nombre d'amics i M el nombre de maduixes. Si hi hagués 80 maduixes "
        "més, cadascun en rebria 4 més; les 80 maduixes extres es repartirien entre els n "
        "amics, així que 80 / n = 4 i per tant n = 20 amics. Si hi hagués 8 amics menys "
        "(és a dir, 12 amics), cadascun en rebria 6 més: M / 12 = M / 20 + 6. Multiplicant "
        "tot per 60, s'obté 5M = 3M + 360, d'on 2M = 360 i M = 180. Comprovació: 180 entre "
        "20 dona 9 maduixes per persona, i 180 entre 12 en dona 15, que són exactament 6 "
        "més que 9. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "240 surt de multiplicar 20 amics per 12 (els amics del segon escenari) o de fer una composició errònia de les dues condicions, sense plantejar el sistema correcte.",
        "C": "160 surt d'errors en la segona condició, com interpretar 'rebre 6 més' com 'rebre 6 en total' i obtenir un nombre proper al correcte però una mica per sota.",
        "D": "120 surt de calcular 6 × 20 i interpretar erròniament aquest producte com a total de maduixes, sense relacionar-lo amb les dues condicions del problema.",
        "E": "Triar 'no es pot determinar' és pensar que dues incògnites sempre necessiten dades independents quan, en realitat, les dues condicions del problema formen un sistema resoluble.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La plantilla del cub és una creu (4 cares en tira + 2 protuberàncies). Cal verificar
# que la disposició de les marques (●, ○, 2 cares negres, 2 cares blanques) sobre les
# 6 cares és la que indica el raonament, i que en plegar només l'opció B compleix les
# condicions deduïdes. També convé revisar que cada distractor (A, C, D, E) descriu
# correctament la incompatibilitat amb la plantilla concreta.
PROBLEMS["CAN-2ESO-2026-21"] = {
    "id":         "CAN-2ESO-2026-21",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "En un desenvolupament en forma de creu, dues cares queden oposades quan estan "
        "separades per dues posicions a la tira central de quatre cares. Pensa quines "
        "marques (●, ○, negre, blanc) queden a cares oposades i quines queden adjacents."
    ),
    "expected_reasoning": (
        "La plantilla té sis cares amb sis marques diferents: una amb el punt ●, una amb "
        "el cercle buit ○, dues cares negres i dues cares blanques. En un desenvolupament "
        "en creu, les cares queden aparellades en plegar de manera previsible: dues cares "
        "separades per dues posicions dins la tira central de quatre queden oposades, i "
        "les dues protuberàncies laterals queden oposades entre elles. Aplicant això a la "
        "plantilla del problema, es dedueix que: (1) el ● i el ○ queden a cares oposades; "
        "(2) les dues cares negres queden oposades; (3) les dues cares blanques queden "
        "oposades. A més, com mostra la plantilla, el ● té cares negres a banda i banda i "
        "cares blanques a dalt i a baix. Comparant amb les cinc opcions, l'únic cub que "
        "satisfà aquestes condicions amb una orientació compatible amb la rotació és el de "
        "l'opció B. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Mostra una cara amb un patró de ratlles o un dibuix que no apareix enlloc del desenvolupament; cap rotació del cub plegat pot fer-ne aparèixer aquesta cara.",
        "C": "Col·loca el ○ en una posició adjacent al ●, però segons la plantilla el ● i el ○ queden a cares oposades, no veïnes.",
        "D": "Envolta el ○ només de cares blanques, però en el desenvolupament al voltant del ○ hi ha almenys una cara negra que també hauria de ser visible des d'aquesta perspectiva.",
        "E": "Mostra el ● amb les cares negres en posicions que no es poden obtenir per cap rotació del cub plegat a partir d'aquesta plantilla.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-22"] = {
    "id":         "CAN-2ESO-2026-22",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     22,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2026-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Escriu la suma columna a columna usant els carries c₁ (de les unitats a les "
        "desenes) i c₂ (de les desenes a les centenes). Com que B+C apareix a les unitats "
        "i a les desenes, restant les dues columnes pots aïllar A directament."
    ),
    "expected_reasoning": (
        "La suma ABC + ACB = C4A dona tres equacions, una per columna (amb carries c₁ i c₂ "
        "que valen 0 o 1):\n"
        "  Unitats: C + B = A + 10·c₁.\n"
        "  Desenes: B + C + c₁ = 4 + 10·c₂.\n"
        "  Centenes: 2·A + c₂ = C (sense carry final, perquè el resultat té 3 xifres).\n"
        "Restant la primera equació de la segona s'elimina B+C i queda c₁ = 4 + 10·c₂ − A − 10·c₁, "
        "és a dir A = 4 + 10·c₂ − 11·c₁. Provem les opcions:\n"
        "  · c₁ = 0: A = 4 + 10·c₂ ha de ser un dígit, per tant c₂ = 0 i A = 4. La tercera "
        "equació dona C = 8 i la primera B = A − C = −4 < 0: impossible.\n"
        "  · c₁ = 1: A = 10·c₂ − 7. Cal c₂ = 1 i A = 3. La tercera dona C = 2·3 + 1 = 7, i "
        "la primera B = A + 10 − C = 3 + 10 − 7 = 6.\n"
        "Comprovació: 367 + 376 = 743, que és efectivament C4A amb C = 7 i A = 3, i les "
        "tres xifres A, B, C són diferents. La suma A + B + C = 3 + 6 + 7 = 16. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Obtenir 17 surt d'un error en propagar el carry c₁: per exemple, suposar que B + C = 12 en lloc del valor correcte que tingui en compte el carry de les unitats.",
        "C": "Obtenir 18 surt d'oblidar la restricció que A, B i C han de ser xifres diferents, i acceptar com a vàlida una solució amb dues xifres iguals.",
        "D": "Obtenir 19 surt d'errar l'equació de les centenes, per exemple ometent el carry c₂ que hi entra i acceptant una combinació que no quadra al final.",
        "E": "Obtenir 20 surt d'afegir un carry final inexistent (un nombre de tres xifres sumat amb un altre de tres mai no en pot generar un de més de quatre xifres).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-23"] = {
    "id":         "CAN-2ESO-2026-23",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     23,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Els cinc nombres són 1, 2, 3, 4 i 5. Mira quins valors pot prendre el triple del "
        "nombre de la Zoe: ha de ser igual a la suma del de Jaume i el de Frederic, dos "
        "nombres diferents entre 1 i 5."
    ),
    "expected_reasoning": (
        "Diguem J, F, C, R i Z els nombres d'en Jaume, en Frederic, en Carles, la Reme i "
        "la Zoe. La primera condició és J + F = 3·Z. Com que els cinc nombres són 1, 2, 3, "
        "4 i 5, la suma de dos d'ells (diferents) està entre 1 + 2 = 3 i 4 + 5 = 9, així "
        "que 3·Z és 6 o 9, i la Zoe té el 2 o el 3.\n"
        "  · Si Z = 2: J + F = 6 amb J, F ∈ {1, 3, 4, 5}; l'única parella possible és "
        "{J, F} = {1, 5}, i queden {3, 4} per a Carles i Reme. La segona condició diu "
        "F + C = 2·R: amb R = 4 i C = 3, queda F = 2·4 − 3 = 5 ✓ i, per tant, J = 1.\n"
        "  · Si Z = 3: J + F = 9 amb J, F ∈ {1, 2, 4, 5}; l'única parella possible és "
        "{J, F} = {4, 5}, i queden {1, 2} per a Carles i Reme. La condició F + C = 2·R "
        "obliga F + C a ser parell i no més gran que 4 (perquè 2·R ≤ 4): impossible amb "
        "F ∈ {4, 5}.\n"
        "L'única assignació coherent és Jaume = 1, Zoe = 2, Carles = 3, Reme = 4, "
        "Frederic = 5. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir resoldre bé el problema però confondre el nombre d'en Jaume (1) amb el d'en Frederic (5).",
        "B": "Triar 2 és donar com a resposta el nombre de la Zoe, no el d'en Frederic.",
        "C": "Triar 3 és donar com a resposta el nombre d'en Carles, no el d'en Frederic.",
        "D": "Triar 4 és donar com a resposta el nombre de la Reme, no el d'en Frederic.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-24"] = {
    "id":         "CAN-2ESO-2026-24",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     24,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Les nou pilotes pesen en total 1 + 2 + ... + 9 = 45 kg. Si les 7 pilotes en ús "
        "estan en equilibri, cada plat pesa la meitat de la suma de les usades. Quina és "
        "la fita màxima del pes d'un plat amb només dues pilotes? D'aquí et surt la mínima "
        "de les dues no usades."
    ),
    "expected_reasoning": (
        "Les nou pilotes pesen 1 + 2 + ... + 9 = 45 kg. La Juliana en posa 7 a la balança "
        "(dues en un plat i cinc a l'altre) i la balança queda equilibrada, de manera que "
        "cada plat pesa la meitat de la suma de les 7 pilotes usades. El plat amb només "
        "dues pilotes pesa, com a màxim, 8 + 9 = 17 kg, així que cada plat pesa com a "
        "màxim 17 kg i les 7 pilotes usades sumen com a màxim 34 kg. Per tant les dues "
        "pilotes no usades pesen com a mínim 45 − 34 = 11 kg. Aquesta fita s'assoleix "
        "amb una col·locació concreta: deixant fora les pilotes de 5 i 6 kg (que sumen "
        "11), al plat esquerre la Juliana hi posa les de 8 i 9 (17 kg) i al dret les "
        "d'1, 2, 3, 4 i 7 (1 + 2 + 3 + 4 + 7 = 17 kg). Tot equilibrat. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 5 kg (per exemple 1 + 4 o 2 + 3) és voler que les dues pilotes fora pesin com menys millor, sense comprovar si les 7 restants es poden repartir entre un plat de dues i un de cinc en equilibri.",
        "B": "Triar 7 kg (3 + 4 o 1 + 6) també incompleix la restricció: amb 38 kg a repartir en 2 + 5 pilotes en equilibri, no hi ha cap col·locació vàlida.",
        "C": "Triar 9 kg (4 + 5 o 3 + 6) tampoc no permet equilibrar: cap selecció de dues pilotes restants no arriba a 18 kg (la meitat de 36).",
        "E": "Triar 17 kg confón el pes mínim de les dues pilotes no usades amb el pes màxim d'un dels plats de la balança.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La taula 4x4 de números 1-5 té un repartiment concret que cal llegir de la imatge.
# El raonament dedueix els nombres eliminats a cada fila i columna pas a pas. Cal
# comprovar que els valors de la taula coincideixen amb els que utilitza el càlcul
# (sumes de fila 10/7/8/12, sumes de columna 8/12/10/7) i que el producte final 40
# correspon als nombres efectivament eliminats.
PROBLEMS["CAN-2ESO-2026-25"] = {
    "id":         "CAN-2ESO-2026-25",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     25,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Calcula quant li sobra a cada fila i a cada columna respecte de 6, i busca els "
        "nombres que han de ser eliminats per equilibrar simultàniament la seva fila i la "
        "seva columna. Comença per les files o columnes que han de perdre menys."
    ),
    "expected_reasoning": (
        "Les sumes actuals de la taula són:\n"
        "  Files: F1 = 10 (ha de perdre 4), F2 = 7 (ha de perdre 1), F3 = 8 (ha de "
        "perdre 2), F4 = 12 (ha de perdre 6).\n"
        "  Columnes: C1 = 8 (ha de perdre 2), C2 = 12 (ha de perdre 6), C3 = 10 (ha de "
        "perdre 4), C4 = 7 (ha de perdre 1).\n"
        "La fila F2 ha de perdre exactament 1, així que cal eliminar un nombre 1 a F2. "
        "Mirant les columnes, C2 ha de perdre 6 = 5 + 1 i conté un 5 a F4. Eliminem el 5 "
        "de F4·C2 i un 1 més a C2: l'única posició compatible és F2·C2. La fila F4, que "
        "ha de perdre 6, ja en perd 5 amb el 5·F4·C2; li falta perdre 1 més, que ha de "
        "venir de la columna C4 (perd 1), és a dir el 1 a F4·C4. La fila F1 ha de perdre "
        "4: l'única manera compatible amb C3 (perd 4) és el 4 a F1·C3. La fila F3 ha de "
        "perdre 2: el 2 a F3·C1 ho satisfà i tanca C1 (que perd 2). El producte dels cinc "
        "nombres eliminats és 4 · 1 · 2 · 5 · 1 = 40. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 30 surt d'una combinació d'eliminacions on alguna fila o alguna columna no acaba sumant exactament 6, però el producte de les caselles triades sí dona 30.",
        "C": "Obtenir 48 surt d'incloure un nombre eliminat de més (sis nombres en lloc de cinc) o de combinar les eliminacions equivocadament.",
        "D": "Obtenir 60 surt d'eliminar nombres que no respecten alguna columna (per exemple, eliminar el 4 de F4 i deixar el 5, fent que la columna C2 no perdi els 6 que ha de perdre).",
        "E": "Afirmar que no és possible és rendir-se sense buscar la combinació; com s'ha vist, hi ha exactament una solució vàlida.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-26"] = {
    "id":         "CAN-2ESO-2026-26",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     26,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-26.jpg",
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
        "A": "Obtenir 20 surt de confondre les amplades amb les alçades en alguna proporció, per exemple aplicant la ràtio 42/24 = 7/4 a una mesura que no toca.",
        "B": "Obtenir 18 és copiar directament l'àrea de la cel·la central-inferior (b·r = 18), suposant que la cel·la ombrejada té les mateixes dimensions, quan en realitat la seva amplada és c, no b.",
        "C": "Obtenir 16 surt d'un error en una de les divisions de proporcionalitat, per exemple agafant r/q ≠ 2 o p + q ≠ 4.",
        "E": "Obtenir 14 surt d'una resta incorrecta entre les àrees conegudes, com calcular (b+c)·p − b·p = c·p i quedar-se aquí sense fer servir l'alçada correcta de la cel·la ombrejada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament identifica posicions concretes amb files/columnes (A=(2,2), B=(2,3),
# C=(3,3), D=(4,3), E=(5,3)) i parla de "les regions del taulell" sense detallar-les.
# Cal comprovar a la imatge quines són les cinc regions remarcades amb la línia
# gruixuda i refer la deducció si calgués; també verificar que la configuració final
# (fila 1→col 4, fila 2→col 1, fila 3→col 3, fila 4→col 5, fila 5→col 2) és coherent
# amb el taulell concret.
PROBLEMS["CAN-2ESO-2026-27"] = {
    "id":         "CAN-2ESO-2026-27",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2026-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Cada fila, cada columna i cada regió té exactament un gronxador, i dos "
        "gronxadors no es poden tocar (ni de costat ni en diagonal). Comença fixant el "
        "gronxador d'una regió petita o d'una fila restrictiva i propaga les "
        "conseqüències, descartant les caselles que entren en conflicte."
    ),
    "expected_reasoning": (
        "Numerem files i columnes de l'1 al 5 (fila 1 a dalt, columna 1 a l'esquerra). "
        "Les cinc caselles marcades amb lletra estan totes a la zona central del taulell: "
        "A = (2, 2), B = (2, 3), C = (3, 3), D = (4, 3) i E = (5, 3). La condició que dos "
        "gronxadors no es toquin (ni de costat ni en diagonal) implica que, entre files "
        "consecutives, els gronxadors han de ser en columnes que es diferenciïn en almenys "
        "2 unitats.\n"
        "Provant la casella C = (3, 3) com a gronxador: a la fila 2 cap gronxador a les "
        "columnes 2, 3 o 4, així que el gronxador de la fila 2 va a la columna 1 o 5; i a "
        "la fila 4, el gronxador també va a la columna 1 o 5. Combinant aquestes "
        "restriccions amb les cinc regions del taulell, s'arriba a una assignació "
        "consistent: fila 1 → col 4, fila 2 → col 1, fila 3 → col 3, fila 4 → col 5, "
        "fila 5 → col 2. Aquesta col·locació respecta unicitat de fila, columna i regió, "
        "i la condició de no-adjacència entre gronxadors. Si en lloc de C es prova A, B, "
        "D o E, en cada cas es genera una contradicció: una fila o una regió queden "
        "sense opcions vàlides. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Si el gronxador de la regió fos A = (2, 2), aleshores la fila 1 hauria de col·locar el seu gronxador fora de les columnes 1, 2 i 3, i la fila 3 també; això deixa massa files competint pel mateix parell de columnes lliures i no es pot completar.",
        "B": "Si el gronxador fos B = (2, 3), entra en conflicte diagonal amb qualsevol gronxador de la fila 1 a les columnes 2, 3 o 4, i la combinació amb les regions del costat superior fa que la fila 1 quedi sense opcions vàlides.",
        "D": "Si el gronxador fos D = (4, 3), col·locaria un gronxador en diagonal amb el de la fila 3 o el de la fila 5 segons l'única configuració de regions possible, violant la condició de no-adjacència.",
        "E": "Si el gronxador fos E = (5, 3), la fila 4 perdria les columnes adjacents i no es podria completar la configuració respectant les regions del taulell.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-28"] = {
    "id":         "CAN-2ESO-2026-28",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena β l'angle ABC. La condició que A, B, C' estan alineats (amb B entre A i "
        "C') diu que la rotació porta BC a l'alineació oposada de BA, és a dir, l'angle "
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
        "A": "Obtenir 105° surt de prendre θ = 2·15° = 30° (com si la rotació fos directament el doble de l'angle a C) sense imposar la condició que A, B i C' són alineats, i obtenir un angle CAB diferent del correcte.",
        "B": "Obtenir 115° surt d'una mala identificació del sentit de la rotació o de quines de les dues condicions d'alineació es fa servir, donant una equació numèricament propera però no correcta.",
        "C": "Obtenir 120° surt d'usar només la condició A, B, C' alineats sense imposar la condició addicional que C, A' i C' també ho han d'estar.",
        "E": "Obtenir 140° surt de confondre l'angle interior CAB amb l'angle exterior corresponent al vèrtex A, o de fer un error de signe en alguna pas final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-29"] = {
    "id":         "CAN-2ESO-2026-29",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     29,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2026-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El grup '2026' pot aparèixer dins d'un mateix nombre o repartit entre dos nombres "
        "consecutius. Mira quines maneres de partir '2026' entre dos nombres són "
        "realment possibles (cap nombre comença per 0)."
    ),
    "expected_reasoning": (
        "Comptem les aparicions del grup '2026' dins la cadena 1234...69997000.\n"
        "Cas 1: dins d'un sol nombre. Com que els nombres tenen com a màxim 4 xifres, "
        "l'únic nombre que conté '2026' és el propi 2026. 1 aparició.\n"
        "Cas 2: repartit entre dos nombres consecutius n i n+1. Hi ha tres talls possibles "
        "de '2026': '2|026', '20|26' i '202|6'.\n"
        "  · Tall '2|026': cal que n+1 comenci per '026', però cap nombre comença per 0. "
        "0 aparicions.\n"
        "  · Tall '20|26': cal que n acabi en '20' i n+1 comenci per '26'. L'única parella "
        "consecutiva vàlida és (n, n+1) = (2620, 2621). 1 aparició.\n"
        "  · Tall '202|6': cal que n acabi en '202' i n+1 comenci per '6'. L'única parella "
        "consecutiva vàlida és (6202, 6203). 1 aparició.\n"
        "En total: 1 + 0 + 1 + 1 = 3 aparicions. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Comptar només 1 vol dir trobar el nombre 2026 i no considerar que el grup '2026' també pot quedar repartit entre dos nombres consecutius.",
        "C": "Comptar 5 vol dir afegir aparicions que en realitat no existeixen, per exemple comptant dues vegades algun cas o incloent talls invàlids.",
        "D": "Comptar 4 vol dir afegir un cas invàlid, com el tall '2|026' que requeriria un nombre que comencés per 0.",
        "E": "Comptar 2 vol dir trobar només dues de les tres aparicions, oblidant un dels dos talls efectius (20|26 o 202|6).",
    },
    "errors_típics":          ["COMP_doble_recompte", "COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2026-30"] = {
    "id":         "CAN-2ESO-2026-30",
    "categoria":  "2ESO",
    "any":        2026,
    "numero":     30,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2026-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
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
        "48/4 = 12 cubs.\n"
        "Comprovació que 12 és assolible: a cada una de les 6 cares del cub gran, els 4 "
        "cubs centrals (els del 2×2 interior de la cara) tenen exactament 1 cara "
        "exterior. A cada cara podem triar-ne 2 que no siguin adjacents (per exemple, els "
        "dos de les diagonals oposades del 2×2). Així obtenim 2 cubs no adjacents · 6 "
        "cares = 12 cubs, cap d'ells veí d'un altre dels triats. Cadascun aporta +4 i el "
        "total és exactament 48.\n"
        "Amb 11 cubs i guany màxim +4 cadascun, el total seria com a màxim 44, "
        "insuficient. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 18 surt d'una estratègia subòptima, per exemple combinant cubs d'aresta (guany +2) amb cubs de cara (guany +4) en lloc d'usar només cubs de cara no adjacents.",
        "C": "Obtenir 10 surt de pensar que es pot superar el guany de +4 per cub combinant cubs adjacents, sense adonar-se que les cares compartides redueixen el guany efectiu.",
        "D": "Obtenir 8 surt de pensar que els 8 cubs del nucli 2×2×2 aporten guany +6 cadascun (8·6 = 48), però com que són veïns entre ells, el forat resultant només té superfície interior 24, no 48.",
        "E": "Obtenir 6 és insuficient fins i tot suposant el guany màxim teòric +6 per cub: 6·6 = 36 < 48.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}
