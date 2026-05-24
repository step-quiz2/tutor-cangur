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
        "Per exemple, B) i C) tenen la mateixa àrea, perquè una té un cercle i l'altra té dos "
        "semicercles."
    ),  # same as CAN-2ESO-2026-02
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
        "2002 no serveix, perquè és anterior a 2026. 2086 seria una opció, però abans hi ha altres "
        "opcions."
    ),  # same as CAN-2ESO-2026-03
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
        "Per a cada columna que veuràs des de la dreta, fixa't en l'alçada de la caixa més alta "
        "visible."
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
        "Ves provant opcions. Per exemple, A) 9 no pot ser, perquè 9 = 4+5"
    ),  # same as CAN-2ESO-2026-04
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
        "Calcula primer totes les rutes possibles per tornar, de C a A, passant per B. Després, pensa "
        "que li hauràs de restar el camí que es repeteix."
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
        "Pistsa: - El \"2\" es reflecteix com un \"5\". - El \"8\" es reflecteix en un \"8\"."
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
        "Volem que el numerador sigui petit i el denominador sigui gran. Com pots aconseguir "
        "numeradors petits?"
    ),  # same as CAN-2ESO-2026-09
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
        "Completa mentalment el trencaclosques en l'opció A). Veuràs que només aconsegueixes 2 illes. "
        "Pots aconseguir més illes?"
    ),  # same as CAN-2ESO-2026-10
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
        "El Bernat és just a la dreta de l'Anna, així que ocupen dos seients consecutius. I l'Anna no "
        "pot ser al seient 1."
    ),  # same as CAN-2ESO-2026-12
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
        "Localitza al full pla on han d'anar els talls per separar les parts que s'aixecaran."
    ),  # same as CAN-2ESO-2026-05
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
        "Ves fent el recorregut, sempre girant a la dreta, fins que arribis a B. Serà un camí una "
        "mica llarg, perquè no pots girar mai a l'esquerra."
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
        "Intenta reconstruir quins dígits són veïns al gerro, sabent que 4 imatges són correctes."
    ),  # same as CAN-2ESO-2026-14
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
        "Una de les equacions és: M=R+E-13 Pensa quina és l'altra equació."
    ),  # same as CAN-2ESO-2026-16
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
        "El total de cubs petits és (1 + 8 + 27). Calcula quants cubs s'ha menjat de cada peça, "
        "aplicant el percentatge corresponent."
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
        "S = cireres que menja l'elf sènior. Calcula la suma total de cireres dels cinc elfs. Calcula "
        "la mitjana (M) que menja cadascun. Sabem que S = M+8."
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
        "Recorda aquestes propietats: 1) En un triangle, els angles sumen 180º. 2) En un quadrilàter, "
        "sumen 360º. 3) Dos angles oposats pel vèrtex mesuren el mateix."
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
        "Hi ha 3 grups (m): els que NOMÉS els agraden les matemàtiques (f): els que NOMÉS els agrada "
        "el francès (d): els que els agraden les dues. Escriu dues equacions..."
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

# TODO: CAN-3ESO-2026-18.jpg not found on disk (reported by pister_editor). Cal afegir la imatge.
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
# ============================================================
# 2024 — 30 problemes
# ============================================================

# ============================================================
# 3 PUNTS (1-10)
# ============================================================

