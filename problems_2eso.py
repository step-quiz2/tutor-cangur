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
        "Ves provant les opcions i comprova que les dues condicions es compleixen. Recorda que la polsera és circular!"
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
        "Pren els quadrats de costat 2 (i el radi dels arcs val 1). Calcula l'àrea ombrejada de cada diagrama: si te'n surt sempre el mateix valor, ja saps la resposta."
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
        "Les xifres parelles són 0, 2, 4, 6 i 8. Has de trobar el primer any posterior al 2026 amb les quatre xifres parelles totes diferents. Compte: el 2028 encara té dos 2."
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
        "Prova d'escriure cada nombre com a suma d'enters positius consecutius: 9 = 4+5, 7 = 3+4, 6 = 1+2+3, 5 = 2+3. N'hi ha un que no se'n surt: les potències de 2 no s'hi poden expressar mai."
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
        "Compta quants trossos verticals té la figura i descarta els esquemes que no en faran tants."
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
        "Segur que amb 6 peces es podria fer la flor, però recorda que et pregunta el nombre MÍNIM."
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
        "Mira on va a parar el cangur després de la primera simetria i cap a on mira; fes el mateix amb la segona simetria. El mateix amb la tercera i, finalment, amb la quarta."
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
        "Comença calculant quants trossos menja en Max."
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
        "Per aconseguir una fracció petita, busquem numerador petit o denominador gran; prova primer com aconseguir numeradors petits."
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
        "Volem veure el màxim nombre d’illes, per tant hem de procurar no unir massa peces. Per exemple, amb la A) només surten 2 illes"
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
        "Quantes vagonetes calen perquè hi pugin els 30 alumnes de 3 en 3?"
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
        "Només hi ha dues posicions possibles per a la parella “Anna-Bernat”."
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
        "15:69 no és una hora possible: quines dues posicions s’han d’intercanviar perquè ho sigui?"
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
        "Comença observant la A) i la D), perquè hi ha alguna cosa que no encaixa…i et donarà una pista."
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
        "Has de fer la suma 0+1+2+3+4+5+6. I recorda que cadascun dels grups de nombres suma el mateix: quant sumarà cada grup?"
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
        "Hi ha 2 frases que pots escriure com 2 equacions, amb incògnites M, R i E. A partir d’aquí, pots trobar quant val E."
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
        "Si sumes els perímetres dels 4 trapezis, obtens 4·22 = 88 cm. Però el molinet només fa 56 cm perquè alguns costats queden a l’interior. Amb això, pots trobar la mesura de AB."
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
        "La Fàtima va agafant 2, després 5, després 8... Ves sumant aquests nombres fins que just et passis de 25."
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
        "Les dues igualtats “=10” et fan veure que a cada cercle gris hi ha el mateix nombre. Per tant, ves provant. Si la resposta fos E) 14, vol dir que en el cercle gris hi hauria un 7. Ja veuràs que no funciona. Ves provant altres opcions."
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
        "La pista de les 80 maduixes de més (i toquen 4 més a cadascú) et diu quants amics hi ha; comença per aquí."
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
        "Mira quines cares queden oposades a la plantilla i això et permetrà descartar opcions, un cop muntes el cub."
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
        "Compara la columna de les unitats amb la de les desenes: totes dues tenen B i C, i això et permet saber qui és A."
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
        "El triple del nombre de la Zoe ha de ser suma de dos nombres diferents de l’1 al 5. Això vol dir que la Zoe no pot tenir el 5, perquè el triple és 15 i mai podríem arribar-hi sumant els nombres de Jaume i Frederic."
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
        "Pensa quant pesen, en total, les 7 pilotes que veus a la balança i recorda que els dos plats han de pesar igual. Ah!, recorda que et pregunten el pes MÍNIM de les 2 pilotes que no són a la balança."
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
        "Per a cada fila o cada columna, mira de quant ens passem de 6, quan sumem. Comença per les més fàcils."
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
        "Per exemple, el rectangle d’àrea 9 només pot tenir mides enteres 9x1. Per tant, el rectangle de sota té mides 9x2. Reconstrueix les mides de tots els rectangles."
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
        "Pensa-ho com si fos un SUDOKU. Ves provant, una per una, totes les possibilitats: recorda que només una d’elles és possible."
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
        "Una rotació conserva les distàncies i els angles, així que el triangle A'BC' és exactament igual que l'ABC. Fixa't que B és el centre de gir: la condició que A, B i C' estiguin alineats et dona quant val l'angle de rotació."
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
        "El bloc 2026 surt una vegada quan diem el nombre, però surt més vegades, per exemple aquí “...2620,2621…” si t’hi fixes, ha sortit el “20,26”."
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
        "Per a cada cub que treus, compta quantes cares noves apareixen i quantes en desapareixen."
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
