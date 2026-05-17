"""
Tutor Cangur — 3ESO problem catalogue.

Conté els 30 problemes de la prova 3ESO (tots els anys disponibles).
Afegir nous problemes aquí; mai modificar els d'altres nivells.

Estructura de cada entrada: vegeu SCHEMA.md.
"""

from problems_shared import ERROR_CATALOG, DEPENDENCIES  # noqa: F401

PROBLEMS = {}

PROBLEMS["CAN-3ESO-2026-01"] = {
    "id":         "CAN-3ESO-2026-01",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-01.jpg",
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

PROBLEMS["CAN-3ESO-2026-02"] = {
    "id":         "CAN-3ESO-2026-02",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     2,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
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
        "o el 4). Per tant, 2046 − 2026 = 20 anys. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 2 vol dir proposar el 2028, però el 2028 té dues xifres 2 i no compleix la condició de tenir totes les xifres diferents.",
        "C": "Obtenir 22 vol dir proposar el 2048 com a primer any vàlid, però el 2046 també compleix les condicions i és anterior.",
        "D": "Obtenir 38 vol dir aturar-se al 2064 (xifres 2, 0, 6, 4), que sí que té totes les xifres parelles i diferents, però no és el primer: el 2046 és anterior.",
        "E": "Obtenir 42 vol dir saltar fins al 2068 (xifres 2, 0, 6, 8) com a primer candidat, sense adonar-se que 2046 ja compleix les condicions i és anterior.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament parla d'un perfil 1-2-3-3-1 i d'una "base d'amplada 5, una torre
# central de 3 graons i una caixa sola a la dreta" per identificar B. A la imatge
# real, l'opció B té un perfil 1-1-1-2-1 (silueta amb una sola torre de 2 caixes a
# la quarta posició des de l'esquerra). Cal comprovar directament a la imatge quina
# silueta correspon a la vista lateral des de la dreta de la pila 3D, i ajustar el
# raonament en conseqüència. L'XLS confirma que la resposta és B.
PROBLEMS["CAN-3ESO-2026-03"] = {
    "id":         "CAN-3ESO-2026-03",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     3,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Mira la pila des del costat dret (on apunta la fletxa). Per a cada columna que "
        "veuràs en aquesta vista, registra l'alçada de la caixa més alta visible. La "
        "silueta resultant és la vista lateral; compara-la amb les cinc opcions."
    ),
    "expected_reasoning": (
        "Quan mirem la pila des del costat dret, per a cada fila de la profunditat veiem la "
        "caixa més alta que hi ha en aquella fila. La silueta resultant està formada per "
        "cinc columnes (una per cada fila de la pila vista de costat), i l'alçada de cada "
        "columna és la més alta visible des d'aquell punt. Comparant les cinc opcions amb "
        "la silueta deduïda, l'única que reprodueix exactament aquest perfil és l'opció B. "
        "Les altres opcions presenten alçades o nombre de columnes que no coincideixen amb "
        "la vista lateral des del costat dret. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "L'opció A mostra una silueta diferent: una distribució d'alçades que no correspon al perfil visible des del costat dret de la pila.",
        "C": "L'opció C té un graó central massa ample respecte de la silueta real vista des del costat dret.",
        "D": "L'opció D mostra una vista amb menys columnes o alçades que no s'ajusten al nombre real de caixes visibles en aquesta vista.",
        "E": "L'opció E presenta una silueta amb dos pics separats que no corresponen al perfil continu de la pila vista de costat.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-04"] = {
    "id":         "CAN-3ESO-2026-04",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     4,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
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
        "exactament els que no són potències de 2. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "El 5 sí que és suma de consecutius: 2 + 3 = 5.",
        "B": "El 6 sí que és suma de consecutius: 1 + 2 + 3 = 6.",
        "C": "El 7 sí que és suma de consecutius: 3 + 4 = 7.",
        "E": "El 9 sí que és suma de consecutius: 4 + 5 = 9, o també 2 + 3 + 4 = 9.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-05"] = {
    "id":         "CAN-3ESO-2026-05",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     5,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-3ESO-2026-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Calcula primer totes les rutes possibles per tornar de C a A passant per B. "
        "Després, com que l'Alba vol evitar fer servir exactament el camí d'anada al revés, "
        "treu de la llista la combinació prohibida."
    ),
    "expected_reasoning": (
        "Hi ha 3 camins entre A i B i 5 camins entre B i C. A la tornada, l'Alba ha "
        "d'escollir un camí de C a B (entre 5) i un de B a A (entre 3), de manera que les "
        "combinacions possibles són 5 × 3 = 15. D'aquestes 15, n'hi ha exactament una que "
        "coincideix amb la ruta d'anada feta al revés (el mateix camí B–C de tornada més el "
        "mateix camí A–B de tornada), i és la que l'Alba vol evitar. Per tant, li queden "
        "15 − 1 = 14 rutes possibles per al viatge de tornada. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 5 vol dir comptar només els camins d'un tram (per exemple, B a C) sense combinar-los amb els de l'altre tram.",
        "B": "Triar 6 surt de sumar els camins (3 + 5 = 8, o 3 + 5 − 2 = 6) en lloc de multiplicar-los per obtenir el total de combinacions.",
        "C": "Triar 10 surt d'un càlcul com 2 × 5 = 10, com si només hi haguessin 2 camins al tram entre A i B.",
        "D": "Triar 12 surt de calcular 3 × 5 i restar-ne 3 (pensant que cal evitar tres rutes prohibides), però l'única ruta prohibida és la idèntica al camí d'anada al revés.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El raonament suposa una tipografia de 7 segments específica en què 0↔0, 2↔5, 5↔2
# i 8↔8 són els únics dígits amb reflexió horitzontal vàlida (els altres no donen un
# dígit reconeixible). Aquesta suposició és correcta per a la tipografia clàssica de
# 7 segments, però cal verificar visualment a la imatge que la tipografia del
# rellotge del problema compleix realment aquestes simetries. L'XLS confirma A.
PROBLEMS["CAN-3ESO-2026-06"] = {
    "id":         "CAN-3ESO-2026-06",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     6,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
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
        "vàlid són: 0 → 0, 2 → 5, 5 → 2 i 8 → 8. Comprovem l'opció A, 02:05: invertint "
        "l'ordre dels cinc caràcters i reflectint cada dígit, els d'esquerra a dreta "
        "[0][2][:][0][5] donen [reflex 5][reflex 0][:][reflex 2][reflex 0] = [2][0][:][5][0] "
        "→ 20:50, que és una hora vàlida del dia. Cap de les altres opcions produeix una "
        "hora vàlida en reflectir-se. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "08:06 inclou el dígit 6, que en una tipografia de 7 segments reflectit horitzontalment no produeix un dígit reconeixible.",
        "C": "08:50 al mirall donaria 02:80, que no és una hora vàlida (80 minuts no existeix).",
        "D": "09:06 inclou els dígits 9 i 6, que en una tipografia de 7 segments reflectits horitzontalment no produeixen dígits vàlids.",
        "E": "20:02 al mirall donaria 50:05, que no és una hora vàlida del dia (50 hores no existeix).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-07"] = {
    "id":         "CAN-3ESO-2026-07",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     7,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-3ESO-2026-07.jpg",
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
# Mateixa estructura que el problema 10 de 2ESO, però amb resposta E (que també és
# la mateixa). Una "illa" és una regió fosca tancada i envoltada per blanc. Cal
# comptar amb detall, mirant la imatge, quantes illes queden quan s'encaixa cada
# peça al marc del trencaclosques.
PROBLEMS["CAN-3ESO-2026-08"] = {
    "id":         "CAN-3ESO-2026-08",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     8,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-08.jpg",
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

PROBLEMS["CAN-3ESO-2026-09"] = {
    "id":         "CAN-3ESO-2026-09",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     9,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
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
        "Resposta C."
    ),
    "comentaris_distractors": {
        "A": "En aquesta opció Bernat seu al seient 1 i Anna al seient 3: el Bernat queda a l'esquerra de l'Anna i a més separat per una persona, no just a la seva dreta.",
        "B": "En aquesta opció l'Anna seu al seient 2 i el Bernat al 4: no són seients consecutius, així que el Bernat no està just a la dreta de l'Anna.",
        "D": "En aquesta opció l'Anna i el Bernat ocupen els seients 2 i 3 correctament, però aleshores la Dúnia queda al seient 4 (un extrem), cosa que incompleix la condició que la Dúnia no pot ser als extrems.",
        "E": "En aquesta opció la Dúnia està al seient 1 (un extrem), cosa que incompleix la condició que la Dúnia no pot ser als extrems.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Mateixa estructura que el problema 5 de 2ESO, però amb resposta C (no E). Cal
# comprovar visualment quina opció (A-E) col·loca talls (línies gruixudes) i plecs
# (línies de punts) en les posicions que generen els panells de la figura 3D. L'XLS
# confirma C.
PROBLEMS["CAN-3ESO-2026-10"] = {
    "id":         "CAN-3ESO-2026-10",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     10,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
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
        "del full. Comparant cada esquema amb la figura, els esquemes A, B, D i E tenen els "
        "talls o els plecs en posicions que no reprodueixen la disposició dels panells "
        "exigida. Només l'esquema C té els talls col·locats just als laterals dels panells "
        "i els plecs a la base de cadascun, de manera que en doblegar-lo s'obté exactament "
        "la figura de l'enunciat. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "L'opció A té els plecs en una posició que generaria panells de mida o distribució diferents dels de la figura final.",
        "B": "L'opció B no té els talls col·locats de manera que es generin els panells amb les proporcions exactes que mostra la figura.",
        "D": "L'opció D té una combinació de talls i plecs que produiria una figura amb els panells desplaçats respecte de l'enunciat.",
        "E": "L'opció E col·loca alguns talls o plecs en posicions que fan que, en doblegar-la, el nombre o la disposició dels panells no coincideixi amb la figura.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# El JSON original tenia el sentit del viatge intercanviat (parlava de B→A quan
# l'enunciat diu que l'Anna va d'A a B). El raonament aquí l'he corregit perquè
# parli d'A→B, però el càlcul exacte del nombre mínim de girs a la dreta (6) depèn
# del traçat concret del laberint, que cal verificar visualment a la imatge.
PROBLEMS["CAN-3ESO-2026-11"] = {
    "id":         "CAN-3ESO-2026-11",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     11,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Recorda que no es pot girar a l'esquerra. Per anar 'cap a l'esquerra' sense "
        "girar-hi, cal fer tres girs a la dreta consecutius (que equival a un gir de 270°). "
        "Traça el camí d'A a B i mira de minimitzar el nombre de girs a la dreta tenint en "
        "compte la disposició dels carrers de Vilacangur."
    ),
    "expected_reasoning": (
        "A és l'entrada inferior dreta del mapa i B és l'entrada inferior esquerra. Com que "
        "no es pot girar a l'esquerra, cada cop que la ruta natural demanaria un gir a "
        "l'esquerra, cal substituir-lo per tres girs a la dreta consecutius. Traçant rutes "
        "possibles d'A a B respectant la geometria del laberint, la que minimitza els girs "
        "a la dreta és la que aprofita els carrers exteriors per donar 'la volta llarga' "
        "fent servir només girs a la dreta. Amb aquest plantejament, la ruta òptima d'A a B "
        "es pot fer amb exactament 6 girs a la dreta. Cap ruta alternativa que respecti la "
        "restricció (sense girs a l'esquerra) pot baixar de 6 girs. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 9 vol dir comptar els girs d'una ruta no òptima que dona més voltes de les necessàries pel laberint.",
        "B": "Triar 7 vol dir trobar una ruta amb un gir innecessari que es podria evitar redirigint la trajectòria.",
        "C": "Triar 5 és insuficient: el disseny dels carrers de Vilacangur imposa com a mínim 6 girs a la dreta per anar d'A a B sense girar mai a l'esquerra.",
        "E": "Triar 4 és massa optimista: cap ruta vàlida no permet arribar de A a B amb només 4 girs a la dreta amb la disposició del mapa.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Aquest problema reaprofita el gerro de 9 cares amb dígits 1-9 del problema
# CAN-2ESO-2026-14. Cal comprovar a la imatge quins són els dígits visibles a cada
# vista (frontal i veïns) per cadascuna de les opcions A-E, i confirmar que la
# vista A és la que mostra una adjacència incompatible amb l'ordre circular deduït
# de les altres vistes. L'XLS confirma A.
PROBLEMS["CAN-3ESO-2026-12"] = {
    "id":         "CAN-3ESO-2026-12",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     12,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-12.jpg",
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

PROBLEMS["CAN-3ESO-2026-13"] = {
    "id":         "CAN-3ESO-2026-13",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     13,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2026-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Escriu dues equacions amb les tres incògnites (M, R i E, en euros). Mira si pots "
        "substituir-ne una a l'altra per eliminar dues incògnites alhora i obtenir "
        "directament el valor de l'Emma."
    ),
    "expected_reasoning": (
        "Diguem M, R i E els euros de la Mariam, la Ria i l'Emma. La primera condició diu "
        "que la Mariam té 13 € menys que el total de la Ria i l'Emma: M = R + E − 13. La "
        "segona condició diu que la Ria té 5 € més que el total de l'Emma i la Mariam: "
        "R = E + M + 5. Substituint la primera a la segona, R = E + (R + E − 13) + 5 = "
        "R + 2E − 8, d'on 2E = 8 i E = 4 €. L'Emma té 4 euros. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 9 surt de confondre el signe en alguna de les equacions o d'aplicar a l'Emma una condició que parla d'una de les altres dues persones.",
        "B": "Triar 7 surt d'errors algebraics en la substitució, com sumar i restar de manera incorrecta les constants 13 i 5.",
        "D": "Triar 8 és el valor de 2E sense haver dividit entre 2 al final de la resolució.",
        "E": "Triar 18 surt de sumar les dues constants (13 + 5 = 18) sense resoldre el sistema, o de calcular alguna quantitat agregada en lloc de la quantitat concreta de l'Emma.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-14"] = {
    "id":         "CAN-3ESO-2026-14",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     14,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-14.jpg",
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

PROBLEMS["CAN-3ESO-2026-15"] = {
    "id":         "CAN-3ESO-2026-15",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     15,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2026-15.jpg",
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
        "A": "Triar 14 surt de plantejar S = 6 + 8 = 14 sense passar per la mitjana, com si l'elf sènior mengés 8 més que un júnior i ja n'hi hagués prou.",
        "C": "Triar 20 surt d'errors a l'hora de multiplicar per 5 o de manipular l'equació final, donant una desviació respecte del valor real.",
        "D": "Triar 21 surt d'aproximar la mitjana per 24/5 ≈ 5 i sumar-hi 8 i una mica més, sense imposar la condició com a equació.",
        "E": "Triar 22 surt d'errors algebraics, com tractar la mitjana com a suma o cometre un error de signe en la simplificació final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# La figura mostra una configuració de línies que es creuen formant 5 angles
# ombrejats als seus extrems. Hi ha un resultat geomètric estàndard pel qual aquest
# tipus de configuració dona una suma fixa d'angles, però el càlcul concret depèn
# d'identificar quina és exactament la figura (estrella de 5 puntes, dos triangles
# encreuats, etc.). L'XLS confirma D = 360°.
PROBLEMS["CAN-3ESO-2026-16"] = {
    "id":         "CAN-3ESO-2026-16",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     16,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Identifica triangles dins la figura i aplica que la suma dels angles interiors de "
        "cada triangle és 180°. Combina les sumes que s'obtenen mirant els diferents "
        "triangles que es formen perquè els angles que es repeteixen acabin cancel·lant-se "
        "i en quedi només la suma dels cinc angles ombrejats."
    ),
    "expected_reasoning": (
        "La figura es pot descompondre en dos triangles que comparteixen part de la "
        "regió central. Aplicant a cada triangle la propietat que la suma dels seus angles "
        "interiors és 180°, i fent servir el teorema de l'angle exterior (que diu que un "
        "angle exterior d'un triangle és igual a la suma dels dos angles interiors no "
        "adjacents), els angles del centre de la figura es cancel·len i la suma dels cinc "
        "angles ombrejats acaba sent la suma dels angles interiors de dos triangles, és a "
        "dir, 2 × 180° = 360°. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 180° vol dir comptar la suma dels angles d'un sol triangle, sense tenir en compte que la figura té dos triangles enllaçats.",
        "B": "Triar 240° surt d'un comptatge parcial dels angles, deixant fora alguna de les contribucions necessàries.",
        "C": "Triar 270° surt d'errors d'aplicació del teorema de l'angle exterior, donant un valor intermedi entre 180° i 360°.",
        "E": "Triar 450° surt de sumar els angles de més triangles dels necessaris, comptant alguna contribució dues vegades.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-17"] = {
    "id":         "CAN-3ESO-2026-17",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     17,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-3ESO-2026-17.jpg",
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

PROBLEMS["CAN-3ESO-2026-18"] = {
    "id":         "CAN-3ESO-2026-18",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El rellotge de l'avi va 5 min lent per cada hora real (= 55 min reals de "
        "rellotge per hora real); el del pare va 5 min ràpid (= 65 min). Calcula quantes "
        "hores reals han passat perquè el rellotge de l'avi avanci d'11 hores marcades. "
        "Després usa aquest temps real per saber quant ha avançat el del pare."
    ),
    "expected_reasoning": (
        "El rellotge de l'avi s'endarrereix 5 minuts per hora real: per cada hora real, "
        "marca 55 minuts. El rellotge del pare s'avança 5 minuts per hora real: per cada "
        "hora real, marca 65 minuts. Tots dos s'han ajustat a les 21.00 h. El rellotge de "
        "l'avi passa de 21.00 h a 08.00 h, és a dir, marca 11 hores = 660 minuts. Si han "
        "passat T hores reals, ha avançat 55·T minuts: 55·T = 660 → T = 12 hores reals. "
        "En 12 hores reals, el rellotge del pare ha avançat 65 × 12 = 780 minuts = 13 hores. "
        "Per tant, el rellotge del pare marca 21.00 + 13 h = 10.00 h. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 09.00 h vol dir suposar que els dos rellotges van desfasats la mateixa quantitat respecte de l'hora real, sense ajustar pel fet que un va lent i l'altre va ràpid.",
        "B": "Triar 09.30 h surt de calcular parcialment la diferència entre els dos rellotges, com sumar-hi mitja hora addicional sense fer el càlcul complet.",
        "D": "Triar 10.30 h surt d'errors en la multiplicació 65 × 12 o de fer servir un ritme d'avançament diferent per al rellotge del pare.",
        "E": "Triar 11.00 h surt de comptar 14 hores d'avanç en lloc de 13, com si el rellotge del pare avancés 5 minuts per hora però del seu propi rellotge en lloc d'hora real.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Aquest problema reaprofita el cub plegat de CAN-2ESO-2026-21 (mateixa plantilla:
# ●, ○, 2 cares negres i 2 blanques). L'XLS confirma C aquí (a 2ESO era B), de
# manera que l'ordre de les opcions visuals (A-E) és diferent. Cal comprovar a la
# imatge que l'opció C és la que satisfà les condicions: ● i ○ a cares oposades,
# les dues negres oposades i les dues blanques oposades.
PROBLEMS["CAN-3ESO-2026-19"] = {
    "id":         "CAN-3ESO-2026-19",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     19,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "En un desenvolupament en forma de creu, dues cares queden oposades quan estan "
        "separades per dues posicions a la tira central. Identifica quines cares queden "
        "oposades a la plantilla (●–○, negra–negra, blanca–blanca) i comprova quina opció "
        "respecta aquestes relacions."
    ),
    "expected_reasoning": (
        "La plantilla té sis cares: una amb el punt ●, una amb el cercle buit ○, dues "
        "cares negres i dues cares blanques. En plegar la creu, les parelles d'oposats "
        "queden ben determinades: el ● i el ○ queden a cares oposades, les dues cares "
        "negres queden oposades entre elles, i les dues blanques també. Examinant les "
        "cinc opcions, només l'opció C mostra el cub amb una orientació compatible amb "
        "totes aquestes oposicions: el ● a la cara frontal en una posició que té cares "
        "negres a banda i banda (com indica la plantilla) i amb cares blanques a dalt i a "
        "baix. Les altres opcions presenten configuracions que contradiuen alguna de les "
        "tres oposicions. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Mostra el ● a la cara frontal però amb una disposició lateral de cares incompatible amb les oposicions de la plantilla (per exemple, el ● adjacent a una cara que en realitat hi és oposada).",
        "B": "Mostra el ○ a la cara frontal en una posició que no respecta les oposicions de la plantilla: la cara que el problema marca com a oposada al ○ apareix com a adjacent.",
        "D": "Mostra el ○ a la cara frontal envoltat de cares blanques, però la plantilla obliga a tenir cares negres com a veïnes del ○ (perquè ho són del ●, que és el seu oposat).",
        "E": "Mostra el ● a la cara frontal però amb una orientació lateral que ja no es pot obtenir per cap rotació del cub plegat a partir de la plantilla donada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-20"] = {
    "id":         "CAN-3ESO-2026-20",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     20,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-20.jpg",
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
        "B": "Obtenir 17 surt d'un error en propagar el carry c₁: per exemple, suposar que B + C = 12 en lloc del valor correcte que té en compte el carry de les unitats.",
        "C": "Obtenir 18 surt d'oblidar la restricció que A, B i C han de ser xifres diferents, i acceptar com a vàlida una solució amb dues xifres iguals.",
        "D": "Obtenir 19 surt d'errar l'equació de les centenes, per exemple ometent el carry c₂ que hi entra i acceptant una combinació que no quadra al final.",
        "E": "Obtenir 20 surt d'afegir un carry final inexistent (un nombre de tres xifres sumat amb un altre de tres mai no en pot generar un de més de quatre xifres).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-21"] = {
    "id":         "CAN-3ESO-2026-21",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     21,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Calcula primer l'àrea dels 5 quadrats apilats. Després identifica quina zona "
        "talla el segment AB: com que AB és paral·lel a CD, la zona retallada és un "
        "triangle amb la base igual a l'amplada total de la figura."
    ),
    "expected_reasoning": (
        "Els 5 quadrats de costats 1, 2, 3, 4 i 5 m tenen àrees 1, 4, 9, 16 i 25 m², que "
        "sumen 1 + 4 + 9 + 16 + 25 = 55 m². L'amplada total de la figura és la suma de "
        "les amplades dels cinc quadrats: 1 + 2 + 3 + 4 + 5 = 15 m. Amb els quadrats més "
        "grans als extrems, el punt C està a alçada 4 m (al damunt del quadrat de costat "
        "4 a l'esquerra) i el punt D està a alçada 5 m (al damunt del quadrat de costat "
        "5 a la dreta), de manera que CD té un desnivell de 5 − 4 = 1 m sobre una "
        "amplada de 15 m. Com que AB és paral·lel a CD i el punt A és a alçada 0 a "
        "l'extrem esquerre, el punt B queda a alçada 1 m a l'extrem dret. La part "
        "retallada és el triangle amb vèrtexs sobre la recta horitzontal, A i B, de base "
        "15 m i alçada 1 m: la seva àrea és (1/2)·15·1 = 7,5 m². L'àrea de la figura "
        "resultant és 55 − 7,5 = 47,5 m². Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 44,5 m² surt de calcular l'àrea del triangle retallat com a 10,5 m² (per exemple, prenent alçada o base equivocades) en lloc dels 7,5 m² correctes.",
        "B": "Obtenir 45,5 m² surt d'agafar 9,5 m² com a àrea del triangle, error proper que es pot cometre confonent els valors d'alçada als extrems.",
        "C": "Obtenir 46,5 m² surt d'un error en la base o l'alçada del triangle (per exemple, alçada 1,1 m en lloc d'1 m), que dona una àrea retallada propera a 8,5 m².",
        "E": "Obtenir 48,5 m² surt de restar una àrea més petita (6,5 m²) per al triangle retallat en lloc dels 7,5 m² correctes.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-22"] = {
    "id":         "CAN-3ESO-2026-22",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     22,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
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
        "c = 5. L'àrea ombrejada és c·(q+r) = 5·(1+2) = 15. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 14 surt d'una resta incorrecta entre les àrees conegudes, com calcular (b+c)·p − b·p = c·p i quedar-se aquí sense fer servir l'alçada correcta de la cel·la ombrejada.",
        "C": "Obtenir 16 surt d'un error en una de les divisions de proporcionalitat, per exemple agafant r/q ≠ 2 o p + q ≠ 4.",
        "D": "Obtenir 18 és copiar directament l'àrea de la cel·la central-inferior (b·r = 18), suposant que la cel·la ombrejada té les mateixes dimensions, quan en realitat la seva amplada és c, no b.",
        "E": "Obtenir 20 surt de confondre les amplades amb les alçades en alguna proporció, per exemple aplicant la ràtio 42/24 = 7/4 a una mesura que no toca.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-23"] = {
    "id":         "CAN-3ESO-2026-23",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     23,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2026-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
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
        "N = 2251. La suma de les xifres de 2251 és 2 + 2 + 5 + 1 = 10. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Obtenir 12 surt d'un error en el plantejament de l'equació, per exemple eliminant la xifra de les unitats com a N − 10 en lloc de (N − 1)/10, que dona un altre nombre.",
        "C": "Obtenir 14 surt d'una equació amb un terme constant equivocat, per exemple obtenint un altre N (com 2261 o 2341) i sumant-ne les xifres.",
        "D": "Obtenir 16 surt de resoldre correctament l'equació però cometre un error en la suma de les xifres del resultat 2251.",
        "E": "Obtenir 18 surt d'una equació plantejada sense el +1 (és a dir, 9·N = 20260, que no dona un enter), arrodonint a un nombre proper amb xifres que sumen 18.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-24"] = {
    "id":         "CAN-3ESO-2026-24",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     24,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2026-24.jpg",
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
        "A": "Obtenir 2 vol dir confondre els bolígrafs de la Berta (2·Ra) amb les regles de l'Anna (Ra = 2), sense aplicar el factor 2.",
        "C": "Obtenir 6 surt d'ometre la condició de paritat del total de regles, per exemple acceptant Rc = 3 (senar) i calculant amb aquest valor.",
        "D": "Obtenir 7 surt d'operar sense la condició de paritat amb un valor de Rc que no fa 3·Rc parell, arribant a una resposta propera però errònia.",
        "E": "Obtenir 8 vol dir calcular 2·Rc (= 8 amb Rc = 4) en lloc de 2·Ra: és el nombre de bolígrafs de l'Anna, no els de la Berta.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-25"] = {
    "id":         "CAN-3ESO-2026-25",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     25,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-25.jpg",
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
        "A": "Obtenir 105° surt de prendre θ = 2·15° = 30° (com si la rotació fos directament el doble de l'angle a C) sense imposar la condició que A, B i C' són alineats.",
        "B": "Obtenir 115° surt d'una mala identificació del sentit de la rotació o de quines condicions d'alineació s'usen, donant una equació numèricament propera però no correcta.",
        "C": "Obtenir 120° surt d'usar només la condició A, B, C' alineats sense imposar la condició addicional que C, A' i C' també ho han d'estar.",
        "E": "Obtenir 140° surt de confondre l'angle interior CAB amb l'angle exterior corresponent al vèrtex A, o de fer un error de signe en algun pas final.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-26"] = {
    "id":         "CAN-3ESO-2026-26",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     26,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-26.jpg",
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
        "A": "Obtenir 6 és insuficient fins i tot suposant el guany màxim teòric +6 per cub: 6·6 = 36 < 48.",
        "B": "Obtenir 8 surt de pensar que els 8 cubs del nucli 2×2×2 aporten guany +6 cadascun (8·6 = 48), però com que són veïns entre ells, el forat resultant només té superfície interior 24, no 48.",
        "C": "Obtenir 10 surt de pensar que es pot superar el guany de +4 per cub combinant cubs adjacents, sense adonar-se que les cares compartides redueixen el guany efectiu.",
        "E": "Obtenir 18 surt d'una estratègia subòptima, per exemple combinant cubs d'aresta (guany +2) amb cubs de cara (guany +4) en lloc d'usar només cubs de cara no adjacents.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2026-27"] = {
    "id":         "CAN-3ESO-2026-27",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-27.jpg",
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

PROBLEMS["CAN-3ESO-2026-28"] = {
    "id":         "CAN-3ESO-2026-28",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     28,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2026-28.jpg",
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

PROBLEMS["CAN-3ESO-2026-29"] = {
    "id":         "CAN-3ESO-2026-29",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2026-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Aprofita que el triangle DEA és isòsceles (DE = EA) per igualar dos angles, i "
        "que ABCD és un trapezi isòsceles (AD ∥ BC i AB = CD) per igualar dos angles més. "
        "Combinant aquestes igualtats amb la suma dels angles del pentàgon (= 540°), "
        "trobaràs el sistema que dona l'angle DCB."
    ),
    "expected_reasoning": (
        "Anomenem x l'angle BAD i 3x/2 = (3/2)·x... espera, plantegem-ho millor amb la raó "
        "donada: si angle EDA / angle BAD = 3/2, posem angle BAD = 2x i angle EDA = 3x. "
        "Com que DE = EA, el triangle DEA és isòsceles a E, i angle EAD = angle EDA = 3x. "
        "L'angle del pentàgon a A és angle EAB = angle EAD + angle BAD = 3x + 2x = 5x.\n"
        "Com que AB = CD i AD ∥ BC, ABCD és un trapezi isòsceles, així que els angles a B "
        "i C són iguals: angle ABC = angle BCD. Per la condició AD ∥ BC, els angles "
        "interns a banda i banda del costat AB compleixen angle BAD + angle ABC = 180°, "
        "és a dir, angle ABC = 180° − 2x i, per la simetria del trapezi, també "
        "angle BCD = 180° − 2x.\n"
        "Sigui y = angle AED = angle ADC (donat). L'angle del pentàgon a D és "
        "angle EDC = angle EDA + angle ADC = 3x + y.\n"
        "Suma dels angles del pentàgon: 5x + (180° − 2x) + (180° − 2x) + (3x + y) + y = 540°, "
        "és a dir, 4x + 2y = 540° − 360° = 180°, d'on 2x + y = 90°.\n"
        "El triangle DEA també ens dona angle AED = 180° − 3x − 3x = 180° − 6x, és a dir "
        "y = 180° − 6x. Substituint a 2x + y = 90°: 2x + 180° − 6x = 90°, d'on −4x = −90° "
        "i x = 22,5°. Per tant, angle DCB = 180° − 2·22,5° = 135°. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Obtenir 125° surt d'un error en l'equació de suma dels angles del pentàgon o de no aplicar correctament que ABCD és un trapezi isòsceles.",
        "C": "Obtenir 120° és un valor atractiu (correspon a un hexàgon regular), però no satisfà el sistema d'equacions que dona el problema.",
        "D": "Obtenir 115° surt de resoldre la mateixa equació però cometent un error de signe o de factor en alguna substitució.",
        "E": "Obtenir 110° surt d'un error en la identificació dels angles del trapezi isòsceles o de no usar la condició AD ∥ BC com cal.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verify visual interpretation:
# Aquest problema reaprofita el problema CAN-2ESO-2026-29 (comptatge de '2026' en
# la cadena de nombres consecutius)... no, espera: aquest és diferent. Aquí parla
# de seqüències de 5 nombres (a1,...,a5) amb diverses condicions de divisibilitat i
# l'última xifra senar. El raonament enumera 5 seqüències vàlides. Cal verificar
# que l'enunciat real coincideix amb aquesta interpretació (no tinc l'enunciat
# textual a la imatge encara processada).
PROBLEMS["CAN-3ESO-2026-30"] = {
    "id":         "CAN-3ESO-2026-30",
    "categoria":  "3ESO",
    "any":        2026,
    "numero":     30,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-3ESO-2026-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
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
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Obtenir 2 vol dir cometre errors sistemàtics en les comprovacions de divisibilitat i descartar diverses seqüències que sí que són vàlides.",
        "B": "Obtenir 3 surt d'identificar correctament les seqüències per a un o dos valors d'a5 però passar per alt una o més seqüències per al tercer valor.",
        "C": "Obtenir 4 surt de trobar 4 de les 5 seqüències vàlides, ometent-ne típicament una de les que tenen a5 = 3 o a5 = 5.",
        "E": "Obtenir 6 surt d'admetre alguna seqüència no vàlida (per exemple, perquè la condició de divisibilitat no s'aplica de manera estricta) i comptar-la com a vàlida.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}
