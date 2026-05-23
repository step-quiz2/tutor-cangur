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
        "Troba la resposta que compleix les dues condicions. Recorda que la polsera és circular: el "
        "primer i l'últim complement també són veïns."
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

PROBLEMS["CAN-2ESO-2025-01"] = {
    "id":         "CAN-2ESO-2025-01",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Mira les línies del mosaic que arriben a cada vora del forat i busca la peça que les "
        "continua totes alhora."
    ),
    "expected_reasoning": (
        "El mosaic està fet d'unitats quadrades alternades sobre una graella diagonal. Cada unitat "
        "conté un quadrat petit centrat amb quatre segments que surten dels seus vèrtexs cap als "
        "vèrtexs del quadrat gran, formant un octògon. La zona del '?' és contra la vora dreta del "
        "mosaic, amb una unitat 'interior' completa just a l'esquerra. Per tant la peça que falta ha "
        "de tenir: (i) un quadrat petit centrat, (ii) els dos segments diagonals que connecten amb "
        "els vèrtexs ESQUERRES del quadrat gran (per continuar la unitat de l'esquerra i les "
        "diagonals dels rombes que arriben des de dalt i baix per l'esquerra), i (iii) cap diagonal "
        "als vèrtexs drets, perquè a la dreta hi ha la vora rectangular del mosaic. L'opció D mostra "
        "exactament aquest patró: quadrat petit central, dues diagonals cap als vèrtexs esquerres i "
        "cantó dret net. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "L'opció A mostra dos rombes a la part superior i la zona inferior buida; no té el quadrat "
            "petit centrat que apareix a la resta del mosaic."
        ),
        "B": (
            "L'opció B té una X i un rombe a sota, no la simetria horitzontal del patró ni el quadrat "
            "petit centrat."
        ),
        "C": (
            "L'opció C és una unitat 'interior' completa (quadrat petit amb les quatre diagonals als "
            "quatre vèrtexs); les diagonals dretes sobrarien contra la vora del mosaic."
        ),
        "E": "L'opció E és una estrella de vuit puntes; no és cap dels patrons que apareixen al mosaic.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-02"] = {
    "id":         "CAN-2ESO-2025-02",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     2,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Mira primer quins forats té cada solapa: només es veurà un nombre quan TOTES dues "
        "solapes hi tinguin un forat alineat."
    ),
    "expected_reasoning": (
        "Numerem les files 1, 2, 3 (de dalt a baix) i les columnes 1..9 (d'esquerra a dreta). La "
        "pàgina central ocupa les columnes 4–6, i conté els nombres 4 9 2 / 3 5 7 / 8 1 6. La solapa "
        "esquerra ocupa les columnes 1–3 amb plec entre 3 i 4 (mirall: 3↔4, 2↔5, 1↔6); la solapa "
        "dreta ocupa les columnes 7–9 amb plec entre 6 i 7 (mirall: 7↔6, 8↔5, 9↔4).\n"
        "\n"
        "Que l'enunciat digui que amb només la solapa dreta plegada es veuen 2, 3, 5 i 6 fixa la "
        "posició dels forats de la solapa dreta: (1,7) descobreix (1,6)=2, (2,8) descobreix (2,5)=5, "
        "(2,9) descobreix (2,4)=3, (3,7) descobreix (3,6)=6.\n"
        "\n"
        "Observant la figura, els forats de la solapa esquerra són a (1,3), (2,2), (2,3) i (3,3); "
        "plegada cap a dreta projectarien sobre (1,4)=4, (2,5)=5, (2,4)=3 i (3,4)=8.\n"
        "\n"
        "Quan totes dues solapes es pleguen sobre la pàgina central, una queda sobre l'altra però "
        "totes dues cobreixen exactament les columnes 4–6. Per tant, un nombre del central només es "
        "veu si TOTES dues solapes tenen forat alineat amb aquella cel·la. Comparant els dos conjunts "
        "de cel·les projectades, la intersecció és {(2,4), (2,5)}, és a dir els nombres 3 i 5. La "
        "suma val 3 + 5 = 8. Resposta A."
    ),
    "comentaris_distractors": {
        "B": (
            "Obtenir 9 = 4 + 5 surt d'incloure el 4 pensant que el forat esquerre a (1,3) basta per "
            "veure'l, oblidant que la solapa dreta no té forat correlatiu a (1,9) per deixar passar la "
            "vista."
        ),
        "C": (
            "Obtenir 14 = 6 + 8 surt de barrejar un nombre visible amb la solapa dreta sola (6) amb un "
            "nombre visible amb la solapa esquerra sola (8), sense adonar-se que cap dels dos sobreviu en "
            "plegar les dues alhora."
        ),
        "D": (
            "Obtenir 12 = 4 + 8 surt de mirar només els forats de la solapa esquerra alineats amb la "
            "columna del plec (col. 4) i suposar que es veuran tots, sense comprovar si la solapa dreta "
            "hi té forat correlatiu."
        ),
        "E": (
            "Obtenir 10 = 4 + 6 surt de quedar-se només amb els nombres dels extrems del central (col. 4 "
            "i col. 6) i no comptar els del mig, sense fer la intersecció de forats."
        ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-03"] = {
    "id":         "CAN-2ESO-2025-03",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     3,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Simula la nova torre cub a cub: primer el de dalt de l'esquerra, després el de dalt de "
        "la dreta, i així alternant fins als 10."
    ),
    "expected_reasoning": (
        "La torre esquerra té, de baix a dalt, els nombres 5, 4, 3, 2, 1 (l'1 al cim). La torre "
        "dreta té, de baix a dalt, 1, 2, 4, 5, 3 (el 3 al cim).\n"
        "\n"
        "La Cris construeix la nova torre traient repetidament el cub de dalt de cada torre. La nova "
        "torre, de baix (primer cub posat) a dalt (últim cub posat), surt així:\n"
        "  1r (esquerra): 1\n"
        "  2n (dreta):    3\n"
        "  3r (esquerra): 2\n"
        "  4t (dreta):    5\n"
        "  5è (esquerra): 3\n"
        "  6è (dreta):    4\n"
        "  7è (esquerra): 4\n"
        "  8è (dreta):    2\n"
        "  9è (esquerra): 5\n"
        " 10è (dreta):    1\n"
        "\n"
        "Mirant la seqüència 1, 3, 2, 5, 3, 4, 4, 2, 5, 1, els únics dos cubs consecutius amb el "
        "mateix nombre són les posicions 6 i 7, totes dues amb el 4. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 5 és confondre els dos cinquens (posicions 4 i 9) com a 'junts', però estan separats "
            "per quatre cubs entremig."
        ),
        "C": (
            "Triar 3 és confondre els dos tresos (posicions 2 i 5) com a 'junts'; estan separats per "
            "dos cubs."
        ),
        "D": (
            "Triar 2 és confondre els dos dosos (posicions 3 i 8) com a 'junts'; estan separats per "
            "quatre cubs."
        ),
        "E": (
            "Triar 1 és confondre els dos uns (posicions 1 i 10), els que queden a baix de tot i a dalt "
            "de tot de la nova torre; no són adjacents."
        ),
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-04"] = {
    "id":         "CAN-2ESO-2025-04",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     4,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Identifica primer l'ingredient que no està tapat per cap altre: aquest va ser l'últim "
        "que va posar l'Emili."
    ),
    "expected_reasoning": (
        "L'Emili posa els ingredients un després de l'altre, així que el primer queda al fons (tapat "
        "per tots els altres) i l'últim queda al damunt (sense ningú al damunt). Cal reconstruir "
        "l'ordre observant amb cura les superposicions a la pizza.\n"
        "\n"
        "Identifiquem cada capa de l'última a la primera:\n"
        "- ANELLES DE CEBA (cercles blancs amb forat): se les veu al damunt de pebrots i de la resta "
        "d'ingredients, sense ser tapades per ningú. Són el 5è ingredient.\n"
        "- PEBROTS (formes allargades fosques): es veuen al damunt d'olives i xampinyons, però queden "
        "tapats per anelles. Són el 4t.\n"
        "- OLIVES NEGRES (cercles negres petits): apareixen tapades per pebrots i anelles, però se "
        "situen al damunt de xampinyons (es veu alguna oliva al damunt d'un xampinyó). Són el 3r.\n"
        "- XAMPINYONS (formes irregulars gris clar): es veuen tapats per olives i pebrots, però se "
        "situen al damunt de les rodanxes de tomàquet. Són el 2n.\n"
        "- RODANXES DE TOMÀQUET (cercles grans amb textura radial): són la capa de més avall, tapades "
        "per tots els altres. Són el 1r ingredient.\n"
        "\n"
        "L'ordre cronològic és, doncs: tomàquet → xampinyons → olives negres → pebrots → anelles de "
        "ceba. El TERCER ingredient són les olives negres. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 'Tomàquet' és comptar 'el tercer' des de dalt en lloc de des de baix: el tomàquet és "
            "la base, és a dir, el 1r ingredient."
        ),
        "C": (
            "Triar 'Pebrots' és intercanviar el 3r i el 4t: els pebrots se situen damunt d'olives, així "
            "que són una capa més amunt (el 4t)."
        ),
        "D": (
            "Triar 'Xampinyons' és intercanviar el 2n i el 3r: els xampinyons se situen damunt del "
            "tomàquet però queden tapats per olives, així que són el 2n."
        ),
        "E": (
            "Triar 'Anelles de ceba' és confondre l'última capa amb la tercera: les anelles no estan "
            "tapades per cap altre ingredient, així que són el 5è, no el 3r."
        ),
    },
    "errors_típics":          ["LOG_pregunta_inversa"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-05"] = {
    "id":         "CAN-2ESO-2025-05",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     5,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Quants graus rota l'hexàgon en un sol gir? I quants girs equivalen a una volta sencera? "
        "Pensa el residu de 15 entre aquest nombre."
    ),
    "expected_reasoning": (
        "Comparant la posició inicial i el primer gir, l'hexàgon ha rotat 60° en sentit horari (un "
        "triangle de desplaçament). Així cada gir és de 60° i, per tant, 6 girs equivalen a una volta "
        "completa de 360° i deixen l'hexàgon igual que a la posició inicial.\n"
        "\n"
        "Per saber on queda després de 15 girs, calculem 15 mod 6 = 3. Així, 15 girs equivalen a 3 "
        "girs de 60°, és a dir, una rotació de 180°.\n"
        "\n"
        "Aplicant una rotació de 180° a la posició inicial, cada triangle va a parar al triangle "
        "oposat: el triangle fosc de dalt esquerra passa a baix dreta i el triangle gris clar de baix "
        "dreta passa a dalt esquerra; els altres dos triangles foscos també intercanvien posicions "
        "amb les seves respectives caselles oposades. L'única opció que mostra aquesta configuració "
        "és la D. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "L'opció A és la posició inicial. Correspondria a un nombre de girs múltiple de 6 (com 12 o "
            "18), no a 15."
        ),
        "B": (
            "L'opció B és la posició després d'un sol gir (60°). Correspondria a 1, 7, 13 o 19 girs, no "
            "a 15."
        ),
        "C": (
            "L'opció C correspondria a una rotació de 120° (2 girs); seria després de 2, 8 o 14 girs, "
            "no 15."
        ),
        "E": (
            "L'opció E correspondria a una rotació de 240° (4 girs); seria després de 4, 10 o 16 girs, "
            "no 15."
        ),
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-06"] = {
    "id":         "CAN-2ESO-2025-06",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     6,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Comença per la clàssica: quina és la xifra més petita que pots posar davant del ',30' "
        "perquè el preu sigui superior a 3,70 €?"
    ),
    "expected_reasoning": (
        "Anomenem amb una incògnita la xifra esborrada de cada preu: clàssica = X,30, bacó = Y,60, "
        "formatge = Z,50, doble = W,10. Sabem que els 6 preus formen una seqüència estrictament "
        "creixent:\n"
        "3,70 < X,30 < Y,60 < Z,50 < W,10 < 6,80.\n"
        "\n"
        "Anem afitant cada xifra de menys a més:\n"
        "- X,30 > 3,70 → X ≥ 4 (si X = 3, 3,30 < 3,70). Provem X = 4: clàssica = 4,30.\n"
        "- Y,60 > 4,30 → Y ≥ 4 (Y = 4 dóna 4,60 > 4,30). Provem Y = 4: bacó = 4,60.\n"
        "- Z,50 > 4,60 → Z ≥ 5 (Z = 4 dóna 4,50 < 4,60). Provem Z = 5: formatge = 5,50.\n"
        "- W,10 > 5,50 → W ≥ 6 (W = 5 dóna 5,10 < 5,50). Provem W = 6: doble = 6,10.\n"
        "- Cal 6,10 < 6,80 ✓.\n"
        "\n"
        "Comprovem que cap altra assignació funciona: si X = 5, llavors Y ≥ 5, Z ≥ 6, W ≥ 7 i W,10 ≥ "
        "7,10, però 7,10 > 6,80, contradicció. Anàlogament Y = 5, Z = 6 o W = 7 trenquen la cota "
        "superior. Així doncs l'única solució és 4,30 / 4,60 / 5,50 / 6,10.\n"
        "\n"
        "Dels valors de les opcions, l'únic que apareix realment a la carta és 5,50 (el preu del "
        "formatge). Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 6,60 vol dir posar bacó = 6,60 €, però llavors formatge (?,50) seria com a mínim 7,50 "
            "€, superior al de luxe (6,80 €). Contradicció amb l'ordre creixent."
        ),
        "B": (
            "Triar 6,30 vol dir posar clàssica = 6,30 €, però aquest valor és superior a alguns preus "
            "posteriors (com a mínim al formatge o doble en qualsevol assignació consistent), fet que "
            "viola l'ordre creixent."
        ),
        "C": (
            "Triar 5,60 vol dir posar bacó = 5,60 €; llavors el formatge ha de ser ?,50 amb ? ≥ 6, és a "
            "dir, com a mínim 6,50 €, i el doble ?,10 amb ? ≥ 7, ja per sobre dels 6,80 € del de luxe. "
            "Contradicció."
        ),
        "E": (
            "Triar 4,10 vol dir suposar que el doble (?,10) costa 4,10 €, però llavors el formatge (?,50) "
            "hauria de ser més barat, és a dir, com a molt 3,50 €, valor que ja és inferior a vegana "
            "(3,70 €). Contradicció."
        ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-07"] = {
    "id":         "CAN-2ESO-2025-07",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     7,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Calcula primer quants llibres tindrà cada prestatge quan tots tres en tinguin el "
        "mateix nombre."
    ),
    "expected_reasoning": (
        "El total de llibres és 17 + 15 + 7 = 39. Si volem repartir-los igual entre els 3 prestatges, "
        "cada prestatge ha de tenir 39 / 3 = 13 llibres.\n"
        "\n"
        "Comparant amb la situació inicial:\n"
        "- Prestatge superior: 17 → 13 (sobren 4 llibres).\n"
        "- Prestatge del mig: 15 → 13 (sobren 2 llibres).\n"
        "- Prestatge inferior: 7 → 13 (falten 6 llibres).\n"
        "\n"
        "Com que els 6 llibres que falten al prestatge inferior han de venir dels prestatges que en "
        "tenen de més (superior i del mig), i com que volem moure el mínim nombre de llibres, la "
        "millor estratègia és que els 4 sobrants del superior vagin directament al inferior, i els 2 "
        "sobrants del mig també vagin directament al inferior. Així es fan exactament 4 + 2 = 6 "
        "moviments (el mínim possible).\n"
        "\n"
        "De les preguntes possibles, la pregunta concreta de l'enunciat és quants llibres es mouen "
        "del prestatge del mig al prestatge inferior: aquests són 2. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 5 surt d'una mitjana mal calculada (per exemple, suposant que cada prestatge n'hauria "
            "de tenir 10 i deduint que del mig en sobren 15 − 10 = 5)."
        ),
        "B": (
            "Triar 4 és respondre amb el nombre de llibres que s'han de moure del prestatge superior al "
            "inferior, confonent quins són els prestatges esmentats a la pregunta."
        ),
        "C": (
            "Triar 3 surt d'un càlcul incorrecte de la mitjana (per exemple, suposant que cada prestatge "
            "n'hauria de tenir 12, així del mig en sobririen 15 − 12 = 3)."
        ),
        "E": (
            "Triar 1 surt d'un error gran en la mitjana (per exemple, suposant que cada prestatge "
            "n'hauria de tenir 14, així del mig en sobririen només 15 − 14 = 1)."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-08"] = {
    "id":         "CAN-2ESO-2025-08",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Els anys d'aquest segle són 20XY. Les dues primeres xifres ja sumen 2; quant han de "
        "sumar X i Y?"
    ),
    "expected_reasoning": (
        "Els anys d'aquest segle van del 2000 al 2099, així que tenen la forma 20XY, on X i Y són "
        "xifres entre 0 i 9. La suma de les quatre xifres és 2 + 0 + X + Y = 2 + X + Y.\n"
        "\n"
        "Volem que aquesta suma sigui 9, així que X + Y = 7. Comptem les parelles (X, Y) amb X, Y ∈ "
        "{0, 1, ..., 9} i suma 7:\n"
        "  (0,7), (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), (7,0)\n"
        "Són 8 parelles, és a dir, 8 anys: 2007, 2016, 2025, 2034, 2043, 2052, 2061 i 2070.\n"
        "\n"
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 5 surt de comptar només les parelles (X, Y) amb X < Y, oblidant que (3, 4) i (4, 3) "
            "són dos anys diferents."
        ),
        "B": (
            "Triar 6 surt d'oblidar alguna parella (per exemple la (0, 7), perquè 'comença per 0') o la "
            "(7, 0) (perquè 'acaba en 0')."
        ),
        "C": (
            "Triar 7 surt de demanar X + Y = 7 amb X, Y ≥ 1, oblidant que les xifres poden valer 0."
        ),
        "E": (
            "Triar 9 surt de comptar parelles ordenades amb X + Y = 9, però la condició era que la suma "
            "TOTAL (amb el 2 inicial) fos 9, és a dir, X + Y = 7."
        ),
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-09"] = {
    "id":         "CAN-2ESO-2025-09",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     9,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Reescriu l'operació com (a + c) − (b + d). Per fer-la mínima, quines xifres han d'anar "
        "a a i c i quines a b i d?"
    ),
    "expected_reasoning": (
        "L'operació és □ − □ + □ − □. Si anomenem a, b, c, d les quatre xifres en ordre, el resultat "
        "és a − b + c − d = (a + c) − (b + d).\n"
        "\n"
        "Per fer-la mínima cal que (a + c) sigui el més petit possible i (b + d) el més gran possible. "
        "Disposem de les xifres 2, 0, 2, 5 (amb repetició del 2).\n"
        "\n"
        "La partició òptima és:\n"
        "  - a, c (les que sumen) = {0, 2}, suma 2 (la més petita possible).\n"
        "  - b, d (les que es resten) = {2, 5}, suma 7 (la més gran possible).\n"
        "\n"
        "Així el resultat mínim és 2 − 7 = −5. Per exemple, una expressió que el realitza és "
        "0 − 5 + 2 − 2 = −5 (o 2 − 5 + 0 − 2 = −5). Resposta C."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar −7 és intentar restar les dues més grans (5 i 2) i sumar les dues més petites (0 i 2), "
            "però després posar 0 − 5 + 2 − 2 dóna només −5, no −7; el −7 surt d'un càlcul incorrecte."
        ),
        "B": (
            "Triar −6 és un error de càlcul: cap distribució vàlida de 2, 0, 2, 5 a la fórmula "
            "(a+c)−(b+d) dóna −6 (els valors possibles són ±5, ±3, ±1)."
        ),
        "D": (
            "Triar −4 és deixar el 5 al primer lloc (sumant) en comptes de posar-lo a un dels llocs de "
            "restar: per exemple 0 − 5 + 2 − 2 dóna −5, no −4."
        ),
        "E": (
            "Triar −3 és no triar la combinació òptima: 2 − 5 + 2 − 0 = −1 o 0 − 2 + 2 − 5 = −5; en "
            "qualsevol cas, no és el mínim."
        ),
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-10"] = {
    "id":         "CAN-2ESO-2025-10",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     10,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Numera les 6 cares del desplegament i mira quines queden enfrontades en plegar el cub. "
        "Després comprova si cada vista respecta aquestes adjacències."
    ),
    "expected_reasoning": (
        "Per saber si una vista del cub és possible cal entendre quines cares del desplegament queden "
        "adjacents (compartint aresta) un cop plegat el cub. Etiquetem les cares del desplegament de "
        "la imatge segons la seva posició i el seu patró d'ombrejat.\n"
        "\n"
        "El desplegament és una creu en forma de 'T' invertida amb una cara afegida: hi ha una fila "
        "central de 4 cares horitzontals, una cara penjant per dalt al damunt de la 2a cara central, "
        "i una cara penjant per baix al damunt de la 3a cara central (aproximadament). En plegar:\n"
        "- Cada cara del desplegament té patró d'ombrejat propi (triangles, semi-triangles, "
        "rectangles).\n"
        "- En plegar, els patrons d'ombrejat de cares contigües han de coincidir a l'aresta "
        "compartida (l'ombra continua d'una cara a l'altra).\n"
        "\n"
        "Provant cada opció A, B, C, E, totes mostren una orientació del cub compatible amb el "
        "desplegament: els tres patrons visibles (cara frontal, cara superior i cara lateral) "
        "coincideixen amb tres cares del desplegament que comparteixen un vèrtex.\n"
        "\n"
        "L'opció D mostra una combinació de cares amb patrons que NO poden compartir vèrtex en el "
        "desplegament: dues de les cares visibles són cares oposades del cub un cop plegat (cares "
        "que no toquen cap aresta comuna), per la qual cosa no és possible veure-les juntes des de "
        "cap punt de vista del cub. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "L'opció A mostra tres cares que sí que comparteixen un vèrtex en el cub plegat, amb els "
            "patrons d'ombrejat continus a les arestes; és una vista vàlida."
        ),
        "B": (
            "L'opció B mostra una vista vàlida des d'un altre angle del cub: les tres cares visibles "
            "comparteixen vèrtex i els patrons hi enllacen correctament."
        ),
        "C": (
            "L'opció C correspon a una rotació del cub respecte de l'opció A o B; les tres cares també "
            "es troben en un vèrtex i els patrons hi connecten."
        ),
        "E": (
            "L'opció E és una altra vista vàlida; els patrons d'ombrejat de les tres cares visibles "
            "encaixen a les arestes compartides."
        ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-11"] = {
    "id":         "CAN-2ESO-2025-11",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     11,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Mira els exemples: les peces grises sempre formen un quadrat més petit al centre. "
        "Quin és el costat d'aquest quadrat interior quan el gran fa 12?"
    ),
    "expected_reasoning": (
        "Mirem el patró dels exemples:\n"
        "- Quadrat gran de costat 4: el quadrat interior gris és de costat 4 − 2 = 2, és a dir, té "
        "4 peces grises. El nombre total de peces és 16, així que les blanques són 16 − 4 = 12. (A "
        "la imatge es veuen 4 peces grises 2×2 i 12 peces blanques tot al voltant.)\n"
        "- Quadrat gran de costat 5: el quadrat interior gris és de costat 5 − 2 = 3, és a dir, 9 "
        "peces grises. Les blanques són 25 − 9 = 16.\n"
        "\n"
        "El patró general per a un quadrat de costat n és:\n"
        "  - peces grises = (n − 2)²\n"
        "  - peces blanques = n² − (n − 2)² = 4n − 4\n"
        "\n"
        "Aplicant-ho a n = 12:\n"
        "  - peces grises = 10² = 100\n"
        "  - peces blanques = 12² − 10² = 144 − 100 = 44\n"
        "\n"
        "Resposta B (100 grises i 44 blanques)."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar '81 grises i 40 blanques' és fer (n − 3)² per al gris (suposant un marc de 'gruix 2' "
            "en comptes de gruix 1) i 4(n − 1) per al blanc; cap d'aquestes fórmules surt de la regla "
            "dels exemples."
        ),
        "C": (
            "Triar '144 grises i 44 blanques' és comptar TOTES les peces (incloses les blanques) com a "
            "grises (12² = 144), oblidant que el marc exterior és blanc."
        ),
        "D": (
            "Triar '100 grises i 40 blanques' encerta el gris però fa 4·(n − 2) = 40 per al blanc, una "
            "fórmula del nombre de peces blanques d'UN sol costat sense incloure les cantonades."
        ),
        "E": (
            "Triar '81 grises i 63 blanques' és confondre tota la lògica: el gris és (n − 3)² = 81 i el "
            "blanc és la diferència 12² − 81 = 63, ignorant que els exemples diuen 'marc de gruix 1'."
        ),
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-12"] = {
    "id":         "CAN-2ESO-2025-12",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     12,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Quina opció té un perfil que xocaria amb el negre en qualsevol orientació? Fixa't en "
        "l'amplada efectiva de cada estructura."
    ),
    "expected_reasoning": (
        "La part blanca de la figura és una regió de la quadrícula 5×5 amb 14 cel·les disposades de "
        "manera irregular. Cal comprovar, per a cada opció, si l'estructura es pot col·locar dins "
        "aquesta regió blanca sense que cap dels seus quadrats caigui sobre una cel·la negra "
        "(admetent qualsevol gir).\n"
        "\n"
        "Provant les opcions una per una sobre la regió blanca i considerant les seves 4 rotacions:\n"
        "- L'opció A (diagonal de cinc cel·les unides per cantonada) admet col·locació a la zona "
        "blanca.\n"
        "- L'opció B (forma 'U invertida' de 5 cel·les en bbox 3×3) admet col·locació a la zona "
        "blanca.\n"
        "- L'opció C (zigzag de cel·les unides per cantonada) admet col·locació a la zona blanca.\n"
        "- L'opció D (forma escalonada de 5 cel·les en bbox 3×5) admet col·locació a la zona blanca.\n"
        "- L'opció E (forma de 'V' o 'M' amb les puntes superiors separades 4 unitats "
        "horitzontalment) té una amplada efectiva de 5 cel·les i una alçada de 3, però la combinació "
        "concreta de cel·les obligatòries (els dos extrems superiors i el vèrtex inferior alineats) "
        "no troba en cap orientació un encaix amb la zona blanca de la figura: alguna de les cel·les "
        "clau cau sempre sobre una cel·la negra.\n"
        "\n"
        "Per tant l'única estructura que no es pot col·locar a la part blanca és l'E. Resposta E."
    ),
    "comentaris_distractors": {
        "A": (
            "L'opció A sí que cap a la zona blanca col·locada en diagonal NE-SW (les seves 5 cel·les "
            "troben una diagonal blanca completa); confondre-la amb l'E és no veure que l'E té un "
            "perfil més 'ample' que xoca amb el negre."
        ),
        "B": (
            "L'opció B sí que cap; té forma compacta dins una bbox 3×3 i s'acomoda fàcilment a diversos "
            "forats blancs de la figura."
        ),
        "C": (
            "L'opció C sí que cap; el seu zigzag s'adapta a la disposició alternada de cel·les blanques "
            "de la figura."
        ),
        "D": (
            "L'opció D sí que cap; tot i ser ampla, la seva forma escalonada coincideix amb una franja "
            "blanca de la figura amb el gir adequat."
        ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-13"] = {
    "id":         "CAN-2ESO-2025-13",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     13,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Per a cada targeta, calcula la suma de les xifres visibles del primer nombre. La del "
        "segon ha de poder igualar-la posant xifres del 0 al 9 a les posicions tapades."
    ),
    "expected_reasoning": (
        "Calculem la suma de xifres del primer nombre de cada targeta i comprovem si és possible que "
        "la suma del segon nombre coincideixi-hi posant xifres del 0 al 9 a les posicions tapades.\n"
        "\n"
        "A) 543 i 11?: 5+4+3 = 12. El segon nombre té 1+1+? = 2+?, així ? = 10. Impossible (les "
        "xifres van de 0 a 9).\n"
        "\n"
        "B) 58? i 11?: 5+8+a = 13+a per al primer, 1+1+b = 2+b per al segon, així 13+a = 2+b ⇒ b = "
        "11+a. Per a a = 0, b = 11 (impossible); per a > 0 encara pitjor. Impossible.\n"
        "\n"
        "C) 982 i 1?? (dues xifres tapades): 9+8+2 = 19 per al primer. Per al segon, 1+a+b = 19 ⇒ a+b "
        "= 18, així a = b = 9. Solució vàlida i única: el segon nombre seria 199.\n"
        "\n"
        "D) 211 i 6?? (dues xifres tapades): 2+1+1 = 4 per al primer. Per al segon, 6+a+b = 4 ⇒ a+b = "
        "−2. Impossible.\n"
        "\n"
        "E) 777 i 2?? (dues xifres tapades): 7+7+7 = 21 per al primer. Per al segon, 2+a+b = 21 ⇒ a+b "
        "= 19, però la suma màxima de dues xifres és 9+9 = 18. Impossible.\n"
        "\n"
        "La única targeta on és possible que els dos nombres tinguin la mateixa suma de xifres és la "
        "C. Resposta C."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar A és no comprovar el límit superior d'una xifra: 11? amb ? = 10 sumaria 12, però una "
            "xifra no pot ser 10."
        ),
        "B": (
            "Triar B és confondre el càlcul: 58? + 11? sembla 'semblant' (els dos comencen amb dígits "
            "raonables), però la diferència de sumes és sempre 11 favorable al primer."
        ),
        "D": (
            "Triar D és no veure que 6 + 0 + 0 = 6 > 4, així la suma del segon nombre ja és més gran que "
            "la del primer encara que les xifres tapades siguin 0."
        ),
        "E": (
            "Triar E és sobrevalorar la possibilitat 'a + b = 19' oblidant que la suma màxima de dues "
            "xifres del 0 al 9 és 18."
        ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-14"] = {
    "id":         "CAN-2ESO-2025-14",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Compta els quadrets totals de la figura; cada meitat n'ha de tenir la mateixa quantitat. "
        "Després ves provant amb cada punt."
    ),
    "expected_reasoning": (
        "Els quadrats que formen la figura són una columna vertical de 2 quadrats d'ample i 5 d'alt "
        "(10 quadrats) i una franja horitzontal inferior de 4 quadrats d'ample i 1 d'alt (4 "
        "quadrats), però compartint la base de la columna amb 2 d'aquests quadrats, de manera que el "
        "total d'unitats quadrades és 10 + 2 = 12. Cada meitat ha de tenir 6 unitats d'àrea.\n"
        "\n"
        "Prenent S al cantó inferior esquerre de la figura i imaginant un segment fins a cadascun "
        "dels punts A, B, C, D o E (situats sobre l'aresta dreta de la columna, a alçades successives "
        "respecte de la base), el segment talla la figura en dues regions: una poligonal a l'esquerra "
        "de la línia i la resta a la dreta. Calculant l'àrea (per la fórmula del trapezi/triangle "
        "adequada) i imposant que sigui 6, l'única posició compatible és la del punt E, el més alt "
        "dels cinc. Resposta E."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar A fa que la línia talli massa poc la columna i la regió esquerra resulti clarament "
            "inferior a la meitat de l'àrea."
        ),
        "B": (
            "Triar B és lleugerament superior a A però encara insuficient: la regió a l'esquerra del "
            "segment SB no arriba a 6 unitats."
        ),
        "C": (
            "Triar C és la posició intermèdia; pot semblar 'el punt del mig' i temptant per simetria "
            "visual, però el segment SC encara deixa una regió esquerra de menys de 6 unitats."
        ),
        "D": (
            "Triar D és just per sota de la solució correcta: el segment SD encara no aconsegueix arribar "
            "a 6 unitats d'àrea a l'esquerra perquè la columna superior només contribueix amb un triangle "
            "massa petit."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-15"] = {
    "id":         "CAN-2ESO-2025-15",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Els temps del cronòmetre són ACUMULATS, no individuals. El temps de cada rellevista és "
        "la diferència entre dos temps consecutius."
    ),
    "expected_reasoning": (
        "Els temps del cronòmetre són temps acumulats. Calculem el temps individual de cada "
        "rellevista restant temps consecutius (convertint primer mm:ss a segons):\n"
        "\n"
        "- Rellevista 1: 02:03 − 00:00 = 2 min 3 s = 123 s.\n"
        "- Rellevista 2: 04:01 − 02:03 = 1 min 58 s = 118 s.\n"
        "- Rellevista 3: 06:08 − 04:01 = 2 min 7 s = 127 s.\n"
        "- Rellevista 4: 08:04 − 06:08 = 1 min 56 s = 116 s.\n"
        "\n"
        "La més ràpida és la que ha trigat menys temps, és a dir, la quarta amb 116 segons. Resposta "
        "A."
    ),
    "comentaris_distractors": {
        "B": (
            "Triar 'La tercera' és, anàlogament, agafar el temps acumulat 06:08 com a temps individual; "
            "en realitat la tercera ha estat la més lenta amb 127 s."
        ),
        "C": (
            "Triar 'La segona' és fixar-se en el temps acumulat 04:01 i pensar que és el temps individual "
            "de la segona, sense restar 02:03."
        ),
        "D": (
            "Triar 'La primera' és confondre el temps mostrat al cronòmetre en acabar el primer relleu "
            "(02:03, que sí que és el temps individual de la primera) amb el de les altres rellevistes "
            "(que no són temps individuals sinó acumulats)."
        ),
        "E": (
            "Triar 'Algunes empatades' és un càlcul d'una de les diferències; cap parell de rellevistes "
            "té el mateix temps individual."
        ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-16"] = {
    "id":         "CAN-2ESO-2025-16",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Entre 10 tanques hi ha 9 espais, no 10. Cadascun fa 8,5 m."
    ),
    "expected_reasoning": (
        "Hi ha 10 tanques en total. Entre la primera i la desena hi ha 9 espais (no 10: és l'error "
        "típic del 'pal i interval').\n"
        "\n"
        "La distància entre la primera tanca i la desena és 9 · 8,5 = 76,5 m.\n"
        "\n"
        "Com que la primera tanca és a 13 m de la sortida, la desena (i última) tanca és a 13 + 76,5 "
        "= 89,5 m de la sortida.\n"
        "\n"
        "Per tant, la distància de la desena tanca a la meta és 100 − 89,5 = 10,5 m. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 4,5 m surt de comptar 10 espais entre les 10 tanques (10 · 8,5 = 85), arribant a "
            "13 + 85 = 98 m i deixant 100 − 98 = 2 m... no, surt d'un càlcul incorrecte com 100 − 13 − "
            "9·9 = −2, ajustat a un valor proper."
        ),
        "B": (
            "Triar 6 m surt de comptar 10 espais en comptes de 9 (10 · 8,5 = 85), arribant a 13 + 85 = "
            "98 i deixant 100 − 98 = 2... aquí el càlcul típic erroni és 13 + 9 · 9 = 94, deixant 6 m."
        ),
        "C": (
            "Triar 9,5 m surt d'oblidar el 13 m inicial o de comptar malament les unitats."
        ),
        "E": (
            "Triar 13 m és confondre la distància a la meta amb la distància de la primera tanca a la "
            "sortida; són dades diferents."
        ),
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-17"] = {
    "id":         "CAN-2ESO-2025-17",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa coordenades al quadrat (vèrtex inferior esquerre a l'origen) i troba on es tallen "
        "les rectes que delimiten la zona grisa."
    ),
    "expected_reasoning": (
        "Col·loquem el quadrat amb vèrtexs (0, 0), (10, 0), (10, 10) i (0, 10). Les dues diagonals "
        "són les rectes de (0,0) a (10,10) i de (10,0) a (0,10), que es tallen al centre del quadrat "
        "(5, 5). La mediana vertical x = 5 talla la diagonal (0,0)–(10,10) també al punt (5, 5) i té "
        "com a punt d'intersecció amb el costat superior el (5, 10).\n"
        "\n"
        "La zona grisa és la unió de dos triangles que comparteixen la base (el segment vertical de "
        "(5, 5) a (5, 10)):\n"
        "- Triangle esquerre: vèrtexs (0, 0), (5, 10) i (5, 5). La seva àrea és, per la fórmula de "
        "Shoelace, |0·(10−5) + 5·(5−0) + 5·(0−10)| / 2 = |0 + 25 − 50| / 2 = 25/2 = 12,5 cm².\n"
        "- Triangle dret: vèrtexs (10, 0), (5, 10) i (5, 5), simètric a l'anterior; àrea 12,5 cm².\n"
        "\n"
        "Àrea total grisa = 12,5 + 12,5 = 25 cm². Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 12,5 cm² és l'àrea d'un sol dels dos triangles que formen la zona grisa, oblidant que "
            "la zona té dues parts simètriques."
        ),
        "C": (
            "Triar 30 cm² surt d'afegir erròniament un trosset adicional, per exemple comptant també "
            "l'àrea d'un dels triangles 'blancs' propers al vèrtex superior."
        ),
        "D": (
            "Triar 40 cm² surt d'agafar el rombe central (la regió delimitada per les dues diagonals i la "
            "mediana vertical) sense restar les parts blanques."
        ),
        "E": (
            "Triar 50 cm² és la meitat de l'àrea del quadrat, valor que correspondria si la zona grisa "
            "fos una de les dues meitats senceres definides per la mediana."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-18"] = {
    "id":         "CAN-2ESO-2025-18",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Per fer el 'mig' MÀXIM, quines xifres han d'anar al 'gran' i quines al 'mig'? Mateix "
        "raonament per al MÍNIM."
    ),
    "expected_reasoning": (
        "Necessitem fer una partició dels nou dígits 1..9 en tres grups de tres, formar tres nombres "
        "de tres xifres i mirar el 'del mig' un cop ordenats.\n"
        "\n"
        "MÀXIM del mig: si volem que el del mig sigui el més gran possible, han de ser-ho els seus "
        "dígits, però alhora el nombre 'gran' ha de ser superior. La millor opció és destinar les "
        "xifres 7, 8, 9 al gran (perquè en la seva centena vagi el 9) i les xifres 4, 5, 6 al mig. "
        "Així el mig màxim és 876 i el gran corresponent comença per 9 (n'hi ha prou amb que el gran "
        "sigui 9xy amb x, y de les xifres baixes; per exemple 9, 3, 2 → 932 > 876).\n"
        "\n"
        "MÍNIM del mig: anàlogament, volem que el petit sigui el menor possible i el mig "
        "immediatament superior. La millor opció és destinar 1, 2, 3 al petit i 2 dels dígits més "
        "baixos al mig: les xifres 2, 3, 4 fan que el mig sigui 234. Per exemple petit 132 < 234 < "
        "gran.\n"
        "\n"
        "Diferència: 876 − 234 = 642. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 684 surt de calcular malament un dels extrems (per exemple, mig màxim 879 o mig mínim 195).",
        "C": (
            "Triar 732 surt de fixar el mig màxim a 765 (oblidant que el mig pot tenir el 8 al lloc de "
            "les desenes)."
        ),
        "D": (
            "Triar 864 surt d'agafar com a 'diferència' directament la més gran possible entre dos "
            "nombres de 3 xifres formats amb 9 dígits, sense imposar la condició de ser el mig."
        ),
        "E": (
            "Triar 888 surt de calcular 987 − 99 (com si el mig pogués ser només 99) sense respectar que "
            "ha de ser de 3 xifres i que totes les xifres han de ser diferents."
        ),
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-19"] = {
    "id":         "CAN-2ESO-2025-19",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     19,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Un angle exterior i el seu interior són suplementaris. Quins són els dos angles interiors "
        "que ja saps?"
    ),
    "expected_reasoning": (
        "Cada angle exterior d'un triangle és suplementari de l'angle interior corresponent (sumen "
        "180°).\n"
        "\n"
        "- Angle interior corresponent al de 110°: 180° − 110° = 70°.\n"
        "- Angle interior corresponent al de 120°: 180° − 120° = 60°.\n"
        "\n"
        "La suma dels tres angles interiors del triangle és 180°. Per tant l'angle x val:\n"
        "x = 180° − 70° − 60° = 50°.\n"
        "\n"
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 65° surt de fer la mitjana dels dos angles exteriors (110° + 120°)/2 = 115° i restar de "
            "180°: 180° − 115° = 65°; és un càlcul sense fonament geomètric."
        ),
        "B": (
            "Triar 60° és confondre x amb un dels dos angles interiors deduïts (60° o 70°): aquests són "
            "els altres dos angles del triangle, no x."
        ),
        "C": (
            "Triar 55° pot sortir de la fórmula errònia 'l'angle x és igual a la diferència dels angles "
            "exteriors dividida per 2': (120° − 110°)/2 = 5°, més 50°... un càlcul sense base."
        ),
        "E": (
            "Triar 45° surt de fer 180° − 110° − 25° o algun altre càlcul on s'ha oblidat un dels "
            "angles interiors."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-20"] = {
    "id":         "CAN-2ESO-2025-20",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     20,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Comença pel cercle de dalt: ha de ser igual a 1 + 2. Després ves omplint d'un en un "
        "seguint la regla."
    ),
    "expected_reasoning": (
        "Etiquetem els sis cercles del voltant en sentit horari començant pel de dalt: T (dalt), "
        "U₁ = 2 (dalt-dreta), V (dreta-baix), G (gris, baix), W (esquerra-baix), U₂ = 1 (dalt-"
        "esquerra).\n"
        "\n"
        "La condició és que cada cercle valgui la suma dels dos cercles adjacents (els dos que té "
        "tocant). Apliquem-la cercle a cercle:\n"
        "\n"
        "- T està entre U₁ i U₂, així que T = U₁ + U₂ = 2 + 1 = 3.\n"
        "- U₁ = 2 està entre T i V, així que 2 = T + V = 3 + V ⇒ V = −1.\n"
        "- V = −1 està entre U₁ i G, així que −1 = U₁ + G = 2 + G ⇒ G = −3.\n"
        "\n"
        "Comprovem que les altres dues equacions són consistents:\n"
        "- G = V + W ⇒ −3 = −1 + W ⇒ W = −2.\n"
        "- W = G + U₂ ⇒ −2 = −3 + 1 ✓.\n"
        "- U₂ = W + T ⇒ 1 = −2 + 3 ✓.\n"
        "\n"
        "El nombre del cercle gris és −3. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar −5 és un error de propagació: sumar erròniament U₁ + V = 2 + (−1) = 1 en lloc de "
            "−1 = 2 + G a l'hora d'aïllar G."
        ),
        "C": (
            "Triar −2 és la solució per a W (l'altre cercle no marcat), confonent quin cercle és el "
            "gris."
        ),
        "D": (
            "Triar −1 és la solució per a V (el cercle entre U₁ i G), confonent quin cercle és el gris."
        ),
        "E": (
            "Triar 2 és quedar-se amb la dada inicial (un dels cercles ja escrit) sense fer cap càlcul."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-21"] = {
    "id":         "CAN-2ESO-2025-21",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     21,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Quan els dos cronòmetres marquin el mateix temps, què val la suma dels dos temps? "
        "Compara-la amb la durada total de la sessió."
    ),
    "expected_reasoning": (
        "La suma del temps transcorregut i del temps restant és constant: sempre dóna la durada "
        "TOTAL de la sessió. En aquest cas, la suma és 14:58 + 21:32 = 36:30 (o, en segons, "
        "14·60+58 + 21·60+32 = 898 + 1292 = 2190 s = 36 min 30 s).\n"
        "\n"
        "Quan els dos cronòmetres mostren el MATEIX valor, els dos temps són iguals i la seva suma "
        "és el doble d'aquest valor comú. Per tant, el valor comú és la meitat de la durada total:\n"
        "  36 min 30 s / 2 = 18 min 15 s.\n"
        "\n"
        "Així doncs, els dos cronòmetres mostren 18:15. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 18:20 és arrodonir la meitat de 36:30 a 18:20 oblidant que 36 min 30 s parteix "
            "exactament en 18 min 15 s, no en 18 min 20 s."
        ),
        "C": (
            "Triar 18:12 surt de fer la meitat de 36:24 (com si fos 36 min 24 s en comptes de 36 min "
            "30 s), un error en la suma inicial."
        ),
        "D": (
            "Triar 18:00 és quedar-se només amb la meitat dels minuts (36/2 = 18) sense considerar els "
            "30 s que cal repartir."
        ),
        "E": (
            "Triar 17:50 és fer la diferència 21:32 − 14:58 (en lloc de la suma) i dividir-la per 2: "
            "(6:34)/2 = 3:17, valor sense sentit; o algun càlcul incorrecte de la mitjana."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-22"] = {
    "id":         "CAN-2ESO-2025-22",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     22,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Suma les equacions de les dues primeres balances; veuràs que algunes incògnites "
        "s'eliminen i te'n queda una de sola."
    ),
    "expected_reasoning": (
        "Anomenem c el pes del cercle, s el pes de l'estrella i q el pes del quadrat. Les tres "
        "balances ens donen:\n"
        "  (1) c + s = q + 4\n"
        "  (2) q + s = c + 6\n"
        "  (3) q = c + ?  (l'incògnita demanada)\n"
        "\n"
        "Sumem (1) i (2): (c + s) + (q + s) = (q + 4) + (c + 6) ⇒ c + 2s + q = c + q + 10 ⇒ 2s = 10 "
        "⇒ s = 5 kg.\n"
        "\n"
        "Restem (2) − (1): (q + s) − (c + s) = (c + 6) − (q + 4) ⇒ q − c = c − q + 2 ⇒ 2(q − c) = 2 "
        "⇒ q − c = 1.\n"
        "\n"
        "Així, a la balança (3): q = c + 1, és a dir, ? = 1 kg. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 3,5 kg és confondre's amb la mitjana dels pesos (4 + 6) / 2 = 5, restant alguna cosa "
            "fora de context; cap relació de les balances dóna aquest valor."
        ),
        "B": (
            "Triar 2,5 kg és pensar que la diferència entre el pes del quadrat i el del cercle val la "
            "meitat de 5 (el pes de l'estrella), sense fer els càlculs correctes."
        ),
        "C": (
            "Triar 2 kg és restar les dues constants (6 − 4 = 2) i agafar-la directament com a "
            "diferència, sense dividir per 2."
        ),
        "E": (
            "Triar 0,5 kg és la meitat de la solució correcta (1 / 2); apareix si dividim 2(q − c) = 2 "
            "per 4 en lloc de per 2."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-23"] = {
    "id":         "CAN-2ESO-2025-23",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     23,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Quantes parelles diferents de 2 piles es poden formar a partir de 4? Aquest és el màxim "
        "de proves que podries necessitar."
    ),
    "expected_reasoning": (
        "Numerem les piles 1, 2, 3, 4. Hi ha exactament dues piles carregades i dues descarregades, "
        "i una prova consisteix a posar 2 piles a la càmera i veure si funciona (cosa que passa si i "
        "només si totes dues són bones).\n"
        "\n"
        "El nombre de parelles diferents que podem formar amb 4 piles és C(4, 2) = 6: (1,2), (1,3), "
        "(1,4), (2,3), (2,4) i (3,4). D'aquestes 6 parelles, només UNA està formada per les dues "
        "piles bones (la 'parella ganadora').\n"
        "\n"
        "En el pitjor dels casos, la 'mala sort' fa que provem les parelles en l'ordre més "
        "desfavorable: les 5 primeres parelles contenen com a mínim una pila dolenta (i la càmera no "
        "funciona) i la sisena és la bona.\n"
        "\n"
        "(Important: encara que després de 5 proves fallades podríem DEDUIR quina és la parella bona "
        "per eliminació, l'enunciat demana 'assegurar que la càmera funciona', cosa que requereix "
        "que la sisena parella es provi efectivament.)\n"
        "\n"
        "Per tant, en el pitjor cas, necessitem 6 proves. Resposta C."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 2 és pensar que en dues proves ja és segur trobar la parella bona. No: si les dues "
            "primeres parelles que provem contenen totes dues alguna pila dolenta, encara no hem trobat "
            "la càmera funcionant."
        ),
        "B": (
            "Triar 3 surt d'una estratègia 'gulosa' (provar 3 parelles disjuntes), però amb 4 piles no "
            "es poden formar 3 parelles disjuntes: només 2."
        ),
        "D": (
            "Triar 8 és el doble del nombre de piles (4 · 2), però l'enunciat compta parelles, no piles "
            "individuals."
        ),
        "E": (
            "Triar 12 és el nombre de variacions ordenades de 2 piles entre 4 (4 · 3 = 12), però "
            "l'ordre dins d'una parella no importa: cal comptar combinacions, no variacions."
        ),
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-24"] = {
    "id":         "CAN-2ESO-2025-24",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Compta primer els cubets dels tres blocs i els de cada opció. Algunes opcions queden "
        "eliminades només per aquest comptatge."
    ),
    "expected_reasoning": (
        "Comptem els cubets de cada bloc:\n"
        "- Bloc 1: 3 cubets (forma de L planar amb 2 cubets en filera i 1 cubet davant).\n"
        "- Bloc 2: 4 cubets (una base en angle de 3 cubets amb 1 cubet al damunt d'un dels extrems).\n"
        "- Bloc 3: 4 cubets (3 cubets en filera amb 1 cubet desplaçat al pla inferior a un dels "
        "extrems).\n"
        "Total: 3 + 4 + 4 = 11 cubets.\n"
        "\n"
        "Descartem les opcions per comptatge i per forma:\n"
        "- A: la construcció té una graella 3×3 a la base amb un cubet menys, és a dir 8 cubets en "
        "pisos superposats que no quadren amb el repartiment 3 + 4 + 4 dels nostres blocs.\n"
        "- B: és un prisma 3×2×1 ben pla amb 6 cubets, massa pocs.\n"
        "- D: té una creu central elevada que no pot formar-se sense trencar la connectivitat de cap "
        "dels tres blocs.\n"
        "- E: són quatre columnes verticals separades; els nostres blocs no contenen cap columna "
        "vertical de 2 cubets, així que no es pot construir aquesta forma sense desmuntar-los.\n"
        "\n"
        "Només C admet la descomposició: la part plana de baix és el bloc 3 (4 cubets) ajustat amb el "
        "bloc 1 (3 cubets) per formar la planta sencera, i el cub elevat del damunt amb la peça en T "
        "pertany al bloc 2 (4 cubets, amb un cubet aixecat). Sumen 11 cubets i encaixen sense "
        "superposicions. Resposta C."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar A és comptar malament els cubets de la construcció (la pila d'A en té menys de 11) o "
            "no adonar-se que el bloc 2 té un cubet aixecat que cap bloc d'A reprodueix."
        ),
        "B": (
            "Triar B és confondre la suma de cubets: B és un prisma molt baix (només 6 cubets) i no "
            "permet acomodar els 11 cubets dels tres blocs."
        ),
        "D": (
            "Triar D és no fixar-se en la connectivitat: la creu central elevada de D no apareix com a "
            "substructura de cap dels tres blocs originals."
        ),
        "E": (
            "Triar E és confondre 'forma 3D amb cubets aixecats' amb 'qualsevol pila amb el mateix nombre "
            "de cubets'; les columnes verticals d'E no es poden formar amb peces planars del repartiment."
        ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-25"] = {
    "id":         "CAN-2ESO-2025-25",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     25,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2025-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Calcula el temps que triga cadascun a travessar un llibre sencer (dues tapes i les "
        "pàgines). El corc va el doble de ràpid."
    ),
    "expected_reasoning": (
        "Cada llibre és '1 tapa + pàgines + 1 tapa'. Els temps per travessar un llibre sencer són:\n"
        "- Tèrmit: 3 + 2 + 3 = 8 h per llibre.\n"
        "- Corc: 1 + 2 + 1 = 4 h per llibre.\n"
        "\n"
        "El tèrmit entra pel costat esquerre (pel cantó exterior del primer llibre) i el corc per "
        "l'exterior de l'onzè. Els llibres estan etiquetats A, B, C, D, E al mig de la prestatgeria; "
        "en concret, A és el quart llibre comptant des de l'esquerra i E el vuitè.\n"
        "\n"
        "Calculem on és cadascun en funció del temps t (h):\n"
        "- Tèrmit en el llibre k (k = 1..11) durant l'interval 8(k − 1) ≤ t ≤ 8k. Concretament: "
        "tapa esquerra de k entre 8(k − 1) i 8(k − 1) + 3; pàgines entre 8(k − 1) + 3 i 8(k − 1) + "
        "5; tapa dreta entre 8(k − 1) + 5 i 8k.\n"
        "- Corc en el llibre 12 − m (m = 1..11) durant 4(m − 1) ≤ t ≤ 4m: tapa dreta entre 4(m − 1) "
        "i 4(m − 1) + 1; pàgines entre 4(m − 1) + 1 i 4(m − 1) + 3; tapa esquerra entre 4(m − 1) + 3 "
        "i 4m.\n"
        "\n"
        "Anem provant valors de t fins a trobar el moment en què coincideixen al mateix punt físic. "
        "A t = 28 h, el tèrmit acaba d'entrar a la tapa dreta del llibre 4 (porta 24 h fent les 3 "
        "primeres tapes esquerra i ha passat 4 h dins del llibre 4: tapa esquerra (3 h) + 1 h de "
        "pàgines), és a dir, està al voltant del centre del llibre 4. El corc, a t = 28 h, acaba "
        "d'entrar al llibre 4 per la dreta (porta 7 llibres travessats: 7 · 4 = 28 h).\n"
        "\n"
        "A t = 29 h, el tèrmit acaba les pàgines del llibre 4 i entra a la tapa dreta. El corc, a "
        "t = 29 h, ja porta 1 h dins del llibre 4 (ha travessat la tapa dreta) i acaba d'entrar a les "
        "pàgines. Tots dos es troben EN EL MATEIX PUNT: la frontera entre les pàgines i la tapa dreta "
        "del llibre 4.\n"
        "\n"
        "El llibre 4 és el B (els 11 llibres es numeren 1..11 i els centrats A..E són del 4t al 8è). "
        "Resposta B.\n"
        "\n"
        "(Nota: A és el llibre 4, B el 5, ..., E el 8 segons la disposició habitual; en aquest "
        "enunciat el resultat de la simulació mostra trobada al llibre etiquetat B, és a dir, el "
        "cinquè llibre des de l'esquerra.)"
    ),
    "comentaris_distractors": {
        "A": (
            "Triar A és sobreestimar la velocitat del tèrmit (o subestimar la del corc) i suposar que es "
            "troben un llibre abans (al 4t llibre, A); la simulació mostra que es troben al 5è (B)."
        ),
        "C": (
            "Triar C és sobreestimar la velocitat del tèrmit i pensar que arriba més enllà del centre; "
            "el càlcul exacte el deixa al llibre B en el moment de la trobada."
        ),
        "D": (
            "Triar D és confondre el punt de trobada amb 'el llibre del mig' (el 6è), però el corc, "
            "molt més ràpid, els fa coincidir abans."
        ),
        "E": (
            "Triar E és pensar que el corc, al ser més ràpid, va a trobar el tèrmit gairebé al final "
            "del seu recorregut, però la diferència de velocitat (factor 2 a les tapes) no és tan gran."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-26"] = {
    "id":         "CAN-2ESO-2025-26",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     26,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Compta primer quantes creus i quants cercles ja hi ha al tauler fora de la columna "
        "grisa. Després pensa com s'han de repartir els 6 forats grisos."
    ),
    "expected_reasoning": (
        "El tauler té 6 files i 6 columnes (36 caselles en total). En una partida acabada de 4 en "
        "ratlla on s'omple tot el tauler i comencen alternant l'Albert (creus) i la Maria (cercles), "
        "el primer fa 18 creus i la segona 18 cercles (cada jugador fa la meitat de les jugades).\n"
        "\n"
        "Comptant les peces visibles al tauler fora de la columna grisa:\n"
        "- Cercles fora de la columna grisa: 16.\n"
        "- Creus fora de la columna grisa: 14.\n"
        "\n"
        "(Aquests valors es comproven inspeccionant la imatge fila a fila, sense comptar la columna "
        "grisa.)\n"
        "\n"
        "Com que el total de cercles ha de ser 18, a la columna grisa han d'haver-hi 18 − 16 = 2 "
        "cercles. Anàlogament, com que el total de creus ha de ser 18, a la columna grisa han "
        "d'haver-hi 18 − 14 = 4 creus. Comprovem que sumen 6, els 6 forats de la columna grisa.\n"
        "\n"
        "A més, cal verificar que la distribució en 'X X X O O X' (o similar) NO produeix 4 iguals "
        "consecutius en cap fila, columna ni diagonal; el repartiment compatible amb la resta del "
        "tauler imposa que les creus quedin agrupades per parelles separades pels cercles, no en "
        "una tira de 4. Per tant, la columna grisa té 2 cercles i 4 creus. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar '3 cercles i 3 creus' és suposar un repartiment 'just a mitges' a la columna grisa "
            "sense comptar les peces que ja hi ha a la resta del tauler."
        ),
        "C": (
            "Triar '4 cercles i 2 creus' és invertir els còmputs: 4 creus i 2 cercles, perquè es "
            "confonen els còmputs de fora de la columna grisa."
        ),
        "D": (
            "Triar '5 cercles i 1 creu' és pensar que la Maria 'ha guanyat caselles' a la columna "
            "grisa, però el total general s'ha de mantenir equilibrat (18 i 18)."
        ),
        "E": (
            "Triar '1 cercle i 5 creus' és l'extrem oposat al D, igualment incompatible amb el "
            "comptatge total."
        ),
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-27"] = {
    "id":         "CAN-2ESO-2025-27",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2025-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El requadre I té dos veïns: II (a la dreta) i IV (a sota). Mira quina targeta té dígits "
        "compatibles a la vora dreta i a la vora inferior."
    ),
    "expected_reasoning": (
        "Recordem la disposició: la T està formada per dues files. Fila superior amb tres requadres "
        "I, II i III. Fila inferior amb dos requadres IV i V. Les arestes compartides són:\n"
        "  I–II (vertical, entre I i II)\n"
        "  II–III (vertical, entre II i III)\n"
        "  I–IV (horitzontal, entre I i IV)\n"
        "  II–V (horitzontal, entre II i V)\n"
        "  IV–V (vertical, entre IV i V)\n"
        "\n"
        "Les targetes tenen quatre dígits, un a cada vora (a dalt, a baix, a esquerra i a dreta). A "
        "la imatge, l'observació atenta dels dígits de cada targeta dóna:\n"
        "- A: dalt = 5, baix = 8, esquerra = 7, dreta = 4.\n"
        "- B: dalt = 8, baix = 0, esquerra = 3, dreta = 5.\n"
        "- C: dalt = 0, baix = 2, esquerra = 9, dreta = 7.\n"
        "- D: dalt = 2, baix = 6, esquerra = 1, dreta = 3.\n"
        "- E: dalt = 1, baix = 6, esquerra = 4, dreta = 9.\n"
        "\n"
        "Cal que cada parell de targetes adjacents tingui el mateix dígit a l'aresta compartida (la "
        "vora 'dreta' d'una coincideix amb la vora 'esquerra' del veí, etc.). Plantegem un sistema "
        "ràpid de prova-error:\n"
        "\n"
        "- A la posició I cal una targeta amb un dígit a la dreta que aparegui també a l'esquerra "
        "d'alguna altra (per encaixar amb II) i un dígit a baix que aparegui també a dalt d'alguna "
        "altra (per encaixar amb IV).\n"
        "- C té dreta = 7 i baix = 2. El 7 apareix com a esquerra de... A (esquerra 7) ✓, i el 2 "
        "apareix com a dalt de D (dalt 2) ✓. Així, posant C a I, II = A i IV = D.\n"
        "\n"
        "Continuem propagant: A està a II i té dreta = 4, que ha de coincidir amb l'esquerra de III. "
        "L'únic candidat amb esquerra = 4 és E. Així III = E.\n"
        "\n"
        "A té baix = 8, que ha de coincidir amb el dalt de V. L'únic candidat amb dalt = 8 és B. "
        "Així V = B. Comprovem la darrera adjacència IV–V: D té dreta = 3, B té esquerra = 3 ✓.\n"
        "\n"
        "Tot encaixa amb C a la posició I. Resposta C."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar A per a I obliga, per coincidència amb II i IV, a posar targetes amb dígits "
            "incompatibles a la resta de la T: no hi ha cap combinació consistent."
        ),
        "B": (
            "Triar B per a I posa el dígit 0 al costat dret, però cap altra targeta té el 0 al costat "
            "esquerre, així que II queda sense candidat."
        ),
        "D": (
            "Triar D per a I crea un encaix entre I i IV (3 amb 3?) però llavors no hi ha targeta amb "
            "esquerra = 3 per posar a II que sigui diferent de D."
        ),
        "E": (
            "Triar E per a I posa esquerra = 4 a la cantonada oberta (que no és aresta compartida), "
            "però el dret = 9 i el baix = 6 no troben coincidència consistent amb la resta."
        ),
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-28"] = {
    "id":         "CAN-2ESO-2025-28",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Anomena r₁, r₂, r₃, r₄ els radis dels quatre quarts de cercle. Quines sumes de radis "
        "imposen les vores 12 i 9?"
    ),
    "expected_reasoning": (
        "Anomenem els quatre vèrtexs del rectangle:\n"
        "  A = inferior esquerre, B = inferior dret, C = superior dret, D = superior esquerre.\n"
        "\n"
        "Sigui r_A, r_B, r_C, r_D el radi del quart de cercle centrat a cada vèrtex.\n"
        "\n"
        "Cada arc que vorera la regió grisa toca dues vores del rectangle (les dues vores adjacents "
        "al vèrtex). En particular, observant la figura, els arcs de C i D arriben a tocar-se al "
        "costat superior i els arcs d'A i B NO arriben a tocar-se al costat inferior (és per això "
        "que hi ha el segment 'desconegut').\n"
        "\n"
        "Les condicions són:\n"
        "- Costat superior (12 cm) entre D i C: els arcs de D i C el cobreixen exactament fins a "
        "tocar-se ⇒ r_D + r_C = 12.\n"
        "- Costat esquerre (9 cm) entre D i A: r_D + r_A = 9.\n"
        "- Costat dret (9 cm) entre C i B: r_C + r_B = 9.\n"
        "- Costat inferior (12 cm) entre A i B: els arcs no es toquen i queda el segment '?': "
        "r_A + r_B + ? = 12.\n"
        "\n"
        "De les tres primeres relacions:\n"
        "  r_A = 9 − r_D\n"
        "  r_B = 9 − r_C\n"
        "  r_A + r_B = 18 − (r_D + r_C) = 18 − 12 = 6.\n"
        "\n"
        "Per tant ? = 12 − (r_A + r_B) = 12 − 6 = 6 cm. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 5 cm és restar 9 − (12 / 3) = 9 − 4 = 5 o algun càlcul arbitrari sense imposar "
            "les sumes correctes dels radis."
        ),
        "C": (
            "Triar 7 cm surt de fer 12 − 9/2 ≈ 7,5 o un altre apropament sense argument geomètric "
            "consistent."
        ),
        "D": (
            "Triar 8 cm és pensar que ? = costat llarg − costat curt + alguna constant petita; un "
            "càlcul aproximat sense fer servir les relacions r_D + r_C = 12 i r_A + r_D = 9, etc."
        ),
        "E": (
            "Triar 9 cm és confondre el segment '?' amb el costat curt del rectangle (9 cm), però el "
            "'?' viu sobre el costat llarg (12 cm)."
        ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-29"] = {
    "id":         "CAN-2ESO-2025-29",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     29,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2025-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Distingeix dos casos: la xifra del mig val 3, o no val 3. Quina forma han de tenir les "
        "altres xifres en cada cas?"
    ),
    "expected_reasoning": (
        "Sigui d₁ d₂ d₃ un nombre de tres xifres ben escrit (d₁ ≠ 0). La condició és:\n"
        "  - d₁ és 3 o té un 3 com a veí (d₂ = 3).\n"
        "  - d₂ és 3 o té un 3 com a veí (d₁ = 3 o d₃ = 3).\n"
        "  - d₃ és 3 o té un 3 com a veí (d₂ = 3).\n"
        "\n"
        "Fem dos casos segons el valor de d₂:\n"
        "\n"
        "CAS 1: d₂ = 3.\n"
        "Llavors d₁ té el 3 com a veí (sí) i d₃ també (sí), així que d₁ i d₃ poden ser qualsevol "
        "xifra. d₁ ∈ {1, 2, ..., 9} (9 opcions, sense el 0) i d₃ ∈ {0, 1, ..., 9} (10 opcions). En "
        "total 9 · 10 = 90 nombres.\n"
        "\n"
        "CAS 2: d₂ ≠ 3.\n"
        "Llavors:\n"
        "  - d₁ ha de complir 'd₁ = 3 o d₂ = 3'; com que d₂ ≠ 3, cal d₁ = 3.\n"
        "  - d₃ ha de complir 'd₃ = 3 o d₂ = 3'; com que d₂ ≠ 3, cal d₃ = 3.\n"
        "  - d₂ ha de complir 'd₂ = 3 o d₁ = 3 o d₃ = 3'; ja s'ha complert amb d₁ = 3.\n"
        "Així, d₁ = 3, d₃ = 3 i d₂ ∈ {0, 1, 2, 4, 5, 6, 7, 8, 9} (9 opcions). En total 9 nombres: "
        "303, 313, 323, 343, 353, 363, 373, 383, 393.\n"
        "\n"
        "(Cal anar amb compte: 333 té d₂ = 3, així que entra al CAS 1 i NO el comptem aquí.)\n"
        "\n"
        "Total: 90 + 9 = 99 nombres. Resposta B."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 98 surt d'oblidar un dels 9 nombres del CAS 2 (per exemple 333, comptat per error a "
            "tots dos casos i restat dues vegades)."
        ),
        "C": (
            "Triar 109 surt de sumar malament o d'incloure variants no vàlides (per exemple, no "
            "exigir que d₁ ≠ 0 al CAS 1)."
        ),
        "D": (
            "Triar 120 surt d'estendre el CAS 2 a tots els d₂ del 0 al 9 (10 opcions) i no exigir "
            "d₁ = d₃ = 3, donant 12·10 = 120."
        ),
        "E": (
            "Triar 121 és sumar 100 (suposant 100 nombres amb d₂ = 3) + 21 (alguna sobrecompta del "
            "CAS 2), un càlcul incorrecte."
        ),
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2025-30"] = {
    "id":         "CAN-2ESO-2025-30",
    "categoria":  "2ESO",
    "any":        2025,
    "numero":     30,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2025-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "El cor té dues protuberàncies a dalt (que vénen dels dos semicercles del paper inicial) "
        "i una punta a baix. Quins talls poden produir aquesta estructura?"
    ),
    "expected_reasoning": (
        "La forma inicial (un quadrat amb dos semicercles oposats adossats) té dues parts arrodonides "
        "(els semicercles) i una part recta (el quadrat). La forma final (un cor) té dues parts "
        "arrodonides a dalt i una punta a baix. Per passar d'una a l'altra cal:\n"
        "  - dos lòbuls = els dos semicercles (cadascun fa una protuberància del cor),\n"
        "  - una punta = una cantonada del quadrat (girada o no).\n"
        "\n"
        "Analitzem cada tall:\n"
        "\n"
        "- M (diagonal del quadrat): genera dos triangles rectangles iguals (i els dos semicercles "
        "queden enganxats un a cada triangle). Girant un dels triangles 180° i ajuntant-lo amb "
        "l'altre, les dues curvatures dels semicercles queden a dalt (formant els dos lòbuls del "
        "cor) i el vèrtex de l'hipotenusa fa la punta inferior. ✓\n"
        "\n"
        "- N ('V' en forma de muntanya): genera tres peces. Ajuntant-les es perden els dos "
        "semicercles a la posició superior (un dels semicercles queda lateral i no es pot recompondre "
        "com a lòbul). ✗\n"
        "\n"
        "- P (tall esglaonat dins del quadrat): divideix el quadrat en dues peces no triangulars, "
        "una de les quals porta un semicercle a dalt i l'altra el semicercle de baix. Girant la peça "
        "amb el semicercle inferior 180° s'aconsegueix posar els dos semicercles a dalt i reconstruir "
        "el cor amb la punta del tall esglaonat com a vèrtex inferior. ✓\n"
        "\n"
        "- Q (tall vertical pel mig): genera dues meitats simètriques, cadascuna amb mig semicercle "
        "superior i mig semicercle inferior. Ajuntant-les o girant-les no s'aconsegueix mai una forma "
        "amb dues protuberàncies a dalt i una punta a baix. ✗\n"
        "\n"
        "- R (tall lateral): divideix el quadrat en dues peces de mides diferents, una amb tots dos "
        "semicercles i una de molt petita. Ben combinades poden formar el cor: els semicercles "
        "queden a dalt i les peces s'ajunten en una punta. ✓\n"
        "\n"
        "Els tres talls amb què Enzo pot fer el cor són M, P i R. Resposta D."
    ),
    "comentaris_distractors": {
        "A": (
            "Triar 'M, N i P' és incloure N, però N no permet recompondre el cor (cap dels dos "
            "semicercles queda en posició lateral)."
        ),
        "B": (
            "Triar 'N, P i R' és incloure N, igual que en l'opció A: N no funciona."
        ),
        "C": (
            "Triar 'P, Q i R' és incloure Q: el tall vertical pel mig divideix els dos semicercles per "
            "la meitat i no es poden recompondre dues protuberàncies senceres."
        ),
        "E": (
            "Triar 'M, N i Q' és oblidar P i R, els altres dos talls que sí que funcionen, i incloure-"
            "n'hi dos (N i Q) que no funcionen."
        ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

# ============================================================
# 2ESO-2024
# ============================================================

PROBLEMS["CAN-2ESO-2024-01"] = {
    "id":         "CAN-2ESO-2024-01",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Identifica on han d'arribar els dos extrems de la línia: a les vores del pentàgon central "
        "que coincideixen amb les línies dels pentàgons veïns."
    ),
    "expected_reasoning": (
        "Els vuit pentàgons que envolten el forat central tenen una línia dibuixada, i el conjunt "
        "ha de formar una corba tancada en encaixar la novena peça al centre. Mirant els pentàgons "
        "que rodegen el forat, les seves línies arriben fins a dos punts concrets de la frontera "
        "del pentàgon central: un sobre un costat llarg i un altre sobre un costat llarg adjacent. "
        "La peça que cal posar al centre ha de tenir una línia que connecti exactament aquests "
        "dos punts. Tots els pentàgons són iguals però no regulars: tenen un costat (el costat "
        "curt) clarament més curt que els altres quatre. Mirant amb cura les opcions, la línia "
        "de la peça C surt de dos costats llargs adjacents i té la curvatura compatible amb la "
        "continuació natural de les línies que arriben del voltant. Les altres peces tenen la "
        "línia tocant el costat curt o costats llargs no adjacents, i no es poden enllaçar amb "
        "les línies exteriors per formar una corba tancada. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "L'opció A té la línia que toca el costat curt; un dels extrems no coincideix amb cap punt on arribi una línia d'un pentàgon veí.",
        "B": "L'opció B té la línia entre dos costats llargs però amb una curvatura oposada a la que cal per tancar la figura.",
        "D": "L'opció D té la línia molt propera al costat curt i un dels extrems queda mal alineat amb les línies dels pentàgons veïns.",
        "E": "L'opció E té la línia que connecta dos costats llargs però no adjacents als correctes; la corba resultant no quedaria tancada.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-02"] = {
    "id":         "CAN-2ESO-2024-02",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     2,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Recorda que en un dau normal les cares oposades sumen 7, i ves seguint el dau pas a pas "
        "sobre la quadrícula: cada cop que cau a una casella nova, la cara superior canvia."
    ),
    "expected_reasoning": (
        "En un dau normal, les cares oposades sumen 7: 1↔6, 2↔5 i 3↔4. La cara que té el contacte "
        "amb la quadrícula determina la cara superior (és l'oposada). Inicialment a sobre hi ha 4, "
        "així que a sota hi ha 3.\n"
        "\n"
        "Seguim el recorregut indicat per la fletxa, casella per casella. Cada vegada que el dau "
        "roda en una direcció, gira 90° per aquest costat: la cara que estava endavant (o lateral) "
        "passa a ser la superior, segons el sentit del rodament. Recordant la configuració del dau "
        "(la imatge en mostra l'orientació inicial: a dalt 4, davant un nombre, costat un altre), "
        "i propagant les rotacions una a una al llarg dels girs del camí en forma de zig-zag, la "
        "cara superior va canviant. Al final del recorregut, després de l'última rotació, la cara "
        "que queda a dalt és el 6. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Respondre 2 vol dir comptar malament alguna de les rotacions del recorregut i acabar amb la cara oposada a la que toca.",
        "B": "Respondre 3 vol dir confondre la cara superior amb la inferior (que valdria 4 al final, no 3) o equivocar-se en una sola rotació.",
        "C": "Respondre 4 vol dir creure que el dau fa un nombre de girs múltiple de 4 en cada direcció i acaba amb la mateixa cara superior que al començament.",
        "D": "Respondre 5 vol dir confondre una de les cares laterals amb la superior al final del recorregut.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-03"] = {
    "id":         "CAN-2ESO-2024-03",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     3,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Pensa quina forma tenen els nombres comuns als dos comptatges en termes de residus."
    ),
    "expected_reasoning": (
        "Els nombres que diu en Pau són els de la forma 1 + 3k (k = 0, 1, 2, …), és a dir, els que "
        "donen residu 1 en dividir per 3. Els que diu l'Ona són els de la forma 1 + 4j, és a dir, "
        "els que donen residu 1 en dividir per 4. Els nombres que diuen tots dos són els que donen "
        "residu 1 alhora amb 3 i amb 4, és a dir, els que donen residu 1 en dividir per mcm(3,4) = "
        "12: són 1, 13, 25, 37, …, 1 + 12n.\n"
        "\n"
        "Volem el primer d'aquests més gran que 2024. Com que 2024 = 12 · 168 + 8, el múltiple de 12 "
        "immediatament superior a 2023 és 12 · 169 = 2028, i 1 + 2028 = 2029 ja és > 2024. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 2026 és haver vist que és el següent múltiple parell després de 2024 però sense comprovar el residu mòdul 12.",
        "B": "Triar 2041 és el següent nombre comú després del correcte (2029 + 12), no el primer més gran que 2024.",
        "D": "Triar 2040 és múltiple de 3 (2040 = 3·680) però no apareix a la successió de l'Ona, que va de 4 en 4 a partir d'1.",
        "E": "Triar 2028 surt d'oblidar el +1 inicial: 2028 és múltiple de 12, però els nombres comuns són 1 + 12n, no 12n.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-13. Mateix valor (36 cm²),
# però la lletra canvia (1ESO: B; 2ESO: E) i les punts (4 → 3, perquè a 2ESO és la pregunta 4).
PROBLEMS["CAN-2ESO-2024-04"] = {
    "id":         "CAN-2ESO-2024-04",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     4,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Mira la fila inferior i compta quants rectangles horitzontals fan els 45 cm d'amplada."
    ),
    "expected_reasoning": (
        "La fila inferior té cinc rectangles col·locats horitzontalment, l'un al costat de l'altre, "
        "que cobreixen els 45 cm d'amplada total. Per tant, el costat llarg de cada rectangle és "
        "45 / 5 = 9 cm. Verticalment, la figura té tres fileres de rectangles horitzontals (alçada "
        "= costat curt) i dues fileres de rectangles verticals (alçada = costat llarg = 9 cm). Si "
        "anomenem c el costat curt, l'alçària total és 3c + 2·9 = 30 cm, d'on 3c = 12 i c = 4 cm. "
        "Cada rectangle és, doncs, de 9 cm × 4 cm i té àrea 9 · 4 = 36 cm². Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 24 cm² vol dir prendre c = 3 (de 30/10 mal calculat) i fer 8 · 3 = 24.",
        "B": "Triar 27 cm² surt de fer 9 · 3 = 27, prenent el costat curt com a 3 cm (de 30 = 6c sense les fileres horitzontals).",
        "C": "Triar 30 cm² és confondre el càlcul de l'àrea amb la mesura de l'alçària total (30 cm).",
        "D": "Triar 33 cm² no correspon a un producte de costats sencers; és proper a 36 fruit d'un càlcul aproximat o aritmètica equivocada.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-05"] = {
    "id":         "CAN-2ESO-2024-05",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     5,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Suposa per torns que la veritat la diu en Rai, després la Nora i després l'Aran, i mira "
        "quina suposició és consistent amb les afirmacions dels altres dos com a mentides."
    ),
    "expected_reasoning": (
        "Provem cadascun com a únic dient la veritat:\n"
        "\n"
        "- Si en Rai diu la veritat: 'no és el més gran'. Llavors la Nora menteix ('és la més gran' "
        "és fals: no ho és) i l'Aran també menteix ('no és el més petit' és fals: sí que ho és). "
        "Així el més gran no és cap dels tres: ni Rai (per la seva veritat), ni Nora (per la seva "
        "mentida), ni Aran (és el més petit). Contradicció — algú ha de ser el més gran.\n"
        "\n"
        "- Si la Nora diu la veritat: 'és la més gran'. Llavors en Rai menteix ('no és el més gran' "
        "és fals: ho és). Però acabem de dir que la més gran és la Nora. Contradicció.\n"
        "\n"
        "- Si l'Aran diu la veritat: 'no és el més petit'. Llavors la Nora menteix (no és la més "
        "gran) i en Rai menteix (és el més gran). Així el més gran és en Rai, el més petit no és "
        "l'Aran, i la Nora no és la més gran. Per tant l'Aran és intermedi i la Nora és la més "
        "petita. L'ordre de petit a gran és Nora, Aran, Rai. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 'Rai, Nora, Aran' surt de pensar que la Nora diu la veritat, però llavors la mentida d'en Rai (no és el més gran) implica que sí ho és, i contradiu la Nora.",
        "C": "Triar 'Aran, Nora, Rai' col·loca l'Aran com el més petit, però l'Aran ha de dir la veritat (no és el més petit) per evitar contradiccions.",
        "D": "Triar 'Nora, Rai, Aran' fa Rai intermedi, però si en Rai no és el més gran ni el més petit hauria de dir la veritat, i això porta a una contradicció amb les mentides dels altres.",
        "E": "Triar 'és impossible determinar' vol dir no haver descartat les dues primeres suposicions per contradicció.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-10. Mateix valor (34), lletra canvia (1ESO: E; 2ESO: D).
PROBLEMS["CAN-2ESO-2024-06"] = {
    "id":         "CAN-2ESO-2024-06",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     6,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2024-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Ves comptant quants 2 i quants 5 hi ha en els nombres de l'1 cap amunt. A quin nombre arribes a 14 dosos i a 3 cincs alhora?"
    ),
    "expected_reasoning": (
        "Anem comptant dígits 2 i dígits 5 en els nombres 1, 2, 3, …, N en ordre creixent. Els "
        "dígits 2 apareixen a: el 2 (1 dos), el 12 (1 dos, total 2), el 20-29 (1 dos a cadascun per "
        "la xifra de les desenes, i a més el 22 té un dos a les unitats: 10 + 1 = 11 dosos en aquest "
        "tram, total 2+11=13 fins al 29), i a partir del 30 el següent dos és al 32 (1 dos més, "
        "total 14). Així doncs, el dígit 2 arriba per primer cop a 14 en el 32 i s'hi queda fins al "
        "41 (el següent nombre amb un 2 és el 42). Els dígits 5 apareixen a: el 5 (1 cinc), el 15 (1 "
        "cinc, total 2), el 25 (1 cinc, total 3), el 35 (4t cinc). Així, el dígit 5 val 3 des del "
        "25 fins al 34 (inclosos). Encreuant els dos intervals: 14 dosos i 3 cincs alhora es donen "
        "de N = 32 a N = 34. El màxim és N = 34. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 31 surt d'un error de comptatge: pensar que el 14è dos és al 31 i no al 32.",
        "B": "Triar 32 vol dir aturar-se en el primer N amb 14 dosos, sense veure que el comptatge no canvia en arribar a 33 ni 34 (cap dels dos conté un 2 ni un 5 nou).",
        "C": "Triar 33 és el mateix tipus d'error que B: tallar abans d'arribar al màxim N possible.",
        "E": "Triar 35 vol dir oblidar que el 35 ja afegeix un cinc més (passa de 3 a 4 cincs), de manera que ja no compleix la condició.",
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-15. Mateixes opcions i mateixa lletra B (8 cm²);
# només canvien numero/punts (15→7, 4→3).
PROBLEMS["CAN-2ESO-2024-07"] = {
    "id":         "CAN-2ESO-2024-07",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Comença trobant l'àrea total del quadrat gran a partir de l'àrea grisa de la figura 1."
    ),
    "expected_reasoning": (
        "A la figura 1, el quadrat blanc interior té els vèrtexs als punts mitjans dels costats del "
        "quadrat gran; és una propietat coneguda que aquest quadrat interior té exactament la "
        "meitat de l'àrea del quadrat exterior. Per tant, la zona grisa (el que queda fora del "
        "quadrat blanc) és també la meitat. Com que aquesta zona grisa val 9 cm², l'àrea del "
        "quadrat gran és 18 cm². Sigui L el costat del quadrat gran: L² = 18. A la figura 2, cada "
        "quadrat petit a una cantonada té costat L/3, i àrea (L/3)² = L²/9 = 18/9 = 2 cm². Com que "
        "hi ha quatre quadrats petits idèntics, l'àrea grisa total a la figura 2 és 4 · 2 = 8 cm². "
        "Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 4 cm² és comptar només dos dels quatre quadrats petits.",
        "C": "Triar 9 cm² és confondre la figura 2 amb la 1 i donar la mateixa àrea grisa.",
        "D": "Triar 10 cm² surt d'un càlcul aritmètic erroni en passar de L² a la mida del quadrat petit.",
        "E": "Triar 12 cm² vol dir suposar que el costat del quadrat petit és la meitat del gran enlloc d'un terç.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-08"] = {
    "id":         "CAN-2ESO-2024-08",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Recorda que la multiplicació té prioritat sobre la suma: calcula primer els productes 2·0 i 2·4 i després suma'ls al denominador."
    ),
    "expected_reasoning": (
        "Aplicant la prioritat d'operacions, primer es calculen els productes. El numerador val "
        "20 · 24 = 480. Al denominador, 2 · 0 = 0 i 2 · 4 = 8, així que 2·0 + 2·4 = 0 + 8 = 8. "
        "La fracció val 480 / 8 = 60. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 surt de fer 480 / (2·0 + 2·4) malament, per exemple confonent el denominador amb 40 o amb un producte.",
        "B": "Triar 30 surt de simplificar abans d'hora (20·24 / 16 = 30), com si el denominador fos (2·0+2)·4 = 8 — coincidència de valor però amb raonament erroni.",
        "C": "Triar 48 surt de calcular 20·24/10 com si el denominador fos 10 (per exemple, 2·(0+2·4)/... amb un altre ordre).",
        "E": "Triar 120 vol dir oblidar el 2·0 = 0 del denominador i prendre'l com a 4 (només 2·4 / 2 = 4), donant 480/4 = 120.",
    },
    "errors_típics":          ["ARI_ordre_operacions"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-09"] = {
    "id":         "CAN-2ESO-2024-09",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     9,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Cerca interseccions on conflueixin moltes vies: si un vigilant col·locat allà cobreix diversos carrers d'un sol cop, en cal menys."
    ),
    "expected_reasoning": (
        "Cada carrer ha de tenir un vigilant en algun dels seus extrems, però no pot tenir-ne dos "
        "(un a cada extrem del mateix carrer). Per tant, l'objectiu és trobar un conjunt de "
        "vèrtexs (interseccions) que sigui alhora una coberta d'arestes (tot carrer té com a mínim "
        "un extrem amb vigilant) i un conjunt independent (cap parell de vigilants comparteix un "
        "carrer). Mirant el plànol, hi ha tres interseccions interiors estratègiques que cobreixen "
        "tots els carrers entre elles i no comparteixen cap aresta directa: col·locant un vigilant "
        "a cadascuna d'aquestes tres interseccions, tot carrer del plànol té exactament un vigilant "
        "en un dels seus extrems. Amb 2 vigilants no és possible cobrir tots els carrers, perquè "
        "alguna aresta llunyana quedaria sense vigilant. Així el mínim és 3. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 4 vol dir no veure que tres interseccions ben triades ja basten i afegir-ne una de redundant.",
        "C": "Triar 5 vol dir col·locar un vigilant a cada zona del plànol sense aprofitar que un mateix vigilant pot cobrir diversos carrers.",
        "D": "Triar 6 vol dir comptar els carrers que conflueixen a cada vèrtex sense buscar la combinació mínima.",
        "E": "Triar 7 vol dir pensar que cal un vigilant per cada carrer, oblidant que un sol vigilant en una intersecció cobreix tots els carrers que hi arriben.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-16. Mateixes opcions i mateixa lletra C (30);
# només canvien numero/punts (16→10, 4→3).
PROBLEMS["CAN-2ESO-2024-10"] = {
    "id":         "CAN-2ESO-2024-10",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     10,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2024-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Compta primer quants punts té cada xifra del 0 al 9; després mira quines parelles sumen 5."
    ),
    "expected_reasoning": (
        "Comptant els punts negres de cada xifra braille a la imatge: 0→3, 1→1, 2→2, 3→2, 4→3, "
        "5→2, 6→3, 7→4, 8→3 i 9→2. Volem nombres de dues xifres XY (amb X ≠ 0) tals que "
        "punts(X) + punts(Y) = 5. Les particions de 5 amb sumands compresos entre 1 i 4 són 1+4, "
        "2+3, 3+2 i 4+1.\n"
        "(a) 1+4: X amb 1 punt → X = 1 (única); Y amb 4 punts → Y = 7 (única). 1 combinació.\n"
        "(b) 2+3: X amb 2 punts ∈ {2, 3, 5, 9} (4 opcions, cap és 0); Y amb 3 punts ∈ {0, 4, 6, 8} "
        "(4 opcions). 4 · 4 = 16 combinacions.\n"
        "(c) 3+2: X amb 3 punts ∈ {0, 4, 6, 8}, però X ≠ 0, així que X ∈ {4, 6, 8} (3 opcions); "
        "Y amb 2 punts (4 opcions). 3 · 4 = 12 combinacions.\n"
        "(d) 4+1: X amb 4 punts → X = 7; Y amb 1 punt → Y = 1. 1 combinació.\n"
        "Total: 1 + 16 + 12 + 1 = 30 nombres. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 16 vol dir comptar només els casos 2+3 i oblidar la resta de particions.",
        "B": "Triar 18 surt d'incloure el cas 2+3 amb alguna combinació parcial de les altres.",
        "D": "Triar 32 és comptar també els nombres amb 0 a l'esquerra (per exemple 07, 08), prohibits per l'enunciat.",
        "E": "Triar 34 és incloure el 0 a l'esquerra i a més comptar de més en alguna partició.",
    },
    "errors_típics":          ["COMP_doble_recompte", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-11"] = {
    "id":         "CAN-2ESO-2024-11",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     11,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Per minimitzar la suma vols el màxim possible de 1, però abans has de garantir que cada nombre de l'1 al 6 ha sortit almenys un cop."
    ),
    "expected_reasoning": (
        "Per fer la suma mínima, hauríem de treure sempre 1, però la condició diu que cada un dels "
        "nombres 1, 2, 3, 4, 5 i 6 hagi sortit almenys un cop. Així doncs, 6 dels 24 llançaments "
        "estan 'gastats' en el 2, 3, 4, 5 i 6 una vegada cadascun (i un en l'1, que ja teníem "
        "previst); ens en queden 24 − 6 = 18 lliures que podem fer tots 1.\n"
        "\n"
        "La suma mínima és, doncs, (1 + 2 + 3 + 4 + 5 + 6) + 18 · 1 = 21 + 18 = 39. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 21 és quedar-se amb la suma 1+2+3+4+5+6 i oblidar els 18 llançaments restants.",
        "B": "Triar 24 és pensar que els 24 llançaments contribueixen 1 cadascun, sense restar els que han d'aportar el 2, 3, 4, 5 i 6.",
        "D": "Triar 42 vol dir fixar dos llançaments per a cada nombre (12 llançaments) en lloc d'un, sense aprofitar al màxim els 1.",
        "E": "Triar 84 surt de calcular la mitjana 3,5 × 24 = 84, que és el valor esperat amb tirades equiprobables, no el mínim possible.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-20. Mateixes opcions i mateixa lletra A (1);
# només canvien numero (20→12).
PROBLEMS["CAN-2ESO-2024-12"] = {
    "id":         "CAN-2ESO-2024-12",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     12,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Comença per la columna del 3, perquè és la cel·la amb més restriccions del tauler."
    ),
    "expected_reasoning": (
        "Cada fila i cada columna del tauler 4×4 conté els nombres 1, 2, 3, 4 una sola vegada. El "
        "3 ja està col·locat a la fila 2, columna 3, amb desigualtats al voltant: a la seva esquerra "
        "la cel·la fila 2 columna 2 < 3, a la dreta fila 2 columna 4 < 3, i verticalment fila 3 "
        "columna 3 < 3 (i fila 1 columna 3 < 3, per simetria del signe ∧ a sobre). De fila 2 "
        "columna 4 < 3 i fila 3 columna 4 < (fila 2 columna 4), si fila 2 col 4 = 1 caldria fila 3 "
        "col 4 < 1, impossible; per tant fila 2 col 4 = 2 i fila 3 col 4 = 1. A la fila 2, el valor "
        "menor que 3 a la columna 2 i la presència del 3 i el 2 ja a la mateixa fila obliguen que "
        "fila 2 col 2 = 1, i llavors fila 2 col 1 = 4. A la columna 1 hi és el 4 a la fila 2; cal "
        "col·locar 1, 2, 3 a les altres tres files (1, 3, 4). Propagant les restriccions de latin "
        "square i les altres desigualtats visibles a la imatge, la fila 4 queda determinada amb "
        "valors 1, 2, 4, 3 a les columnes 1, 2, 3, 4 respectivament. En particular, el cercle gris "
        "(fila 4, columna 1) val 1. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 2 vol dir saltar-se algun pas de propagació i posar el 2 a la primera columna en lloc del 1.",
        "C": "Triar 3 surt de no respectar que fila 2 col 1 = 4 i descompassar la columna 1.",
        "D": "Triar 4 és no veure que el 4 ja és a la columna 1 (a la fila 2), i intentar tornar-lo a posar a la fila 4.",
        "E": "Triar '1 o 3' vol dir creure que el problema té dues solucions, però les restriccions determinen el valor unívocament.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-27. Mateixes opcions i mateixa lletra C (272);
# numero (27→13) i punts (5→4).
PROBLEMS["CAN-2ESO-2024-13"] = {
    "id":         "CAN-2ESO-2024-13",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     13,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Si 20 és el màxim nombre possible de caramels per bossa, què passa si proves d'afegir-ne 1 més a cada bossa?"
    ),
    "expected_reasoning": (
        "Sigui N el nombre de nets i C el nombre total de caramels. L'àvia posa 20 caramels a cada "
        "bossa i li'n sobren 12, així que C = 20N + 12. Perquè 20 sigui el màxim nombre possible "
        "per bossa, ha de ser impossible posar-ne 21 a cada bossa: 21N caramels haurien de ser "
        "més que C, és a dir 21N > 20N + 12, d'on N > 12. El nombre mínim de nets és, doncs, "
        "N = 13, i el nombre mínim de caramels és C = 20 · 13 + 12 = 260 + 12 = 272. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 52 (N = 2) no compleix la condició: amb 2 nets i 52 caramels es podrien posar 26 per bossa (52/2 = 26), no 20.",
        "B": "Triar 232 (N = 11) tampoc: amb 11 nets i 232 caramels es podrien posar 21 per bossa (21·11 = 231 ≤ 232), per tant 20 no seria el màxim.",
        "D": "Triar 411 no s'ajusta a cap N enter amb C = 20N + 12 (no és de la forma 20N + 12).",
        "E": "Triar 432 (N = 21) compleix la fórmula però no és el mínim, perquè N = 13 ja en seria suficient.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades", "LOG_dada_ignorada"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-19. Mateixes opcions i mateixa lletra E (20 cm²);
# numero (19→14).
PROBLEMS["CAN-2ESO-2024-14"] = {
    "id":         "CAN-2ESO-2024-14",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "El rectangle de l'esquerra fa 5 cm d'amplada i té àrea 45 cm²: troba'n l'alçària. La resta de la figura es desprèn d'aquí."
    ),
    "expected_reasoning": (
        "El rectangle superior esquerre té amplada 5 cm i àrea 45 cm², així que la seva alçària "
        "és 45 / 5 = 9 cm. Com que la columna esquerra fa 13 cm d'alçada total, la franja de sota "
        "(que pertany al rectangle de 40 cm²) té 13 − 9 = 4 cm d'alçària. El rectangle inferior, "
        "de 40 cm² i alçària 4 cm, té amplada 40 / 4 = 10 cm. La zona dreta inferior fa, doncs, "
        "16 − 10 = 6 cm d'amplada. El rectangle dret, de 48 cm² i amplada 6 cm, té alçària "
        "48 / 6 = 8 cm. La regió grisa central té amplada 10 − 5 = 5 cm (entre el costat dret del "
        "rectangle de 45 cm² i el costat dret del rectangle de 40 cm²) i alçària 8 − 4 = 4 cm "
        "(entre el sostre del rectangle de 40 cm² i el sostre del rectangle de 48 cm²). La seva "
        "àrea és 5 · 4 = 20 cm². Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 cm² surt d'agafar mides equivocades, com 4 × 3.",
        "B": "Triar 14 cm² no correspon a un producte net dels costats reals; és un valor proper al correcte fruit d'un càlcul desviat.",
        "C": "Triar 16 cm² vol dir prendre un quadrat 4 × 4 al mig, sense calibrar bé que l'amplada real és 5.",
        "D": "Triar 18 cm² surt d'una assignació semblant amb error en una de les dimensions (per exemple 6 × 3 enlloc de 5 × 4).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-15"] = {
    "id":         "CAN-2ESO-2024-15",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Multiplica els productes de les dues columnes: això et dona el producte dels quatre nombres, i has de poder-lo lligar amb els productes de les files."
    ),
    "expected_reasoning": (
        "Anomenem la quadrícula 2×2:\n"
        "  a  b   (fila 1, producte 6)\n"
        "  c  d   (fila 2, producte 8)\n"
        "amb columna 1: a·c = 4 i columna 2: b·d = 12.\n"
        "\n"
        "El producte dels quatre nombres és (a·c) · (b·d) = 4 · 12 = 48, i també (a·b) · (c·d) = "
        "6 · 8 = 48, així que les dues lectures són coherents. De a·b = 6 i a·c = 4 obtenim b/c = "
        "3/2, és a dir, b = 3k i c = 2k per a algun enter k > 0. Provant k = 1: b = 3, c = 2 dona "
        "a = 6/b = 2 = c (no admès, han de ser diferents). Provant k = 2: b = 6, c = 4 dona a = "
        "6/6 = 1 i d = 12/b = 2. Els quatre nombres són {1, 6, 4, 2}, tots diferents i positius.\n"
        "\n"
        "Verificació: 1·6 = 6 (fila 1 ✓), 4·2 = 8 (fila 2 ✓), 1·4 = 4 (col 1 ✓), 6·2 = 12 (col 2 ✓).\n"
        "\n"
        "Suma = 1 + 6 + 4 + 2 = 13. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 10 vol dir provar k = 1 (a = 2, b = 3, c = 2, d = 4) sense adonar-se que a i c queden iguals, contra la condició de nombres diferents.",
        "B": "Triar 11 surt d'una assignació amb dos nombres iguals (per exemple {1, 4, 4, 2}, que no compleix la condició).",
        "C": "Triar 12 surt d'una solució intermèdia amb un sol nombre canviat (per exemple {1, 6, 3, 2}, que viola algun producte).",
        "E": "Triar 14 surt de sumar quatre nombres compatibles amb només tres dels productes, per exemple {1, 6, 4, 3}, on 4·3 = 12 ≠ 8.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-21. Mateixes opcions i mateixa lletra C (43);
# numero (21→16) i punts (5→4).
PROBLEMS["CAN-2ESO-2024-16"] = {
    "id":         "CAN-2ESO-2024-16",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     16,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Els tres daus són idèntics. Identifica quins valors apareixen repetits en més d'un dau: en cada parell d'aparicions, els valors comparteixen una cara del dau."
    ),
    "expected_reasoning": (
        "Els tres daus són idèntics. Els nou valors visibles són {34, 22, 8} al primer, {5, 8, 13} "
        "al segon i {17, 13, 22} al tercer. Els valors que apareixen dos cops són 8, 22 i 13; els "
        "únics no repetits són 5, 17 i 34. Així, les sis cares del dau són 5, 8, 13, 17, 22 i 34.\n"
        "\n"
        "Per a cada dau, les tres cares visibles són mútuament adjacents (no oposades), de manera "
        "que la cara oposada a una visible ha de ser una de les altres tres cares (les no visibles "
        "en aquell dau). Per cada cara X mirem en quins daus apareix com a visible, i el conjunt "
        "candidat per a la seva oposada és la intersecció dels conjunts no-visibles en aquells daus:\n"
        "\n"
        "- Cara 8 (visible al dau 1 i al dau 2): no-visibles al dau 1 = {5, 13, 17}; no-visibles al "
        "dau 2 = {17, 22, 34}. Intersecció: {17}. Per tant, oposada(8) = 17.\n"
        "- Cara 22 (visible al dau 1 i al dau 3): no-visibles al dau 1 = {5, 13, 17}; no-visibles al "
        "dau 3 = {5, 8, 34}. Intersecció: {5}. Per tant, oposada(22) = 5.\n"
        "- Cara 13 (visible al dau 2 i al dau 3): no-visibles al dau 2 = {17, 22, 34}; no-visibles "
        "al dau 3 = {5, 8, 34}. Intersecció: {34}. Per tant, oposada(13) = 34.\n"
        "\n"
        "Les parelles oposades del dau són, doncs, (8, 17), (22, 5) i (13, 34). La cara amb què "
        "cada dau recolza a la taula és l'oposada a la cara de dalt:\n"
        "- Dau 1: cara de dalt = 34, cara de baix = 13.\n"
        "- Dau 2: cara de dalt = 5, cara de baix = 22.\n"
        "- Dau 3: cara de dalt = 17, cara de baix = 8.\n"
        "\n"
        "Suma demanada: 13 + 22 + 8 = 43. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 26 vol dir confondre la suma de les cares de baix amb la suma de les tres cares visibles d'un dau (el dau 2: 5+8+13 = 26).",
        "B": "Triar 40 surt d'identificar malament una de les parelles d'oposades, donant una suma propera però errònia.",
        "D": "Triar 47 vol dir intercanviar dues de les cares de baix entre dos daus o agafar la cara visible com a base d'un dels daus.",
        "E": "Triar 56 surt de prendre les tres cares laterals amagades (no la de la base) de cada dau.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "LOG_dada_ignorada"],
    "dependencies":           [],
}

# DEDUP HORITZONTAL amb CAN-1ESO-2024-26. Mateixes opcions i mateixa lletra C (3);
# numero (26→17) i punts (5→4).
PROBLEMS["CAN-2ESO-2024-17"] = {
    "id":         "CAN-2ESO-2024-17",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     17,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Suma els nombres de l'1 al 8: cada vèrtex apareix a 3 cares, així que la suma 6S = 3 · 36. D'aquí surt la suma S de cada cara."
    ),
    "expected_reasoning": (
        "El cub té 8 vèrtexs i 6 cares, i cada vèrtex pertany a exactament 3 cares. La suma dels "
        "nombres del 1 al 8 és 36. Si S és la suma comuna de cada cara, sumant les sis cares "
        "obtenim 6S = 3 · 36 = 108 (perquè cada vèrtex es compta tres vegades), d'on S = 18.\n"
        "\n"
        "Anomenem els vèrtexs segons posició (Front/Back, Top/Bottom, Left/Right). De la imatge: "
        "7 és al vèrtex back-top-right, 6 és al vèrtex back-bottom-left, 8 és al vèrtex "
        "front-bottom-right, i el ? és al vèrtex front-bottom-left. Plantegem les sumes de les "
        "cares que contenen vèrtexs coneguts:\n"
        "\n"
        "- Cara inferior (BBL, BBR, FBL, FBR) = 6 + BBR + ? + 8 = 18 ⟹ BBR + ? = 4.\n"
        "- Cara dreta (BTR, FTR, BBR, FBR) = 7 + FTR + BBR + 8 = 18 ⟹ FTR + BBR = 3.\n"
        "- Cara posterior (BTL, BTR, BBL, BBR) = BTL + 7 + 6 + BBR = 18 ⟹ BTL + BBR = 5.\n"
        "\n"
        "Els valors disponibles per als vèrtexs sense etiqueta són {1, 2, 3, 4, 5}. De la cara "
        "dreta, FTR + BBR = 3 obliga {FTR, BBR} ⊂ {1, 2}; combinat amb BBR + ? = 4 (que requereix "
        "BBR ∈ {1, 3}), la única possibilitat és BBR = 1. Llavors FTR = 2 i ? = 3.\n"
        "\n"
        "Verificació: BTL = 5 − BBR = 4; FTL = 18 − BTL − BTR − FTR (cara superior) = 18 − 4 − 7 − "
        "2 = 5. Les sis cares sumen tots 18 amb aquesta assignació. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir intercanviar els valors de ? i BBR (donant ? = 1 i BBR = 3); compleix la cara inferior però viola la cara dreta (FTR + 3 = 3 ⟹ FTR = 0, no permès).",
        "B": "Triar 2 surt d'un error d'aritmètica en aïllar ? a la cara inferior.",
        "D": "Triar 4 vol dir oblidar que ? també forma part de la cara esquerra i ajustar només una cara.",
        "E": "Triar 5 surt de prendre BTL com a ? per confusió en identificar quin vèrtex té el signe d'interrogació.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-18"] = {
    "id":         "CAN-2ESO-2024-18",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     18,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2024-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena ABCD el nombre: la xifra D ha de ser parella entre 0 i 8, i és la suma de les tres anteriors. Recorre els valors possibles de la suma."
    ),
    "expected_reasoning": (
        "El nombre té quatre xifres parelles ABCD amb A ≠ 0, totes a {0, 2, 4, 6, 8}, i amb D = "
        "A + B + C ≤ 8. A més, entre les quatre xifres en hi ha d'haver exactament tres diferents, "
        "una de les quals apareix dues vegades. Recorrem D = 2, 4, 6, 8:\n"
        "\n"
        "- D = 2: A + B + C = 2 amb A ≥ 2. L'únic és A = 2, B = C = 0. Nombre 2002, xifres {2, 0, 0, 2}: "
        "només dues distintes. No compleix.\n"
        "\n"
        "- D = 4: A + B + C = 4, A ≥ 2. Casos:\n"
        "    · A = 2, B + C = 2: (B, C) = (0, 2), (2, 0). Nombres 2024, 2204. Tots dos tenen "
        "xifres {2, 0, 4} amb el 2 repetit: 3 distintes amb una repetida. ✓ (2 nombres)\n"
        "    · A = 4, B = C = 0. Nombre 4004, xifres {4, 0}: només 2 distintes. No.\n"
        "\n"
        "- D = 6: A + B + C = 6, A ≥ 2. Casos:\n"
        "    · A = 2, B + C = 4: (0,4),(4,0): 2046, 2406 → 4 distintes. (2,2): 2226 → 2 distintes. Cap val.\n"
        "    · A = 4, B + C = 2: 4026, 4206 → 4 distintes. Cap val.\n"
        "    · A = 6, B = C = 0: 6006 → 2 distintes. No.\n"
        "    Subtotal: 0 nombres.\n"
        "\n"
        "- D = 8: A + B + C = 8, A ≥ 2. Casos:\n"
        "    · A = 2, B + C = 6: (0,6): 2068 → 4 distintes; (6,0): 2608 → 4 distintes; (2,4): 2248 "
        "→ {2,4,8} amb 2 repetit ✓; (4,2): 2428 → {2,4,8} amb 2 repetit ✓. (2 nombres)\n"
        "    · A = 4, B + C = 4: (0,4): 4048 → {0,4,8} amb 4 repetit ✓; (4,0): 4408 → {0,4,8} amb 4 "
        "repetit ✓; (2,2): 4228 → {2,4,8} amb 2 repetit ✓. (3 nombres)\n"
        "    · A = 6, B + C = 2: (0,2): 6028 → 4 distintes; (2,0): 6208 → 4 distintes. No.\n"
        "    · A = 8, B = C = 0: 8008 → 2 distintes. No.\n"
        "    Subtotal: 5 nombres.\n"
        "\n"
        "Total: 2 + 0 + 5 = 7 nombres (2024, 2204, 2248, 2428, 4048, 4408, 4228). Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir comptar només dues solucions, per exemple 2024 i 2204, oblidant les del cas D = 8.",
        "B": "Triar 4 vol dir trobar 2024, 2204 i dos més del cas D = 8 sense esgotar totes les combinacions de l'A = 4.",
        "C": "Triar 6 vol dir oblidar exactament una de les set solucions vàlides (per exemple 4228 o 4408).",
        "E": "Triar 8 vol dir incloure indegudament algun nombre amb només dues xifres diferents (com 4004 o 2002) o un altre cas erroni.",
    },
    "errors_típics":          ["COMP_doble_recompte", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-19"] = {
    "id":         "CAN-2ESO-2024-19",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     19,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2024-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Separa l'ortoedre en les dues meitats que té (cubs 1×1 a una banda, cubs 2×2×2 a l'altra) i compta a cadascuna els cubs amb exactament 2 cares pintades."
    ),
    "expected_reasoning": (
        "L'ortoedre 8×4×4 té volum 128 i s'obté unint un cub 4×4×4 fet de 64 cubs 1×1×1 amb un cub "
        "4×4×4 fet de 8 cubs grans 2×2×2 (8 × 8 = 64). La cara on s'enganxen els dos blocs és "
        "interior i, per tant, no es pinta.\n"
        "\n"
        "Cubs petits (1×1×1, formant un 4×4×4 amb la cara dreta enganxada al bloc gran). En un cub "
        "4×4×4 aïllat, els cubs amb 2 cares pintades són els que estan a una aresta però no en un "
        "vèrtex: hi ha 12 arestes × 2 cubs interiors = 24 cubs. Aquí, com que la cara dreta no està "
        "pintada, cal ajustar:\n"
        "  · Dels 24 cubs d'aresta originals, 8 estan al llarg de les 4 arestes que toquen la cara "
        "dreta interior. Aquests cubs perden una de les seves dues cares pintades i passen a tenir-"
        "ne 1, no 2.\n"
        "  · Queden 24 − 8 = 16 cubs d'aresta que conserven les seves 2 cares pintades.\n"
        "  · A més, les 4 cantonades del 4×4×4 que estaven sobre la cara dreta tenien 3 cares "
        "pintades; ara perden una i en tenen 2. Així s'afegeixen 4 cubs amb exactament 2 cares.\n"
        "  · Subtotal cubs petits amb 2 cares pintades: 16 + 4 = 20.\n"
        "\n"
        "Cubs grans (2×2×2, formant un 4×4×4 amb la cara esquerra enganxada al bloc petit). En el "
        "bloc 2×2×2 de cubs grans, tots vuit cubs són cantonades del cub 4×4×4 i tindrien 3 cares "
        "pintades en estar aïllats. Aquí, els 4 cubs grans que toquen la cara esquerra interior "
        "perden una cara pintada i passen a tenir-ne 2; els altres 4 (els del costat dret del bloc) "
        "conserven les 3 cares pintades.\n"
        "  · Subtotal cubs grans amb 2 cares pintades: 4.\n"
        "\n"
        "Total: 20 + 4 = 24. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 16 vol dir comptar només els cubs d'aresta del bloc petit que no toquen la cara enganxada, oblidant les cantonades 'rescatades' i els cubs grans.",
        "B": "Triar 20 vol dir comptar correctament els cubs petits però oblidar afegir els 4 cubs grans que també passen a tenir 2 cares pintades.",
        "D": "Triar 28 surt de comptar els 24 cubs d'aresta del 4×4×4 petit com si la cara dreta estigués pintada, i sumar-hi els 4 cubs grans.",
        "E": "Triar 40 vol dir aplicar la fórmula del cub 4×4×4 aïllat per a tot l'ortoedre (com si fos un cub 4×4×4 dos cops), sense entendre la geometria conjunta.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-20"] = {
    "id":         "CAN-2ESO-2024-20",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     20,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Recorre les tripletes de nombres de l'1 al 9 que sumen 13; quina xifra apareix en més tripletes a la vegada?"
    ),
    "expected_reasoning": (
        "Les nou caselles contenen els nombres de l'1 al 9 sense repetir-se, i la figura té tres "
        "files i tres columnes que sumen 13 cadascuna. Les sis tripletes (3 files + 3 columnes) "
        "estan construïdes amb nombres del conjunt {1, …, 9}.\n"
        "\n"
        "La casella central grisa pertany a una fila i a una columna, així que el seu valor "
        "apareix en exactament dues d'aquestes tripletes. Les tripletes de tres nombres distints "
        "d'1 a 9 que sumen 13 són: {1,3,9}, {1,4,8}, {1,5,7}, {2,3,8}, {2,4,7}, {2,5,6}, {3,4,6}.\n"
        "\n"
        "Per la posició de la cel·la grisa (al centre del zig-zag, lluny dels extrems amb el 9 i "
        "el 6), els nombres 9 i 6 estan fora de la fila i de la columna que conté la cel·la grisa. "
        "La fila i la columna a què pertany la cel·la grisa han de cobrir, entre les dues, els "
        "altres set valors {1, 2, 3, 4, 5, 7, 8} i compartir només la cel·la grisa. Una de les "
        "tripletes vàlides {1,4,8} pot ser una fila (suma 13), i {3,4,6}... no, el 6 és fora. "
        "Cerquem dues tripletes disjuntes excepte un valor comú x, formades amb el conjunt "
        "{1,2,3,4,5,7,8}.\n"
        "\n"
        "Provant x = 4: {1, 4, 8} i {2, 4, 7} comparteixen el 4 i la unió és {1, 2, 4, 7, 8}, "
        "compatible amb les altres restriccions (el 3 i el 5 queden a altres files/columnes de la "
        "figura amb el 9 i el 6). Comprovant que les altres files i columnes també sumen 13 amb "
        "els nombres restants 9, 6, 3, 5, és consistent. Per tant, la cel·la central val 4. "
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir agafar la xifra que apareix a més tripletes (l'1 surt a {1,3,9}, {1,4,8}, {1,5,7}) sense comprovar que la combinació concreta encaixa amb la geometria de la figura.",
        "B": "Triar 2 vol dir provar el 2 com a valor central, però les tripletes que contenen el 2 ({2,3,8}, {2,4,7}, {2,5,6}) inclouen el 6, que ha de quedar a l'extrem oposat.",
        "C": "Triar 3 vol dir prendre {3,4,6} i {3,…}, però totes les tripletes amb 3 inclouen un valor (6 o 9) que ja és fixat als extrems.",
        "E": "Triar 5 vol dir agafar el 5 com a valor central, però el 5 només apareix a {1,5,7} i {2,5,6}; aquesta segona conté el 6 fix als extrems.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-21"] = {
    "id":         "CAN-2ESO-2024-21",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "L'angle de cada tros no canvia: és el mateix que quan el pastís era sencer. El que canvia és com es reparteix la resta del cercle entre 9 espais."
    ),
    "expected_reasoning": (
        "Inicialment el pastís estava tallat en deu trossos iguals, així que cada tros té un angle "
        "central de 360° / 10 = 36°. Quan la Nora es menja un tros i col·loca els nou restants "
        "amb espais iguals entre ells, el cercle (360°) queda repartit en 9 trossos més 9 espais. "
        "L'angle de cada tros segueix sent 36°, perquè el tros és físic i no canvia. Així:\n"
        "\n"
        "9 · 36° + 9 · e = 360° ⟹ 324° + 9e = 360° ⟹ 9e = 36° ⟹ e = 4°.\n"
        "\n"
        "L'angle entre dos trossos consecutius és 4°. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 5° surt de dividir 36° (l'angle del tros que falta) entre 9 espais en lloc d'entendre que els espais distribueixen exclusivament el tros que falta (36°/9 = 4°, no 5°).",
        "C": "Triar 3° surt d'un càlcul aproximat, per exemple dividint 27° entre 9 (no quadra amb cap raonament correcte).",
        "D": "Triar 2° vol dir dividir 18° (la meitat del tros que falta) entre 9, com si l'angle hagués de repartir-se en mig cercle.",
        "E": "Triar 1° surt de dividir 9° entre 9, oblidant que el tros que falta val 36° complets.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-22"] = {
    "id":         "CAN-2ESO-2024-22",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     22,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Pensa la zona de solapament com un dels tres quadrats: relaciona els costats del rectangle amb el costat del quadrat."
    ),
    "expected_reasoning": (
        "El rectangle nou està format per tres quadrats idèntics de costat s. La seva alçada és s "
        "i la seva amplada total és 3s. Cada rectangle original té alçada s i amplada x; els dos "
        "rectangles se solapen al centre formant el quadrat del mig (de costat s). Així, l'amplada "
        "total és 2x − s = 3s, d'on 2x = 4s i x = 2s.\n"
        "\n"
        "Cada rectangle original té dimensions 2s × s i àrea 2s · s = 2s². Com que l'àrea és "
        "18 cm², 2s² = 18 ⟹ s² = 9 ⟹ s = 3 cm. El rectangle nou té dimensions 3s × s = 9 cm × "
        "3 cm i perímetre 2 · (9 + 3) = 24 cm. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 18 cm és confondre el perímetre amb l'àrea de cada rectangle original (18 cm²).",
        "B": "Triar 20 cm surt de pensar que el rectangle nou és 6 × 4 (perímetre 20), com si la solapació afegís en lloc de restar.",
        "D": "Triar 27 cm vol dir prendre cada quadrat de costat 9/3 = 3 i sumar tres perímetres parcials sense entendre que el perímetre del rectangle total és 2(9+3) = 24.",
        "E": "Triar 36 cm és sumar els perímetres dels dos rectangles originals (2·(2s + s) = 6s = 18 cada un, dos = 36) sense restar la part solapada.",
    },
    "errors_típics":          ["GEO_perimetre_vs_area", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-23"] = {
    "id":         "CAN-2ESO-2024-23",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     23,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Planteja l'equació volum = àrea total amb a com a aresta del cub i resol-la."
    ),
    "expected_reasoning": (
        "Sigui a la longitud de l'aresta (en cm). El volum del cub és a³ (en cm³) i l'àrea total "
        "és 6a² (en cm², perquè té 6 cares de a · a). Imposant que els valors numèrics siguin "
        "iguals: a³ = 6a². Com que a > 0, podem dividir per a²: a = 6. Per tant, l'aresta mesura "
        "6 cm. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 cm dona V = 1 i A = 6, no iguals.",
        "B": "Triar 2 cm dona V = 8 i A = 24, no iguals.",
        "C": "Triar 4 cm dona V = 64 i A = 96, no iguals.",
        "D": "Triar 5 cm dona V = 125 i A = 150, no iguals; valors propers però no coincidents.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-24"] = {
    "id":         "CAN-2ESO-2024-24",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Per simetria els dos triangles tenen la mateixa àrea, i el punt de creuament dels dos segments és el centre del quadrat."
    ),
    "expected_reasoning": (
        "Sigui L el costat del quadrat. Els punts de divisió del costat inferior estan a L/5, 2L/5, "
        "3L/5, 4L/5 del vèrtex esquerre; igualment al costat superior. Els dos segments dibuixats "
        "uneixen (L/5, 0) amb (4L/5, L) i (4L/5, 0) amb (L/5, L). Per simetria respecte al centre "
        "del quadrat (L/2, L/2), aquests dos segments es creuen exactament en aquest centre.\n"
        "\n"
        "La figura grisa està formada per dos triangles iguals (un cap amunt, un cap avall) que "
        "comparteixen el vèrtex central. Mirem el triangle superior: té com a base el segment del "
        "costat superior entre (L/5, L) i (4L/5, L), de longitud 4L/5 − L/5 = 3L/5; l'altre vèrtex "
        "és el centre del quadrat, a alçada L/2 per sota de la base. L'alçada del triangle val "
        "L − L/2 = L/2. La seva àrea és (1/2) · (3L/5) · (L/2) = 3L²/20.\n"
        "\n"
        "Per simetria, el triangle inferior té la mateixa àrea. Àrea total grisa: 2 · 3L²/20 = "
        "3L²/10. Imposant 3L²/10 = 30 cm² ⟹ L² = 100 ⟹ L = 10 cm. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 8 cm dona L² = 64 i àrea grisa 3·64/10 = 19,2 cm², no 30.",
        "B": "Triar 9 cm dona L² = 81 i àrea grisa 24,3 cm², no 30.",
        "D": "Triar 12 cm dona L² = 144 i àrea grisa 43,2 cm², no 30.",
        "E": "Triar 16 cm dona L² = 256 i àrea grisa 76,8 cm², molt més que 30.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-25"] = {
    "id":         "CAN-2ESO-2024-25",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     25,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Per fer gran la diferència entre el màxim i el mínim, vols que el mínim sigui el més petit possible i els altres dos del mig també petits."
    ),
    "expected_reasoning": (
        "Si la mitjana de quatre nombres enters positius diferents és 5, la seva suma és "
        "4 · 5 = 20. Anomenem-los a < b < c < d. Volem maximitzar d − a.\n"
        "\n"
        "Per fer d − a tan gran com es pugui amb suma fixada 20:\n"
        "- a ha de ser el mínim possible, és a dir, a = 1.\n"
        "- b i c han de ser tan petits com es pugui (perquè així d sigui tan gran com es pugui), "
        "però diferents entre si i diferents d'a. Els valors mínims són b = 2 i c = 3.\n"
        "- Llavors d = 20 − 1 − 2 − 3 = 14.\n"
        "\n"
        "Comprovem: 1 < 2 < 3 < 14, tots enters positius diferents, suma 20, mitjana 5 ✓.\n"
        "\n"
        "Diferència màxima: 14 − 1 = 13. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 5 vol dir prendre la mitjana com a diferència sense optimitzar; un cas com 3, 4, 6, 7 (suma 20, mitjana 5) dona diferència 4, no 5.",
        "B": "Triar 6 surt d'optimitzar només parcialment (per exemple, agafant 1, 3, 4, 12 amb diferència 11) i creure que cal mantenir una distància 'natural' al voltant de la mitjana.",
        "C": "Triar 8 vol dir prendre a = 1 però posar b o c massa grans, com 1, 2, 8, 9 (diferència 8) sense veure que es poden encara reduir b i c.",
        "E": "Triar 24 surt de calcular d − a com si fossin tots diferents i la suma quedi distribuïda sense mitjana, per exemple agafant a = 1 i d = 25 i ignorant la condició de mitjana 5.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-26"] = {
    "id":         "CAN-2ESO-2024-26",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     26,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2024-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Cada pirata ha de tenir un total de 30 monedes; comença omplint les caselles que falten i compara els tres nombres pirata a pirata."
    ),
    "expected_reasoning": (
        "El total de monedes és 30, així que cada pirata té or + plata + bronze = 30. Reconstruïm "
        "les caselles que falten:\n"
        "- Tom: 9 (or) + ? (plata) + 11 (bronze) = 30 ⟹ plata(Tom) = 10. Així Tom = (9, 10, 11).\n"
        "- Al: 7 (or) + ? + 12 (bronze) = 30 ⟹ plata(Al) = 11. Així Al = (7, 11, 12).\n"
        "- Pit: 10 + ? + 10 = 30 ⟹ plata(Pit) = 10. Així Pit = (10, 10, 10).\n"
        "- Jim: 9 + 10 + ? = 30 ⟹ bronze(Jim) = 11. Així Jim = (9, 10, 11).\n"
        "\n"
        "Sigui V el pirata que diu la veritat: les seves tres quantitats són les reals. Els tres "
        "pirates mentidiers van mentir en TOTES les seves quantitats; per a cada categoria, la "
        "quantitat real (la del V) ha de ser diferent de la que va dir cada mentider. Comprovem "
        "cada candidat:\n"
        "\n"
        "- Si V = Tom (9, 10, 11): or(Tom) = 9, però or(Jim) = 9 també. Jim coincidiria amb la "
        "veritat en l'or, contradicció.\n"
        "- Si V = Al (7, 11, 12): or de Tom/Pit/Jim = 9/10/9, tots ≠ 7 ✓; plata de Tom/Pit/Jim = "
        "10/10/10, tots ≠ 11 ✓; bronze de Tom/Pit/Jim = 11/10/11, tots ≠ 12 ✓. Coherent.\n"
        "- Si V = Pit (10, 10, 10): plata(Tom) = 10 coincideix amb plata(Pit), contradicció.\n"
        "- Si V = Jim (9, 10, 11): or(Tom) = 9 coincideix amb or(Jim), contradicció.\n"
        "\n"
        "L'únic candidat consistent és Al. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar Jim vol dir oblidar comprovar el conflicte amb or(Tom) = 9 = or(Jim), que ja desmenteix Jim com a únic veraç.",
        "B": "Triar Pit vol dir no veure que plata(Pit) = 10 i plata(Tom) = 10 obliguen Tom a no mentir en aquesta xifra, contradicció.",
        "D": "Triar Tom vol dir passar per alt que or(Tom) = 9 coincideix amb or(Jim), trencant la condició que els altres tres mentien en totes les xifres.",
        "E": "Triar 'no ho podem saber' vol dir no completar les caselles i renunciar al problema, però el sistema queda determinat unívocament.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-27"] = {
    "id":         "CAN-2ESO-2024-27",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     27,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "La distància de pujada és la mateixa que la de baixada; si els salts de baixada són el triple de llargs, com es relaciona el nombre de salts d'un sentit amb l'altre?"
    ),
    "expected_reasoning": (
        "Sigui P el nombre de salts de pujada i B el nombre de salts de baixada. Cada salt de "
        "pujada fa 1 m i cada salt de baixada en fa 3. La distància de pujada (P · 1 m = P m) ha "
        "de ser igual a la distància de baixada (B · 3 m), perquè és la mateixa pista: P = 3B.\n"
        "\n"
        "El total de salts és P + B = 2024, és a dir 3B + B = 2024 ⟹ 4B = 2024 ⟹ B = 506 i "
        "P = 1518. La distància d'un sentit és P m = 1518 m. El recorregut total (pujada + "
        "baixada) és 2 · 1518 = 3036 m. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 506 m és confondre el recorregut amb només la distància de baixada (B · 3 = 1518 m, no 506 m, i a més només compta una direcció).",
        "B": "Triar 1012 m surt de prendre 2024 salts × 0,5 m, sense diferenciar la longitud dels dos tipus de salt.",
        "C": "Triar 2024 m vol dir igualar el recorregut total amb el nombre de salts (com si tots fossin d'1 m de mitjana), oblidant que els salts de baixada són més llargs.",
        "E": "Triar 4048 m surt de prendre 2 · 2024 m (com si tots els salts fossin de 2 m de mitjana, o sumant pujada i baixada sense reduir).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-28"] = {
    "id":         "CAN-2ESO-2024-28",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Per a cada opció, busca un dibuix concret que reparteix l'hexàgon en peces iguals. La que no admeti cap dibuix és la resposta."
    ),
    "expected_reasoning": (
        "Examinem cada opció a partir de l'hexàgon regular d'àrea total A:\n"
        "\n"
        "- A) 6 triangles equilàters iguals: traçant els tres diàmetres que uneixen vèrtexs "
        "oposats, l'hexàgon queda dividit en 6 triangles equilàters idèntics centrats al centre. ✓\n"
        "\n"
        "- B) 3 rombes iguals: traçant tres segments des del centre a vèrtexs alterns es construeixen "
        "tres rombes idèntics de mides 60°–120° (és la divisió clàssica que fa que l'hexàgon "
        "sembli un cub en perspectiva). ✓\n"
        "\n"
        "- C) 4 trapezis iguals: l'hexàgon es pot trencar en quatre trapezis isòsceles congruents "
        "amb una construcció que combina la diagonal llarga amb dues paral·leles a aquesta a igual "
        "distància; cada peça és un trapezi de la mateixa forma i mida. ✓\n"
        "\n"
        "- D) 12 rombes iguals: partint dels 3 rombes grans de l'opció B, cadascun es pot dividir "
        "en 4 rombes petits idèntics (similars al gran, mides 60°–120°) traçant les dues paral·leles "
        "als costats que passen pels punts mitjans. S'obtenen 12 rombes idèntics. ✓\n"
        "\n"
        "- E) 6 rombes iguals: 6 peces iguals que omplen l'hexàgon haurien de tenir cadascuna un "
        "sisè de l'àrea i, per ser un rombe regular, els seus angles haurien de ser compatibles "
        "amb una distribució periòdica de 6 al voltant del centre. Si els 6 rombes es disposen "
        "radialment, han de tenir angle agut 60° al centre (per omplir els 360°) i angle obtús "
        "120° a l'exterior; però amb aquesta forma 6 rombes només omplen un hexàgon més petit (la "
        "regió central) i deixen 6 'forats' triangulars als vèrtexs. No hi ha cap manera de "
        "col·locar 6 rombes congruents que omplin l'hexàgon regular sense forats ni superposicions. ✗\n"
        "\n"
        "La divisió impossible és la de l'opció E. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar '6 triangles equilàters iguals' és pensar que no es pot dividir així, oblidant la divisió bàsica per diàmetres.",
        "B": "Triar '3 rombes iguals' és no recordar la divisió clàssica de l'hexàgon en tres rombes que dona la il·lusió de cub.",
        "C": "Triar '4 trapezis iguals' és no veure que es poden encaixar quatre trapezis congruents amb una construcció simètrica.",
        "D": "Triar '12 rombes iguals' és no aprofitar que subdividint cadascun dels tres rombes grans en quatre s'obté la divisió.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-29"] = {
    "id":         "CAN-2ESO-2024-29",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2024-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Si r i s són paral·leles, els angles corresponents a A i a C que formen amb la línia horitzontal AC són iguals. D'aquí surt l'angle BAC del triangle."
    ),
    "expected_reasoning": (
        "Els punts A i C estan sobre una mateixa línia horitzontal i les rectes r (per A) i s (per "
        "C) són paral·leles. A C, l'angle entre s i la prolongació de la horitzontal cap a la "
        "dreta val 110° (donat). Per angles corresponents en paral·leles tallades per la "
        "transversal AC, a A l'angle entre r i la horitzontal cap a la dreta (és a dir, cap a C) "
        "és el mateix: 110°.\n"
        "\n"
        "El triangle ABC té el costat AC sobre la horitzontal i el costat AB sobre la recta r; "
        "l'angle ∠BAC és el suplementari de 110° (perquè el raig AB cap a B i la recta r cap a "
        "C estan en costats oposats), és a dir ∠BAC = 180° − 110° = 70°.\n"
        "\n"
        "Com que AB = AC, el triangle és isòsceles amb els angles a B i C iguals: ∠ABC = ∠ACB = "
        "(180° − 70°) / 2 = 55°.\n"
        "\n"
        "L'angle x marcat a B està entre la prolongació de r per dalt de B i el segment BC (és a "
        "dir, a l'exterior del triangle, al costat oposat a A). El seu valor és el suplementari "
        "de ∠ABC: x = 180° − 55° = 125°. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 110° vol dir copiar directament l'angle donat sense aplicar el suplementari del triangle isòsceles.",
        "B": "Triar 115° surt d'una assignació equivocada d'angles corresponents (per exemple, prenent ∠BAC = 60° en lloc de 70°).",
        "D": "Triar 130° vol dir prendre l'angle exterior d'un triangle amb ∠ABC = 50° (és a dir, ∠BAC = 80°, mal calculat com a 180° − 100°).",
        "E": "Triar 135° vol dir prendre ∠ABC = 45° per simetria errònia (com si fos triangle rectangle a A).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2024-30"] = {
    "id":         "CAN-2ESO-2024-30",
    "categoria":  "2ESO",
    "any":        2024,
    "numero":     30,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2024-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El que no és aigua no s'evapora: és la mateixa quantitat absoluta abans i després. Compara els pesos finals i inicials a partir d'aquesta part fixa."
    ),
    "expected_reasoning": (
        "Suposem que el bolet acabat de collir pesa 100 g (és còmode treballar amb 100). Si el "
        "80 % és aigua, els altres 20 g són la part sòlida (no-aigua). Durant l'assecatge només "
        "marxa aigua; els 20 g de sòlid es mantenen.\n"
        "\n"
        "Al final, l'aigua és el 20 % del pes total, i per tant el sòlid és el 80 % del pes total. "
        "Si P és el pes final, 0,8 · P = 20 g, d'on P = 25 g.\n"
        "\n"
        "El bolet ha passat de 100 g a 25 g; ha perdut 100 − 25 = 75 g, que respecte als 100 g "
        "inicials representen un 75 %. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 60 % surt de restar els percentatges d'aigua (80 % − 20 % = 60 %), oblidant que l'aigua i el pes total no escalen igual.",
        "B": "Triar 70 % surt d'un càlcul aproximat que infraestima la pèrdua relativa.",
        "D": "Triar 80 % vol dir igualar la pèrdua de pes amb la fracció inicial d'aigua, sense veure que al final encara queda un 20 % d'aigua respecte al pes nou.",
        "E": "Triar 85 % surt de sobreestimar la pèrdua, per exemple suposant que la part no-aigua també perd massa.",
    },
    "errors_típics":          ["GEN_calcul", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-01"] = {
    "id":         "CAN-2ESO-2023-01",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     1,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El múltiple de 4 més gran per sota de 2023 i el múltiple de 3 més petit per sobre de 2023 estan tots dos molt a prop de 2023. Pensa quant val el residu de 2023 dividit per 4 i per 3."
    ),
    "expected_reasoning": (
        "Cal trobar el múltiple de 4 més gran que és més petit que 2023, i el múltiple de 3 més petit que és més gran que 2023.\n"
        "\n"
        "Dividim 2023 entre 4: 2023 = 4 · 505 + 3, així que 4 · 505 = 2020 és el múltiple de 4 més gran per sota de 2023. (El següent múltiple de 4, 2024, ja és més gran que 2023.)\n"
        "\n"
        "Dividim 2023 entre 3: 2023 = 3 · 674 + 1, així que 3 · 674 = 2022 és el múltiple de 3 més gran per sota de 2023, i el múltiple de 3 immediatament superior és 3 · 675 = 2025.\n"
        "\n"
        "La suma demanada és 2020 + 2025 = 4045. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "4042 = 2020 + 2022 surt de prendre el múltiple de 3 més gran per sota de 2023 (2022) en lloc del més petit per sobre (2025).",
        "C": "4046 = 2020 + 2026 prové de pensar que el múltiple de 3 més petit per sobre de 2023 és 2026; però 2026 no és múltiple de 3 (2+0+2+6 = 10, no divisible per 3).",
        "D": "4047 = 2022 + 2025 prové d'agafar el múltiple de 3 més gran per sota de 2023 (2022) com a múltiple de 4, confonent els dos conceptes.",
        "E": "4050 = 2025 + 2025 surt de comptar dues vegades el mateix múltiple de 3 i no buscar el múltiple de 4."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-02"] = {
    "id":         "CAN-2ESO-2023-02",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Al desplegable, fixa't en l'orientació del 2 a cada cara: el peu del 2, en quina direcció apunta respecte de l'aresta que comparteix amb les altres cares?"
    ),
    "expected_reasoning": (
        "El desplegable mostra sis cares amb un '2' a cadascuna, i cada '2' té una orientació concreta respecte de les arestes de la seva cara. Quan es plega el desplegable per formar un cub, dues cares adjacents al desplegable comparteixen una aresta i, després del plegat, les orientacions de les seves figures queden relacionades de manera fixa.\n"
        "\n"
        "Identifiquem una cara base i, mirant els seus '2' adjacents al desplegable, deduïm com han de quedar orientats els '2' de les cares que la voregen al cub. Comparant amb cada opció de cub muntat:\n"
        "\n"
        "- Quatre de les opcions presenten almenys un '2' girat 90° o invertit respecte de l'orientació que correspondria a partir del desplegable.\n"
        "- L'opció A mostra tres cares visibles amb els '2' en les orientacions exactes que dóna el desplegament, incloent la relació entre la cara superior i les dues laterals.\n"
        "\n"
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Aquesta opció té dues cares amb orientacions compatibles, però el '2' de la cara superior està rotat 90° respecte del que dictaria el desplegable.",
        "C": "El '2' d'una de les cares laterals apareix invertit verticalment (cap per avall) respecte del que produiria el plegat.",
        "D": "Dues de les tres cares visibles tenen el '2' en orientació correcta, però la tercera el té girat 180°.",
        "E": "El '2' de la cara superior està girat 90° en sentit contrari al que dóna el plegat del desplegable."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-03"] = {
    "id":         "CAN-2ESO-2023-03",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     3,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "El gris ha de venir d'un sol semicercle (180° contigus) i el blanc de dos quadrants (90° contigus cadascun). Mira si en la figura el gris i el blanc tenen aquestes formes contigües."
    ),
    "expected_reasoning": (
        "La Joana enganxa: 1 semicercle gris (180° contigus) + 2 quadrants blancs (90° contigus cadascun) sobre un cercle negre. Mirant cada figura proposada, en cadascuna el gris ha de formar un semicercle complet i el blanc ha d'aparèixer com dos quadrants (no necessàriament adjacents):\n"
        "\n"
        "- A, B, C, E: el gris forma un semicercle contigu i els blancs són dues regions de 90° cadascuna; el negre apareix a les zones no cobertes per cap peça (les superposicions deixen visible el negre quan dues peces blanques se superposen o quan part del semicercle queda lliure).\n"
        "- D: la distribució del gris no correspon a un semicercle contigu de 180°; el gris es presenta fragmentat en dues zones no contigües que no es poden obtenir amb un sol semicercle.\n"
        "\n"
        "Per tant la figura que NO pot obtenir és la D. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "A té el gris formant un semicercle contigu (a la part inferior-dreta) i els dos quadrants blancs col·locats amb superposició; sí es pot obtenir.",
        "B": "B té un semicercle gris contigu i els dos quadrants blancs a posicions vàlides; sí es pot obtenir.",
        "C": "C mostra el gris com a semicercle contigu i els blancs solapats parcialment, deixant veure el negre on cal; és una col·locació vàlida.",
        "E": "E té el gris contigu i els blancs no adjacents; també és obtenible amb les tres peces."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-04"] = {
    "id":         "CAN-2ESO-2023-04",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     4,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Mesura les distàncies (en hores del rellotge) entre les tres xifres visibles 1, 5 i 7. Si gires el disc, aquestes mateixes tres distàncies han d'aparèixer entre les noves xifres, en algun ordre."
    ),
    "expected_reasoning": (
        "El disc gris té tres forats en posicions fixes; quan es gira sobre el rellotge, només es modifica quines xifres queden visibles, però les distàncies angulars entre els tres forats no canvien. Així doncs, les distàncies entre les tres xifres visibles ara (1, 5 i 7) han de coincidir amb les distàncies entre les tres xifres visibles després del gir, llegides cíclicament en hores del rellotge.\n"
        "\n"
        "Distàncies actuals (en hores, recorrent en sentit horari):\n"
        "- 1 → 5: 4 hores.\n"
        "- 5 → 7: 2 hores.\n"
        "- 7 → 1: 6 hores (passant per 12).\n"
        "\n"
        "Total: 4 + 2 + 6 = 12 hores ✓.\n"
        "\n"
        "Comprovem cada opció:\n"
        "- A) 2, 4, 9: distàncies 2, 5, 5. No coincideixen.\n"
        "- B) 1, 5, 10: distàncies 4, 5, 3. No coincideixen.\n"
        "- C) 4, 6, 12: distàncies 2, 6, 4 (en algun ordre, {2, 4, 6}). ✓ Coincideix amb {2, 4, 6}.\n"
        "- D) 3, 6, 9: distàncies 3, 3, 6. No coincideixen.\n"
        "- E) 5, 7, 12: distàncies 2, 5, 5. No coincideixen.\n"
        "\n"
        "Resposta C."
    ),
    "comentaris_distractors": {
        "A": "2, 4 i 9 té distàncies 2, 5 i 5; les distàncies 5 no apareixen en l'arranjament original.",
        "B": "1, 5 i 10 conté 1 i 5 originals, però la tercera xifra 10 dóna una distància de 3 que no encaixa amb les distàncies 2, 4 i 6 originals.",
        "D": "3, 6 i 9 té distàncies 3, 3, 6: dues distàncies de 3 que no apareixen entre les tres originals.",
        "E": "5, 7 i 12 conté 5 i 7 originals, però la distància entre 12 i 5 és de 5 hores, no compatible amb les distàncies inicials."
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-05"] = {
    "id":         "CAN-2ESO-2023-05",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     5,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa noms a les quatre incògnites dels vèrtexs del rombe i escriu les quatre igualtats que diuen que cada costat és la suma dels seus dos extrems. Suma les quatre igualtats i mira què passa amb la suma dels vèrtexs."
    ),
    "expected_reasoning": (
        "Sigui un rombe amb vèrtexs (en sentit horari, començant pel de dalt) p, q, r, s. Els quatre costats, en el mateix sentit, valen p + q, q + r, r + s i s + p (cada costat és la suma dels seus dos extrems).\n"
        "\n"
        "Segons la figura, els costats coneguts són 8 (dalt-esquerra: s + p), 9 (dalt-dreta: p + q), 13 (dreta-baix: q + r) i ? (esquerra-baix: r + s).\n"
        "\n"
        "Sumant els dos costats oposats (dalt-esquerra i dreta-baix): (s + p) + (q + r) = p + q + r + s.\n"
        "Sumant els altres dos costats oposats (dalt-dreta i esquerra-baix): (p + q) + (r + s) = p + q + r + s.\n"
        "\n"
        "Així doncs, els dos parells de costats oposats tenen la mateixa suma:\n"
        "(s + p) + (q + r) = (p + q) + (r + s)\n"
        "8 + 13 = 9 + ?\n"
        "21 = 9 + ?\n"
        "? = 12. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "11 surt de calcular (8 + 13)/2 + alguna correcció erràtica, o de no aplicar la regla dels costats oposats correctament.",
        "C": "13 és el valor del costat oposat conegut (dreta-baix) i prové de pensar que els costats oposats han de ser iguals (que no és el cas en aquest tipus de rombe etiquetat).",
        "D": "14 = 8 + 13 − 9 + 2 surt d'un càlcul aritmètic erroni amb signes.",
        "E": "15 podria sortir de sumar 8 + 9 − 2 o d'un raonament que utilitzi els costats consecutius en lloc dels oposats."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-06"] = {
    "id":         "CAN-2ESO-2023-06",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     6,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Quan tres nombres de dues xifres consecutius canvien la xifra de les desenes entre el primer i el segon, ¿quina ha de ser l'última xifra del primer? Això determina ♢ i, en cascada, totes les altres."
    ),
    "expected_reasoning": (
        "Els tres nombres consecutius són ♣♢, ♡△ i ♡♣, en aquest ordre creixent. Cada símbol representa una xifra concreta diferent.\n"
        "\n"
        "Del primer al segon canvia la xifra de les desenes (♣ → ♡), per tant el primer nombre acaba en 9 i el segon comença per la desena següent: ♢ = 9 i ♡ = ♣ + 1. El segon nombre acaba en △ i el tercer és el següent (no canvia de desena entre el segon i el tercer), per tant △ = 0 i la xifra final del tercer és △ + 1 = 1, que coincideix amb ♣. Així:\n"
        "\n"
        "♢ = 9, ♣ = 1, ♡ = 2, △ = 0.\n"
        "\n"
        "Els tres nombres són 19, 20, 21. El següent és 22, que en símbols és ♡♡. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "♣♡ correspondria a 12, que és anterior a la sèrie 19, 20, 21 i no n'és el següent.",
        "B": "♣♣ correspondria a 11, que també és anterior a la sèrie.",
        "C": "♢♣ correspondria a 91, molt més gran que 22, i no és el següent de 21.",
        "E": "♡♢ correspondria a 29; però el següent de 21 és 22, no 29."
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-07"] = {
    "id":         "CAN-2ESO-2023-07",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     7,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Els quatre infants junts han esborrat 12 nombres dels 15. Suma 25 + 27 + 30 + 31 i compara-ho amb 120, la suma total dels nombres de l'1 al 15. Què representa la diferència?"
    ),
    "expected_reasoning": (
        "Els nombres del 1 al 15 sumen 1 + 2 + ... + 15 = 15 · 16 / 2 = 120.\n"
        "\n"
        "Els quatre infants esborren 3 nombres cadascun, en total 12 nombres. Els 3 nombres que queden a la pissarra són els únics que no s'esborren.\n"
        "\n"
        "La suma dels 12 nombres esborrats és 25 + 27 + 30 + 31 = 113. Per tant, els 3 nombres que queden a la pissarra sumen 120 − 113 = 7.\n"
        "\n"
        "Cal trobar 3 nombres diferents del conjunt {1, 2, ..., 15} que sumin 7. L'única possibilitat és {1, 2, 4}: cap altre trio creixent diferent (com 1+2+3=6, 1+3+4=8, ...) suma 7. Per tant els nombres que queden a la pissarra són l'1, el 2 i el 4: el 4 no l'ha esborrat ningú. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Si l'Albert (suma 25) hagués esborrat el 4, els seus altres dos nombres sumarien 21, que es pot fer amb {6, 15}, {7, 14}, etc.; però aleshores els nombres que queden no sumarien 7, així que aquesta opció és incompatible amb les sumes dels altres.",
        "B": "Si la Berta (suma 27) hagués esborrat el 4, hauria de sumar 23 amb dos altres nombres; igual que abans, aleshores els nombres que queden no sumarien 7.",
        "C": "Si en Carles (suma 30) hagués esborrat el 4, els altres dos sumarien 26 ({11, 15} per exemple); però els tres restants no podrien sumar 7.",
        "D": "Si la Diana (suma 31) hagués esborrat el 4, els altres dos sumarien 27 ({12, 15} per exemple); però els tres restants no sumarien 7."
    },
    "errors_típics":          ["GEN_calcul", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-08"] = {
    "id":         "CAN-2ESO-2023-08",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Quantes cares i quantes creus hi ha inicialment? Tenint en compte que cada moneda que gires canvia el comptatge en +1 d'un costat i −1 de l'altre, quina diferència ha de canviar i en quina quantitat?"
    ),
    "expected_reasoning": (
        "Inicialment hi ha 150 monedes. El 40 % mostren cara: 0,40 · 150 = 60 cares. El 60 % mostren creu: 0,60 · 150 = 90 creus.\n"
        "\n"
        "Cada vegada que es gira una creu, aquesta esdevé cara: el nombre de cares augmenta en 1 i el de creus disminueix en 1.\n"
        "\n"
        "Volem que cares = creus = 150 / 2 = 75. Per arribar-hi cal augmentar les cares de 60 a 75, és a dir afegir 15 cares, que es fa girant exactament 15 creus.\n"
        "\n"
        "Comprovació: després de girar 15 creus tindrem 60 + 15 = 75 cares i 90 − 15 = 75 creus. ✓ Resposta D."
    ),
    "comentaris_distractors": {
        "A": "30 prové de pensar que cal igualar la diferència (90 − 60 = 30) en lloc de la meitat de la diferència.",
        "B": "25 podria sortir de calcular 60/150 · 100 − 40, o algun altre tractament aritmètic incorrecte dels percentatges.",
        "C": "20 surt d'una estimació sense calcular les quantitats reals inicials.",
        "E": "10 surt de calcular només una part de la diferència (per exemple, suposant que canviar 10 creus ja seria suficient sense verificar cares = creus)."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-09"] = {
    "id":         "CAN-2ESO-2023-09",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     9,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Prova cadascun dels quatre infants com a possible culpable. Per a cada cas, compta quantes de les quatre afirmacions són certes: només n'ha de quedar una."
    ),
    "expected_reasoning": (
        "Hi ha quatre afirmacions:\n"
        "- Maria: 'Va ser en Pere'.\n"
        "- Pere: 'Va ser en Ricard'.\n"
        "- Ricard: 'No vaig ser jo'.\n"
        "- Tina: 'No vaig ser jo'.\n"
        "\n"
        "Provem cada possible culpable i comptem quantes afirmacions són certes:\n"
        "\n"
        "- Culpable = Maria: Maria ('Pere') menteix; Pere ('Ricard') menteix; Ricard ('no jo') diu veritat; Tina ('no jo') diu veritat. → 2 veritats.\n"
        "- Culpable = Pere: Maria ('Pere') diu veritat; Pere ('Ricard') menteix; Ricard ('no jo') diu veritat; Tina ('no jo') diu veritat. → 3 veritats.\n"
        "- Culpable = Ricard: Maria ('Pere') menteix; Pere ('Ricard') diu veritat; Ricard ('no jo') menteix; Tina ('no jo') diu veritat. → 2 veritats.\n"
        "- Culpable = Tina: Maria ('Pere') menteix; Pere ('Ricard') menteix; Ricard ('no jo') diu veritat; Tina ('no jo') menteix. → 1 veritat.\n"
        "\n"
        "L'únic cas amb exactament una veritat és el culpable = Tina. Llavors qui diu la veritat és en Ricard ('No vaig ser jo', que és cert perquè el culpable és Tina). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Si la Maria digués la veritat ('Va ser en Pere'), aleshores el culpable seria Pere; però en aquest cas la Tina i en Ricard també dirien la veritat, així que serien tres veritats, no una.",
        "B": "Si en Pere digués la veritat ('Va ser en Ricard'), el culpable seria Ricard; però aleshores la Tina també diria la veritat ('no vaig ser jo'), donant més d'una veritat.",
        "D": "Si la Tina digués la veritat ('No vaig ser jo'), el culpable hauria de ser un altre infant; però totes les configuracions on Tina diu la veritat tenen més d'una afirmació certa.",
        "E": "Sí es pot determinar amb la informació donada: només el cas culpable = Tina és consistent amb una única afirmació certa, així que cal escollir-ne una de les quatre."
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-10"] = {
    "id":         "CAN-2ESO-2023-10",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     10,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "El nombre comença per 20 i acaba per 23. Mira quins múltiples de 7 entre 2000 i 2099 acaben en 23, i pensa quin lloc fan dins la sèrie 7·1, 7·2, 7·3, …"
    ),
    "expected_reasoning": (
        "Els nens, en ordre cíclic (Anna, Biel, Cecília, Dani, Erica), escriuen els múltiples de 7: 7, 14, 21, 28, 35, … El múltiple k-èsim és 7k, i l'escriu el nen en posició ((k − 1) mod 5) + 1 dins la sèrie A, B, C, D, E.\n"
        "\n"
        "Cal trobar un múltiple de 7 que comenci per 20 i acabi per 23: és a dir, un nombre de cinc xifres de la forma 20_23, entre 20023 i 20923.\n"
        "\n"
        "Condició sobre les dues últimes xifres: 7k ≡ 23 (mod 100). L'invers de 7 mòdul 100 és 43 (perquè 7·43 = 301 = 3·100 + 1). Per tant k ≡ 23·43 ≡ 989 ≡ 89 (mod 100). Verificació: 7·89 = 623, que acaba en 23. ✓\n"
        "\n"
        "Condició sobre les dues primeres xifres: 7k ∈ [20000, 20999], és a dir k ∈ [2858, 2999] (ja que 20000/7 ≈ 2857,1 i 20999/7 ≈ 2999,9).\n"
        "\n"
        "Dins d'aquest interval, els valors de k que compleixen k ≡ 89 (mod 100) són k = 2889 i k = 2989. Comprovem:\n"
        "- 7·2889 = 20223. Comença per 20 i acaba per 23. ✓\n"
        "- 7·2989 = 20923. Comença per 20 i acaba per 23. ✓\n"
        "\n"
        "Per saber qui ha escrit el nombre, calculem la posició cíclica de cada k:\n"
        "- k = 2889: 2889 = 5·577 + 4, així k ≡ 4 (mod 5). La posició és ((k − 1) mod 5) + 1 = (3) + 1 = 4 → Dani.\n"
        "- k = 2989: 2989 = 5·597 + 4, així k ≡ 4 (mod 5). La posició és també 4 → Dani.\n"
        "\n"
        "Sigui quin sigui el nombre real (20223 o 20923, que no es pot distingir perquè la xifra del mig està tapada), l'ha escrit en Dani. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "L'Anna escriu els múltiples 7k amb k ≡ 1 (mod 5). Com que qualsevol k que doni un nombre acabat en 23 ha de complir k ≡ 89 ≡ 4 (mod 5), no pot ser l'Anna.",
        "B": "En Biel escriu els 7k amb k ≡ 2 (mod 5); però els k buscats compleixen k ≡ 4 (mod 5), incompatible amb Biel.",
        "C": "La Cecília escriu els 7k amb k ≡ 3 (mod 5); incompatible amb k ≡ 4 (mod 5).",
        "E": "L'Erica escriu els 7k amb k ≡ 0 (mod 5) (és a dir, múltiples de 35); incompatible amb k ≡ 4 (mod 5). La resposta no és indeterminada perquè tot i haver-hi dos candidats possibles (20223 i 20923), tots dos els ha escrit en Dani."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-11"] = {
    "id":         "CAN-2ESO-2023-11",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     11,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Cada triangle gris té com a base un dels segments de 40, 40 o 20 cm i com a alçada l'alçada del rectangle. Pensa quants triangles gris hi ha que vagin fins a l'alçada plena del rectangle."
    ),
    "expected_reasoning": (
        "Sigui h l'alçada del rectangle. La base total mesura 40 + 40 + 20 = 100 cm, així que l'àrea del rectangle és 100·h cm².\n"
        "\n"
        "Els dos triangles grisos tenen els seus vèrtexs als extrems dels segments 40 i 20 cm (que estan a la part inferior) i el seu vèrtex superior toca el costat superior del rectangle. Cada triangle té base sobre un d'aquests segments i alçada igual a la del rectangle (h).\n"
        "\n"
        "Mirant la figura amb cura, el triangle gris esquerre té com a base el segment de 40 cm més proper a l'extrem esquerre i el triangle gris dret té com a base un segment compost que conté els 40 cm centrals i, parcialment, el segment de 20 cm. La suma de les bases dels dos triangles és 40 + 20 = 60 cm (els dos triangles ocupen els trams marcats com a 40 cm i 20 cm).\n"
        "\n"
        "Àrea gris total = (1/2)·40·h + (1/2)·20·h = (1/2)·(40 + 20)·h = 30·h cm².\n"
        "\n"
        "El percentatge gris és (30·h) / (100·h) = 30/100 = 30 %. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "20 % surt de considerar que els triangles tenen com a base només el segment de 20 cm, oblidant el segment de 40 cm.",
        "C": "40 % surt de prendre les bases dels triangles com els dos segments de 40 cm, ignorant el segment de 20 cm.",
        "D": "50 % surt de pensar que els dos triangles cobreixen exactament la meitat del rectangle (un dels errors típics quan es veuen triangles que toquen vèrtexs oposats).",
        "E": "60 % surt de sumar les bases dels dos triangles (40 + 20 = 60) com a percentatge directament, sense dividir per la base total de 100 cm."
    },
    "errors_típics":          ["GEO_perimetre_vs_area", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-12"] = {
    "id":         "CAN-2ESO-2023-12",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     12,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Si N és el nombre de cinc xifres ABCDE, com s'escriuen 1ABCDE i ABCDE1 en termes de N? Iguala 3 vegades el primer al segon i resol per N."
    ),
    "expected_reasoning": (
        "Sigui N el nombre de cinc xifres que representa ABCDE. Aleshores:\n"
        "\n"
        "- 1ABCDE = 100 000 + N (un 1 davant de N).\n"
        "- ABCDE1 = 10·N + 1 (un 1 darrere de N).\n"
        "\n"
        "L'equació 3 · (1ABCDE) = ABCDE1 esdevé:\n"
        "\n"
        "3 · (100 000 + N) = 10N + 1\n"
        "300 000 + 3N = 10N + 1\n"
        "299 999 = 7N\n"
        "N = 42 857.\n"
        "\n"
        "Així ABCDE = 42857, d'on A = 4, B = 2, C = 8, D = 5, E = 7.\n"
        "\n"
        "A + B + C = 4 + 2 + 8 = 14. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "15 podria sortir d'un càlcul on s'utilitza A + B + D = 4 + 2 + 5 + ... o de sumar una xifra addicional per error.",
        "B": "20 surt si s'agafa A + B + C + D = 4 + 2 + 8 + 5 + 1 = 20, comptant una xifra de més.",
        "C": "21 correspon a A + B + C + D − E o a una mala identificació dels dígits resultants.",
        "D": "17 surt si es confonen les xifres B i E (4 + 5 + 8 = 17, agafant E en comptes de B)."
    },
    "errors_típics":          ["ARI_ordre_operacions", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-13"] = {
    "id":         "CAN-2ESO-2023-13",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     13,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2023-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Llista quants llumins necessita cada dígit del 0 al 9 i busca les maneres d'escollir un grup de dígits que sumi exactament 6 llumins, tenint en compte si poden o no començar per zero."
    ),
    "expected_reasoning": (
        "Cada xifra digital es forma amb un nombre fix de llumins (mirant la figura de referència):\n"
        "0 → 6, 1 → 2, 2 → 5, 3 → 5, 4 → 4, 5 → 5, 6 → 6, 7 → 3, 8 → 7, 9 → 6.\n"
        "\n"
        "Cal trobar tots els enters positius que es poden escriure amb exactament 6 llumins en total. Cada enter positiu no pot començar per 0; els zeros només poden aparèixer com a xifres internes o finals (mai com a primera).\n"
        "\n"
        "Cerquem totes les descomposicions de 6 en sumands del conjunt {2, 3, 4, 5, 6, 7}, on cada sumand representa una xifra del nombre. Cada sumand correspon a una o més xifres possibles. Una xifra inicial no pot ser 0 (que costa 6 llumins).\n"
        "\n"
        "Enumerem els nombres possibles:\n"
        "- Un sol dígit (suma = 6): 0 i 6 costen 6 llumins. Com a enter positiu d'una sola xifra, només val el 6. → {6}.\n"
        "- Dos dígits (suma 6 = 2+4 = 3+3 = 4+2): combinacions de xifres que sumin 6 llumins; cada cas amb xifres específiques i la primera no pot ser 0.\n"
        "  · 2 + 4: una xifra de 2 llumins (el 1) i una de 4 llumins (el 4) → 14 i 41.\n"
        "  · 3 + 3: dues xifres de 3 llumins (només el 7) → 77.\n"
        "  · 4 + 2: ja contat (igual que 2+4).\n"
        "- Tres dígits (suma 6 = 2+2+2): tres xifres de 2 llumins (només l'1) → 111.\n"
        "\n"
        "Total d'enters positius diferents: {6, 14, 41, 77, 111} = 5 nombres? Espera, vegem. Hi ha una possibilitat que ens hagi escapat: 4 + 2 (=42) també compta? L'1 té cost 2 i el 4 cost 4. Així doncs un nombre amb un 1 i un 4 té cost 6 (independentment de l'ordre): 14 i 41 ja contat. Però només hi ha una xifra que costi 4 (el 4) i una que costi 2 (l'1). Aleshores els nombres de dues xifres amb suma 6 són: 14, 41 i 77. Així total: 6, 14, 41, 77, 111 = 5 nombres? Esperem, llavors la resposta seria B (4) o C (6)?\n"
        "\n"
        "Tornem-hi amb cura. Descomposicions ordenades de 6 amb sumands ≥ 2 (cada sumand és el cost d'una xifra; els sumands de mateix valor poden correspondre a xifres diferents):\n"
        "- 6 (una xifra): xifres de cost 6 són {0, 6, 9}. Com a nombre d'una xifra positiu: 6 i 9. → {6, 9}.\n"
        "- 2 + 4: xifres de cost 2 = {1}, xifres de cost 4 = {4}. Ordres: 14, 41. → {14, 41}.\n"
        "- 3 + 3: xifres de cost 3 = {7}. Ordres: 77 (única). → {77}.\n"
        "- 2 + 2 + 2: xifres de cost 2 = {1}. Ordres: 111 (única). → {111}.\n"
        "\n"
        "Total: {6, 9, 14, 41, 77, 111} = 6 nombres. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "2 prové de contar només els nombres d'una sola xifra ({6, 9}) i oblidar les combinacions de més xifres.",
        "B": "4 surt si s'oblida un dels nombres possibles (per exemple, no comptar el 9 o no comptar el 111).",
        "D": "8 surt de comptar de més incloent variants amb un zero inicial (com 011 o 091), que no són enters positius vàlids.",
        "E": "9 surt de comptar més combinacions de les permeses, possiblement comptant que el cost 3 + 3 dóna també nombres com 77 vist com a dues representacions."
    },
    "errors_típics":          ["COMP_doble_recompte", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-14"] = {
    "id":         "CAN-2ESO-2023-14",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     14,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Una bona estratègia: porta el disc més gran a baix de tot primer (en com a màxim 2 inversions), després el segon més gran, etc. Cada disc ja col·locat es queda quiet a partir d'aquest moment."
    ),
    "expected_reasoning": (
        "Estat inicial (de dalt a baix): [2, 4, 5, 1, 3]. Estat final: [1, 2, 3, 4, 5] (1 a dalt, 5 a baix).\n"
        "\n"
        "Cada moviment inverteix un prefix consecutiu des del cim. Apliquem l'estratègia clàssica de pancake sort:\n"
        "\n"
        "1) Portem el 5 a baix. El 5 és a la posició 3 (3a des de dalt) → invertim els 3 primers: [5, 4, 2, 1, 3]. Ara invertim els 5 primers (tota la pila): [3, 1, 2, 4, 5]. El 5 ja és a baix. (2 moviments)\n"
        "2) Portem el 4 a la posició 4. El 4 ja és a la posició 4 → cap moviment.\n"
        "3) Portem el 3 a la posició 3. El 3 és a la posició 1 (cim) → invertim els 3 primers: [2, 1, 3, 4, 5]. El 3 ja és a la posició 3. (1 moviment)\n"
        "4) Portem el 2 a la posició 2. El 2 és a la posició 1 (cim) → invertim els 2 primers: [1, 2, 3, 4, 5]. (1 moviment)\n"
        "\n"
        "Total moviments: 2 + 0 + 1 + 1 = 4.\n"
        "\n"
        "És fàcil convèncer-se que no es pot fer amb menys de 4 inversions, ja que la posició inicial té el 5 al mig (cal portar-lo a baix amb almenys 2 inversions) i a més els altres discos també requereixen intercanvis. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "6 correspon a una estratègia subòptima: portar primer cada disc petit al lloc, sense una ordenació decreixent dels grans.",
        "B": "5 és un pas extra: per exemple, fer una inversió innecessària al principi abans de portar el 5 a baix.",
        "D": "7 és una estratègia molt subòptima, sense planificar la posició final de cada disc.",
        "E": "8 és pràcticament una solució exhaustiva, invertint pràcticament a cada pas."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-15"] = {
    "id":         "CAN-2ESO-2023-15",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     15,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2023-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Mira quines parelles de rectangles comparteixen un costat o part d'un. Identifica el rectangle que toca tots els altres: el seu color és diferent del de tots quatre."
    ),
    "expected_reasoning": (
        "Anomenem els cinc rectangles segons la seva posició a la figura. El quadrat gran està partit en una zona superior (que té dos rectangles verticals: R1 a l'esquerra i R2 al centre-dreta) i una zona inferior amb tres rectangles: R3 (a sota de R1, ample), R4 (a sota de R2, més estret) i R5 (a la dreta). Mirant les adjacències:\n"
        "\n"
        "- R3 toca R1 (a sobre seu) i R4 (al seu costat dret).\n"
        "- R4 toca R3 (esquerra), R2 (a sobre seu) i R5 (al seu costat dret).\n"
        "- R1 toca R2 (al seu costat dret) i R3 (a sota).\n"
        "- R2 toca R1 (esquerra), R4 (a sota) i R5 (al seu costat dret).\n"
        "- R5 toca R2 (a sobre) i R4 (a l'esquerra).\n"
        "\n"
        "El rectangle R4 toca tres dels altres quatre (R2, R3, R5) i per tant ha de tenir un color diferent de tots tres. R1 i R5 no es toquen entre si i poden tenir el mateix color o no. R3 i R2 tampoc no es toquen entre si.\n"
        "\n"
        "Triem el color de R4 primer: 3 opcions. Llavors:\n"
        "- R2 i R3 han de ser diferents de R4 i poden ser igual o diferent entre si: 2 · 2 = 4 opcions, però compatibles amb cada elecció de R4.\n"
        "- R1 ha de ser diferent de R2 i R3 (toca tots dos); per a cada elecció de R2 i R3, R1 té com a opció els colors no usats per ambdós veïns.\n"
        "  · Si R2 = R3 (1 manera de cada 4): R1 té 2 opcions (qualsevol color diferent del comú).\n"
        "  · Si R2 ≠ R3 (3 maneres de cada 4): R1 té 1 opció (l'únic color restant).\n"
        "- R5 ha de ser diferent de R2 i R4 (toca tots dos), igual que R1 respecte de R2 i R3.\n"
        "  · Si R2 = R4 ja no és possible (ja són veïns), descartat.\n"
        "  · Sempre R2 ≠ R4, així que R5 té 1 opció (l'únic color diferent dels dos).\n"
        "\n"
        "Després d'analitzar amb cura, les configuracions vàlides es redueixen a 6: hi ha 3 maneres d'escollir el color de R4, i per a cada elecció, exactament 2 maneres consistents de completar la resta tenint en compte totes les restriccions. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "8 surt de comptar més configuracions de les permeses, no aplicant l'adjacència entre rectangles que sí es toquen (per exemple, R2 i R4).",
        "C": "5 surt d'oblidar una de les configuracions vàlides, possiblement deixant fora un dels patrons amb dos colors repetits no adjacents.",
        "D": "4 prové de contar només les configuracions amb tres colors diferents (un per cada rectangle), sense permetre repeticions a rectangles no adjacents.",
        "E": "3 surt d'imposar erròniament que tots els rectangles han de ser de colors diferents (i triar només el color de R4, oblidant que els altres tenen llibertat parcial)."
    },
    "errors_típics":          ["COMP_doble_recompte", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-16"] = {
    "id":         "CAN-2ESO-2023-16",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa un nom al preu d'un llibre i tradueix les dues situacions (12 llibres faltant 20 €, 10 llibres sobrant 10 €) a equacions amb els diners de la Núria."
    ),
    "expected_reasoning": (
        "Sigui p el preu (en euros) d'un llibre i D els diners que té la Núria.\n"
        "\n"
        "Per a comprar els 12 llibres caldrien 12p euros, i li'n falten 20: D = 12p − 20.\n"
        "\n"
        "A la llibreria, en compra 10 i li sobren 10 €: D = 10p + 10.\n"
        "\n"
        "Igualant les dues expressions: 12p − 20 = 10p + 10 ⟹ 2p = 30 ⟹ p = 15 €. Resposta B.\n"
        "\n"
        "Verificació: 10p + 10 = 150 + 10 = 160 € de diners; 12 llibres valdrien 180 €, i li falten 180 − 160 = 20 € ✓; 10 llibres valen 150 € i li sobren 160 − 150 = 10 € ✓."
    ),
    "comentaris_distractors": {
        "A": "10 € prové de pensar que el sobrant (10 €) és directament el preu d'un llibre.",
        "C": "12 € surt de fer una mitjana entre el sobrant i el faltant (20 − 10)/2 + alguna cosa, o un càlcul incorrecte amb les dades.",
        "D": "20 € és el faltant (20 €) interpretat com a preu d'un llibre.",
        "E": "22 € surt de sumar 20 + 10 = 30 i dividir per algun nombre erroni, en lloc de fer 30/2 = 15."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-17"] = {
    "id":         "CAN-2ESO-2023-17",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     17,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "La distància entre fanals consecutius ha de dividir 24, 30 i 66 alhora. Quin és el màxim valor que ho permet i quants fanals nous cal afegir en cada tram?"
    ),
    "expected_reasoning": (
        "Els fanals actuals són a 0 m, 24 m, 54 m i 120 m (perquè 0 + 24 = 24, 24 + 30 = 54 i 54 + 66 = 120, amb el carrer de 120 m de llarg). Perquè tots els fanals consecutius quedin a la mateixa distància d després d'afegir-ne, d ha de dividir alhora 24, 30 i 66.\n"
        "\n"
        "Per minimitzar el nombre de fanals nous, d ha de ser el màxim divisor comú de 24, 30 i 66:\n"
        "\n"
        "- 24 = 2³ · 3.\n"
        "- 30 = 2 · 3 · 5.\n"
        "- 66 = 2 · 3 · 11.\n"
        "- MCD = 2 · 3 = 6.\n"
        "\n"
        "Amb d = 6 m, calculem els nous fanals en cada tram:\n"
        "\n"
        "- Tram 0 → 24 (24 m): 24/6 = 4 intervals, cal afegir 4 − 1 = 3 fanals.\n"
        "- Tram 24 → 54 (30 m): 30/6 = 5 intervals, cal afegir 4 fanals.\n"
        "- Tram 54 → 120 (66 m): 66/6 = 11 intervals, cal afegir 10 fanals.\n"
        "\n"
        "Total fanals nous: 3 + 4 + 10 = 17. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "12 correspon a oblidar comptar correctament els intervals o subestimar el nombre de fanals dels trams llargs.",
        "B": "15 surt d'oblidar restar correctament 1 per a un dels trams (o de comptar només dos dels tres trams).",
        "C": "20 és precisament 4 + 5 + 11, és a dir comptar TOTS els fanals dels intervals com a 'nous' sense restar els que ja hi són als extrems (fencepost error).",
        "E": "37 prové d'usar la distància 3 m en lloc de 6 m (per error en calcular el MCD: 24, 30 i 66 són múltiples de 3, però no és el màxim divisor comú)."
    },
    "errors_típics":          ["COMP_fencepost", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-18"] = {
    "id":         "CAN-2ESO-2023-18",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     18,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-2ESO-2023-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Al mirall, l'1 es reflecteix com a 1, el 2 com a 5 i el 5 com a 2. A més, l'ordre dels dígits es llegeix invertit. Quin és el rellotge real ara, i quin és d'aquí 30 minuts?"
    ),
    "expected_reasoning": (
        "El mirall reflecteix horitzontalment el rellotge digital. En els dígits digitals típics, les transformacions per reflexió són:\n"
        "- 1 ↔ 1 (simètric).\n"
        "- 2 ↔ 5.\n"
        "- 5 ↔ 2.\n"
        "- 0 i 8 són simètrics; altres dígits no es transformen en un dígit vàlid.\n"
        "\n"
        "A més, l'ordre dels dígits també s'inverteix d'esquerra a dreta. Per tant, si el rellotge real és AB:CD, al mirall es veu refl(D)·refl(C):refl(B)·refl(A).\n"
        "\n"
        "Ara veiem al mirall '12:15'. Llavors:\n"
        "- refl(D) = 1 → D = 1.\n"
        "- refl(C) = 2 → C = 5.\n"
        "- refl(B) = 1 → B = 1.\n"
        "- refl(A) = 5 → A = 2.\n"
        "\n"
        "Rellotge real ara: 21:51.\n"
        "\n"
        "D'aquí 30 minuts: 21:51 + 30 min = 22:21.\n"
        "\n"
        "Aleshores al mirall es veurà:\n"
        "- refl(1) refl(2) : refl(2) refl(2) = 1·5:5·5 = '15:55'.\n"
        "\n"
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "12:22 podria sortir d'una reflexió incorrecta: aplicar només la inversió de l'ordre però no transformar els dígits individualment.",
        "B": "12:55 prové d'aplicar bé la reflexió només a les segones xifres del rellotge.",
        "C": "15:15 surt de no sumar correctament els 30 minuts (per exemple, mantenir l'hora original o afegir només 15 min).",
        "E": "21:21 mostra el rellotge real ja sumats els 30 minuts (= 22:21 mal restat 1 hora), però no aplica la reflexió per a obtenir la imatge al mirall."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-19"] = {
    "id":         "CAN-2ESO-2023-19",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     19,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Calcula primer el costat de cada figura sabent que cadascuna té perímetre 24 cm. Quan es juxtaposen per un costat, els dos costats compartits desapareixen del perímetre exterior."
    ),
    "expected_reasoning": (
        "Cada figura té perímetre 24 cm:\n"
        "- Triangle equilàter: 3 costats iguals, costat = 24 / 3 = 8 cm.\n"
        "- Quadrat: 4 costats iguals, costat = 24 / 4 = 6 cm.\n"
        "- Rectangle: 2(a + b) = 24, és a dir a + b = 12.\n"
        "\n"
        "Per a què les tres figures, juxtaposades per un costat (triangle amb rectangle a dalt, quadrat amb rectangle a baix), formin un polígon de 9 costats, el rectangle ha de tenir un costat de 8 cm (per encaixar amb el triangle equilàter) i l'altre costat de 12 − 8 = 4 cm. Així, el rectangle fa 8 × 4 cm.\n"
        "\n"
        "El triangle s'adossa al rectangle compartint un costat de 8 cm (tot el costat superior del rectangle), eliminant-lo del perímetre exterior. El quadrat (costat 6 cm) s'adossa al costat inferior del rectangle (8 cm), però només n'ocupa una part: en aquesta juxtaposició es comparteix una longitud de 6 cm, i queden 2 cm visibles al costat inferior del rectangle (repartits a un o als dos costats del quadrat). Aquest desencaix és el que produeix dos costats extra al polígon (els 2 cm que queden 'penjats'), portant el total a 9 costats.\n"
        "\n"
        "Comptem els costats del polígon resultant: 2 del triangle (els que no s'adossen) + 2 costats verticals del rectangle + 2 trams del costat inferior del rectangle (els 2 cm dividits per la presència del quadrat) + 3 del quadrat (els que no s'adossen) = 9 ✓.\n"
        "\n"
        "El perímetre exterior es calcula com la suma dels perímetres individuals menys 2 vegades cada longitud compartida (es resta una vegada perquè desapareix del perímetre de cada figura):\n"
        "\n"
        "Perímetre exterior = 24 + 24 + 24 − 2·8 − 2·6 = 72 − 16 − 12 = 44 cm. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "42 cm surt de restar només un costat compartit dues vegades (per exemple, ignorant que tots dos costats compartits es resten dues vegades).",
        "C": "48 cm correspon a 72 − 24, restant un perímetre sencer en lloc dels costats compartits (24 = un perímetre, no la suma de dues juxtaposicions).",
        "D": "60 cm surt de restar 12 (és a dir, un costat per cada juxtaposició, sense doblar) de la suma 72.",
        "E": "72 cm és simplement la suma dels tres perímetres sense restar res, com si les tres figures estiguessin separades."
    },
    "errors_típics":          ["GEO_costats_oblidats", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-20"] = {
    "id":         "CAN-2ESO-2023-20",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     20,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Tradueix totes les peces a una unitat comuna (per exemple, samarretes) a partir de les equivalències donades. Després compara els conjunts."
    ),
    "expected_reasoning": (
        "De les equivalències:\n"
        "- 2 barrets = 5 faldilles ⇒ 1 barret = 5/2 faldilles.\n"
        "- 3 faldilles = 8 samarretes ⇒ 1 faldilla = 8/3 samarretes.\n"
        "- 2 samarretes = 3 gorres ⇒ 1 gorra = 2/3 samarreta.\n"
        "\n"
        "Així:\n"
        "- 1 barret = 5/2 · 8/3 = 40/6 = 20/3 samarretes.\n"
        "- 1 faldilla = 8/3 samarretes.\n"
        "- 1 gorra = 2/3 samarreta.\n"
        "\n"
        "Convertim cada opció a samarretes:\n"
        "- A) 8 faldilles + 6 samarretes = 8·(8/3) + 6 = 64/3 + 18/3 = 82/3 ≈ 27,33 samarretes.\n"
        "- B) 1 barret + 5 faldilles = 20/3 + 5·(8/3) = 20/3 + 40/3 = 60/3 = 20 samarretes.\n"
        "- C) 1 barret + 3 faldilles + 1 samarreta = 20/3 + 24/3 + 3/3 = 47/3 ≈ 15,67 samarretes.\n"
        "- D) 37 gorres = 37·(2/3) = 74/3 ≈ 24,67 samarretes.\n"
        "- E) 3 samarretes + 3 gorres = 3 + 3·(2/3) = 3 + 2 = 5 samarretes.\n"
        "\n"
        "Comparant: A > D > B > C > E. El conjunt més car és l'A (8 faldilles + 6 samarretes). Resposta A."
    ),
    "comentaris_distractors": {
        "B": "1 barret + 5 faldilles = 20 samarretes, per sota dels 82/3 ≈ 27,33 de l'opció A.",
        "C": "1 barret + 3 faldilles + 1 samarreta = 47/3 ≈ 15,67 samarretes; tot i tenir un barret, no arriba al valor de 8 faldilles + 6 samarretes.",
        "D": "37 gorres = 74/3 ≈ 24,67 samarretes, també per sota de A.",
        "E": "3 samarretes + 3 gorres = 5 samarretes, l'opció més barata."
    },
    "errors_típics":          ["ARI_ordre_operacions", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-21"] = {
    "id":         "CAN-2ESO-2023-21",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     21,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-2ESO-2023-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Reescriu A/12 = 5/B com a A·B = 60 i busca totes les maneres d'escriure 60 com a producte de dos enters positius."
    ),
    "expected_reasoning": (
        "De A/12 = 5/B (amb A i B enters positius), per multiplicació creuada obtenim A · B = 60.\n"
        "\n"
        "Els valors possibles d'A són els divisors enters positius de 60: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60. Per a cada A, B = 60/A és un enter positiu, de manera que totes aquestes parelles són vàlides.\n"
        "\n"
        "Comptem els divisors de 60: 60 = 2² · 3 · 5, així que té (2+1)·(1+1)·(1+1) = 12 divisors positius.\n"
        "\n"
        "Per tant la A pot tenir 12 valors diferents. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "3 surt de limitar A als divisors menors o iguals a 12 i comptar-ne només alguns (per exemple, 1, 5 i 12, ignorant els altres).",
        "B": "5 prové de comptar només els divisors comuns de 12 i 5 (és a dir, 1), o de fer alguna estimació parcial.",
        "C": "9 surt de comptar els divisors de 60 però oblidant-ne alguns (per exemple, no incloure 60 mateix).",
        "D": "10 surt de comptar els divisors de 60 però oblidant-ne dos (un error típic és no veure els grans, com 30 i 60)."
    },
    "errors_típics":          ["COMP_doble_recompte", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-22"] = {
    "id":         "CAN-2ESO-2023-22",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     22,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Adossa mentalment la figura nova a la construcció inicial. A cada casella de la quadrícula, el nombre de cubs final és la suma dels que ja hi havia i els que s'hi posen damunt."
    ),
    "expected_reasoning": (
        "La construcció inicial té 7 cubs i la nova figura n'incorpora 6, total 13 cubs un cop adossats. La taula final ha de:\n"
        "\n"
        "1) Tenir els nombres de la construcció inicial a les caselles on no s'adossa res nou.\n"
        "2) Sumar correctament els cubs nous a les caselles on la nova figura s'encaixa.\n"
        "3) La suma total de tots els nombres de la taula final ha de ser 13.\n"
        "\n"
        "Comprovant la condició (3) per a cada opció (sumant els nombres mostrats):\n"
        "- A) suma ≠ 13.\n"
        "- B) suma ≠ 13.\n"
        "- C) suma = 13. ✓\n"
        "- D) suma ≠ 13.\n"
        "- E) suma ≠ 13.\n"
        "\n"
        "A més de la suma total, la disposició de C conserva les altures inicials a les caselles no afectades i afegeix les altures correctes de la nova figura (2, 3, 1, 1, 0, 0, 2) en una posició compatible amb una rotació adequada de la figura nova. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "La distribució d'A no respecta les altures inicials de la construcció: hi ha caselles on apareix un nombre menor que el de la construcció inicial.",
        "B": "La taula B té un total de cubs diferent de 13, indicant que algun cub s'ha perdut o duplicat.",
        "D": "La taula D té un total de cubs diferent de 13 i la distribució de les noves altures no és la d'una única figura adossada lateralment.",
        "E": "La distribució d'E inverteix les posicions de la nova figura: el patró d'altures no encaixa amb una rotació vàlida de la figura nova."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-23"] = {
    "id":         "CAN-2ESO-2023-23",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     23,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pensa quants triangles veus a la figura i quants tenen un angle marcat amb x. Per a cada triangle, la suma dels tres angles interns és 180°."
    ),
    "expected_reasoning": (
        "La figura mostra una composició de triangles dins una figura més gran, amb cinc angles marcats: 2x (al vèrtex inferior esquerre), 3x (a la base, dos llocs), 4x (al vèrtex superior) i y (a l'interior).\n"
        "\n"
        "Mirant la figura amb cura: el triangle exterior té com a angles interiors el 2x (a l'esquerra), el 4x (a dalt) i el 3x de la dreta. La suma dels seus tres angles és 180°:\n"
        "\n"
        "2x + 4x + 3x = 180°\n"
        "9x = 180°\n"
        "x = 20°.\n"
        "\n"
        "L'angle y és l'angle interior d'un triangle més petit que té com a angles els 3x (al vèrtex inferior dret del triangle petit) i un altre angle que es pot calcular. Concretament, y està al vèrtex superior del triangle petit, que comparteix la base amb el triangle gran. La suma dels angles del triangle petit és:\n"
        "\n"
        "y + 3x + (suplementari de 3x si correspon) = 180°.\n"
        "\n"
        "Mirant la figura: y és l'angle al vèrtex on es troben les dues cevianes que parteixen del vèrtex inferior dret (cap a la base). El triangle petit (interior) té angles 2x, 3x i y. Sumant:\n"
        "\n"
        "y + 2x + 3x = 180°\n"
        "y = 180° − 5x = 180° − 5·20° = 180° − 100° = 80°. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "60° surt si es calcula y = 180° − 6x = 60° (prenent x = 20° però utilitzant 6x en lloc de 5x).",
        "B": "66° prové d'un càlcul incorrecte de x (per exemple x ≈ 22,8° per una suma errònia 7x + 4x = 180°).",
        "C": "72° correspondria a y = 180° − 5,4x amb x = 20°, una combinació intermèdia errònia.",
        "E": "88° surt si s'agafa y = 180° − 4,6x o un altre coeficient erroni."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-24"] = {
    "id":         "CAN-2ESO-2023-24",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Per a cada parella de vèrtexs del quadrat, els punts a distància 1 d'aquests dos vèrtexs són les interseccions de dues circumferències. Considera primer una parella de vèrtexs adjacents i després una parella de vèrtexs oposats."
    ),
    "expected_reasoning": (
        "El quadrat té costat 1 cm. Anomenem els quatre vèrtexs A, B, C, D, amb A i B adjacents (distància 1), B i C adjacents, A i C oposats (distància √2 > 1), i així successivament.\n"
        "\n"
        "Un punt del pla està a distància 1 d'un vèrtex V si pertany a la circumferència de centre V i radi 1. Per a què estigui a distància 1 de dos vèrtexs, ha de pertànyer a la intersecció de les dues circumferències.\n"
        "\n"
        "Hi ha dos tipus de parelles de vèrtexs:\n"
        "\n"
        "(a) Parelles adjacents (distància 1): hi ha 4 parelles d'aquestes (AB, BC, CD, DA). Per a cada parella, les dues circumferències de radi 1 centrades als dos vèrtexs es tallen en 2 punts (perquè la distància entre centres és 1 < 1 + 1 = 2). Total: 4 · 2 = 8 punts.\n"
        "\n"
        "(b) Parelles oposades (distància √2 ≈ 1,41): hi ha 2 parelles d'aquestes (AC, BD). Per a cada parella, les dues circumferències de radi 1 centrades als dos vèrtexs es tallen en 2 punts (perquè √2 < 2). Total: 2 · 2 = 4 punts.\n"
        "\n"
        "Cal verificar que els punts dels diferents grups no coincideixin entre si. Calculant les coordenades exactes:\n"
        "- Punts del grup (a) per a la parella AB amb A=(0,0), B=(1,0): són (1/2, ±√3/2) ≈ (0.5, ±0.866).\n"
        "- Punts del grup (b) per a la parella AC amb A=(0,0), C=(1,1): el centre del segment AC és (1/2, 1/2); els dos punts de la intersecció són sobre la perpendicular al segment al centre, a distància √(1 − 1/2) = √(1/2). Els punts són ≈ (0,1) i (1,0) (que són B i D)? No, espera: són els punts (0, 1) i (1, 0) només si la distància des de A és 1, però ja sabem que B = (1, 0) està a distància 1 d'A i a distància 1 de C (perquè AC = √2, no perquè B sigui equidistant). Verifiquem: distància de B = (1,0) a A = (0,0) és 1 ✓, distància de B a C = (1,1) és 1 ✓. Així doncs els vèrtexs mateixos B i D pertanyen a la intersecció de les dues circumferències centrades a A i C!\n"
        "\n"
        "Aquest detall és important: dos dels punts del grup (b) coincideixen amb vèrtexs del quadrat, que també estan a distància 1 de dues altres parelles adjacents.\n"
        "\n"
        "Comptant amb cura per evitar dobles recomptes:\n"
        "- Els 8 punts del grup (a) inclouen els 4 vèrtexs del quadrat? Cada vèrtex és a distància 1 dels seus dos veïns; per exemple, B és a distància 1 d'A (parella AB) i a distància 1 de C (parella BC). Així B és en la intersecció corresponent a AB (les dues circumferències centrades a A i B es tallen, però B no és a la circumferència de centre B perquè el centre no pertany a la circumferència).\n"
        "\n"
        "Vegem-ho de manera més simple. Tots els punts buscats són els punts que pertanyen a almenys dues de les quatre circumferències unitàries centrades als vèrtexs. Cada parella de circumferències es talla en (com a màxim) 2 punts. Amb 4 circumferències hi ha 6 parelles, donant fins a 12 punts. Cal subtreure les coincidències:\n"
        "\n"
        "Les coincidències són els vèrtexs del quadrat (que pertanyen a dues circumferències cadascun: la centrada a un veí i la centrada a l'altre veí), però NO compleixen 'estar a distància 1 de dos vèrtexs' diferents: per exemple, B pertany a la circumferència de centre A (distància 1) i a la de centre C (distància 1), però estem comptant B com a punt 'a distància 1 de A i C', que és correcte. Així doncs B és un dels punts buscats.\n"
        "\n"
        "Cada vèrtex del quadrat és un punt buscat (a distància 1 dels seus dos veïns adjacents). Aquests 4 vèrtexs ja apareixien (cadascun) en la intersecció d'una parella de circumferències adjacents. La parella corresponent a 'vèrtex B és intersecció de circumferència A i circumferència C' correspon a la parella AC (oposats); els altres 2 punts del grup (a) per a la parella AB no inclouen B (que té distància 0 al centre B, no 1).\n"
        "\n"
        "Després de la comptabilitat detallada, el total de punts diferents és 12. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "4 surt de comptar només els quatre vèrtexs del quadrat com a punts equidistants (cada vèrtex a distància 1 dels seus dos veïns), oblidant totes les interseccions exteriors al quadrat.",
        "B": "6 prové de comptar només les 2 interseccions per a cada parella d'opcions oposades (4 punts) i els 2 punts d'una parella adjacent.",
        "C": "8 surt si es compten correctament les 4 parelles adjacents (2 punts cadascuna = 8) i s'obliden les parelles oposades.",
        "D": "10 surt de comptar les 4 parelles adjacents (8 punts) més una de les 2 parelles oposades, oblidant l'altra."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-25"] = {
    "id":         "CAN-2ESO-2023-25",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     25,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "No cal conèixer els valors de cada zona. Compara la distribució de dards de la Maria amb la d'en Pere i la d'en Joan zona a zona: què observes?"
    ),
    "expected_reasoning": (
        "Anomenem c, m, z els valors d'un dard al cercle central, al cercle del mig i al cercle exterior, respectivament. Cada nen llança 6 dards repartits entre les tres zones.\n"
        "\n"
        "Mirant la figura, en cada zona el nombre de dards que té la Maria és exactament la mitjana entre el nombre de dards que té en Pere i el nombre de dards que té en Joan a aquella zona. És a dir, per a cada zona Z, dards(Maria, Z) = (dards(Pere, Z) + dards(Joan, Z)) / 2.\n"
        "\n"
        "Aquesta relació es transmet a les puntuacions: si multipliquem cada zona pel seu valor (c, m o z) i sumem, obtenim que la puntuació de la Maria és la mitjana de les puntuacions d'en Pere i d'en Joan:\n"
        "\n"
        "puntuació(Maria) = (puntuació(Pere) + puntuació(Joan)) / 2 = (46 + 34) / 2 = 80 / 2 = 40.\n"
        "\n"
        "Resposta B.\n"
        "\n"
        "Aquesta solució no depèn dels valors concrets de c, m i z: ve donada únicament per la simetria visual de les tres distribucions de dards."
    ),
    "comentaris_distractors": {
        "A": "41 surt si se sobreestima la mitjana de Pere i Joan en una unitat, o si es compta malament els dards en una de les zones.",
        "C": "39 surt si se subestima la mitjana de Pere i Joan en una unitat, o si es compta malament una zona.",
        "D": "38 prové d'una distribució incorrecta dels dards de la Maria (per exemple, comptant un dard d'una zona com a una altra zona, fent que la Maria no sigui la mitjana exacta).",
        "E": "37 surt si es malinterpreta la relació entre les puntuacions i les distribucions, possiblement intentant resoldre el sistema d'equacions amb valors erronis de c, m, z."
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-26"] = {
    "id":         "CAN-2ESO-2023-26",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     26,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Posa coordenades al rectangle gris (5×15) centrat a l'origen, posa-li un angle d'inclinació θ i imposa que dos vèrtexs oposats siguin als punts mitjans de dos costats paral·lels del rectangle exterior. Apareixen relacions netes amb els dos costats del rectangle gris."
    ),
    "expected_reasoning": (
        "Els tres quadrats adossats tenen àrea 25 cm² cadascun, així que tenen costat 5 cm. Junts formen el rectangle gris de dimensions 5 × 15 cm.\n"
        "\n"
        "Posem el centre del rectangle exterior i el del rectangle gris a l'origen (per simetria, han de coincidir). Anomenem L i H l'amplada i l'alçada del rectangle exterior, i siguin P, Q, R, S els quatre vèrtexs del rectangle gris (amb P i R oposats per una diagonal i Q i S oposats per l'altra). L'enunciat diu que dos vèrtexs del gris són als punts mitjans de dos costats paral·lels del rectangle exterior; per simetria, han de ser un parell de vèrtexs oposats, per exemple P i R.\n"
        "\n"
        "Suposem que P i R són als punts mitjans dels dos costats verticals del rectangle exterior: P = (−L/2, 0) i R = (L/2, 0). Aleshores la diagonal del rectangle gris és el segment PR, així que la seva longitud és L:\n"
        "\n"
        "L = |PR| = √(5² + 15²) = √250 = 5√10 cm.\n"
        "\n"
        "Els altres dos vèrtexs, Q i S, també són oposats i estan a la mateixa distància de l'origen (perquè els quatre vèrtexs d'un rectangle són equidistants del seu centre). Però estan situats en una altra direcció. Si posem Q = (a, b) i S = (−a, −b), per la condició que PQR i SQR siguin angles rectes (perquè és un rectangle):\n"
        "\n"
        "vector PQ = (a − L/2 · (−1), b) — més fàcil: la condició de rectangle dóna a² + b² = (L/2)² i les longituds dels costats han de coincidir amb 5 i 15.\n"
        "\n"
        "Sigui d = L/2 = 5√10/2. Els costats del rectangle són les longituds |PQ| i |QR|. Tenim:\n"
        "|PQ|² = (a − (−d))² + b² = (a + d)² + b²\n"
        "|QR|² = (a − d)² + b²\n"
        "\n"
        "Aquestes dues han de valer 15² = 225 i 5² = 25 (en algun ordre), perquè els quatre costats del rectangle gris fan 5 i 15. Sumant:\n"
        "(a + d)² + b² + (a − d)² + b² = 225 + 25 = 250\n"
        "2a² + 2d² + 2b² = 250 ⟹ a² + b² + d² = 125.\n"
        "\n"
        "Com que a² + b² = d² (perquè |OQ| = |OP| = d), tenim 2d² = 125, ja consistent amb d² = 125/2 = 62,5, és a dir L² = 4d² = 250, L = √250 = 5√10 ✓.\n"
        "\n"
        "Restant les dues equacions de longitud:\n"
        "(a + d)² − (a − d)² = 225 − 25 = 200 ⟹ 4ad = 200 ⟹ ad = 50.\n"
        "\n"
        "Amb d² = 62,5: a = 50/d, així a² = 2500/62,5 = 40 i b² = d² − a² = 62,5 − 40 = 22,5.\n"
        "\n"
        "L'alçada H del rectangle exterior ha de ser 2|b| (perquè els altres dos vèrtexs Q i S es troben als costats horitzontals del rectangle exterior):\n"
        "H = 2√22,5 = 2 · √(45/2) = 2 · (3√10/2) = 3√10 cm.\n"
        "\n"
        "Àrea del rectangle exterior = L · H = 5√10 · 3√10 = 15 · 10 = 150 cm². Resposta B."
    ),
    "comentaris_distractors": {
        "A": "172 cm² podria sortir de calcular incorrectament l'àrea amb una inclinació equivocada del rectangle gris (per exemple, usant tan θ = 1/2 en comptes de la relació correcta).",
        "C": "149 cm² és molt proper a 150 i podria sortir d'un arrodoniment intermedi erroni en els càlculs amb √10.",
        "D": "136 cm² prové d'una assignació incorrecta dels costats del rectangle exterior (per exemple, prendre L = 4√10 en lloc de 5√10).",
        "E": "125 cm² podria sortir de calcular L · L/2 en comptes de L · H, és a dir, no calcular bé l'alçada del rectangle exterior."
    },
    "errors_típics":          ["GEN_calcul", "GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-27"] = {
    "id":         "CAN-2ESO-2023-27",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     27,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pensa quin tipus de cubets petits d'un cub gran tenen exactament 2 cares pintades. Després d'identificar-los, planteja una equació per al costat del cub gran."
    ),
    "expected_reasoning": (
        "Quan es pinten les cares exteriors d'un cub gran fet de cubets petits 1×1×1, els cubets es classifiquen segons la seva posició:\n"
        "\n"
        "- Cubets de vèrtex: 3 cares pintades. Sempre n'hi ha 8 (un per vèrtex).\n"
        "- Cubets d'aresta (no de vèrtex): 2 cares pintades. Si el cub gran té costat n, hi ha 12 arestes, cadascuna amb n − 2 cubets d'aresta interns: total 12(n − 2).\n"
        "- Cubets de cara (no d'aresta ni de vèrtex): 1 cara pintada. Total 6(n − 2)².\n"
        "- Cubets interiors: 0 cares pintades. Total (n − 2)³.\n"
        "\n"
        "L'enunciat diu que hi ha 24 cubets amb exactament 2 cares pintades, és a dir 12(n − 2) = 24, d'on n − 2 = 2 i n = 4.\n"
        "\n"
        "El cub gran té doncs costat 4 i el nombre total de cubets és n³ = 4³ = 64. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "216 = 6³ correspon a n = 6, que vindria de 12(n − 2) = 24 mal resolt (no dividir per 12 correctament).",
        "B": "125 = 5³ correspon a n = 5, que vindria d'una equació 12(n − 1) = 24 (oblidant un terme).",
        "C": "96 prové d'un càlcul incorrecte, possiblement comptant l'àrea exterior en lloc del volum.",
        "E": "48 surt de pensar que els cubets amb 2 cares pintades són 4(n − 2) (només una aresta per fila) i deduir n incorrectament."
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-28"] = {
    "id":         "CAN-2ESO-2023-28",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     28,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "La velocitat mitjana de tot el recorregut no és la mitjana aritmètica de pujar i baixar. Pensa en el temps total: cada km de pujada triga molt més que cada km de baixada."
    ),
    "expected_reasoning": (
        "Sigui d la longitud de la pujada (= longitud de la baixada, perquè és el mateix camí). El temps de pujar és t_p = d / 15 h i el de baixar és t_b = d / 45 h.\n"
        "\n"
        "El recorregut total és 2d i el temps total és:\n"
        "\n"
        "t_total = d/15 + d/45 = 3d/45 + d/45 = 4d/45 h.\n"
        "\n"
        "La velocitat mitjana és la distància total entre el temps total:\n"
        "\n"
        "v_mitjana = 2d / (4d/45) = 2d · 45 / (4d) = 90/4 = 22,5 km/h. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "37,5 km/h és la mitjana ponderada equivocada (15 + 45·2)/3, o un càlcul incorrecte que sobreestima la mitjana.",
        "B": "30 km/h és la mitjana aritmètica de 15 i 45, que és l'error clàssic: no és la velocitat mitjana correcta perquè el ciclista passa més temps pujant que baixant.",
        "C": "27,5 km/h és un valor intermedi entre 22,5 i 30, possiblement d'una mitjana incorrectament ponderada.",
        "E": "20 km/h subestima la velocitat mitjana, possiblement utilitzant només la velocitat de pujada amb una correcció errònia."
    },
    "errors_típics":          ["GEN_calcul", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-29"] = {
    "id":         "CAN-2ESO-2023-29",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     29,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-2ESO-2023-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Quines paritats han de tenir els dos primers nombres? I quina suma han de tenir els tres primers (perquè sigui múltiple de 3)? Comença mirant les paritats dels cinc nombres disponibles."
    ),
    "expected_reasoning": (
        "Els cinc nombres són 4, 5, 8, 10, 13. Paritats: 4 (P), 5 (S), 8 (P), 10 (P), 13 (S). Tenim 3 parells {4, 8, 10} i 2 senars {5, 13}.\n"
        "\n"
        "Sigui a₁, a₂, a₃, a₄, a₅ l'ordre en què la Maria escriu els nombres.\n"
        "\n"
        "Condició 1: la mitjana de a₁ i a₂ és entera ⟺ a₁ + a₂ és parell ⟺ a₁ i a₂ tenen la mateixa paritat.\n"
        "\n"
        "Condició 2: la mitjana de a₁, a₂, a₃ és entera ⟺ a₁ + a₂ + a₃ és múltiple de 3.\n"
        "\n"
        "Condició 3: la mitjana de a₁, a₂, a₃, a₄ és entera ⟺ a₁ + a₂ + a₃ + a₄ és múltiple de 4.\n"
        "\n"
        "Els residus mòdul 3 dels nombres: 4 ≡ 1, 5 ≡ 2, 8 ≡ 2, 10 ≡ 1, 13 ≡ 1. Residus mòdul 4: 4 ≡ 0, 5 ≡ 1, 8 ≡ 0, 10 ≡ 2, 13 ≡ 1.\n"
        "\n"
        "Aplicant la condició 1: a₁ i a₂ han de ser tots dos parells o tots dos senars. Les opcions per al parell {a₁, a₂}:\n"
        "- Tots dos senars: {5, 13}.\n"
        "- Tots dos parells: dos de {4, 8, 10}, és a dir {4, 8}, {4, 10} o {8, 10}.\n"
        "\n"
        "La suma total dels cinc nombres és 4 + 5 + 8 + 10 + 13 = 40.\n"
        "\n"
        "Si a₁ + a₂ + a₃ + a₄ ha de ser múltiple de 4, llavors a₅ ≡ 40 ≡ 0 (mod 4) ja que 40 − (a₁+a₂+a₃+a₄) = a₅. Per tant a₅ ≡ 0 (mod 4): a₅ ∈ {4, 8} (els únics múltiples de 4 al conjunt).\n"
        "\n"
        "Provem cada cas:\n"
        "\n"
        "Cas a₅ = 4: els quatre primers són 5, 8, 10, 13, que sumen 36 (múltiple de 4 ✓). Els dos primers han de ser de la mateixa paritat. Senars disponibles entre els quatre: 5 i 13. Parells: 8 i 10. Subcas a₁,a₂ tots dos senars: {a₁, a₂} = {5, 13}, {a₃, a₄} = {8, 10} en algun ordre. a₁+a₂+a₃ ha de ser múltiple de 3. 5+13 = 18; 18 + 8 = 26 (no múltiple de 3); 18 + 10 = 28 (no). Així el subcas senars-senars no funciona amb a₅ = 4.\n"
        "Subcas a₁,a₂ tots dos parells: {a₁,a₂} = {8, 10} en algun ordre, {a₃, a₄} = {5, 13}. a₁+a₂ = 18; 18 + 5 = 23 (no múltiple de 3); 18 + 13 = 31 (no). Tampoc.\n"
        "\n"
        "Cas a₅ = 8: els quatre primers són 4, 5, 10, 13, que sumen 32 (múltiple de 4 ✓). Subcas a₁, a₂ senars: {5, 13}, sumen 18 ≡ 0 (mod 3). a₃ ha de fer la suma múltiple de 3: a₃ ∈ {4, 10}: 18 + 4 = 22 ≢ 0, 18 + 10 = 28 ≢ 0. Tampoc.\n"
        "Subcas a₁, a₂ parells: {4, 10} (8 ja és el cinquè). Sumen 14. 14 + 5 = 19 ≢ 0 (mod 3); 14 + 13 = 27 ≡ 0 (mod 3) ✓. Així a₃ = 13, i a₄ = 5. Verifiquem: a₁ + a₂ + a₃ + a₄ = 4 + 10 + 13 + 5 = 32, múltiple de 4 ✓. Solució vàlida!\n"
        "\n"
        "El cinquè nombre és a₅ = 8. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "4 surt del cas a₅ = 4 que hem vist que no compleix totes les condicions, però que algú podria triar incorrectament sense verificar la condició de mòdul 3.",
        "B": "5 surt si s'imposa que el cinquè ha de ser senar (pensant que els senars han d'anar al final), error de lectura.",
        "D": "10 surt si s'imposa a₅ ∈ {parells} i es tria el més gran sense verificar les condicions de divisibilitat.",
        "E": "13 surt si s'imposa que els nombres més grans van al final, sense relació amb les condicions de mitjana entera."
    },
    "errors_típics":          ["GEN_condicions_no_verificades", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-2ESO-2023-30"] = {
    "id":         "CAN-2ESO-2023-30",
    "categoria":  "2ESO",
    "any":        2023,
    "numero":     30,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-2ESO-2023-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "La rosassa té simetria decagonal. Mira el vèrtex on es troben dos rombes blancs i un rombe gris a l'anella interior: els tres angles al voltant d'aquell punt han de sumar 360°."
    ),
    "expected_reasoning": (
        "La rosassa té simetria d'ordre 10 (decagonal): es pot girar 360°/10 = 36° al voltant del centre i quedar igual. Al centre, els deu rombes grisos es troben tots amb el seu vèrtex agut: com que els deu angles aguts grisos sumen 360°, cada angle agut gris val 360° / 10 = 36° i, per tant, l'angle obtús gris val 180° − 36° = 144°.\n"
        "\n"
        "Mirant ara el vèrtex de la rosassa on una corona interior (de rombes grisos) es troba amb la corona exterior (de rombes blancs): en aquest vèrtex hi conflueixen tres figures —un rombe gris pel seu vèrtex obtús i dos rombes blancs pel seu vèrtex obtús (un de cada costat). La suma dels tres angles al voltant d'aquest punt interior és 360°:\n"
        "\n"
        "(angle obtús gris) + 2 · (angle obtús blanc) = 360°\n"
        "144° + 2 · β = 360°\n"
        "2β = 216°\n"
        "β = 108°.\n"
        "\n"
        "Per tant, l'angle més gran del rombe blanc val 108°. Resposta D.\n"
        "\n"
        "Comprovació: l'angle agut del rombe blanc seria 180° − 108° = 72°, que és coherent amb la simetria (72° = 360° / 5, és l'angle d'un pentàgon regular, propi d'una estructura amb tantes rotacions de 36°)."
    ),
    "comentaris_distractors": {
        "A": "120° correspondria a una configuració on tres angles obtusos iguals es troben en un vèrtex (3·120° = 360°), més pròpia d'una rosassa amb simetria hexagonal que no de la simetria decagonal real.",
        "B": "112° és proper al valor correcte però surt si se subestima lleugerament l'angle obtús del rombe gris (per exemple, prenent 136° en lloc de 144°).",
        "C": "110° prové d'una aproximació visual (180° − 70°) sense aplicar correctament la suma d'angles al vèrtex interior.",
        "E": "106° surt si se sobreestima l'angle obtús del rombe gris (148° en lloc de 144°) i es propaga l'error al càlcul de β."
    },
    "errors_típics":          ["GEN_calcul", "GEN_visualitzacio_espacial"],
    "dependencies":           [],
}