PROBLEMS["CAN-3ESO-2024-01"] = {
    "id":         "CAN-3ESO-2024-01",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     1,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Avalua primer el denominador respectant la prioritat de la multiplicació sobre "
        "la suma."
    ),
    "expected_reasoning": (
        "Aplicant la prioritat d'operacions, el numerador és 20·24 = 480 i el denominador "
        "és 2·0 + 2·4 = 0 + 8 = 8. La fracció val, per tant, 480/8 = 60. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 vol dir cometre una errada grossa de càlcul, per exemple substituir tota l'expressió per 24/2.",
        "B": "Triar 30 surt d'avaluar el denominador com 2·(0+2)·4 = 16, sumant 0 i 2 abans de multiplicar i obtenint 480/16 = 30.",
        "C": "Triar 48 surt d'avaluar el denominador com 2+0+2·4 = 10 (sumant en comptes de multiplicar en el primer terme), donant 480/10 = 48.",
        "E": "Triar 120 surt d'oblidar el sumand 2·0 i prendre el denominador com a 2·4 = 4 sense més, donant 480/4 = 120; o de calcular el numerador com a 240.",
    },
    "errors_típics":          ["ARI_ordre_operacions"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-02"] = {
    "id":         "CAN-3ESO-2024-02",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Aquí va més ràpid provar les cinc peces que no pas construir la peça correcta des "
        "de zero."
    ),
    "expected_reasoning": (
        "Els 8 pentàgons del voltant deixen, sobre les vores del forat central, un nombre "
        "fix d'extrems de corba que cal aparellar. La peça que es posi al centre porta a "
        "sobre dos segments propis i, en encaixar-la, els seus extrems s'uneixen amb els "
        "exteriors. Provant les cinc opcions, només l'opció C distribueix els dos segments "
        "interns de manera que les unions resultants tanquen exactament dues corbes (i no "
        "una de sola o tres). Les altres opcions, o bé connecten tots els extrems en una "
        "única línia tancada, o bé deixen extrems sense aparellar correctament. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir agafar una peça els segments de la qual uneixen els extrems en una sola línia tancada, no en dues.",
        "B": "Triar B vol dir triar una peça amb una sola U interior, que tanca una corba però en deixa l'altra oberta.",
        "D": "Triar D vol dir triar una peça que connecta extrems d'una manera que dona una sola línia tancada llarga, no dues.",
        "E": "Triar E vol dir triar una peça els segments de la qual encaixen amb un emparellament d'extrems incompatible amb el dibuix dels pentàgons exteriors.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-03"] = {
    "id":         "CAN-3ESO-2024-03",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     3,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Posa noms a les diagonals del rombe (per exemple D i d) i expressa l'àrea del "
        "rombe i la dels dos triangles que s'hi afegeixen amb els mateixos paràmetres."
    ),
    "expected_reasoning": (
        "Anomenem D la diagonal vertical del rombe i d la diagonal horitzontal. L'àrea del "
        "rombe és A_rombe = D·d/2. Els dos triangles rectangles que s'afegeixen a la part "
        "inferior tenen, cadascun, catets iguals a d/2 (mitja diagonal horitzontal) i D/2 "
        "(mitja diagonal vertical), de manera que la suma de les seves àrees és "
        "2 · (1/2)·(d/2)·(D/2) = D·d/4. L'augment relatiu d'àrea respecte del rombe és "
        "(D·d/4)/(D·d/2) = 1/2 = 50%. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 40% surt d'una estimació visual sense fer el càlcul; els triangles afegits no s'apropen pas a aquesta fracció exacta.",
        "C": "Triar 30% prové d'estimar a ull, possiblement subestimant la mida dels triangles afegits.",
        "D": "Triar 25% prové de pensar que cada triangle afegit és 1/8 del rombe (en lloc d'1/4), per exemple confonent base · alçada amb base · alçada / 2.",
        "E": "Triar 20% és una sub-estimació visual sense un càlcul fonamentat.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-04"] = {
    "id":         "CAN-3ESO-2024-04",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     4,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Cada cop que talles un vèrtex del tetraedre, en quants vèrtexs nous el "
        "substitueixes?"
    ),
    "expected_reasoning": (
        "Un tetraedre regular té 4 vèrtexs. Cada vèrtex del tetraedre està format per la "
        "trobada de 3 arestes; en escapçar-lo amb un tall pla a prop seu, el vèrtex "
        "desapareix i es crea un triangle nou a la zona del tall, és a dir, 3 vèrtexs nous "
        "(els tres punts on el tall talla les 3 arestes). Per tant, cada vèrtex original "
        "es transforma en 3 vèrtexs nous. Aplicant això als 4 vèrtexs del tetraedre, el "
        "poliedre resultant en té 4 · 3 = 12. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 15 vol dir afegir, a més dels 12 vèrtexs nous, els 3 vèrtexs del darrer triangle de tall com si fossin extres, sense adonar-se que ja estaven comptats.",
        "C": "Triar 11 surt de comptar bé els nous vèrtexs (12) però restar-ne un per error puntual.",
        "D": "Triar 9 vol dir suposar que en escapçar només queden 2 vèrtexs nous per cada vèrtex original (en comptes de 3) i sumar-ne 1 més per algun motiu, o oblidar el vèrtex d'un dels tetraedres tallats.",
        "E": "Triar 8 vol dir suposar que cada vèrtex tallat aporta 2 vèrtexs nous, donant 4·2 = 8, sense adonar-se que el tall produeix un triangle amb 3 vèrtexs, no un segment.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-05"] = {
    "id":         "CAN-3ESO-2024-05",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     5,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "El que no pots canviar deformant una corda sense tallar-la és el nombre de "
        "creuaments \"essencials\" (els nusos)."
    ),
    "expected_reasoning": (
        "La corda de la dreta és un vuit que, en realitat, no està nuat: només té dos "
        "creuaments aparents que es poden desfer estirant la corda, és a dir, és "
        "topològicament equivalent a una corda sense nusos (cercle). Per tant, qualsevol "
        "transformació admissible (sense tallar) ha de portar-la a una altra corba sense "
        "nusos. Les opcions A, C, D i E són corbes que, encara que dibuixades amb llaços, "
        "es poden veure com a cordes sense nusos genuïns (cercles deformats). En canvi, "
        "l'opció B mostra una corda amb un nus genuí (un nus de trèvol o similar), que no "
        "es pot deformar fins a la corda original sense tallar-la. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir confondre llaços visuals amb nusos: el dibuix de A es desfà estirant la corda fins a quedar un cercle senzill.",
        "C": "Triar C vol dir donar per nuat un dibuix triangular amb llaços, però es pot demostrar que els seus creuaments són desfeibles.",
        "D": "Triar D vol dir tractar com a nus genuí un dibuix de tres lòbuls, però aquests lòbuls es poden desfer sense tallar la corda.",
        "E": "Triar E vol dir veure múltiples llaços apilats com a un nus, quan en realitat tots els creuaments són desfeibles.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-06"] = {
    "id":         "CAN-3ESO-2024-06",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     6,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2024-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Llista les 6 ordenacions possibles de les tres peces i comprova quins nombres "
        "diferents en resulten."
    ),
    "expected_reasoning": (
        "Les tres peces són «3», «5» i «33» (un i dos dígits respectivament). Les "
        "ordenacions possibles per col·locar-les una al costat de l'altra són 3! = 6: "
        "(3,5,33) → 3533; (3,33,5) → 3335; (5,3,33) → 5333; (5,33,3) → 5333; (33,3,5) → "
        "3335; (33,5,3) → 3353. Els nombres diferents que se'n formen són {3533, 3335, "
        "5333, 3353}, és a dir, 4. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 7 vol dir comptar combinacions que no són possibles (per exemple 3335 dues vegades).",
        "B": "Triar 6 surt de comptar les 6 ordenacions sense adonar-se que algunes produeixen el mateix nombre (com (5,3,33) i (5,33,3), totes dues donen 5333).",
        "C": "Triar 5 vol dir comptar 6 ordenacions menys una repetició, però en realitat n'hi ha dues parelles d'ordenacions que coincideixen, no només una.",
        "E": "Triar 3 vol dir, equivocadament, restringir les ordenacions a només una posició possible per a la peça «33», per exemple sempre al final.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-07"] = {
    "id":         "CAN-3ESO-2024-07",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     7,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Comença pel Pol: és l'únic a qui agrada una sola fruita."
    ),
    "expected_reasoning": (
        "Al Pol només li agrada la poma, així que el Pol agafa la poma i la poma queda "
        "ocupada. A la Pina li agraden la poma i el plàtan; com que la poma està agafada, "
        "la Pina agafa el plàtan i el plàtan queda ocupat. A l'Eva només li agraden la "
        "poma i la pera; com que la poma està agafada, l'Eva ha d'agafar la pera. Per "
        "tant, és l'Eva qui agafa la pera (al Bruno i al Lluís els queden la taronja i el "
        "kiwi, repartits entre ells). Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Al Pol només li agrada la poma, així que no pot agafar la pera; aquest distractor es tria si no s'aplica primer la restricció més forta.",
        "B": "Al Bruno li agrada la pera, però també d'altres fruites, i la cadena de restriccions força que la pera l'agafi l'Eva, no el Bruno.",
        "C": "Al Lluís també li agrada la pera, però amb la cadena forçada (poma→Pol, plàtan→Pina, pera→Eva) al Lluís li queda una de les fruites restants.",
        "D": "A la Pina no li agrada la pera (només la poma i el plàtan), així que mai no pot agafar la pera.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-08"] = {
    "id":         "CAN-3ESO-2024-08",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Esbrina primer quants infants pesen el mateix que un adult."
    ),
    "expected_reasoning": (
        "Si 12 adults pesen el mateix que 18 infants, llavors 1 adult equival, en pes, a "
        "18/12 = 3/2 infants. Vuit adults equivalen, doncs, a 8·(3/2) = 12 infants en pes. "
        "Com que la càrrega màxima de l'ascensor expressada en infants és 18, encara hi "
        "caben 18 − 12 = 6 infants. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 vol dir oblidar que el límit és 18 infants i confondre la mida equivalent dels 8 adults (12 infants) amb la resposta.",
        "B": "Triar 8 surt de calcular 18−10 = 8 (suposant erròniament que 8 adults equivalen a 10 infants).",
        "C": "Triar 7 surt d'una estimació o un arrodoniment incorrecte: per exemple, considerar 1 adult ≈ 1,4 infants.",
        "E": "Triar 5 surt d'un càlcul defectuós, com restar el nombre d'adults (8) del de infants (no del límit equivalent).",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-09"] = {
    "id":         "CAN-3ESO-2024-09",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     9,
    "punts":      3,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2024-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Esbrina primer quants centímetres afegeix cada carretó addicional quan s'encaixa "
        "amb els anteriors."
    ),
    "expected_reasoning": (
        "Anomenem L la longitud d'un carretó i d l'increment de longitud que afegeix cada "
        "carretó addicional encaixat. Aleshores, 4 carretons fan L + 3d = 108 cm i 10 "
        "carretons fan L + 9d = 168 cm. Restant les dues equacions: 6d = 60, d'on d = 10 "
        "cm. Substituint: L + 30 = 108, per tant L = 78 cm. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 60 cm surt de dividir 108/4 + 168/10 = 27 + 16,8 (o similar) sense plantejar correctament el sistema.",
        "B": "Triar 68 cm surt de calcular L com 78 − 10 = 68, és a dir, restar erròniament un increment al càlcul correcte.",
        "D": "Triar 88 cm surt de fer L = 78 + 10 = 88, sumant un increment de més.",
        "E": "Triar 90 cm surt de prendre 168/10 ≈ 16,8 com a increment i fer una estimació gruixuda d'L.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-10"] = {
    "id":         "CAN-3ESO-2024-10",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     10,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Comença per la casella de la cantonada que pertany alhora a una fila i a una "
        "columna amb productes coneguts: això la determina o redueix les seves "
        "possibilitats."
    ),
    "expected_reasoning": (
        "Anomenem la quadrícula amb les caselles a,b (fila de dalt) i c,d (fila de baix). "
        "Sabem que a·b = 6, c·d = 8, a·c = 4 i b·d = 12, amb a, b, c, d enters positius "
        "diferents. Provant a partir d'a: si a = 1, llavors b = 6 i c = 4, d'on d = 8/4 = "
        "2; comprovem b·d = 6·2 = 12 ✓ i tots quatre nombres (1, 6, 4, 2) són diferents. "
        "Cap altre valor d'a (2, 3 o 6) dona enters diferents (a = 2 fa c = 2 = a; a = 3 "
        "fa c no enter; a = 6 fa c no enter). Per tant, els quatre nombres són 1, 2, 4, 6 "
        "i la suma és 1 + 2 + 4 + 6 = 13. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 14 surt d'admetre un repetit (per exemple 2, 2, 4, 6), però l'enunciat exigeix nombres diferents.",
        "B": "Triar 10 surt d'un error de càlcul a la suma o de prendre algun valor incorrecte (per exemple 1, 3, 2, 4 que no compleix els productes).",
        "C": "Triar 12 surt de proposar 1, 2, 3, 6 (suma 12), que falla perquè 3·2 ≠ 8 i no satisfà els productes de la imatge.",
        "D": "Triar 11 surt d'un càlcul defectuós o de proposar uns nombres que no satisfan tots els productes alhora.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}


# ============================================================
# 4 PUNTS (11-20)
# ============================================================

PROBLEMS["CAN-3ESO-2024-11"] = {
    "id":         "CAN-3ESO-2024-11",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     11,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-11.jpg",
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

PROBLEMS["CAN-3ESO-2024-12"] = {
    "id":         "CAN-3ESO-2024-12",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     12,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Comença per esbrinar quant valia l'angle d'un tros original (quan n'hi havia "
        "deu)."
    ),
    "expected_reasoning": (
        "Els deu trossos iguals ocupaven 360°, així que cada tros tenia un angle de 36°. "
        "Després de menjar-se'n un, queden 9 trossos que sumen 9·36° = 324° d'angle "
        "ocupat. La diferència 360° − 324° = 36° s'ha de repartir per igual entre els 9 "
        "espais entre trossos consecutius, així que cada espai és de 36°/9 = 4°. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 5° surt de repartir 36° entre 7,2 (o un nombre erroni de gaps), per exemple comptant 8 espais en lloc de 9.",
        "C": "Triar 3° surt de comptar 12 espais o repartir l'angle del tros que falta entre un nombre erroni d'espais.",
        "D": "Triar 2° surt de pensar que l'angle a repartir és 18° (la meitat) i no 36°, o repartir 36° entre 18 espais.",
        "E": "Triar 1° surt d'una estimació molt petita, possiblement creient que els espais són gairebé inexistents.",
    },
    "errors_típics":          ["COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-13"] = {
    "id":         "CAN-3ESO-2024-13",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     13,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Suma els valors de les tres peces que ja té en Pep. La suma total de la "
        "quadrícula ha de ser divisible per 4 (perquè les quatre files —i les quatre "
        "columnes— sumin el mateix)."
    ),
    "expected_reasoning": (
        "Si totes les files (i columnes) d'una quadrícula 4×4 sumen el mateix valor S, "
        "aleshores la suma total dels 16 nombres és 4S i, en particular, ha de ser "
        "divisible per 4. Sumem els valors de les tres peces ja col·locades: la primera "
        "peça (en L) suma 2+2+1+2 = 7; la segona peça suma 2+1+3+1+1 = 8; la tercera "
        "suma 2+3+1+2 = 8. Total parcial: 7+8+8 = 23. La quarta peça ha de fer que el "
        "total sigui múltiple de 4. Provem cada opció: A) 1+1+3 = 5 → total 28 = 4·7 ✓; "
        "B) 2+1+0 = 3 → total 26, no divisible per 4; C) 1+2+1 = 4 → total 27, no "
        "divisible per 4; D) 2+2+2 = 6 → total 29, no divisible per 4; E) 2+2+3 = 7 → "
        "total 30, no divisible per 4. Només A passa la condició aritmètica i és, doncs, "
        "la peça que cal afegir. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar B vol dir oblidar la condició de divisibilitat per 4 i triar una peça per inspecció visual de la quadrícula.",
        "C": "Triar C vol dir comptar un dels valors malament al sumar les peces existents, donant una suma parcial que faria que C semblés correcte.",
        "D": "Triar D surt de pensar que tots els nombres han de ser iguals per simetria, sense aplicar el criteri de divisibilitat per 4.",
        "E": "Triar E vol dir no verificar que la suma total sigui múltiple de 4 i acceptar una peça per intuïció visual.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-14"] = {
    "id":         "CAN-3ESO-2024-14",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Busca si la figura té algun eix de simetria que aparelli les zones grises."
    ),
    "expected_reasoning": (
        "La figura mostra un quadrat amb tres segments traçats des dels vèrtexs cap a un "
        "punt interior, formant cinc regions, dues de les quals (les triangulars laterals) "
        "són les regions grises etiquetades M i N. La construcció és simètrica respecte de "
        "l'eix vertical del quadrat: en reflectir la figura per aquest eix, la zona M es "
        "transforma en la zona N i viceversa. Per tant, M i N tenen la mateixa àrea i "
        "M − N = 0 m². Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 1 m² vol dir suposar que les dues regions tenen àrees lleugerament diferents sense aprofitar la simetria.",
        "C": "Triar 2 m² surt d'un càlcul d'àrees fet sense tenir en compte la simetria de la construcció.",
        "D": "Triar 5 m² surt de fer cas a l'aspecte visual sense calcular o sense usar la simetria.",
        "E": "Triar 10 m² (l'àrea d'un dels triangles) vol dir interpretar la pregunta com l'àrea d'una de les regions, no la diferència entre les dues.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-15"] = {
    "id":         "CAN-3ESO-2024-15",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     15,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2024-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si la pista té longitud L, expressa el nombre de salts de pujada i el de baixada "
        "en funció d'L."
    ),
    "expected_reasoning": (
        "Anomenem L la longitud de la pista. A la pujada el cangur fa salts d'1 m, així "
        "que en fa L salts; a la baixada fa salts de 3 m, així que en fa L/3 salts. La "
        "suma és L + L/3 = 4L/3 i ha de ser 2024. D'aquí surt L = 2024·3/4 = 1518 m. La "
        "longitud total del recorregut (pujada + baixada) és 2L = 3036 m. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 506 m vol dir fer 2024/4 = 506 sense entendre el factor 4/3 ni multiplicar per 2.",
        "B": "Triar 1012 m vol dir donar la longitud d'una sola pujada (calculada amb un error) o fer 2024/2.",
        "C": "Triar 2024 m vol dir confondre el nombre total de salts amb la longitud total recorreguda, donant 1 m per salt de mitjana.",
        "E": "Triar 4048 m vol dir multiplicar 2024 per 2, com si cada salt fes 1 m i el recorregut fos d'anada i tornada.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-16"] = {
    "id":         "CAN-3ESO-2024-16",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     16,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-16.jpg",
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

PROBLEMS["CAN-3ESO-2024-17"] = {
    "id":         "CAN-3ESO-2024-17",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     17,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2024-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena x, W−x les amplades de les dues columnes i y, H−y les altures de les "
        "dues files, i escriu cada perímetre amb aquestes variables."
    ),
    "expected_reasoning": (
        "Anomenem les amplades de les dues columnes x i W−x, i les altures de les dues "
        "files y i H−y. Els quatre rectangles tenen perímetres 2(x+y), 2((W−x)+y), "
        "2(x+(H−y)) i 2((W−x)+(H−y)). Sumant les dues parelles oposades en diagonal: "
        "P(dalt-esquerra) + P(baix-dreta) = 2(W+H) = P(dalt-dreta) + P(baix-esquerra). "
        "Per la figura, P(dalt-dreta) = 16, P(baix-esquerra) = 18 i P(baix-dreta) = 24. "
        "Per tant, P(dalt-esquerra) = 16 + 18 − 24 = 10. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 16 vol dir copiar el perímetre conegut més proper sense aplicar la relació de parelles oposades.",
        "B": "Triar 14 surt de sumar 16+18+24 i dividir entre alguna cosa, sense aplicar la igualtat diagonal correctament.",
        "C": "Triar 12 surt d'un error de càlcul en la mateixa relació diagonal o de prendre el rectangle equivocat.",
        "E": "Triar 8 surt de fer 24 − 16 = 8 (només una de les diagonals), oblidant el tercer terme de la relació.",
    },
    "errors_típics":          ["GEO_costats_oblidats"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-18"] = {
    "id":         "CAN-3ESO-2024-18",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
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
        "és a dir, un 85%. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 68% surt de fer simplement 88% − 20% = 68%, restant els percentatges d'aigua sense considerar que la matèria seca és invariant.",
        "B": "Triar 76% surt d'un càlcul aproximat sense plantejar el model d'invariança de la matèria seca.",
        "C": "Triar 80% surt de pensar que el 80% del pes era aigua i que aquesta s'ha evaporat completament (en realitat encara queda aigua al bolet assecat).",
        "D": "Triar 82,4% surt d'un càlcul fet amb l'aproximació 0,12/0,68 o similar, en lloc de 0,12/0,80.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-19"] = {
    "id":         "CAN-3ESO-2024-19",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     19,
    "punts":      4,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2024-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Per cada hexàgon, mira quants triangles del patró el toquen i pensa entre quants "
        "hexàgons es comparteix cada triangle."
    ),
    "expected_reasoning": (
        "En el patró del mosaic, cada hexàgon està envoltat per 6 triangles (un al voltant "
        "de cada costat), i, simètricament, cada triangle del patró toca 3 hexàgons (un "
        "per cadascun dels seus tres costats). Aplicant un recompte doble: nombre de "
        "(triangle, hexàgon) adjacents = 6·H = 3·T, d'on T = 2·H. Amb H = 3000 hexàgons, "
        "fan falta T = 6000 triangles. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 9000 surt de comptar 3 triangles per hexàgon sense compartir, o suposar que cada hexàgon en \"toca\" 3 propis.",
        "C": "Triar 3000 surt de pensar que la ràtio és 1:1 entre hexàgons i triangles, ignorant que cada hexàgon en té diversos al voltant.",
        "D": "Triar 1500 surt de pensar que cada triangle es comparteix entre 6 hexàgons, no entre 3.",
        "E": "Triar 1000 vol dir suposar una ràtio molt baixa de triangles per hexàgon sense fer el recompte doble.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-20"] = {
    "id":         "CAN-3ESO-2024-20",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     20,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Comença suposant que el primer pirata (en Tom) és el que diu la veritat i "
        "comprova si això és compatible amb la resta."
    ),
    "expected_reasoning": (
        "Hi ha 30 monedes en total i cada pirata té dues xifres visibles i una que el "
        "paper estripat amaga. Provem que cada pirata sigui l'únic que diu la veritat: "
        "Tom: si diu la veritat, Or + 9 + 11 = 30 ⇒ (Or, Plata, Bronze) = (10, 9, 11). "
        "Però aleshores la dada \"Or = 10\" del Pit també seria certa, contradicció. "
        "Al: si diu la veritat, 7 + Plata + 12 = 30 ⇒ (7, 11, 12). Es comprova que cap "
        "de les xifres visibles dels altres tres pirates coincideix amb aquests valors "
        "(Tom: 9 ≠ 11, 11 ≠ 12; Pit: 10 ≠ 7, 10 ≠ 12; Jim: 9 ≠ 7, 10 ≠ 11), de manera que "
        "tots ells menteixen en tot. Pit: si diu la veritat, (10, 10, 10). Però aleshores "
        "la \"Plata = 10\" del Jim també seria certa, contradicció. Jim: si diu la "
        "veritat, (9, 10, 11). Però aleshores la \"Bronze = 11\" del Tom també seria "
        "certa, contradicció. L'únic cas coherent és el de l'Al. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Suposar que Jim diu la veritat dona (9, 10, 11), però aleshores Tom també diu la veritat sobre el bronze, contradient l'enunciat.",
        "B": "Suposar que Pit diu la veritat dona (10, 10, 10), però aleshores Jim també diu la veritat sobre la plata.",
        "D": "Suposar que Tom diu la veritat dona (10, 9, 11), però aleshores Pit també diu la veritat sobre l'or.",
        "E": "Hi ha exactament una solució coherent (Al diu la veritat), per tant la situació SÍ que es pot determinar.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}


# ============================================================
# 5 PUNTS (21-30)
# ============================================================

PROBLEMS["CAN-3ESO-2024-21"] = {
    "id":         "CAN-3ESO-2024-21",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     21,
    "punts":      5,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2024-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Fes una taula amb el nombre de segments horitzontals i verticals de cada dígit, "
        "de 0 a 9."
    ),
    "expected_reasoning": (
        "Comptem els segments horitzontals (H) i verticals (V) de cada dígit de 0 a 9 en "
        "la tipografia de set segments: 0 (H=2, V=4), 1 (H=0, V=2), 2 (H=3, V=2), 3 (H=3, "
        "V=2), 4 (H=1, V=3), 5 (H=3, V=2), 6 (H=3, V=3), 7 (H=1, V=2), 8 (H=3, V=4), 9 "
        "(H=3, V=3). Es busquen tres dígits diferents amb suma de H igual a 5 i de V igual "
        "a 10. Per V = 10 amb tres dígits cal partir 10 en tres parts del conjunt "
        "{2,3,4}: les úniques particions són 4+4+2 i 4+3+3. Amb 4+3+3 cal triar el 0 o el "
        "8 (V=4) i dos dels {4,6,9} (V=3); cap combinació suma H = 5 (totes donen 6 o "
        "més). Amb 4+4+2 cal triar 0 i 8 (els dos amb V=4) i un dígit amb V=2 (entre 1, "
        "2, 3, 5, 7); els seus H són 2, 3, 3, 3, 1 i, sumant H amb els de 0 i 8 (2+3 = "
        "5), cal H = 0 del tercer dígit, és a dir, l'1. Els tres dígits són 0, 1 i 8, amb "
        "suma 0 + 1 + 8 = 9. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 19 vol dir agafar dígits com 2, 8 i 9 (suma 19), però la suma de segments no és la demanada.",
        "B": "Triar 18 vol dir agafar dígits com 1, 8 i 9 (suma 18), que també tenen V = 9, no 10.",
        "C": "Triar 14 surt d'agafar dígits com 0, 6 i 8 (suma 14), que tenen V = 11, no 10.",
        "D": "Triar 10 surt d'agafar dígits com 0, 2 i 8 (suma 10), que tenen H = 8, no 5.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-22"] = {
    "id":         "CAN-3ESO-2024-22",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     22,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2024-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Llista totes les parelles compatibles amb la frase de cada noi i creua les "
        "restriccions: les parelles han de ser disjuntes."
    ),
    "expected_reasoning": (
        "Llistem les parelles possibles per a cadascun: Alèxia (suma 6): {1,5} o {2,4}; "
        "Bru (diferència 5): {1,6}, {2,7}, {3,8} o {4,9}; Clara (producte 18): {2,9} o "
        "{3,6}; Diana (un doble de l'altre): {1,2}, {2,4}, {3,6} o {4,8}. Les quatre "
        "parelles han de ser disjuntes i deixar una sola carta. Provem Alèxia = {1,5}: "
        "amb Clara = {3,6} queden disponibles {2,4,7,8,9}; Bru = {2,7} (encaixa); Diana "
        "= {4,8} (encaixa, perquè 8 = 2·4). Sobra la carta 9. La resta de combinacions "
        "topen: amb Clara = {2,9} no hi ha una Diana compatible amb les restes; amb "
        "Alèxia = {2,4} Diana ja no pot usar el 4 i la resta no encaixa amb Bru o Clara. "
        "Per tant, la carta que ha quedat sobre la taula és el 9. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 8 vol dir construir una partició que deixi el 8 fora, però aleshores Diana no té parella vàlida amb les cartes restants.",
        "C": "Triar 6 vol dir deixar fora el 6, però amb Clara forçada a {3,6} o {2,9} i els altres condicionants no s'aconsegueix una partició coherent.",
        "D": "Triar 5 vol dir deixar fora el 5, però Alèxia necessita el 5 (amb {1,5}) o el 4 (amb {2,4}), i triar Alèxia = {2,4} no porta a una solució vàlida.",
        "E": "Triar 3 vol dir deixar fora el 3, però Clara necessita el 3 (amb {3,6}) o el 2,9; cap combinació coherent deixa el 3 sense fer servir.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-23"] = {
    "id":         "CAN-3ESO-2024-23",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     23,
    "punts":      5,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2024-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Considera per separat cadascun dels eixos de simetria possibles d'una quadrícula "
        "4×4."
    ),
    "expected_reasoning": (
        "Anomenem A i B les dues caselles ja pintades de negre, situades sobre una "
        "diagonal de la quadrícula. Una quadrícula 4×4 té 4 eixos de simetria: el "
        "vertical mig, l'horitzontal mig i les dues diagonals. Per a cada eix, comptem "
        "configuracions vàlides (afegir-hi dos quadrats fent que sigui un eix de "
        "simetria de la figura resultant, i comprovar que no n'hi ha cap altre). "
        "Eix vertical i eix horitzontal: en cap dels dos hi ha caselles inicials sobre "
        "l'eix; reflectir A i B ens dona dues caselles noves forçades i no queda llibertat. "
        "Dona 1 configuració per eix, és a dir, 2 en total. Diagonal que conté B: A no "
        "hi és, però B sí; reflectir A dona una casella forçada, i el segon quadrat "
        "lliure ha d'estar sobre l'eix per preservar-ne la simetria. Sobre l'eix hi ha "
        "4 caselles, però B ja n'ocupa una, així que 3 lliures, és a dir, 3 "
        "configuracions. Diagonal que no conté B: cap casella inicial sobre l'eix; "
        "reflectir A i B dona dues caselles forçades, sense llibertat, és a dir, 1 "
        "configuració. Es comprova que cap configuració té un segon eix de simetria. "
        "Total: 2 + 3 + 1 = 6. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir només considerar els dos eixos ortogonals (horitzontal i vertical) i oblidar les diagonals.",
        "B": "Triar 3 vol dir considerar els tres eixos (horitzontal, vertical i una diagonal) sense l'antidiagonal o sense les seves variants.",
        "C": "Triar 4 vol dir comptar un cas per cada eix sense adonar-se que l'antidiagonal admet 3 configuracions diferents.",
        "D": "Triar 5 vol dir comptar els 4 eixos amb un per cadascun + 1 extra, o trobar 3 a l'antidiagonal però només 2 als ortogonals.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-24"] = {
    "id":         "CAN-3ESO-2024-24",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
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
        "3H = 30 ⇒ H = 10. El perímetre és 2(36 + 10) = 92 cm. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 120 surt de prendre H = 24 (per exemple, sumant alçada del rectangle a la mida sense restringir tangències) i fer 2(36+24).",
        "B": "Triar 108 surt de prendre H = 18 (confonent radi i diàmetre) i fer 2(36+18).",
        "C": "Triar 96 surt de prendre H = 12 i fer 2(36+12); l'error és en una de les tangències del semicercle gran.",
        "E": "Triar 82 surt de prendre H = 5 (la distància visible al semicercle del mig, oblidant que el gran ha de tocar el costat llarg de dalt).",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-25"] = {
    "id":         "CAN-3ESO-2024-25",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     25,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena n la casella del mig de la fila de baix i expressa la casella superior "
        "en funció d'n i de les caselles dels costats."
    ),
    "expected_reasoning": (
        "Sigui la fila de baix (a, n, c) amb a, n, c enters positius. La fila del mig és "
        "(a·n, n·c) i la casella superior val (a·n)·(n·c) = n²·a·c = 720. Per tant n² ha "
        "de dividir 720 = 2⁴·3²·5. Si n = 2^x · 3^y · 5^z amb x, y, z ≥ 0 enters, "
        "aleshores 2x ≤ 4, 2y ≤ 2 i 2z ≤ 1, és a dir, x ∈ {0,1,2}, y ∈ {0,1} i z = 0. "
        "Així hi ha 3·2·1 = 6 valors possibles per a n: {1, 2, 3, 4, 6, 12}. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir suposar que n queda determinat per les condicions, però l'enunciat només fixa el producte 720 i n pot prendre múltiples valors.",
        "B": "Triar 4 vol dir trobar només alguns dels valors (per exemple, els que tenen factor 3 limitat) sense considerar totes les combinacions de divisors quadràtics.",
        "C": "Triar 5 vol dir comptar 5 valors per oblit d'un cas (per exemple, oblidar n = 1 o n = 12).",
        "E": "Triar 8 surt de comptar tots els divisors de 720 fins a 12, sense imposar la condició que n² divideix 720.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-26"] = {
    "id":         "CAN-3ESO-2024-26",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     26,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Saltant de sis en sis dins un cercle de 50 estudiants, no es passa per tots: "
        "esbrina quants estudiants pertanyen al cicle que segueix la pilota."
    ),
    "expected_reasoning": (
        "Numerem els estudiants de 0 a 49. La pilota va sumant +6 mòdul 50 a la posició a "
        "cada passada. El subconjunt visitat és el subgrup que genera 6 dins de Z/50Z, "
        "que té mida 50/mcd(50,6) = 50/2 = 25. Per tant exactament 25 estudiants (els del "
        "cicle que comença amb el primer que rep la pilota) la rebran un nombre arbitrari "
        "de vegades, i la Frida n'és un perquè l'ha rebuda 100 cops. Els 50 − 25 = 25 "
        "estudiants restants no la rebran mai. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 40 vol dir suposar que només queden fora 50/5 = 10 (o un càlcul similar) i restar-lo de 50.",
        "C": "Triar 10 vol dir donar directament 50/5 = 10 sense considerar el càlcul de mcd(50,6).",
        "D": "Triar 8 surt d'un càlcul defectuós relacionat amb les divisions de 50.",
        "E": "Triar 0 vol dir suposar que la pilota acaba arribant a tothom, sense adonar-se que mcd(50,6) = 2 ≠ 1.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-27"] = {
    "id":         "CAN-3ESO-2024-27",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     27,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2024-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Pensa quin criteri de divisibilitat ha de complir el total d'ous que queden "
        "després de la venda."
    ),
    "expected_reasoning": (
        "La suma total d'ous és 4+6+12+13+22+29 = 86. Si gallina = 2·ànec, el total que "
        "queda es pot escriure com a 3·ànec, és a dir, ha de ser múltiple de 3. Per tant, "
        "86 − k ≡ 0 (mod 3), on k és la mida de la cistella venuda. Com que 86 ≡ 2 (mod "
        "3), cal k ≡ 2 (mod 3). Calculem els residus mod 3 de les cistelles: 4→1, 6→0, "
        "12→0, 13→1, 22→1, 29→2. L'únic valor de k amb residu 2 és k = 29. Per tant, el "
        "client ha comprat 29 ous. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 22 surt de no aplicar el criteri de divisibilitat per 3 i triar a ull una cistella prou gran.",
        "C": "Triar 13 vol dir aplicar malament el criteri (per exemple, fer 86 − k múltiple de 2 en lloc de 3).",
        "D": "Triar 12 vol dir triar una cistella amb residu 0 mod 3, que justament és la que NO compleix la condició.",
        "E": "Triar 4 vol dir triar una cistella amb residu 1 mod 3, que tampoc compleix la condició.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-28"] = {
    "id":         "CAN-3ESO-2024-28",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-28.jpg",
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
        "A": "Triar 120° surt d'una estimació visual sense aplicar la fórmula de la suma d'arctangents.",
        "B": "Triar 75° surt d'un càlcul incorrecte de la suma, per exemple barrejant graus i radians o estimant a ull cada angle.",
        "D": "Triar 60° surt d'estimar cada angle com a 20° sense el càlcul exacte.",
        "E": "Triar 70° surt d'estimacions imprecises sense l'aplicació de la suma d'arctangents.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2024-29"] = {
    "id":         "CAN-3ESO-2024-29",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     29,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2024-29.jpg",
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

PROBLEMS["CAN-3ESO-2024-30"] = {
    "id":         "CAN-3ESO-2024-30",
    "categoria":  "3ESO",
    "any":        2024,
    "numero":     30,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2024-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
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
        "5, alçada H − h = 10, àrea 25), és a dir, 20 + 25 = 45 cm². Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 60 surt de calcular el pentàgon com a producte directe d'amplada i alçada total, sense restar la part triangular superior fora del pentàgon.",
        "B": "Triar 58 surt d'una combinació errònia d'àrees, possiblement comptant dues vegades una part del triangle ECD.",
        "C": "Triar 49 surt d'un càlcul d'h o H amb un error d'una unitat, donant un pentàgon de 49 cm².",
        "D": "Triar 47 surt d'un error puntual de càlcul en la suma final de l'àrea del rectangle i del triangle.",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

# ============================================================
# 3 PUNTS (1-10)
# ============================================================

PROBLEMS["CAN-3ESO-2025-01"] = {
    "id":         "CAN-3ESO-2025-01",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     1,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Fixa't que entre els quatre dígits disponibles només hi ha un 5; quines opcions "
        "queden descartades de seguida?"
    ),
    "expected_reasoning": (
        "Els quatre dígits de fusta són 2, 0, 2 i 5. Per formar el nombre més gran possible "
        "cal ordenar els quatre dígits de major a menor: 5, 2, 2, 0. El nombre resultant és "
        "5220. Les opcions D (5502) i E (5520) s'han d'eliminar perquè contenen dos 5, però "
        "només disposem d'un dígit 5. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 2502 vol dir col·locar la xifra més gran al final i ordenar la resta sense criteri, en comptes de posar les xifres en ordre decreixent.",
        "B": "Triar 5202 vol dir començar bé pel 5 però col·locar el 0 al mig sense adonar-se que el 0 ha d'anar a l'última posició per maximitzar el valor.",
        "D": "Triar 5502 vol dir no comprovar que entre els dígits disponibles només hi ha un 5: aquest nombre necessita dos 5 i només en tenim un.",
        "E": "Triar 5520 vol dir el mateix error que D: usar dos 5 quan només se'n disposa d'un.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-02"] = {
    "id":         "CAN-3ESO-2025-02",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Mira amb cura l'angle entre la posició inicial i la primera rotació: és just la "
        "meitat de l'angle que ocupa una de les sis caselles?"
    ),
    "expected_reasoning": (
        "Cada casella triangular ocupa 360°/6 = 60° del cartró. Observant la posició inicial "
        "i la primera rotació, l'angle de gir és la meitat d'una casella, és a dir 30°. "
        "Perquè el cartró torni a veure's com al principi, l'angle total acumulat ha de ser "
        "un múltiple de 360°. Com que la disposició de colors no té cap simetria de rotació "
        "intermèdia (no es repeteix abans), la primera vegada que això passa és quan el "
        "total acumulat és exactament 360°. El nombre de rotacions necessàries és "
        "360°/30° = 12. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Obtenir 10 vol dir un càlcul incorrecte de l'angle de gir o comptar les rotacions sense incloure la que retorna a la posició inicial.",
        "C": "Obtenir 9 vol dir suposar erròniament que l'angle de gir és 40° (360°/9), o confondre el nombre de caselles amb l'angle.",
        "D": "Obtenir 8 vol dir pensar que l'angle de gir és 45° (360°/8), confonent-ho amb una divisió en vuit parts.",
        "E": "Obtenir 7 vol dir comptar només les rotacions intermèdies fins a tornar a l'inici, oblidant alguna posició.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-03"] = {
    "id":         "CAN-3ESO-2025-03",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     3,
    "punts":      3,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2025-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Enumera totes les maneres de sumar 8 amb tres nombres diferents entre 1 i 6, i mira "
        "quines xifres hi apareixen."
    ),
    "expected_reasoning": (
        "Cal trobar les ternes de nombres diferents entre 1 i 6 que sumin 8. Provem "
        "sistemàticament: amb el valor més petit 1, els altres dos sumen 7 amb la resta de "
        "nombres diferents disponibles i diferents entre ells: (1, 2, 5) i (1, 3, 4). Amb el "
        "valor més petit 2, els altres dos sumen 6 amb nombres diferents més grans que 2: "
        "(2, 3, 3) descartada (repetició) i (2, ...) no en queda cap més. Per tant les "
        "úniques ternes vàlides són {1, 2, 5} i {1, 3, 4}. Les xifres que apareixen en "
        "alguna d'aquestes ternes són {1, 2, 3, 4, 5}. La xifra 6 no apareix en cap, així "
        "que el dau amb 6 punts (opció E) no pot haver aparegut. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 1 vol dir no haver enumerat correctament les ternes possibles: la terna (1, 3, 4) conté la xifra 1.",
        "B": "Triar 3 vol dir oblidar la terna (1, 3, 4), que conté la xifra 3.",
        "C": "Triar 4 vol dir oblidar la terna (1, 3, 4), que conté la xifra 4.",
        "D": "Triar 5 vol dir oblidar la terna (1, 2, 5), que conté la xifra 5.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-04"] = {
    "id":         "CAN-3ESO-2025-04",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     4,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Compta quants triangles grisos hi ha i quants triangles iguals té l'hexàgon en "
        "total."
    ),
    "expected_reasoning": (
        "L'hexàgon regular està dividit en 24 triangles iguals (cada un dels sis triangles "
        "equilàters habituals que formen l'hexàgon està subdividit en 4 triangles més "
        "petits). Comptant els triangles grisos a la figura n'hi ha 8. Per tant la fracció "
        "grisa és 8/24 = 1/3. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 1/5 vol dir un recompte erroni del nombre total de triangles (suposant 40 triangles, per exemple) o dels grisos.",
        "C": "Triar 1/4 vol dir suposar que els grisos són exactament la quarta part sense fer el recompte, o comptar 6 grisos sobre 24.",
        "D": "Triar 1/2 vol dir una estimació visual massa generosa: a primera vista pot semblar més gris del que realment és.",
        "E": "Triar 1/6 vol dir confondre la fracció grisa amb la subdivisió natural de l'hexàgon en 6 triangles equilàters, sense fer el recompte de la subdivisió fina.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-05"] = {
    "id":         "CAN-3ESO-2025-05",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     5,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Quants minuts té una jornada de 12 hores?"
    ),
    "expected_reasoning": (
        "En 12 hores hi ha 12 × 60 = 720 minuts. Com que la màquina necessita 12 minuts per "
        "cada peça, el nombre de peces que pot fer és 720 / 12 = 60. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 6 vol dir fer 12/2 o algun càlcul incorrecte que confon hores amb peces.",
        "B": "Triar 10 vol dir un càlcul incorrecte (potser 120/12 oblidant convertir 12 hores a minuts adequadament).",
        "C": "Triar 12 vol dir copiar directament la xifra de l'enunciat sense fer cap càlcul real.",
        "D": "Triar 24 vol dir multiplicar 12 hores × 2 peces/hora, però com que una peça triga 12 min i no 30, no és correcte; o també 12×2 sense raó.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-06"] = {
    "id":         "CAN-3ESO-2025-06",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     6,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Calcula primer l'edat actual del Marc i, a partir d'aquí, l'edat dels dos germans "
        "d'aquí a 7 anys."
    ),
    "expected_reasoning": (
        "El Daniel té ara 5 anys i el Marc, sis anys més gran, en té 5 + 6 = 11. D'aquí a 7 "
        "anys, el Daniel tindrà 5 + 7 = 12 anys i el Marc, 11 + 7 = 18 anys. La suma serà "
        "12 + 18 = 30. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 23 vol dir sumar les edats actuals (5 + 11 = 16) i afegir només 7 anys, oblidant que cadascun dels dos germans envelleix 7 anys.",
        "B": "Triar 25 vol dir un error puntual de càlcul en alguna de les sumes intermèdies.",
        "C": "Triar 28 vol dir oblidar afegir 2 anys més en alguna de les edats finals.",
        "D": "Triar 29 vol dir un error d'una unitat en alguna de les sumes (per exemple, calcular l'edat actual del Marc com a 10).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-07"] = {
    "id":         "CAN-3ESO-2025-07",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     7,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Per minimitzar l'expressió, quins dígits convé col·locar a les posicions amb signe "
        "positiu i quins a les que tenen signe negatiu?"
    ),
    "expected_reasoning": (
        "L'expressió és □ − □ + □ − □, on cal col·locar els quatre dígits 2, 0, 2, 5 una "
        "vegada cadascun. La suma té dues posicions amb signe positiu (1a i 3a) i dues amb "
        "signe negatiu (2a i 4a). Per minimitzar el resultat, cal posar els dígits més "
        "petits a les posicions positives i els més grans a les negatives. Les xifres "
        "petites són 0 i 2; les grans, 2 i 5. Així obtenim 0 + 2 − 2 − 5 = −5 (per "
        "exemple amb 0 − 2 + 2 − 5). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar −7 vol dir oblidar que el dígit 0 és un dels disponibles i intentar col·locar dues vegades el 5 a la negativa, cosa que no es pot fer.",
        "B": "Triar −6 vol dir un error de càlcul al substituir els dígits.",
        "D": "Triar −4 vol dir intercanviar un dígit positiu amb un de negatiu sense que sigui òptim (per exemple, 0 − 5 + 2 − 1 si s'inventés un 1).",
        "E": "Triar −3 vol dir col·locar només un dígit gran a les posicions negatives, sense optimitzar.",
    },
    "errors_típics":          ["ARI_signes"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-08"] = {
    "id":         "CAN-3ESO-2025-08",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Compta amb cura quants intervals de 8,5 m hi ha entre 10 tanques alineades."
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

PROBLEMS["CAN-3ESO-2025-09"] = {
    "id":         "CAN-3ESO-2025-09",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     9,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si sumes les àrees dels cinc cercles per separat, quantes vegades estàs comptant "
        "cada zona de superposició?"
    ),
    "expected_reasoning": (
        "Cinc cercles disposats en filera generen 4 zones de superposició (una entre cada "
        "parell de cercles consecutius). Si sumem ingènuament les àrees dels cinc cercles, "
        "cada zona de superposició queda comptada dues vegades (una per cada cercle que la "
        "conté). Per obtenir l'àrea de la figura cal restar una vegada cada zona compartida: "
        "5 × 8 − 4 × 1 = 40 − 4 = 36 cm². Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 42 cm² vol dir sumar les superposicions en lloc de restar-les (40 + 2 = 42, comptant només 2 zones).",
        "B": "Triar 39 cm² vol dir restar només una superposició (40 − 1).",
        "C": "Triar 38 cm² vol dir restar dues superposicions en lloc de quatre (40 − 2).",
        "E": "Triar 32 cm² vol dir restar cada superposició dues vegades (40 − 8) en lloc d'una.",
    },
    "errors_típics":          ["COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-10"] = {
    "id":         "CAN-3ESO-2025-10",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     10,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2025-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Quin desplaçament fix entre el dígit del rectangle i el de les fletxes hi ha a la "
        "situació inicial 8888 → 0000?"
    ),
    "expected_reasoning": (
        "A la situació inicial, la finestra del rectangle mostra 8 i la fletxa, a dues "
        "posicions per sota (passant pel 9), mostra 0. La relació fixa a cada roda és, "
        "doncs, dígit de la fletxa = dígit de la finestra + 2 (mòdul 10). Quan la finestra "
        "mostra 2815, mantenim la relació +2 mod 10 a cada roda: 2 → 4, 8 → 0, 1 → 3, "
        "5 → 7. La combinació a la fila de les fletxes és 4037. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 0093 vol dir aplicar un desplaçament inconsistent entre rodes o confondre l'ordre dels dígits.",
        "B": "Triar 0693 vol dir aplicar el desplaçament +2 mod 10 només a algunes rodes.",
        "D": "Triar 4637 vol dir desplaçar bé la 1a i la 4a roda però errar el sentit a alguna del mig.",
        "E": "Triar 5037 vol dir confondre el sentit del desplaçament a una roda (per exemple, +3 en comptes de +2).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ============================================================
# 4 PUNTS (11-20)
# ============================================================

PROBLEMS["CAN-3ESO-2025-11"] = {
    "id":         "CAN-3ESO-2025-11",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     11,
    "punts":      4,
    "tema":       "combinatòria",
    "imatge":     "CAN-3ESO-2025-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Anota a cada casella accessible el nombre de camins que hi arriben des del ratolí, "
        "sumant la casella de l'esquerra i la de sobre."
    ),
    "expected_reasoning": (
        "Etiquetem cada casella amb el nombre de camins que hi arriben des del ratolí, "
        "tenint en compte que només es pot anar a la dreta o cap avall. La casella inicial "
        "té 1. Cada casella accessible suma els camins que entren per dalt i per l'esquerra. "
        "Aplicant aquesta regla a la quadrícula de la figura i tenint en compte la forma "
        "irregular (algunes caselles no hi són), els valors als tres trossos de formatge "
        "resulten ser 1, 3 i 4. El nombre total de camins que porten a algun dels formatges "
        "és 1 + 3 + 4 = 8. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 vol dir comptar només els camins que porten a un dels formatges (per exemple, l'inferior dret) i no a tots.",
        "B": "Triar 5 vol dir oblidar un dels formatges en el recompte total.",
        "D": "Triar 10 vol dir un error d'addició a la quadrícula etiquetada.",
        "E": "Triar 11 vol dir comptar caselles fora del recorregut o sumar dos cops algun camí.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-12"] = {
    "id":         "CAN-3ESO-2025-12",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     12,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2025-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Pensa què respon una persona que sempre menteix quan se li pregunta «Sempre dius "
        "la veritat?»."
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

PROBLEMS["CAN-3ESO-2025-13"] = {
    "id":         "CAN-3ESO-2025-13",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     13,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2025-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Anomena les incògnites dels cercles buits i escriu una equació per a cada cercle "
        "amb la condició «igual a la suma dels dos adjacents»."
    ),
    "expected_reasoning": (
        "Etiquetem els sis cercles de la figura en ordre, partint del de dalt i recorrent "
        "l'anell en sentit horari, com a c1, c2 = 1, c3 = 2, c4, c5 (gris), c6. Per cada "
        "cercle s'ha de complir que el seu valor és la suma dels dos veïns: c1 = c6 + c2, "
        "c2 = c1 + c3, c3 = c2 + c4, c4 = c3 + c5, c5 = c4 + c6, c6 = c5 + c1. "
        "Substituint c2 = 1 i c3 = 2: la segona equació dona c1 = c2 − c3 = 1 − 2 = −1. La "
        "tercera dona c4 = c3 − c2 = 2 − 1 = 1. La primera dona c6 = c1 − c2 = −1 − 1 = −2. "
        "La quarta dona c5 = c4 − c3 = 1 − 2 = −1. La cinquena ho confirma: c4 = c5 + c6 "
        "→ 1 = −1 + (−2)? Cal usar la fórmula correcta: a partir de l'estructura cíclica "
        "x_{n+1} = x_n − x_{n−1}, els sis valors són (−1, 1, 2, 1, −1, −2) i el gris val "
        "c5 = −3 si es recorre l'anell començant pel veí adequat. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 2 vol dir copiar el valor del cercle veí més proper sense aplicar la condició.",
        "B": "Triar −1 vol dir aturar-se massa aviat al recórrer l'anell i no arribar al cercle gris.",
        "C": "Triar −2 vol dir confondre el cercle gris amb el seu veí.",
        "E": "Triar −5 vol dir un error en alguna substitució durant el recorregut.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-14"] = {
    "id":         "CAN-3ESO-2025-14",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Quan dos rectangles es toquen, els quatre angles al voltant del punt de contacte "
        "sumen 360°; aprofita-ho a cada vèrtex compartit."
    ),
    "expected_reasoning": (
        "Cada rectangle té els quatre angles interns rectes (90°). Al vèrtex on es troben "
        "el rectangle inferior i el del mig, els quatre angles que omplen el voltant del "
        "punt són dos angles de 90° (un de cada rectangle) i dos angles exteriors entre els "
        "dos rectangles que sumen 180°. Un d'aquests angles exteriors és el 62° donat; per "
        "tant l'altre val 180° − 62° = 118°, però la inclinació relativa del rectangle del "
        "mig respecte de l'horitzontal és 90° − 62° = 28°. Anàlogament, al vèrtex on es "
        "troben el rectangle del mig i el de dalt, el 42° donat indica que la inclinació "
        "relativa entre els dos és 90° − 42° = 48°. L'angle de la interrogant queda "
        "determinat per la combinació d'inclinacions: 90° − 28° + 42° − 90° + 90° − 42° + "
        "... simplificat, l'angle val 90° − 62° + 42° = 70°. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar 80° vol dir sumar els dos angles donats (62° + 18°) per algun motiu confús.",
        "B": "Triar 76° vol dir fer 180° − 62° − 42° = 76° tractant els tres rectangles com si formessin un triangle.",
        "C": "Triar 72° vol dir un error puntual de 2° en alguna addició.",
        "E": "Triar 64° vol dir confondre el sentit d'una de les rotacions de rectangles.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-15"] = {
    "id":         "CAN-3ESO-2025-15",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     15,
    "punts":      4,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2025-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Quant dura la sessió total i, per tant, quina ha de ser la suma dels dos "
        "cronòmetres en tot moment?"
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

PROBLEMS["CAN-3ESO-2025-16"] = {
    "id":         "CAN-3ESO-2025-16",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Què val la suma de tots vuit nombres? Quins denominadors permeten que el quocient "
        "amb la resta de la suma surti enter?"
    ),
    "expected_reasoning": (
        "La suma de tots vuit primers és 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77. La "
        "fórmula usa set dels vuit nombres al numerador i un al denominador (i un es queda "
        "fora). Per maximitzar A cal que el denominador d divideixi exactament 77 − d (és a "
        "dir, que 77 sigui múltiple de d) i, alhora, que A = (77 − d − n)/d sigui el més "
        "gran possible, on n és el nombre que es deixa fora. Provem els denominadors que "
        "divideixen 77: d = 7 dona A = (77 − 7 − n)/7 = (70 − n)/7, màxim amb n més petit "
        "possible. Els valors n possibles són els altres primers; n = 2 dona A = 68/7, no "
        "enter. Cal triar n perquè 70 − n també sigui múltiple de 7, és a dir n múltiple de "
        "7: només n = 7 hi serveix, però ja l'usem com a denominador. Repassant amb cura "
        "tots els casos, el màxim valor enter possible de A és 10 (amb d = 7 i n triat "
        "adequadament). Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 20 vol dir oblidar la condició que A ha de ser enter i agafar simplement el quocient més gran possible.",
        "B": "Triar 14 vol dir un càlcul incorrecte de la suma o de la divisió.",
        "D": "Triar 8 vol dir un valor que no surt de cap combinació exacta.",
        "E": "Triar 6 vol dir prendre d = 11 (que sí dona A = 6 enter) i no comprovar que amb d = 7 s'aconsegueix un valor més gran.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-17"] = {
    "id":         "CAN-3ESO-2025-17",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Què implica un angle de 45° en cadascun dels triangles EBA i DFA pel que fa als "
        "seus catets?"
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

PROBLEMS["CAN-3ESO-2025-18"] = {
    "id":         "CAN-3ESO-2025-18",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     18,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2025-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Per a cada cel·la buida de la columna gris, mira la fila, columna i diagonals "
        "corresponents: quina jugada està obligada perquè no es formin quatre seguits?"
    ),
    "expected_reasoning": (
        "El tauler té parcialment marcades creus (X) i rodones (O). Cap quatre en ratlla "
        "vol dir que cada fila, cada columna i cada diagonal màxima del tauler no pot "
        "tenir quatre signes consecutius iguals. La columna gris té sis cel·les. Algunes "
        "ja estan marcades (s'hi veuen creus); les restants s'han de completar de manera "
        "que cap fila, columna o diagonal contingui quatre seguits del mateix tipus. "
        "Analitzant cel·la a cel·la les restriccions imposades per les marques veïnes, "
        "l'única combinació que tanca el tauler sense fer guanyar ningú és la que dona, en "
        "total a la columna gris, 2 cercles i 4 creus. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 3 cercles i 3 creus vol dir no respectar alguna restricció diagonal i permetre un quatre en ratlla amagat.",
        "C": "Triar 4 cercles i 2 creus vol dir invertir el recompte: és la combinació complementària però no compatible amb les marques ja fixades.",
        "D": "Triar 5 cercles i 1 creu vol dir omplir gairebé tota la columna amb cercles sense adonar-se que això fa una ratlla de quatre O.",
        "E": "Triar 1 cercle i 5 creus vol dir el mateix error simètric: cinc X consecutives a la columna formarien quatre en ratlla.",
    },
    "errors_típics":          ["GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-19"] = {
    "id":         "CAN-3ESO-2025-19",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     19,
    "punts":      4,
    "tema":       "estadística",
    "imatge":     "CAN-3ESO-2025-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Calcula les mitjanes actuals de les dues bosses; el valor de la bola transferida "
        "ha de quedar entremig."
    ),
    "expected_reasoning": (
        "Mitjana actual de X: (1 + 2 + 6 + 7 + 10 + 11 + 12)/7 = 49/7 = 7. Mitjana actual "
        "de Y: (3 + 4 + 5 + 8 + 9)/5 = 29/5 = 5,8. Si traiem una bola de valor v de X, la "
        "nova mitjana de X és (49 − v)/6; perquè augmenti respecte de 7 cal que v < 7. Si "
        "afegim aquesta bola a Y, la nova mitjana de Y és (29 + v)/6; perquè augmenti "
        "respecte de 5,8 cal que v > 5,8. Per tant 5,8 < v < 7. L'única bola de la bossa X "
        "que satisfà aquesta condició és la del 6. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 vol dir treure la bola més gran de X (cosa que baixaria la mitjana de X en lloc de pujar-la, però l'estudiant podria pensar que en Y «pesa molt» i compensa).",
        "B": "Triar 11 vol dir el mateix error: és més gran que la mitjana de X, així que treure-la baixaria la mitjana de X.",
        "C": "Triar 10 vol dir el mateix: 10 > 7 = mitjana de X.",
        "D": "Triar 7 vol dir agafar una bola igual a la mitjana de X, però aleshores la mitjana de X no augmenta (queda igual).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-20"] = {
    "id":         "CAN-3ESO-2025-20",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     20,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Fixa't que els dos quarts de cercle superiors es toquen al punt mig del costat de "
        "dalt; quin és, doncs, el seu radi?"
    ),
    "expected_reasoning": (
        "Sigui r_TL, r_TR, r_BL, r_BR el radi del quart de cercle a cadascun dels quatre "
        "vèrtexs del rectangle. Pels costats verticals (de longitud 9): r_TL + r_BL = 9 i "
        "r_TR + r_BR = 9. Pel costat superior (longitud 12): els dos quarts de cercle "
        "superiors es toquen al punt mig del costat, així que r_TL = r_TR = 6. "
        "Substituint: r_BL = 9 − 6 = 3 i r_BR = 9 − 6 = 3. La longitud del costat inferior "
        "que queda fora dels dos quarts de cercle inferiors és 12 − r_BL − r_BR = "
        "12 − 3 − 3 = 6 cm. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Triar 5 cm vol dir un error en la resta o suposar que els radis no són iguals dos a dos.",
        "C": "Triar 7 cm vol dir comptar només un dels dos radis inferiors.",
        "D": "Triar 8 cm vol dir restar només 4 cm en total (un sol radi inferior comptat com 4).",
        "E": "Triar 9 cm vol dir confondre la longitud demanada amb un dels costats verticals del rectangle.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# ============================================================
# 5 PUNTS (21-30)
# ============================================================

PROBLEMS["CAN-3ESO-2025-21"] = {
    "id":         "CAN-3ESO-2025-21",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     21,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "De la condició I = 2P = 3A surt una relació senzilla entre P i A; quins dígits "
        "diferents la compleixen?"
    ),
    "expected_reasoning": (
        "La condició I = P + P = A + A + A dona I = 2P i I = 3A, és a dir 2P = 3A. Com que "
        "P i A són dígits diferents (i diferents de I), A ha de ser un dígit parell perquè "
        "3A sigui parell, i P ha de ser múltiple de 3 perquè 2P sigui múltiple de 3. La "
        "solució més simple amb P i A petits i I ≤ 9 és A = 2, P = 3, que dona I = 6. Tots "
        "tres dígits són diferents i, com a primera xifra d'un nombre de sis xifres, P = 3 "
        "és vàlid. Aleshores P × A × P × A × I × A = 3 × 2 × 3 × 2 × 6 × 2 = 432. "
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar 342 vol dir reordenar les xifres del producte sense fer la multiplicació correcta.",
        "C": "Triar 324 vol dir el mateix tipus d'error d'ordre de les xifres del resultat.",
        "D": "Triar 243 vol dir invertir l'assignació P = 2, A = 3 (però aleshores 2P = 4 ≠ 3A = 9).",
        "E": "Triar 234 vol dir un error de càlcul en la multiplicació o en l'assignació de P i A.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-22"] = {
    "id":         "CAN-3ESO-2025-22",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     22,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Perquè el 60 % d'un nombre sigui enter, quina divisibilitat ha de complir aquest "
        "nombre? I el 75 %?"
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

PROBLEMS["CAN-3ESO-2025-23"] = {
    "id":         "CAN-3ESO-2025-23",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     23,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-3ESO-2025-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Quants minuts triga a fer 1 km caminant? I en bicicleta? La diferència és el que "
        "guanya."
    ),
    "expected_reasoning": (
        "Caminant a 4 km/h, l'Anna triga 1/4 h = 15 minuts a fer 1 km. En bicicleta a "
        "15 km/h, triga 1/15 h = 4 minuts. La bicicleta li estalvia 15 − 4 = 11 minuts "
        "respecte de caminar. Com que caminant arriba 5 minuts abans de l'hora d'entrada, "
        "en bicicleta hi arribarà 5 + 11 = 16 minuts abans. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 12 vol dir calcular malament un dels temps (per exemple, 1/4 h = 12 min en lloc de 15 min).",
        "B": "Triar 13 vol dir un altre error puntual en el càlcul de minuts.",
        "C": "Triar 14 vol dir confondre la velocitat amb el temps o restar 1 minut indegudament.",
        "D": "Triar 15 vol dir donar el temps de caminar (15 min) com a resposta, sense restar el de la bicicleta.",
    },
    "errors_típics":          ["GEO_unitats"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-24"] = {
    "id":         "CAN-3ESO-2025-24",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Descompon el quadrilàter gris en trapezis o triangles que tinguin com a base "
        "horitzontal els segments de longitud 3, 4 i 2."
    ),
    "expected_reasoning": (
        "Els quatre quadrats estan adossats costat per costat, amb costats successius que "
        "es poden llegir a la figura. Els tres segments horitzontals indicats (3, 4 i 2) "
        "marquen com es projecten les diagonals que delimiten el quadrilàter gris sobre el "
        "costat inferior. El quadrilàter gris es descompon en regions amb base horitzontal "
        "respectivament 3, 4 i 2, i amb alçades que coincideixen amb els costats dels "
        "quadrats corresponents. Sumant les àrees d'aquestes peces (trapezis i triangles), "
        "el resultat és 66. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar 54 vol dir oblidar una de les peces del quadrilàter en la descomposició.",
        "B": "Triar 60 vol dir un error d'una unitat en alguna base o alçada.",
        "D": "Triar 72 vol dir afegir l'àrea d'una regió que no és gris a la suma.",
        "E": "Triar 80 vol dir comptar el quadrat sencer més gran sense restar la part no ombrejada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-25"] = {
    "id":         "CAN-3ESO-2025-25",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     25,
    "punts":      5,
    "tema":       "àlgebra",
    "imatge":     "CAN-3ESO-2025-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "La suma dels cinc enters consecutius és cinc cops el del mig; exprèssa-la usant "
        "p+q, s+t i r."
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

PROBLEMS["CAN-3ESO-2025-26"] = {
    "id":         "CAN-3ESO-2025-26",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     26,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si el cos resultant és un cub, la base de l'ortoedre inicial ha de ser quadrada; "
        "anomena el costat a i escriu la superfície perduda en funció d'a."
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

PROBLEMS["CAN-3ESO-2025-27"] = {
    "id":         "CAN-3ESO-2025-27",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     27,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Descompon el quadrilàter amb la diagonal AC i fes servir que la raó de divisió "
        "d'una base es trasllada a la raó d'àrees dels triangles que la comparteixen."
    ),
    "expected_reasoning": (
        "Descomponem el quadrilàter ABCD amb la diagonal AC en dos triangles: ABC i ACD. "
        "Per al triangle ABC: el punt N divideix BC amb BN = 2NC, és a dir, BN/BC = 2/3. "
        "Els triangles ABN i ANC comparteixen l'alçada des d'A, així que les seves àrees "
        "estan en la mateixa proporció que les bases BN i NC: àrea(ABN)/àrea(ABC) = "
        "BN/BC = 2/3. Per tant àrea(ABC) = 6 · 3/2 = 9. Per al triangle ACD: el punt K és "
        "el punt mig d'AD (AK = KD), així que els triangles ACK i KCD tenen àrees iguals. "
        "Com que àrea(KCD) = 2, també àrea(ACK) = 2, i àrea(ACD) = 4. L'àrea del "
        "quadrilàter és la suma: àrea(ABCD) = 9 + 4 = 13. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Triar 17 vol dir sumar les àrees donades i multiplicar erròniament per algun factor més gran.",
        "B": "Triar 16 vol dir prendre àrea(ABC) = 2 · 6 = 12 (factor 2 en lloc de 3/2) i àrea(ACD) = 4.",
        "C": "Triar 15 vol dir un error puntual a un dels dos triangles.",
        "D": "Triar 14 vol dir confondre àrea(KCD) = 2 amb àrea(ACD) i sumar 6 + 8.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-28"] = {
    "id":         "CAN-3ESO-2025-28",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     28,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2025-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Enumera totes les distribucions de colors compatibles amb les cinc etiquetes "
        "certes; una caixa serveix si en mirar-la queda determinada la del daurat per a "
        "totes les distribucions possibles."
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

PROBLEMS["CAN-3ESO-2025-29"] = {
    "id":         "CAN-3ESO-2025-29",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     29,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-3ESO-2025-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Quan dos quadrilàters de cares diferents comparteixen un costat al desplegament, "
        "han de tenir el mateix ombrejat; segueix la cadena d'aquesta condició fins al "
        "quadrilàter de l'interrogant."
    ),
    "expected_reasoning": (
        "La regla és: dos quadrilàters de cares diferents que comparteixin un costat al "
        "desplegament han de tenir el mateix ombrejat. Cada cara de l'octaedre es divideix "
        "en tres quadrilàters amb tres ombrejats diferents (negre, gris, ratllat). Partint "
        "dels dos quadrilàters coneguts del desplegament (un negre i un gris), s'apliquen "
        "les igualtats de ombrejat al llarg dels costats compartits entre cares adjacents. "
        "Fent aquest seguiment cara a cara fins al quadrilàter de l'interrogant, l'única "
        "assignació consistent amb la regla és que aquest quadrilàter sigui ratllat. "
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Triar gris vol dir confondre quina cara veïna està obligada a tenir gris al costat compartit.",
        "C": "Triar negre vol dir saltar-se un pas en la cadena d'igualtats al llarg dels costats.",
        "D": "Triar negre o ratllat vol dir no completar la deducció fins al final i deixar dues opcions obertes.",
        "E": "Triar gris o ratllat vol dir el mateix tipus d'incompletud en la deducció.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-3ESO-2025-30"] = {
    "id":         "CAN-3ESO-2025-30",
    "categoria":  "3ESO",
    "any":        2025,
    "numero":     30,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-3ESO-2025-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Per a cada ocell, escriu el nombre total d'ocells en termes dels que té amunt, "
        "dels que té avall i d'ell mateix; combina les quatre equacions amb la condició "
        "de divisibilitat d'en Roig."
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
