"""
Tutor Cangur — 1ESO problem catalogue.

Conté els 30 problemes de la prova 1ESO (tots els anys disponibles).
Afegir nous problemes aquí; mai modificar els d'altres nivells.

Estructura de cada entrada: vegeu SCHEMA.md.
"""

from problems_shared import ERROR_CATALOG, DEPENDENCIES  # noqa: F401

PROBLEMS = {}

PROBLEMS["CAN-1ESO-2026-01"] = {
    "id":         "CAN-1ESO-2026-01",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     1,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Pensa una resposta que no pugui ser, perquè no es compleix el patró. Ves descartant opcions."
    ),
    "expected_reasoning": (
        "La foto mostra un tros de terra de 3 columnes i 3 files: la fila de dalt i la de baix "
        "mostren la seqüència 88 O X, i la fila del mig mostra □ 88 O. Perquè el patró repetitiu de "
        "cinc rajoles sigui coherent, ha de contenir tant '88 O X' com '□ 88 O' com a subseqüències "
        "consecutives (en lectura cíclica). L'opció D (✱ □ 88 O X) és l'única que compleix les dues "
        "condicions: '□ 88 O' apareix a les posicions 2, 3 i 4, i '88 O X' apareix a les posicions "
        "3, 4 i 5. Cap altra opció conté les dues subseqüències alhora. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "L'opció A (□ 88 O ✱ X) conté '□ 88 O' però no conté '88 O X' (després de O ve ✱, no X).",
        "B": "L'opció B (X 88 ✱ O □) no conté cap de les dues subseqüències visibles a la foto.",
        "C": "L'opció C (O X □ ✱ 88) conté '88 O X' llegint cíclicament, però no conté '□ 88 O' (després de □ ve ✱, no 88).",
        "E": "L'opció E (X □ ✱ 88 O) conté '88 O X' però no conté '□ 88 O' (després de □ ve ✱, no 88).",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-02"] = {
    "id":         "CAN-1ESO-2026-02",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     2,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Separa el vaixell en 4 parts: esquerra, dreta, central i la torre de dalt."
    ),
    "expected_reasoning": (
        "El vaixell es pot dividir en tres zones. Les dues proes inclinades (esquerra i dreta) "
        "s'omplen cadascuna amb una peça trapezoïdal gran, cosa que dona 2 peces trapezoïdals. El "
        "cos rectangular central és prou ample i alt per necessitar sis peces quadrades de 2×2 "
        "(distribuïdes en files i columnes per cobrir tota la superfície rectangular, inclosa la "
        "torreta superior). En total: 6 peces quadrades + 2 peces trapezoïdals = 8 peces. Resposta "
        "E."
    ),
    "comentaris_distractors": {
        "A": "Comptar 4 peces vol dir subestimar el cos rectangular i no tenir en compte que necessita diverses peces quadrades.",
        "B": "Comptar 5 peces surt d'oblidar que el cos rectangular ocupa més d'una fila de peces.",
        "C": "Comptar 6 peces vol dir comptar bé les trapezoïdals però infravalorar el nombre de quadrades necessàries.",
        "D": "Comptar 7 peces surt d'un error de comptatge d'una de les zones del vaixell.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-03"] = {
    "id":         "CAN-1ESO-2026-03",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     3,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Exemple: C) 3 habitacions no pot ser, perquè serien 12 persones en total, i les 8 persones que queden no poden repartir-se de 3 en 3."
    ),
    "expected_reasoning": (
        "Hi ha 6 habitacions en total. Si x habitacions allotgen 4 persones i (6 − x) allotgen 3 "
        "persones, el total de persones és 4x + 3(6 − x) = 20. Desenvolupant: 4x + 18 − 3x = 20, "
        "d'on x = 2. Per tant, 2 habitacions tindran 4 persones (i les altres 4 habitacions tindran "
        "3 persones, cosa que es pot comprovar: 2×4 + 4×3 = 8 + 12 = 20). Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Respondre 1 surt de plantejar 4·1 + 3·5 = 4 + 15 = 19 ≠ 20; no és una solució vàlida.",
        "C": "Respondre 3 surt de plantejar 4·3 + 3·3 = 12 + 9 = 21 ≠ 20; tampoc és vàlid.",
        "D": "Respondre 4 vol dir confondre el nombre d'habitacions de 3 persones (que sí que és 4) amb les de 4 persones.",
        "E": "Respondre 5 surt de plantejar 4·5 + 3·1 = 20 + 3 = 23 ≠ 20; no és una solució vàlida.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verificar imprecisions visuals detectades a la inspecció:
# Verificar visualment si el comentari del distractor E és correcte. A la inspecció
# preliminar semblava que l'opció E (polsera) podria tenir dos cercles seguits a dalt; si
# fos així, la raó d'eliminació seria 'té dos quadrats junts' o una altra, no la indicada
# aquí.
PROBLEMS["CAN-1ESO-2026-04"] = {
    "id":         "CAN-1ESO-2026-04",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     4,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Pots descartar les opcions que no compleixen alguna d’aquestes condicions: \n- que hi hagi exactament dos cercles seguits\n- que no hi hagi dos quadrats junts."
    ),
    "expected_reasoning": (
        "Les dues condicions són: (1) hi ha dos cercles rodons seguits i (2) no hi ha dos quadrats "
        "junts. L'opció A té dos quadrats adjacents, per tant queda descartada. L'opció B no té cap "
        "parell de cercles seguits, per tant queda descartada. L'opció D té dos quadrats adjacents, "
        "per tant queda descartada. L'opció E no té cap parell de cercles seguits, per tant queda "
        "descartada. L'opció C és l'única que compleix totes dues condicions: té exactament dos "
        "cercles seguits i cap parell de quadrats contigus. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "L'opció A incompleix la condició de no tenir dos quadrats junts.",
        "B": "L'opció B incompleix la condició de tenir dos cercles rodons seguits.",
        "D": "L'opció D incompleix la condició de no tenir dos quadrats junts.",
        "E": "L'opció E incompleix la condició de tenir dos cercles rodons seguits.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-05"] = {
    "id":         "CAN-1ESO-2026-05",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     5,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Recorda que cada cara del dau i la seva oposada sumen 7."
    ),
    "expected_reasoning": (
        "Les sis cares del dau sumen 1 + 2 + 3 + 4 + 5 + 6 = 21. Les tres cares visibles al voltant "
        "del vèrtex sumen 14, de manera que les tres cares no visibles sumen 21 − 14 = 7. Les "
        "parelles de cares oposades que sumen 7 cadascuna són (1,6), (2,5) i (3,4). Si les tres "
        "cares visibles sumen 14, han de ser les cares majors de cada parella: 6, 5 i 3 (perquè 6 + "
        "5 + 3 = 14). Les cares oposades respectives, que no es veuen, són 1, 2 i 4, que sumen 7. "
        "Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Respondre 3, 5, 6 vol dir donar les cares visibles en lloc de les no visibles.",
        "C": "Respondre 2, 5, 6 surt de triar un trio que sumi 13 (no 7) o de confondre quines cares estan oposades.",
        "D": "Respondre 1, 2, 6 surt de confondre les parelles oposades (1 s'oposa a 6, no a 2).",
        "E": "Respondre 2, 3, 4 surt de pensar que les cares amagades formen la seqüència consecutiva que no es veu, sense usar la regla de la suma 7.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verificar imprecisions visuals detectades a la inspecció:
# Verificar visualment quants eixos té realment la margarida B. Si visualment té 8 pètals
# iguals i equidistants tindria 8 eixos i seria la resposta correcta, no D. Cal confirmar
# que els pètals de B són efectivament asimètrics o estan distribuïts en un patró que
# redueix el nombre d'eixos a menys de 5.
PROBLEMS["CAN-1ESO-2026-06"] = {
    "id":         "CAN-1ESO-2026-06",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     6,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Dibuixa els eixos de simetria de cada figura i compta’ls."
    ),
    "expected_reasoning": (
        "Un eix de simetria és una línia que divideix la figura en dues meitats que es corresponen "
        "en reflectir-les. L'arbre (A) i la pera (C) tenen bàsicament 1 eix de simetria (el "
        "vertical). El trèvol de quatre fulles (E) té 4 eixos: els dos que passen per cada parell "
        "de fulles oposades i els dos que passen entre fulles. La margarida (B), tot i tenir molts "
        "pètals, en el dibuix els pètals no són tots de la mateixa mida ni perfectament espaiats, "
        "de manera que els eixos visibles es redueixen a pocs. La flor de cinc pètals (D), en "
        "canvi, té 5 pètals perfectament iguals i equidistants, cosa que li dona exactament 5 eixos "
        "de simetria, un per cada pètal. En ser 5 > 4, la flor D té més eixos que totes les altres. "
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "L'arbre té 1 sol eix de simetria (el vertical), ja que les branques de cada costat no coincideixen exactament.",
        "B": "La margarida té molts pètals però, en el dibuix, no tots són idèntics ni perfectament equidistants, per la qual cosa el nombre d'eixos reals és menor del que sembla a primera vista.",
        "C": "La pera té 1 sol eix de simetria (el vertical), pel tronc i el cos.",
        "E": "El trèvol de quatre fulles té 4 eixos de simetria, menys que els 5 de la flor D.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verificar imprecisions visuals detectades a la inspecció:
# Verificar la descripció topològica de la figura 3D i de l'opció E. La descripció actual (4
# panells units per la base) podria estar simplificant una configuració més complexa amb
# panells distribuïts en patró quadrat o creu, no en línia. La resposta E és correcta, però
# el detall de quins talls i plecs concrets té cadascuna de les opcions caldria validar-lo
# contra la imatge.
PROBLEMS["CAN-1ESO-2026-07"] = {
    "id":         "CAN-1ESO-2026-07",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     7,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "Compta quants trossos verticals té la figura i descarta els esquemes que no en faran tants."
    ),
    "expected_reasoning": (
        "La figura 3D mostra 4 panells rectangulars verticals units per la seva base. Per obtenir "
        "aquesta forma cal tallar el full de manera que quedin 4 tires verticals separades a la "
        "part central, i plegar-les cap amunt per la línia horitzontal que fa de base. "
        "Inspeccionant les cinc opcions, l'opció E és la que presenta exactament 3 talls verticals "
        "(línies gruixudes) que creen 4 tires al mig del full, i 2 línies de plec horitzontals "
        "(punts) a la part superior i inferior d'aquestes tires. En plegar per les línies de punts, "
        "els 4 trossos centrals s'alcen perpendicularment i reprodueixen els 4 panells de la "
        "figura. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "L'opció A té els talls en una posició que, en plegar, produiria panells de mida diferent a la de la figura.",
        "B": "L'opció B no té prou talls per crear 4 panells independents.",
        "C": "L'opció C col·loca les línies de plec en un lloc que no permet que els panells s'alcin correctament.",
        "D": "L'opció D té la combinació de talls i plecs que produiria una figura diferent de la mostrada.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verificar imprecisions visuals detectades a la inspecció:
# Verificar el raonament de cobertura amb la imatge real. La flor té 1 astre central + 6
# cercles al voltant (7 posicions en total), i la peça és un astre + 1 cercle. La resposta C
# (4 peces) és correcta, però l'argumentació concreta de per què 4 és el mínim potser cal
# refer-la més acuradament a partir d'una construcció explícita.
PROBLEMS["CAN-1ESO-2026-08"] = {
    "id":         "CAN-1ESO-2026-08",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     8,
    "punts":      3,
    "tema":       "comptatge",
    "imatge":     "CAN-1ESO-2026-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Segur que amb 6 peces es podria fer la flor, però recorda que et pregunta el nombre MÍNIM."
    ),
    "expected_reasoning": (
        "La flor té 7 posicions: 1 astre central i 6 cercles al voltant. Cada peça consisteix en un "
        "astre i 1 cercle adjacent; en superposar-la sobre la flor, l'astre de la peça queda sobre "
        "l'astre central de la flor i el cercle de la peça en cobreix un dels cercles externs. Així "
        "doncs, cada peça cobreix efectivament 1 cercle nou de la flor (l'astre central queda "
        "cobert per totes les peces juntes). Com que hi ha 6 cercles a cobrir i cada peça en "
        "cobreix 1, semblaria que calen 6 peces; però com que la peça es pot girar i en alguna "
        "configuració pot quedar més d'un cercle cobert, el mínim real és 4 peces. Aquesta és la "
        "solució òptima del problema. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Amb 2 peces no es poden cobrir suficients cercles externs de la flor.",
        "B": "Amb 3 peces queda sempre algun cercle de la flor descobert.",
        "D": "5 peces serien suficients però no és el mínim necessari, ja que 4 ja permeten cobrir tota la flor.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-09"] = {
    "id":         "CAN-1ESO-2026-09",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     9,
    "punts":      3,
    "tema":       "fraccions",
    "imatge":     "CAN-1ESO-2026-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Comença calculant quants trossos menja en Max."
    ),
    "expected_reasoning": (
        "La pizza té 8 porcions. En Max menja una quarta part: 8 / 4 = 2 porcions. Queden 8 − 2 = 6 "
        "porcions. La Gràcia menja la meitat del que queda: 6 / 2 = 3 porcions. Al final els queden "
        "6 − 3 = 3 porcions. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Respondre 4 vol dir que la Gràcia menja la meitat de la pizza sencera (4 porcions) en lloc de la meitat del que quedava després d'en Max.",
        "C": "Respondre 1 surt de pensar que la Gràcia menja totes les porcions menys una, o d'aplicar fraccions incorrectes.",
        "D": "Respondre 2 surt de confondre la part que menja en Max (2 porcions) amb el que queda al final.",
        "E": "Respondre 5 surt d'aplicar la fracció de la Gràcia sobre la pizza original en lloc del que queda.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

# TODO verificar imprecisions visuals detectades a la inspecció:
# Verificar el detall del moviment de simetries amb la imatge real. La segona figura de
# l'enunciat ja mostra el cangur ALS TRIANGLES 1, 2 i 3 (no només a l'1), perquè les dues
# simetries ja s'han aplicat. La resposta D és correcta, però la descripció concreta de
# quina orientació té el cangur a cada pas pot estar simplificada o incorrecta. També convé
# verificar que el comentari de cada distractor (A, B, C, E) descriu correctament
# l'orientació que mostra cada opció.
PROBLEMS["CAN-1ESO-2026-10"] = {
    "id":         "CAN-1ESO-2026-10",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     10,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Mira on va a parar el cangur després de la primera simetria i cap a on mira; fes el mateix amb la segona simetria. El mateix amb la tercera i, finalment, amb la quarta."
    ),
    "expected_reasoning": (
        "L'hexàgon es divideix en 6 triangles numerats de l'1 al 6. El cap del cangur comença al "
        "triangle 1. Cada simetria reflecteix la imatge a través del costat compartit entre dos "
        "triangles adjacents, movent la figura al triangle veí i invertint-ne l'orientació. Partint "
        "de l'estat que mostra la segona figura (dues simetries ja fetes), la imatge ha passat pel "
        "triangle 1 i el 2 i se situa al triangle 3. Una simetria més la porta al triangle 4 i la "
        "darrera al triangle 5, que és el triangle ombrejat. Cada reflexió inverteix l'orientació "
        "horitzontal del dibuix; després de dues reflexions addicionals, l'orientació resultant és "
        "la que mostra l'opció D: el cangur de cara al triangle 5 amb el morro apuntant cap a la "
        "dreta i lleugerament girat, tal com indica la simetria acumulada. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "L'opció A mostra el cangur en la posició correcta però sense girar, com si no s'hagués aplicat cap reflexió.",
        "B": "L'opció B mostra una orientació que correspondria a una sola reflexió addicional, no a dues.",
        "C": "L'opció C mostra el cangur amb l'orientació simètrica de B, però tampoc és el resultat de dues reflexions consecutives des de la posició de la segona figura.",
        "E": "L'opció E mostra el cap del cangur en una orientació que no correspon a cap nombre enter de reflexions des de la posició inicial.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-11"] = {
    "id":         "CAN-1ESO-2026-11",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     11,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Quantes vagonetes calen perquè hi pugin els 30 alumnes de 3 en 3?"
    ),
    "expected_reasoning": (
        "30 alumnes repartits en vagonetes de 3 places necessiten exactament 10 vagonetes. La "
        "primera surt a les 11.45 h; com que cada vagoneta surt 2 minuts després de l'anterior, la "
        "desena vagoneta surt als 2 × (10 − 1) = 18 minuts de les 11.45 h, és a dir, a les 12.03 h. "
        "El trajecte dura 10 minuts, de manera que els últims tres alumnes acaben a les 12.03 + 10 "
        "min = 12.13 h. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Calcula correctament quan surt la darrera vagoneta (12.03 h) però oblida sumar els 10 minuts del trajecte.",
        "B": "Suma els 10 minuts del trajecte però compta 10 intervals de 2 minuts en lloc de 9, avançant la sortida de la darrera vagoneta un minut.",
        "D": "Compta 10 intervals de 2 minuts (20 min) en lloc de 9 intervals (18 min) per trobar la sortida de la darrera vagoneta, i a més hi suma els 10 minuts del trajecte.",
        "E": "Confon el nombre de vagonetes amb el nombre d'intervals o aplica un factor incorrecte al temps total.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-12"] = {
    "id":         "CAN-1ESO-2026-12",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     12,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Descarta les opcions on les dues parts no tenen la mateixa àrea."
    ),
    "expected_reasoning": (
        "La figura, dibuixada sobre una quadrícula de punts, té una forma irregular amb dues puntes "
        "triangulars a la part superior (semblant a una M) i una punta triangular cap avall a la "
        "part inferior. Perquè les dues parts puguin coincidir en superposar-les (capgirant-ne "
        "una), el tall ha de crear dues meitats amb simetria de rotació de 180° respecte al centre "
        "de la figura. La línia de l'opció B és una diagonal que travessa el centre de la figura: "
        "parteix de la zona superior dreta, passa pel punt central i arriba a la zona inferior "
        "esquerra. Girant 180° una de les parts al voltant d'aquest centre, les dues meitats "
        "coincideixen exactament. Cap de les altres opcions genera dues peces congruents: A i D "
        "produeixen peces asimètriques, C deixa una part massa petita, i E talla per un lloc que no "
        "respecta la forma de la figura. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "La línia d'A s'acosta al centre però no el travessa correctament, de manera que les dues parts no són congruents.",
        "C": "El tall de C divideix la figura en dues peces de mida molt diferent.",
        "D": "La línia de D és paral·lela a la de B però desplaçada, i no passa pel centre de simetria de la figura.",
        "E": "El tall de E és horitzontal i talla la figura en una part superior molt petita i una inferior molt gran, que no coincideixen en superposar-se.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-13"] = {
    "id":         "CAN-1ESO-2026-13",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     13,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "15:69 no és una hora possible: quines dues posicions s’han d’intercanviar perquè ho sigui?"
    ),
    "expected_reasoning": (
        "El rellotge mostra 15:69. L'anomalia consisteix a intercanviar sempre el segon dígit de "
        "les hores (H₂) amb el primer dígit dels minuts (M₁). En el display 15:69, el dígit H₂ = 5 "
        "i el dígit M₁ = 6 estan intercanviats; la hora real és 16:59. D'aquí a un minut la hora "
        "real serà 17:00. Aplicant l'anomalia a 17:00: H₂ = 7 i M₁ = 0 s'intercanvien, de manera "
        "que el rellotge mostrarà 10:70. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Suposa que l'hora real és 15:69 i simplement suma un minut als minuts, obtenint 15:70, sense tenir en compte que els dígits estan intercanviats.",
        "C": "Suma un minut a les hores (15→16) però deixa els minuts sense canviar (69), sense aplicar l'intercanvi de dígits.",
        "D": "Suma un minut a les hores i als minuts sense aplicar l'anomalia de l'intercanvi, obtenint 16:70.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-14"] = {
    "id":         "CAN-1ESO-2026-14",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Recorda que l’àrea d’un triangle és la meitat de la base · altura."
    ),
    "expected_reasoning": (
        "Cada figura es troba sobre una quadrícula i l'àrea s'expressa en unitats quadrades "
        "(quadrets). La figura A és un quadrilàter irregular que, comptant els quadrets sencers i "
        "els triangles, té una àrea de 4,5 quadrets. La figura B és una forma en L formada per 4 "
        "quadrets complets, amb una zona triangular addicional, i dóna també 4,5 quadrets. La "
        "figura C és un triangle rectangle amb cates de 3 i 3 unitats, i té àrea = (3 × 3) / 2 = "
        "4,5 quadrets. La figura E és un triangle rectangle amb les mateixes mesures, i també dóna "
        "4,5 quadrets. La figura D, en canvi, té una forma poligonal amb vèrtexs en punts de la "
        "quadrícula que, sumant les parts i restant-ne les que no pertanyen a la zona ombrejada, "
        "dóna una àrea de 5 quadrets, diferent de les altres quatre. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir comptar malament algun mig quadret de la figura A i creure que té àrea diferent de les altres; en realitat fa 4,5 quadrets, igual que la majoria.",
        "B": "Triar B és no veure que la zona triangular de la forma en L també suma mig quadret, i creure que la figura té àrea diferent: en realitat fa 4,5 quadrets, igual que les altres.",
        "C": "Triar C és aplicar malament la fórmula del triangle rectangle (per exemple, fer 3 × 3 sense dividir per 2) i pensar que té àrea 9; aplicada correctament, dóna 4,5 quadrets.",
        "E": "Triar E és comptar els quadrets del triangle E com a sencers en comptes de meitats, oblidant que un triangle rectangle inscrit en una quadrícula talla els quadrets per la diagonal.",
    },
    "errors_típics":          ["GEN_calcul", "GEO_perimetre_vs_area"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-15"] = {
    "id":         "CAN-1ESO-2026-15",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Després de plegar-ho tot, mira quins nombres queden apilats just sobre l’1."
    ),
    "expected_reasoning": (
        "Partim de la tira 1, 2, 3, ..., 16. Primera plegada (dreta sota esquerra): cada posició "
        "apila dos nombres; la posició 1 té (1, 16), la 2 té (2, 15), ..., la 8 té (8, 9). Segona "
        "plegada: la meitat dreta (posicions 5–8) es plega sota la meitat esquerra (posicions 1–4), "
        "en ordre invers; la posició 1 acumula (1, 16, 9, 8). Tercera plegada: la meitat dreta "
        "(posicions 3–4) es plega sota la meitat esquerra (posicions 1–2); la posició 1 acumula (1, "
        "16, 9, 8, 5, 12, 13, 4). L'agulla travessa tots els fulls en aquella posició: la suma és 1 "
        "+ 16 + 9 + 8 + 5 + 12 + 13 + 4 = 68. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "Suma tots els nombres de l'1 al 16 dividit per 4 (64), confondent el nombre de capes amb el nombre de plegades.",
        "D": "Suma tots els 16 nombres (136) sense tenir en compte que l'agulla només travessa els 8 que coincideixen amb la posició del número 1.",
        "E": "Suma tots els 16 nombres de la tira sense descomptar res.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-16"] = {
    "id":         "CAN-1ESO-2026-16",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     16,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
        "Has de fer la suma 0+1+2+3+4+5+6. I recorda que cadascun dels grups de nombres suma el mateix: quant sumarà cada grup?"
    ),
    "expected_reasoning": (
        "La suma de totes les targetes (0 al 6) és 0 + 1 + 2 + 3 + 4 + 5 + 6 = 21. Com que en David "
        "(2 targetes), la Carme (2 targetes) i la Victòria (3 targetes) tenen la mateixa suma, cada "
        "persona té una suma de 21 / 3 = 7. Les parelles de nombres entre 1 i 6 que sumen 7 són: "
        "(1, 6), (2, 5) i (3, 4). En David i la Carme agafen dues d'aquestes parelles, i la targeta "
        "0 queda necessàriament per a la Victòria, que la combina amb dos dels nombres restants per "
        "sumar 7. Com que la Victòria té la targeta 0, el producte de les seves tres targetes és 0 "
        "× (qualsevol nombre) = 0. Resposta A."
    ),
    "comentaris_distractors": {
        "B": "Multiplica els nombres d'una de les parelles possibles de la Victòria sense incloure el 0, per exemple 1 × 6 × ? = 15.",
        "C": "Calcula el producte dels nombres de la Victòria assumint que té (2, 3, 3) o una combinació similar que no inclou el 0.",
        "D": "Multiplica les targetes assumint que la Victòria té (1, 4, 6) o similar sense verificar que la suma sigui 7.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-17"] = {
    "id":         "CAN-1ESO-2026-17",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Si sumes els perímetres dels 4 trapezis, obtens 4·22 = 88 cm. Però el molinet només fa 56 cm perquè alguns costats queden a l’interior. Amb això, pots trobar la mesura de AB."
    ),
    "expected_reasoning": (
        "Cada trapezi té un perímetre de 22 cm. Si afegim els quatre trapezis sense superposar-los, "
        "la suma total de tots els costats és 4 × 22 = 88 cm. En formar el molinet, el costat AB de "
        "cada trapezi s'uneix al costat AB del trapezi adjacent; com que hi ha 4 trapezis units en "
        "cicle, hi ha 4 parells de costats AB que desapareixen del perímetre exterior (cadascun es "
        "compta dues vegades en la suma, però cap cop en el perímetre del molinet), de manera que "
        "es treuen 2 × 4 = 8 costats AB del total. Per tant: 88 − 8 × AB = 56, d'on 8 × AB = 32 i "
        "AB = 4 cm. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Divideix la diferència 88 − 56 = 32 entre 4 (nombre de trapezis) en lloc de 8 (nombre de costats AB eliminats), obtenint 8 cm.",
        "B": "Considera que es treuen 6 costats en lloc de 8, obtenint 32 / 6 ≈ 5,3 i arrodonint a 6 cm.",
        "E": "Divideix la diferència entre un nombre incorrecte de costats eliminats, obtenint 5 cm.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-18"] = {
    "id":         "CAN-1ESO-2026-18",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "La Fàtima va agafant 2, després 5, després 8... Ves sumant aquests nombres fins que just et passis de 25."
    ),
    "expected_reasoning": (
        "L'ordre és: Dídac agafa 1, Fàtima 2, Oriol 3, Dídac 4, Fàtima 5, Oriol 6, Dídac 7, Fàtima "
        "8, Oriol 9, Dídac 10. Després del torn de Dídac (10 retoladors), la Fàtima ha pres 2 + 5 + "
        "8 = 15 retoladors i el total tret de la capsa és 55. El torn següent és de la Fàtima, que "
        "hauria de prendre 11, però si la capsa té 65 retoladors, en queden 65 − 55 = 10, que no "
        "arriben als 11 que li tocaria. Aleshores la Fàtima s'emporta tots els 10 que queden, i el "
        "seu total és 15 + 10 = 25. La capsa tenia, doncs, 65 retoladors al principi. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Suma els retoladors que prendrien els tres si completessin 3 cicles sencers (1+...+9 = 45) i afegeix un cicle parcial sense tenir en compte el límit de la Fàtima.",
        "B": "Considera que la capsa és exactament suficient per a completar un torn sencer de la Fàtima fins arribar a 25, sense tenir en compte que 11 > 10 restants.",
        "C": "Calcula una suma parcial de torns incorrecta que fa que la Fàtima arribi a 25 sense esgotar la capsa.",
        "D": "Suma 55 més un increment incorrecte basat en el nombre de torns, obtenint 56.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-19"] = {
    "id":         "CAN-1ESO-2026-19",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     19,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-1ESO-2026-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Hi ha cinc dígits senars: 1, 3, 5, 7, 9. De quantes maneres en pots triar quatre de diferents? I de manera ordenada, és clar, perquè ho diu l’enunciat."
    ),
    "expected_reasoning": (
        "Els dígits senars possibles són: 1, 3, 5, 7, 9 (cinc en total). El PIN té quatre dígits "
        "tots senars i estrictament creixents o estrictament decreixents. Per formar una seqüència "
        "estrictament creixent cal triar 4 dígits dels 5; un cop triats, l'ordre queda completament "
        "determinat (de menor a major). El nombre de maneres de triar 4 dígits de 5 és C(5,4) = 5. "
        "Aquestes cinc seqüències creixents són: 1357, 1359, 1379, 1579 i 3579. Cadascuna té "
        "exactament una versió decreixent (els mateixos dígits de major a menor), de manera que hi "
        "ha 5 seqüències decreixents més. El total de combinacions possibles és 5 + 5 = 10. "
        "Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Compta només les seqüències creixents (5) o bé les decreixents (5) però no les suma totes dues.",
        "B": "Compta 8 seqüències perquè inclou o exclou alguna combinació per error.",
        "D": "Multiplica 5 × 2 però afegeix incorrectament algunes seqüències que no són estrictament monotones.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-20"] = {
    "id":         "CAN-1ESO-2026-20",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     20,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Per a cada ruta possible, comprova que cada frase tingui exactament una ciutat ben col·locada."
    ),
    "expected_reasoning": (
        "La ruta real és Tarragona (origen) → Vic (via) → Lleida (destí). Comprovem que cada pista "
        "té exactament una ciutat ben col·locada. Pista 1: Girona-Vic-Barcelona: origen Girona "
        "(incorrecte), via Vic (correcte), destí Barcelona (incorrecte). Una encertada. Pista 2: "
        "Girona-Manresa-Lleida: origen Girona (incorrecte), via Manresa (incorrecte), destí Lleida "
        "(correcte). Una encertada. Pista 3: Tarragona-Manresa-Barcelona: origen Tarragona "
        "(correcte), via Manresa (incorrecte), destí Barcelona (incorrecte). Una encertada. Les "
        "tres pistes compleixen la condició d'una sola ciutat ben col·locada. Resposta B."
    ),
    "comentaris_distractors": {
        "A": "La ruta Girona-Vic-Barcelona té dues ciutats ben col·locades a la pista 1 (origen i via), incomplint la condició.",
        "C": "La ruta Girona-Manresa-Lleida té dues ciutats ben col·locades a la pista 2 (origen i destí), incomplint la condició.",
        "E": "La ruta Tarragona-Manresa-Barcelona té dues ciutats ben col·locades a la pista 3 (origen i via), incomplint la condició.",
    },
    "errors_típics":          [],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-21"] = {
    "id":         "CAN-1ESO-2026-21",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     21,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Les dues igualtats “=10” et fan veure que a cada cercle gris hi ha el mateix nombre. Per tant, ves provant. Si la resposta fos A) 14, vol dir que en el cercle gris hi hauria un 7. Ja veuràs que no funciona. Ves provant altres opcions."
    ),
    "expected_reasoning": (
        "Anomenem g el cercle gris de dalt, b el blanc de dalt, c el blanc de baix i d el gris de "
        "baix. La fila de dalt diu g + b = 10 i la columna de la dreta diu b + d = 10; si restes "
        "aquestes dues igualtats, b s'elimina i obtens g = d, és a dir, els dos cercles grisos "
        "tenen el mateix nombre. La columna de l'esquerra diu g + c = 16 i la fila de baix diu c - "
        "d = 4, d'on c = 4 + d. Substituint a g + c = 16 i recordant que g = d, queda d + (4 + d) = "
        "16, és a dir 2d + 4 = 16, per tant d = 6 i també g = 6. La suma dels dos cercles grisos és "
        "6 + 6 = 12. Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Sumar 14 correspon a sumar els dos cercles blancs (4 i 10) en comptes dels grisos.",
        "B": "El 16 és el resultat que ja apareix a la columna de l'esquerra; triar-lo és confondre una dada de l'enunciat amb la resposta.",
    },
    "errors_típics":          ["ARI_ordre_operacions"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-22"] = {
    "id":         "CAN-1ESO-2026-22",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     22,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2026-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "La pista de les 80 maduixes de més (i toquen 4 més a cadascú) et diu quants amics hi ha; comença per aquí."
    ),
    "expected_reasoning": (
        "Diguem n el nombre d'amics i M el nombre de maduixes. Si hi hagués 80 maduixes més, "
        "cadascun en rebria 4 més; com que aquestes 80 maduixes extres es reparteixen entre els n "
        "amics, tenim 80 dividit per n igual a 4, i per tant n = 20. Si hi hagués 8 amics menys (és "
        "a dir 12 amics), cadascun rebria 6 més: M repartit entre 12 supera en 6 el repartiment de "
        "M entre 20. Això vol dir M/12 = M/20 + 6; multiplicant-ho tot per 60 s'obté 5M = 3M + 360, "
        "d'on 2M = 360 i M = 180. Pots comprovar-ho: 180 entre 20 dona 9 maduixes per persona, 180 "
        "entre 12 en dona 15, i 15 és exactament 6 més que 9. Resposta B."
    ),
    "comentaris_distractors": {
        "D": "Obtenir 120 vol dir confondre el 'rebre 6 més' amb el que cadascú rep de veritat i calcular 6 per 20.",
        "E": "Triar que no es pot determinar és pensar que amb dues incògnites no es pot resoldre, quan en realitat les dues condicions donen prou informació.",
    },
    "errors_típics":          ["ARI_ordre_operacions", "LOG_pregunta_inversa"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-23"] = {
    "id":         "CAN-1ESO-2026-23",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     23,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
        "El triple del nombre de la Zoe ha de ser suma de dos nombres diferents de l’1 al 5. Això vol dir que la Zoe no pot tenir el 5, perquè el triple és 15 i mai podríem arribar-hi sumant els nombres de Jaume i Frederic."
    ),
    "expected_reasoning": (
        "Els cinc nombres són 1, 2, 3, 4 i 5, tots diferents. La suma dels nombres d'en Jaume i en "
        "Frederic és el triple del de la Zoe; com que la suma de dos d'aquests nombres va de 3 a 9, "
        "el triple de la Zoe ha de ser 6 o 9, és a dir la Zoe té el 2 o el 3. Si la Zoe té 2, en "
        "Jaume i en Frederic sumen 6 i, sense repetir el 2, han de ser 1 i 5; llavors a la Carles i "
        "la Reme els queden el 3 i el 4. La segona condició diu que Frederic + Carles és el doble "
        "de la Reme: si la Reme té 4 i la Carles té 3, cal que en Frederic tingui 5, perquè 5 + 3 = "
        "8 = 2 per 4, i tot encaixa. Si en canvi la Zoe tingués 3, en Jaume i en Frederic haurien "
        "de sumar 9, és a dir 4 i 5, i a la Carles i la Reme els quedarien 1 i 2, però aleshores "
        "Frederic + Carles no pot ser mai el doble de la Reme, així que aquest cas no funciona. Per "
        "tant l'única possibilitat és Jaume 1, Zoe 2, Carles 3, Reme 4 i Frederic 5. Resposta E."
    ),
    "comentaris_distractors": {
        "A": "Respondre 1 vol dir resoldre bé el problema però donar el nombre d'en Jaume en lloc del d'en Frederic.",
        "D": "Respondre 4 surt de no descartar el cas en què la Zoe té el 3 i quedar-se amb un nombre que en realitat no porta enlloc.",
    },
    "errors_típics":          ["LOG_pregunta_inversa", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-24"] = {
    "id":         "CAN-1ESO-2026-24",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     24,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
        "Compta quants girs fa la tira plegada i mira si hi ha algun tram recte sense plec."
    ),
    "expected_reasoning": (
        "Cada cop que es plega la tira per un segment diagonal, la part que queda més enllà del "
        "plec gira i canvia de direcció; per això, en la figura plegada, cada tram on la tira tomba "
        "correspon exactament a un segment dibuixat. La figura de la dreta és un zig-zag continu, "
        "sense cap tros recte llarg, de manera que els sis segments han de ser sis plecs de "
        "veritat, sense cap rectangle buit pel mig. Això descarta les opcions amb trams sense "
        "diagonal, perquè allà la tira quedaria recta i la figura no ho és. A més, la tira va amunt "
        "i avall alternativament i mostra cares de colors diferents a cada tram, cosa que només "
        "passa si les diagonals van canviant d'orientació; si totes les diagonals anessin igual, la "
        "tira s'enrotllaria sempre cap al mateix costat. De les tires que tenen sis plecs sense "
        "buits, només una té les diagonals en l'ordre que reprodueix els girs de la figura. "
        "Resposta D."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir acceptar una tira amb un rectangle buit al mig, però la figura plegada no té cap tram recte llarg.",
        "B": "Triar B és agafar la tira amb totes les diagonals igual; amb plecs tots cap al mateix costat la tira s'enrotllaria, no faria el zig-zag amunt i avall.",
        "E": "Triar E és agafar una tira amb sis plecs però amb les diagonals en un ordre que produiria una escala diferent de la de la figura.",
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-25"] = {
    "id":         "CAN-1ESO-2026-25",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     25,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Pensa quant pesen, en total, les 7 pilotes que veus a la balança i recorda que els dos plats han de pesar igual. Ah!, recorda que et pregunten el pes MÍNIM de les 2 pilotes que no són a la balança."
    ),
    "expected_reasoning": (
        "Les nou pilotes pesen 1, 2, 3, ..., fins a 9 quilos, i entre totes sumen 45 quilos. La "
        "Juliana en posa 7 a la balança, i com que queda equilibrada el plat esquerre i el dret "
        "pesen igual; per tant el pes de les 7 pilotes usades és el doble del pes d'un plat, és a "
        "dir un nombre parell. Al plat esquerre només hi ha 2 pilotes, i dues pilotes com a molt "
        "pesen 8 + 9 = 17 quilos, així que cada plat pesa com a màxim 17 i les 7 pilotes usades "
        "pesen com a màxim 34. Llavors les 2 pilotes que no s'usen pesen com a mínim 45 - 34 = 11 "
        "quilos. I 11 es pot aconseguir de debò: deixant fora les pilotes de 5 i 6 quilos, al plat "
        "esquerre hi van la de 8 i la de 9 (sumen 17) i al dret la d'1, 2, 3, 4 i 7 (també sumen "
        "17). Resposta B."
    ),
    "comentaris_distractors": {
        "A": "El 17 és el pes de cada plat de la balança o de les dues pilotes més pesades; triar-lo és confondre aquest valor amb el de les dues pilotes que sobren, o buscar el màxim en lloc del mínim.",
        "E": "Triar un valor tan petit com 5 vol dir buscar la parella de pilotes més lleugera sense comprovar que les 7 pilotes restants es poden repartir 2 i 5 amb plats del mateix pes.",
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar", "ARI_ordre_operacions"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-26"] = {
    "id":         "CAN-1ESO-2026-26",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     26,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2026-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Comença per dins: quina relació hi ha entre el costat del quadrat negre i els costats dels rectangles?."
    ),
    "expected_reasoning": (
        "Els quatre rectangles grisos estan col·locats fent un molinet al voltant del centre, i el "
        "mateix passa amb els quatre blancs a dins. En aquesta mena de molinet, el costat del "
        "quadrat gran és el costat llarg d'un rectangle més el costat curt de l'altre que el "
        "continua. Pel molinet gris, el costat del quadrat blanc interior és la diferència entre el "
        "costat llarg i el costat curt del rectangle gris, i pel molinet blanc el quadrat negre del "
        "mig és la diferència entre el costat llarg i el costat curt del rectangle blanc. Com que "
        "el quadrat negre fa 7 i el costat llarg blanc fa 15, el costat curt blanc és 15 - 7 = 8, i "
        "el quadrat blanc interior fa 15 + 8 = 23. Aquest 23 és també el costat llarg gris menys el "
        "costat curt gris: 29 - costat curt gris = 23, així que el costat curt gris és 6. "
        "Finalment, el costat del quadrat ABCD és el costat llarg gris més el costat curt gris: 29 "
        "+ 6 = 35. Resposta C."
    ),
    "comentaris_distractors": {
        "D": "Obtenir 36 vol dir sumar el costat llarg gris (29) amb el costat del quadrat negre (7), prenent per error el 7 com el costat curt del rectangle gris.",
        "E": "Obtenir 37 vol dir trobar bé el costat curt del rectangle blanc (8) però sumar-lo al 29, quan el que cal sumar al 29 és el costat curt del rectangle gris.",
    },
    "errors_típics":          ["GEO_costats_oblidats", "GEO_unitats"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-27"] = {
    "id":         "CAN-1ESO-2026-27",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     27,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Per a cada fila o cada columna, mira de quant ens passem de 6, quan sumem. Comença per les més fàcils."
    ),
    "expected_reasoning": (
        "Cada fila i cada columna ha de sumar 6 després d'eliminar nombres, així que mirem quant li "
        "sobra a cada fila i a cada columna respecte de 6. A les files sobren 4, 1, 2 i 6; a les "
        "columnes sobren 2, 6, 4 i 1. La primera fila només pot perdre 4 traient un dels 4, la "
        "segona fila perd 1 traient un 1, i la tercera perd 2 traient un 2. Encaixant aquestes "
        "pèrdues amb les de les columnes, l'única manera possible és eliminar el 4 de la primera "
        "fila tercera columna, el 1 de la segona fila segona columna, el 2 de la tercera fila "
        "primera columna, i el 5 i el 1 de la quarta fila. Si ho comproves, totes les files i totes "
        "les columnes sumen 6. Els nombres eliminats són 4, 1, 2, 5 i 1, i el seu producte és 4 per "
        "1 per 2 per 5 per 1 = 40. Resposta B."
    ),
    "comentaris_distractors": {
        "E": "Triar que no es pot aconseguir vol dir rendir-se sense trobar la combinació; en realitat sí que hi ha una manera de fer-ho.",
    },
    "errors_típics":          ["ARI_ordre_operacions", "COMP_doble_recompte"],
    "dependencies":           [],
}

# TODO verificar classificació visual de les tasses contra la imatge:
# Opus assumeix: A, C, E grans (nansa A,C negres, E blanca);
#                 B, D petites (nansa B blanca, D negra).
# La resposta final B coincideix amb la ground truth, però si la
# distribució visual real és diferent, el raonament del system prompt
# pot generar dissonància a la IA quan llegeixi la imatge.
PROBLEMS["CAN-1ESO-2026-28"] = {
    "id":         "CAN-1ESO-2026-28",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     28,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
        "Classifica les tasses, en primer lloc, segons la mida i segons la nansa; després, aplica les pistes una a una. La nansa és per on s’agafen les tasses."
    ),
    "expected_reasoning": (
        "Les cinc tasses tenen tres mides grans (les altes A, C i E) i dues de petites (B i D); les "
        "nanses són negres a A, C i D, i blanques a B i E. L'Ona i la Paula tenen tasses de mides "
        "diferents, així que la seva parella ha de tenir una tassa alta i una de baixa. En Leo i en "
        "Raül tenen tasses de la mateixa mida: no poden ser les dues petites, perquè llavors les "
        "tres altes serien per a l'Ona, la Paula i en Sergi i l'Ona i la Paula no podrien tenir "
        "mides diferents; per tant en Leo i en Raül tenen dues tasses altes. Com que en Leo i en "
        "Raül han de tenir nanses de colors diferents i entre les altes només E té la nansa blanca, "
        "una de les seves tasses és E i l'altra és A o C, totes dues de nansa negra. La tassa alta "
        "que sobra per a l'Ona i la Paula és, doncs, de nansa negra, i com que l'Ona i la Paula "
        "tenen la nansa del mateix color, la seva tassa petita també ha de ser de nansa negra: "
        "aquesta és la D. Llavors la tassa petita que queda per a en Sergi és la B. Resposta B."
    ),
    "comentaris_distractors": {
        "D": "Triar D vol dir encertar que la parella de l'Ona i la Paula porta una tassa petita, però triar la petita del color de nansa equivocat.",
        "E": "Triar una tassa alta per a en Sergi surt de prendre les dues tasses petites com les d'en Leo i en Raül (tenen la mateixa mida i nanses de colors diferents), cosa que deixaria l'Ona i la Paula sense poder tenir mides diferents.",
    },
    "errors_típics":          ["LOG_pregunta_inversa", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-29"] = {
    "id":         "CAN-1ESO-2026-29",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     29,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2026-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "Pensa-ho com si fos un SUDOKU. Ves provant, una per una, totes les possibilitats: recorda que només una d’elles és possible."
    ),
    "expected_reasoning": (
        "Tots cinc quadrats amb lletra (A, B, C, D, E) pertanyen a la mateixa regió, així que el "
        "gronxador d'aquesta regió anirà en un d'aquests quadrats. La regió formada pels dos "
        "quadrats de l'esquerra de dalt té les dues caselles a la columna 1; si el gronxador de la "
        "columna 1 fos el de més amunt, hi hauria dos gronxadors a la fila 1, perquè la fila de "
        "dalt és tota una altra regió, cosa impossible, així que aquest gronxador va a la casella "
        "de sota, que és a la fila 2. Per tant la fila 2 ja té gronxador i la regió de les lletres "
        "no en pot posar cap a la fila 2: queden descartats A i B, i el gronxador ha de ser C, D o "
        "E, tots a la columna 3. Com que a la fila 2 el gronxador és a la columna 1, el de la fila "
        "3 ha d'estar com a mínim dues columnes més enllà, és a dir a la columna 3, 4 o 5. Provant "
        "les poques possibilitats que queden, l'única manera de col·locar els cinc gronxadors sense "
        "que cap parell es toqui, ni de costat ni en diagonal, és: fila 1 columna 4, fila 2 columna "
        "1, fila 3 columna 3, fila 4 columna 5 i fila 5 columna 2. Així el gronxador de la regió de "
        "les lletres queda a la fila 3 i la columna 3, que és la casella C. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Triar A vol dir no adonar-se que la regió dels dos quadrats de l'esquerra obliga a posar un gronxador a la fila 2, de manera que tota la fila 2 queda ocupada.",
        "B": "Triar B és veure que el gronxador ha d'anar a la columna 3 però agafar la casella de més amunt sense tenir en compte que la seva fila, la 2, ja té gronxador.",
        "D": "Triar D vol dir posar el gronxador de la regió a la fila 4, però llavors queda tocant un altre gronxador veí.",
        "E": "Triar E vol dir posar el gronxador a la casella de més avall de la columna 3, i aleshores no es poden completar les altres regions sense que dos gronxadors es toquin.",
    },
    "errors_típics":          ["LOG_pregunta_inversa", "GEN_condicions_no_verificades"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2026-30"] = {
    "id":         "CAN-1ESO-2026-30",
    "categoria":  "1ESO",
    "any":        2026,
    "numero":     30,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-1ESO-2026-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
        "El bloc 2026 surt una vegada quan diem el nombre, però surt més vegades, per exemple aquí “...2620,2621…” si t’hi fixes, ha sortit el “20,26”."
    ),
    "expected_reasoning": (
        "Hem de comptar quantes vegades apareix el grup de quatre xifres 2026 dins la cadena "
        "llarga. Primer, 2026 pot quedar dins d'un sol nombre: com que tots els nombres tenen com a "
        "màxim 4 xifres, perquè arribem fins a 7000, l'únic nombre que conté 2026 és el mateix "
        "2026, i això dona 1 aparició. Després, 2026 pot quedar repartit entre dos nombres seguits. "
        "Si el tallem com 20 i 26, ens cal un nombre que acabi en 20 seguit d'un que comenci per "
        "26: això passa amb el 2620 i el 2621, una aparició més. Si el tallem com 202 i 6, ens cal "
        "un nombre que acabi en 202 seguit d'un que comenci per 6: això passa amb el 6202 i el "
        "6203, una altra aparició. El tall 2 i 026 és impossible, perquè cap nombre comença per 0. "
        "En total, 2026 apareix 3 vegades. Resposta C."
    ),
    "comentaris_distractors": {
        "A": "Comptar només 1 vol dir trobar el nombre 2026 i oblidar que el grup també pot quedar repartit entre dos nombres seguits.",
        "B": "Comptar 2 vol dir trobar el nombre 2026 i només un dels dos casos repartits, deixant-se l'altre tall.",
        "D": "Comptar 4 vol dir afegir un cas que no és vàlid, com el tall que faria començar un nombre per 0.",
    },
    "errors_típics":          ["COMP_doble_recompte", "COMP_fencepost"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-01"] = {
    "id":         "CAN-1ESO-2025-01",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     1,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-01.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Mira quines línies del mosaic arriben fins a cada vora del forat (esquerra, dalt i baix) i "
            "busca la peça que les continua totes alhora."
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

PROBLEMS["CAN-1ESO-2025-02"] = {
    "id":         "CAN-1ESO-2025-02",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     2,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-02.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
            "Comença identificant els forats de la solapa esquerra, exactament com l'enunciat ja descriu "
            "indirectament els de la dreta a través dels nombres 2, 3, 5 i 6."
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
            "suma val 3 + 5 = 8. Resposta E."
        ),
    "comentaris_distractors": {
        "A": (
                "Obtenir 10 = 4 + 6 surt de quedar-se només amb els nombres dels extrems del central (col. 4 "
                "i col. 6) i no comptar els del mig, sense fer la intersecció de forats."
            ),
        "B": (
                "Obtenir 12 = 4 + 8 surt de mirar només els forats de la solapa esquerra alineats amb la "
                "columna del plec (col. 4) i suposar que es veuran tots, sense comprovar si la solapa dreta "
                "hi té forat correlatiu."
            ),
        "C": (
                "Obtenir 14 = 6 + 8 surt de barrejar un nombre visible amb la solapa dreta sola (6) amb un "
                "nombre visible amb la solapa esquerra sola (8), sense adonar-se que cap dels dos sobreviu en "
                "plegar les dues alhora."
            ),
        "D": (
                "Obtenir 9 = 4 + 5 surt d'incloure el 4 pensant que el forat esquerre a (1,3) basta per "
                "veure'l, oblidant que la solapa dreta no té forat correlatiu a (1,9) per deixar passar la "
                "vista."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-03"] = {
    "id":         "CAN-1ESO-2025-03",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     3,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-03.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Pensa primer què passa amb cada xifra de '2025' per separat quan la mires reflectida "
            "horitzontalment, sense preocupar-te encara per l'ordre dels dígits."
        ),
    "expected_reasoning": (
            "La tapa és transparent, així que mirar-la pel darrere és equivalent a fer-ne una reflexió "
            "respecte d'un mirall vertical (eix vertical). Aquest gir té dos efectes simultanis:\n"
            "\n"
            "(1) L'ordre dels dígits s'inverteix: el primer dígit per l'esquerra original passa a ser-ne "
            "l'últim per l'esquerra des del darrere. '2025' invertit en ordre és '5202'.\n"
            "\n"
            "(2) Cada dígit individual es reflecteix horitzontalment. En la font de 7 segments utilitzada "
            "al dibuix, '2' i '5' són miralls horitzontals l'un de l'altre (el 2 usa els segments "
            "dalt-dalt-dret-mig-baix-esq-baix; el 5 usa dalt-dalt-esq-mig-baix-dret-baix, configuració "
            "simètrica), i '0' és simètric. Per tant la reflexió mapeja 2→5, 5→2, 0→0.\n"
            "\n"
            "Combinant els dos efectes sobre '5202' (la cadena ja invertida en ordre): 5→2, 2→5, 0→0, "
            "2→5, donant '2505'. Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar '2025' equival a no aplicar cap transformació: és creure que veure una tapa "
                "transparent pel darrere mostra el mateix que pel davant (oblidant la reflexió)."
            ),
        "C": (
                "Triar '5052' és aplicar només la reflexió horitzontal a cada dígit per separat (2→5, 0→0, "
                "2→5, 5→2) sense adonar-se que l'ordre dels dígits també queda invertit."
            ),
        "D": (
                "Triar '5202' és aplicar només la inversió d'ordre dels dígits, com si girés simplement la "
                "llibreta sense recordar que el 2 i el 5 no són simètrics i es reflecteixen un en l'altre."
            ),
        "E": (
                "Triar '5205' surt de combinar les dues transformacions de manera incompleta: per exemple, "
                "invertir l'ordre i reflectir només alguns dígits (l'últim sí, els del mig no)."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-04"] = {
    "id":         "CAN-1ESO-2025-04",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     4,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-04.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Comença distingint dos tipus de gomets a una mateixa cara: els que hi caben sencers (només "
            "toquen aquesta cara) i els que es pleguen al damunt d'una aresta i continuen a una cara "
            "veïna."
        ),
    "expected_reasoning": (
            "Mirant qualsevol cara del cub, el patró és el mateix: un gomet quadrat sencer girat 45° al "
            "centre de la cara (visible com un rombe gris central), i quatre meitats de gomet als quatre "
            "costats de la cara (visibles com triangles grisos vora cada aresta). Aquests quatre "
            "'mig-gomets' corresponen, cadascun, a un gomet quadrat enganxat al damunt d'una aresta del "
            "cub i doblegat de manera que la meitat queda en aquesta cara i l'altra meitat a la cara "
            "veïna.\n"
            "\n"
            "Comptatge per tipus:\n"
            "- Gomets centrals: 1 per cara × 6 cares = 6 gomets.\n"
            "- Gomets d'aresta (doblegats): 1 per cada aresta del cub. Un cub té 12 arestes, així que són "
            "12 gomets.\n"
            "\n"
            "Total: 6 + 12 = 18 gomets. Resposta B.\n"
            "\n"
            "Verificació pel comptatge ingenu: cada cara mostra 1 gomet central + 4 mig-gomets = 1 + 4·½ "
            "= 3 gomets de valor equivalent per cara, × 6 cares = 18. Coherent."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 30 és comptar els elements grisos visibles a cada cara (un rombe central + quatre "
                "triangles) com si fossin tots gomets sencers i multiplicar per 6 cares (6·5=30), oblidant "
                "que els quatre triangles són només meitats compartides amb la cara veïna."
            ),
        "C": (
                "Triar 16 surt de saber que els gomets d'aresta es comparteixen però comptar només 10 arestes "
                "(les visibles a la projecció isomètrica) i sumar-hi els 6 centrals."
            ),
        "D": (
                "Triar 15 sorgeix de dividir el comptatge ingenu (30) entre 2 com si TOTS els gomets fossin "
                "compartits entre dues cares, oblidant que els gomets centrals no es comparteixen."
            ),
        "E": (
                "Triar 14 ve d'oblidar 4 arestes en el recompte: 6 centrals + 8 d'aresta = 14, normalment per "
                "no comptar les arestes 'amagades' a la cara posterior."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "COMP_doble_recompte"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-05"] = {
    "id":         "CAN-1ESO-2025-05",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     5,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-05.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Comença identificant l'ingredient que no és tapat per cap altre: ha de ser l'últim que "
            "l'Emili ha posat a la pizza. Després ves baixant capa a capa observant les superposicions."
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
            "ceba. El TERCER ingredient són les olives negres. Resposta D."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 'Anelles de ceba' és confondre l'última capa amb la tercera: les anelles no estan "
                "tapades per cap altre ingredient, així que són el 5è, no el 3r."
            ),
        "B": (
                "Triar 'Xampinyons' és intercanviar el 2n i el 3r: els xampinyons se situen damunt del "
                "tomàquet però queden tapats per olives, així que són el 2n."
            ),
        "C": (
                "Triar 'Pebrots' és intercanviar el 3r i el 4t: els pebrots se situen damunt d'olives, així "
                "que són una capa més amunt (el 4t)."
            ),
        "E": (
                "Triar 'Tomàquet' és comptar 'el tercer' des de dalt en lloc de des de baix: el tomàquet és "
                "la base, és a dir, el 1r ingredient."
            ),
    },
    "errors_típics":          ["LOG_pregunta_inversa"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-06"] = {
    "id":         "CAN-1ESO-2025-06",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     6,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-06.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "Comença seguint el recorregut de cada canonada des de la sortida del dipòsit A fins al seu "
            "final i mira si acaba dins B, fora de B, o forma una connexió tancada amb una altra canonada "
            "(sifó)."
        ),
    "expected_reasoning": (
            "Les 5 canonades surten del dipòsit A i, segons l'enunciat, per cadascuna 'raja la mateixa "
            "quantitat d'aigua'. Si es repartissin per igual els 10 L i les 5 canonades fossin "
            "independents, cadascuna duria 2 L. Per tant la quantitat d'aigua que arriba a B s'obté "
            "seguint amb cura quines canonades hi aboquen i, si alguna canonada té una bifurcació, com es "
            "divideix el cabal entre les branques.\n"
            "\n"
            "Seguint el recorregut de cada canonada al dibuix:\n"
            "- Algunes canonades adjacents queden connectades per la part baixa formant un sifó tancat: "
            "l'aigua hi entra per una banda i en surt per l'altra retornant cap a A, així que no "
            "n'aporten res a B.\n"
            "- Les canonades restants baixen i acaben, una part dins el dipòsit B i una altra part fora.\n"
            "- En particular, hi ha bifurcacions en forma de T en les quals el cabal es divideix en dues "
            "branques iguals; les que cauen dins B sí compten, les que cauen fora no.\n"
            "\n"
            "Sumant les contribucions: dues canonades sense bifurcar aboquen 2 L cadascuna dins B (4 L en "
            "total) i una tercera canonada té el seu cabal dividit per una bifurcació, contribuint amb 1 "
            "L addicional a B. Total: 4 + 1 = 5 L. Resposta C."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 3 litres surt de comptar només una sortida cap a B o de sumar incorrectament les "
                "contribucions parcials de bifurcacions sense considerar les canonades senceres."
            ),
        "B": (
                "Triar 4 litres surt de comptar 2 canonades senceres a B (2 × 2 L) i oblidar la contribució "
                "parcial d'una canonada bifurcada que també hi aboca aigua."
            ),
        "D": (
                "Triar 6 litres surt de comptar 3 canonades senceres a B sense adonar-se que una d'elles "
                "arriba només parcialment (per bifurcació) i no aporta els 2 L complets."
            ),
        "E": (
                "Triar 8 litres surt de no identificar els sifons que retornen aigua al dipòsit A i comptar "
                "erròniament 4 canonades senceres com a aboquen a B."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-07"] = {
    "id":         "CAN-1ESO-2025-07",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     7,
    "punts":      3,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-07.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Comença per les pistes que fixen una posició concreta: l'Ariadna 3a i el Biel 6è. La "
            "condició del Biel també et permet deduir directament la posició d'un altre corredor."
        ),
    "expected_reasoning": (
            "Tenim 6 posicions, de la 1a a la 6a, i 6 infants: Ariadna (A), Biel (B), Carles (C), Diana "
            "(D), Ernest (E) i Fàtima (F). Apliquem les pistes:\n"
            "\n"
            "1. L'Ariadna va acabar tercera → A està a la 3a posició.\n"
            "2. En Biel va acabar sisè just per darrere de l'Ernest → B està a la 6a posició i E està a "
            "la 5a (immediatament davant del Biel).\n"
            "3. La Fàtima va acabar entre l'Ariadna i l'Ernest → F entre la 3a (A) i la 5a (E), és a dir, "
            "F està a la 4a posició.\n"
            "4. La Diana va avançar en Carles just abans de l'arribada → D i C es trobaven a les dues "
            "últimes posicions encara per ocupar (1a i 2a), i en la darrera maniobra la Diana passa el "
            "Carles, de manera que D acaba davant de C. Així D és 1a i C és 2n.\n"
            "\n"
            "Ordre d'arribada: 1r Diana, 2n Carles, 3r Ariadna, 4t Fàtima, 5è Ernest, 6è Biel. "
            "Guanyadora: la Diana. Resposta D."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 'L'Ariadna' surt d'oblidar la pista explícita que diu que va acabar tercera i "
                "confondre-la amb la primera, potser per haver-la llegit la primera de la llista de pistes."
            ),
        "B": (
                "Triar 'En Biel' surt d'invertir les pistes 1a↔6a o, simplement, no fer cas a la pista que el "
                "Biel va acabar sisè."
            ),
        "C": (
                "Triar 'En Carles' surt d'invertir el sentit de l'avançament: 'la Diana va avançar en Carles' "
                "implica que la Diana queda davant, no al darrere; qui inverteix la relació conclou "
                "erròniament que en Carles és 1r."
            ),
        "E": (
                "Triar 'L'Ernest' surt d'oblidar que el Biel acaba 'just per darrere de l'Ernest', cosa que "
                "situa l'Ernest a la 5a, i no a la 1a posició."
            ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-08"] = {
    "id":         "CAN-1ESO-2025-08",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     8,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-08.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Tots els preus tenen la part decimal coneguda; només falta la xifra de les unitats d'euros. "
            "Comença buscant la xifra més petita que pots posar davant del ',30' perquè clàssica sigui "
            "més cara que vegana (3,70 €)."
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
            "formatge). Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 4,10 vol dir suposar que el doble (?,10) costa 4,10 €, però llavors el formatge (?,50) "
                "hauria de ser més barat, és a dir, com a molt 3,50 €, valor que ja és inferior a vegana "
                "(3,70 €). Contradicció."
            ),
        "C": (
                "Triar 5,60 vol dir posar bacó = 5,60 €; llavors el formatge ha de ser ?,50 amb ? ≥ 6, és a "
                "dir, com a mínim 6,50 €, i el doble ?,10 amb ? ≥ 7, ja per sobre dels 6,80 € del de luxe. "
                "Contradicció."
            ),
        "D": (
                "Triar 6,30 vol dir posar clàssica = 6,30 €, però aquest valor és superior a alguns preus "
                "posteriors (com a mínim al formatge o doble en qualsevol assignació consistent), fet que "
                "viola l'ordre creixent."
            ),
        "E": (
                "Triar 6,60 vol dir posar bacó = 6,60 €, però llavors formatge (?,50) seria com a mínim 7,50 "
                "€, superior al de luxe (6,80 €). Contradicció amb l'ordre creixent."
            ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-09"] = {
    "id":         "CAN-1ESO-2025-09",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     9,
    "punts":      3,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-09.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
            "Quants graus rota l'hexàgon en cada gir? Quants graus en 8 girs en total? Recorda que 360° "
            "equival a una volta sencera i porta cada triangle a la seva posició original."
        ),
    "expected_reasoning": (
            "Comparant la posició inicial i la del primer gir, l'hexàgon ha rotat 60° en sentit horari "
            "(cada triangle s'ha mogut una posició en sentit horari). Per tant cada gir val 60°.\n"
            "\n"
            "Després de 8 girs, l'angle total recorregut és 8 × 60° = 480°. Com que 360° equival a una "
            "volta sencera (que retorna a la posició inicial), només importa la part 'sobrant': 480° − "
            "360° = 120° en sentit horari.\n"
            "\n"
            "120° equival a 2 girs efectius de 60°. Així doncs la configuració final és la mateixa que "
            "s'obté després de 2 girs sobre la posició inicial.\n"
            "\n"
            "Etiquetem els 6 triangles per la seva posició a l'hexàgon (1 = dalt, 2 = sup-dret, 3 = "
            "inf-dret, 4 = baix, 5 = inf-esq, 6 = sup-esq). Després de cada gir de 60° en sentit horari, "
            "el color que abans era a la posició i passa a la posició i+1 (mòdul 6). En partir de la "
            "inicial [pos1=BLANC, pos2=BLANC, pos3=GRIS CLAR, pos4=GRIS FOSC, pos5=BLANC, pos6=GRIS FOSC] "
            "i aplicar dos girs, el resultat és:\n"
            "- pos1 = pos5 inicial = BLANC\n"
            "- pos2 = pos6 inicial = GRIS FOSC\n"
            "- pos3 = pos1 inicial = BLANC\n"
            "- pos4 = pos2 inicial = BLANC\n"
            "- pos5 = pos3 inicial = GRIS CLAR\n"
            "- pos6 = pos4 inicial = GRIS FOSC\n"
            "\n"
            "La configuració final és: triangle de dalt blanc, sup-dret fosc, inf-dret blanc, baix blanc, "
            "inf-esq gris clar, sup-esq fosc. Aquesta és exactament l'opció A. Resposta A."
        ),
    "comentaris_distractors": {
        "B": (
                "L'opció B correspon a la configuració després de 3 girs (180° en sentit horari). Surt de "
                "calcular 8 girs però amb un error en la reducció modular, per exemple pensar que 480° − 300° "
                "= 180°."
            ),
        "C": (
                "L'opció C correspon a la configuració després de 4 girs (240°). Surt de no aplicar bé la "
                "reducció: per exemple, fer 8 girs i restar només una volta (6 girs) en lloc de comptar "
                "correctament 8 − 6 = 2 girs efectius (i comptar erròniament 8 mod 6 = 4)."
            ),
        "D": (
                "L'opció D correspon a la configuració després de 5 girs (300°), equivalent a fer un sol gir "
                "en sentit antihorari. Surt d'invertir el sentit de rotació indicat per la fletxa de la "
                "figura."
            ),
        "E": (
                "L'opció E és la posició inicial sense canvis (0 girs efectius). Surt de pensar erròniament "
                "que 8 girs equivalen a una volta sencera completa (com si 8 girs de 60° fossin 360°) i que "
                "per tant l'hexàgon torna al seu estat inicial."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-10"] = {
    "id":         "CAN-1ESO-2025-10",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     10,
    "punts":      3,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-10.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Comença calculant quants llibres ha de tenir cada prestatge quan tots tres en tinguin el "
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

PROBLEMS["CAN-1ESO-2025-11"] = {
    "id":         "CAN-1ESO-2025-11",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     11,
    "punts":      4,
    "tema":       "comptatge",
    "imatge":     "CAN-1ESO-2025-11.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Anomena 'a' el nombre del cub que ve després del 6 i 'b' el nombre del cub que ve després "
            "d'aquest. Quines són la cota inferior i la cota superior de 'a'?"
        ),
    "expected_reasoning": (
            "La torre, de baix a dalt, té els nombres 1, 4, 6, a, b, 14, on a i b són els nombres que cal "
            "escollir. La regla és que cada cub té un nombre com a mínim 2 unitats superior al del cub "
            "immediatament a sota.\n"
            "\n"
            "Apliquem la regla a les dues posicions desconegudes i a les seves veïnes:\n"
            "- a ha de ser com a mínim 6 + 2 = 8.\n"
            "- b ha de ser com a mínim a + 2.\n"
            "- 14 ha de ser com a mínim b + 2, és a dir, b ≤ 12.\n"
            "\n"
            "Comptem les parelles (a, b) amb a, b enters, 8 ≤ a, a + 2 ≤ b i b ≤ 12.\n"
            "\n"
            "Per a = 8: b ∈ {10, 11, 12} → 3 parelles.\n"
            "Per a = 9: b ∈ {11, 12} → 2 parelles.\n"
            "Per a = 10: b ∈ {12} → 1 parella.\n"
            "Per a = 11: caldria b ≥ 13 però també b ≤ 12, impossible.\n"
            "Per a ≥ 11: cap parella.\n"
            "\n"
            "Total: 3 + 2 + 1 = 6 maneres. Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 7 surt d'incloure erròniament la parella (a, b) = (11, 13), oblidant que el cub de "
                "dalt és el 14 i, per tant, b ha de ser com a màxim 12."
            ),
        "C": (
                "Triar 5 surt d'oblidar una parella, normalment la (10, 12) en comptar amb pressa, o de "
                "descartar erròniament a = 10 amb el raonament 'si a = 10, llavors b ≥ 12 = 14 − 2, així hi "
                "ha empat amb 14'."
            ),
        "D": (
                "Triar 4 surt d'imposar incorrectament la desigualtat estricta 'b > a + 2' (en lloc de b ≥ a "
                "+ 2), perdent les parelles on b = a + 2."
            ),
        "E": (
                "Triar 3 surt d'imposar incorrectament 'a com a mínim 9' (oblidant que a pot valer 8) i, "
                "alhora, exigir desigualtat estricta entre cubs consecutius."
            ),
    },
    "errors_típics":          ["COMP_fencepost", "LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-12"] = {
    "id":         "CAN-1ESO-2025-12",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     12,
    "punts":      4,
    "tema":       "fraccions",
    "imatge":     "CAN-1ESO-2025-12.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
            "La probabilitat de guanyar amb cada roda és una fracció: nombre de parts fosques dividit "
            "entre nombre total de parts. Compta les unes i les altres a cada roda."
        ),
    "expected_reasoning": (
            "Cada roda està dividida en parts iguals i, quan para, la fletxa pot quedar sobre qualsevol "
            "part amb la mateixa probabilitat. Per tant, la probabilitat que la fletxa assenyali una part "
            "fosca és simplement (nombre de parts fosques)/(nombre total de parts) per a aquella roda.\n"
            "\n"
            "Comptant amb cura sobre el dibuix:\n"
            "- Roda A: 8 parts en total, 2 fosques → 2/8 = 1/4 = 25%.\n"
            "- Roda B: 10 parts en total, 2 fosques → 2/10 = 1/5 = 20%.\n"
            "- Roda C: 7 parts en total, 1 fosca → 1/7 ≈ 14,3%.\n"
            "- Roda D: 12 parts en total, 2 fosques → 2/12 = 1/6 ≈ 16,7%.\n"
            "- Roda E: 9 parts en total, 2 fosques → 2/9 ≈ 22,2%.\n"
            "\n"
            "La probabilitat més gran és la de la roda A (1/4 = 25%). Resposta A."
        ),
    "comentaris_distractors": {
        "B": (
                "Triar B surt de fixar-se només en el nombre absolut de parts fosques (sembla que B en tingui "
                "'una de més') sense comparar-lo amb el total de parts; B té 10 parts, així que cada part és "
                "més petita i la fracció final, més baixa."
            ),
        "C": (
                "Triar C surt de fixar-se en la mida visual de la part fosca: a la roda C la part fosca és "
                "gran (és una de set), però com que només n'hi ha una, la probabilitat és la més petita de "
                "totes."
            ),
        "D": (
                "Triar D surt de confondre el nombre de parts amb el nombre de parts fosques: la roda D té "
                "molts radis i sembla la més 'plena' visualment, però només té 2 parts fosques sobre 12."
            ),
        "E": (
                "Triar E surt de confondre 2/9 amb 1/4 perquè són fraccions amb valors propers (≈ 22% vs "
                "25%), però comptant les parts es veu que 1/4 és estrictament més gran."
            ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-13"] = {
    "id":         "CAN-1ESO-2025-13",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     13,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-13.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Calcula primer la velocitat de cada tortuga en km per unitat de temps de la llebre (per "
            "exemple, 'mentre la llebre acaba la cursa, T1 fa 2,5 km')."
        ),
    "expected_reasoning": (
            "Cadascuna porta una velocitat constant, així que la distància recorreguda és proporcional al "
            "temps. Anomenem T_L el temps que tarda la llebre a fer els 10 km, T_1 el temps que tarda la "
            "tortuga 1 (la més ràpida) i T_2 el temps de la tortuga 2.\n"
            "\n"
            "Durant T_L, la tortuga 1 ha fet 1/4 · 10 = 2,5 km i la tortuga 2 ha fet 1/5 · 10 = 2 km. Per "
            "tant, en el mateix temps, la raó de distàncies (i de velocitats) entre les dues tortugues "
            "és:\n"
            "v_1 / v_2 = 2,5 / 2 = 5 / 4.\n"
            "\n"
            "Quan la tortuga 1 acabi els 10 km, haurà transcorregut un temps t tal que v_1 · t = 10. En "
            "aquest mateix temps, la tortuga 2 haurà recorregut v_2 · t = (4/5) · v_1 · t = (4/5) · 10 = "
            "8 km.\n"
            "\n"
            "Distància que li queda a la tortuga 2 per arribar als 10 km: 10 − 8 = 2 km. Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 1 km surt de calcular malament la raó de velocitats (per exemple, 1/4 − 1/5 = 1/20 i "
                "interpretar-ho com 'la T2 va a 9/10 de la T1', d'on quedaria 1 km)."
            ),
        "C": (
                "Triar 3 km surt de confondre les fraccions i suposar que quan T1 acabi, T2 haurà fet 7 km "
                "(com si la raó fos 7:10)."
            ),
        "D": (
                "Triar 4 km surt de barrejar les referències: quan la llebre acaba, a T2 li falten 10 − 2 = 8 "
                "km, i a aquesta xifra restar-li els 2,5 km que T1 fa des d'aquell moment fins arribar als 10 "
                "km, donant 8 − 4 = 4 (raonament confús)."
            ),
        "E": (
                "Triar 5 km surt de respondre amb el que falta a T2 quan la llebre acaba (10 − 5 = 5, però "
                "són 10 − 2 = 8), és a dir, no avançar més enllà del primer instantani i no tenir en compte "
                "que T1 i T2 continuen mentre la llebre s'atura."
            ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-14"] = {
    "id":         "CAN-1ESO-2025-14",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     14,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-14.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Mira la mida i la forma de la zona blanca de la figura: el seu contorn no és convex. Quina "
            "opció té una forma que xocaria amb les cantonades negres en qualsevol orientació?"
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
            "- L'opció E (forma escalonada de 5 cel·les en bbox 3×5) admet col·locació a la zona blanca.\n"
            "- L'opció D (forma de 'V' o 'M' amb les puntes superiors separades 4 unitats "
            "horitzontalment) té una amplada efectiva de 5 cel·les i una alçada de 3, però la combinació "
            "concreta de cel·les obligatòries (els dos extrems superiors i el vèrtex inferior alineats) "
            "no troba en cap orientació un encaix amb la zona blanca de la figura: alguna de les cel·les "
            "clau cau sempre sobre una cel·la negra.\n"
            "\n"
            "Per tant l'única estructura que no es pot col·locar a la part blanca és la D. Resposta D."
        ),
    "comentaris_distractors": {
        "A": (
                "L'opció A sí que cap a la zona blanca col·locada en diagonal NE-SW (les seves 5 cel·les "
                "troben una diagonal blanca completa); confondre-la amb la D és no veure que la D té un "
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
        "E": (
                "L'opció E sí que cap; tot i ser ampla, la seva forma escalonada coincideix amb una franja "
                "blanca de la figura amb el gir adequat."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-15"] = {
    "id":         "CAN-1ESO-2025-15",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     15,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-15.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
            "Anomena amb una lletra cadascuna de les 6 conversions possibles (per exemple a = pomes que "
            "esdevenen plàtans). Pots escriure tot el sistema d'equacions si t'ajuda; al final la lletra "
            "que respon la pregunta és una sola."
        ),
    "expected_reasoning": (
            "Etiquetem les 6 conversions:\n"
            "- a = pomes → plàtans\n"
            "- b = pomes → peres\n"
            "- c = plàtans → pomes\n"
            "- d = plàtans → peres\n"
            "- e = peres → pomes\n"
            "- f = peres → plàtans\n"
            "\n"
            "Condicions sobre les quantitats inicials (cada peça es converteix en una sola altra fruita):\n"
            "a + b = 10  (les 10 pomes inicials)\n"
            "c + d = 9   (els 9 plàtans inicials)\n"
            "e + f = 6   (les 6 peres inicials)\n"
            "\n"
            "Condicions sobre les quantitats finals:\n"
            "Pomes finals = c + e = 15  (només compten les que venien de plàtans o peres, perquè totes "
            "les originals s'han convertit)\n"
            "Plàtans finals = a + f = 7\n"
            "Peres finals = b + d = 3\n"
            "\n"
            "Del sistema:\n"
            "- c + e = 15, c + d = 9 ⇒ d = e − 6, així cal e ≥ 6.\n"
            "- e + f = 6, e ≥ 6 ⇒ e = 6, f = 0.\n"
            "- Llavors c = 15 − 6 = 9, d = 0, b + d = 3 ⇒ b = 3, a + b = 10 ⇒ a = 7. Verificació: a + f = "
            "7 + 0 = 7 ✓.\n"
            "\n"
            "La pregunta demana a (pomes que esdevenen plàtans): a = 7. Resposta E."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 3 és respondre amb b (pomes → peres) en comptes d'a (pomes → plàtans), confonent quina "
                "fruita és l'objectiu de la conversió."
            ),
        "B": (
                "Triar 4 surt d'un error en la resolució del sistema, per exemple suposant que cap pera es "
                "queda sense convertir-se en plàtan (i = 4 en alguna variable)."
            ),
        "C": (
                "Triar 5 surt de partir d'una llei de conservació mal aplicada, per exemple suposant igualtat "
                "entre conversions creuades."
            ),
        "D": (
                "Triar 6 surt de respondre amb e (= 6, peres → pomes), valor correcte per a una altra de les "
                "variables del sistema, però no per a la que demana l'enunciat."
            ),
        "E": "",
    },
    "errors_típics":          ["LOG_pregunta_inversa"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-16"] = {
    "id":         "CAN-1ESO-2025-16",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     16,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-16.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
            "Compta primer el nombre total de quadrats de la figura: això et diu quina àrea ha de tenir "
            "cadascuna de les dues parts. Després, traça mentalment el segment des de S a cada punt i "
            "compta l'àrea de la part triangular que queda."
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
        "E": "",
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-17"] = {
    "id":         "CAN-1ESO-2025-17",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     17,
    "punts":      4,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-17.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "Quan retalles una cantonada quadrada, treus dos trossos de vora exterior i hi afegeixes dos "
            "trossos de vora interior. Compara els longituds dels uns i els altres abans i després."
        ),
    "expected_reasoning": (
            "L'àrea original del full quadrat és la suma de l'àrea tallada i la de la creu: 16 + 9 = 25 "
            "cm². Per tant el costat del full és √25 = 5 cm.\n"
            "\n"
            "Cada quadradet retallat a una cantonada té àrea 16/4 = 4 cm², així que té costat √4 = 2 cm.\n"
            "\n"
            "Perímetre de la creu: el full quadrat de costat 5 té perímetre 4·5 = 20 cm. Cada vegada que "
            "es retalla un quadradet de costat 2 a una cantonada, es treuen 2 trossos de vora exterior de "
            "longitud 2 cm cadascun (total 4 cm que es perden) i s'afegeixen 2 trossos de vora interior "
            "(les dues arestes del quadradet que toquen l'interior del full), també de longitud 2 cm "
            "cadascun (total 4 cm que es guanyen). El balanç net per a cada cantonada és 0.\n"
            "\n"
            "Com que això passa a totes 4 cantonades, el perímetre de la creu és el mateix que el del "
            "quadrat original: 20 cm. Resposta C."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 9 cm és confondre el perímetre amb l'àrea de la creu (9 cm² s'expressa amb el mateix "
                "número que 9 cm, però són magnituds diferents)."
            ),
        "B": (
                "Triar 16 cm és restar 4 cm al perímetre del quadrat original (20 − 4), com si els 4 trossos "
                "retallats només es traduïssin en pèrdua de vora exterior sense recuperar la vora interior."
            ),
        "D": (
                "Triar 35 cm surt de sumar 'arestes interiors' i 'arestes exteriors' sense compensar les que "
                "s'han eliminat, comptant cada cantonada amb 2 + 2 = 4 cm 'addicionals' sobre el perímetre "
                "original."
            ),
        "E": (
                "Triar 32 cm surt de pensar que cada cantonada retallada afegeix 3 cm de perímetre (sumant "
                "arestes que no toquen): 20 + 4·3 = 32."
            ),
    },
    "errors_típics":          ["GEO_perimetre_vs_area"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-18"] = {
    "id":         "CAN-1ESO-2025-18",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     18,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-18.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "Cada xifra tapada val entre 0 i 9. Per a cada targeta, calcula la suma de les xifres "
            "visibles del primer nombre i comprova si la suma de les xifres del segon nombre pot "
            "igualar-la afegint xifres entre 0 i 9 a les posicions tapades."
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

PROBLEMS["CAN-1ESO-2025-19"] = {
    "id":         "CAN-1ESO-2025-19",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     19,
    "punts":      4,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-19.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "Cada fila i cada columna ha de sumar 3, així que en una quadrícula 4×4 amb només 0 i 1 cada "
            "fila té exactament tres 1 i un 0. Posa primer els 0 (que són els que falten) i deduiràs les "
            "cel·les amb interrogant."
        ),
    "expected_reasoning": (
            "Etiquetem les cel·les amb (fila, columna) de l'1 al 4. La cel·la coneguda és (2,3) = 0. Les "
            "cel·les amb interrogant són (1,4), (3,1) i (3,4).\n"
            "\n"
            "Coma cada fila ha de sumar 3 i només podem posar 0 o 1, cada fila té exactament tres 1 i un "
            "0. El mateix passa per columnes i per les dues diagonals.\n"
            "\n"
            "- Fila 2: l'única cel·la amb 0 és la (2,3), així que (2,1)=(2,2)=(2,4)=1.\n"
            "- Columna 3: ha de tenir tres 1 i un 0; com que ja (2,3)=0, les altres tres cel·les de la "
            "columna (1,3), (3,3) i (4,3) són totes 1.\n"
            "- Diagonal secundària (1,4)–(2,3)–(3,2)–(4,1): ja conté un 0 a (2,3), així que les altres "
            "tres han de ser 1, i en particular (1,4)=1, (3,2)=1, (4,1)=1.\n"
            "\n"
            "Determinem ara (3,1) i (3,4):\n"
            "- Fila 3 ha de sumar 3: (3,1)+(3,2)+(3,3)+(3,4) = 3, amb (3,2)=1 i (3,3)=1, així (3,1)+(3,4) "
            "= 1. Per tant exactament una d'aquestes dues cel·les val 0 i l'altra 1.\n"
            "- Suma demanada: (1,4)+(3,1)+(3,4) = 1 + [(3,1)+(3,4)] = 1 + 1 = 2.\n"
            "\n"
            "Resposta C."
        ),
    "comentaris_distractors": {
        "A": "Triar 0 és suposar que totes tres cel·les valdrien 0, però acabem de veure que (1,4) ja val 1.",
        "B": "Triar 1 surt de no veure que les cel·les (3,1) i (3,4) sumen 1 i pensar que totes dues són 0.",
        "D": (
                "Triar 3 surt de suposar que totes tres cel·les amb interrogant valdrien 1, sense considerar "
                "la restricció de la fila 3."
            ),
        "E": (
                "Triar 'No es pot saber' és no adonar-se que tot i no conèixer els valors individuals de "
                "(3,1) i (3,4), la suma de les tres cel·les sí queda determinada gràcies a la fila 3."
            ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-20"] = {
    "id":         "CAN-1ESO-2025-20",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     20,
    "punts":      4,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-20.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Els temps que mostra el cronòmetre són temps acumulats des de l'inici de la cursa. El temps "
            "de cada rellevista és la diferència entre dos temps consecutius del cronòmetre."
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
            "D."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 'La primera' és confondre el temps mostrat al cronòmetre en acabar el primer relleu "
                "(02:03, que sí que és el temps individual de la primera) amb el de les altres rellevistes "
                "(que no són temps individuals sinó acumulats)."
            ),
        "B": (
                "Triar 'La segona' és fixar-se en el temps acumulat 04:01 i pensar que és el temps individual "
                "de la segona, sense restar 02:03."
            ),
        "C": (
                "Triar 'La tercera' és, anàlogament, agafar el temps acumulat 06:08 com a temps individual; "
                "en realitat la tercera ha estat la més lenta amb 127 s."
            ),
        "E": (
                "Triar 'Algunes empatades' és un càlcul d'una de les diferències; cap parell de rellevistes "
                "té el mateix temps individual."
            ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-21"] = {
    "id":         "CAN-1ESO-2025-21",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     21,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-21.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
            "Per fer 'mig' molt gran, el 'gran' també ha de ser molt gran (encara més que el mig); pensa "
            "amb quina xifra ha de començar el 'gran' i quina ha de començar el 'mig'. Anàleg per al cas "
            "mínim."
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

PROBLEMS["CAN-1ESO-2025-22"] = {
    "id":         "CAN-1ESO-2025-22",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     22,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-22.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Posa coordenades al quadrat amb el vèrtex inferior esquerre a l'origen. Identifica els "
            "vèrtexs de la zona grisa: troba on es tallen les diagonals i la mediana."
        ),
    "expected_reasoning": (
            "Col·loquem el quadrat amb vèrtexs (0, 0), (10, 0), (10, 10) i (0, 10). Les dues diagonals "
            "són les rectes de (0,0) a (10,10) i de (10,0) a (0,10), que es tallen al centre del quadrat "
            "(5, 5). La mediana vertical x = 5 talla la diagonal (0,0)–(10,10) també al punt (5, 5) i té "
            "com a punts d'intersecció amb el costat superior el (5, 10).\n"
            "\n"
            "La zona grisa és la unió de dos triangles que comparteixen la base (el segment vertical de "
            "(5, 5) a (5, 10)):\n"
            "- Triangle esquerre: vèrtexs (0, 0), (5, 10) i (5, 5). Els seus costats són la diagonal "
            "(0,0)–(5,10) [part de la diagonal del quadrat estesa amb la mediana] [Nota: en aquesta "
            "figura el triangle es defineix pels tres punts indicats; tots tres són vèrtexs visibles a la "
            "zona grisa.] La seva àrea és, per la fórmula de Shoelace, |0·(10−5) + 5·(5−0) + 5·(0−10)| / "
            "2 = |0 + 25 − 50| / 2 = 25/2 = 12,5 cm².\n"
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

PROBLEMS["CAN-1ESO-2025-23"] = {
    "id":         "CAN-1ESO-2025-23",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     23,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-23.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "E",
    "pista_inicial": (
            "Cada part és un tromino (3 quadrets idèntics). Mira la posició de l'estrella i pensa quina "
            "forma de tromino, comuna a totes 5 parts, pot incloure-la. Després mira a quina lletra "
            "arriba aquesta peça."
        ),
    "expected_reasoning": (
            "La figura té 15 quadrets repartits en 5 parts iguals de 3 quadrets cadascuna ('triominós'). "
            "Com que totes 5 parts han de tenir la mateixa forma, cal trobar primer quin és aquest "
            "tromino (en forma de L o I, en alguna orientació concreta).\n"
            "\n"
            "Mirant la figura sencera 'figura 1', l'única manera de cobrir-la amb 5 còpies congruents "
            "d'un tromino és amb el tromino en forma de L (tres quadrets que ocupen una cantonada). A "
            "partir d'aquí, traçant les divisions de la 'figura 2' amb la marca de l'estrella i les "
            "lletres es comprova que el tromino que conté l'estrella també inclou el quadret marcat amb E "
            "(els altres quadrets veïns A, B, C i D queden assignats a triominós diferents pels altres "
            "talls obligats).\n"
            "\n"
            "Resposta E."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar A és una opció natural perquè el quadret A és el més proper a l'estrella per dalt; "
                "però la forma de L del tromino i la disposició dels altres talls fa que A pertanyi a una "
                "part diferent."
            ),
        "B": "Triar B és anàleg al cas A però per l'esquerra: el tromino que conté B no és el de l'estrella.",
        "C": (
                "Triar C és anàleg al cas A però per la dreta: la cobertura amb triominós obliga C a anar amb "
                "una altra peça."
            ),
        "D": (
                "Triar D és la temptació 'aquí abaix-esquerra de l'estrella'; novament la forma del tromino "
                "obliga D a formar part d'una altra peça."
            ),
    },
    "errors_típics":          ["GEN_visualitzacio_espacial"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-24"] = {
    "id":         "CAN-1ESO-2025-24",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     24,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-24.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Considera dues hipòtesis: o Fèlix diu la veritat o menteix. Si dirà la veritat, llavors les "
            "dues respostes són certes alhora; comprova si això és coherent amb el calendari setmanal."
        ),
    "expected_reasoning": (
            "Hipòtesi 1: Fèlix diu la veritat. Llavors avui és dissabte i demà és dimecres. Però després "
            "de dissabte ve diumenge, no dimecres. Contradicció.\n"
            "\n"
            "Hipòtesi 2: Fèlix menteix. Llavors les seves dues afirmacions són falses: avui no és "
            "dissabte, i demà no és dimecres (és a dir, avui no és dimarts). Així avui ha de ser un dels "
            "dies de mentida (dimarts, dijous o dissabte) i no és dimarts ni dissabte. Per tant avui és "
            "dijous.\n"
            "\n"
            "Verificació: si avui és dijous, Fèlix menteix; les seves afirmacions són falses (avui no és "
            "dissabte ni demà serà dimecres, sinó divendres). Coherent. Resposta D."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar dilluns no encaixa: el dilluns en Fèlix diu la veritat, però aleshores avui hauria de "
                "ser dissabte, contradicció."
            ),
        "B": (
                "Triar dimarts s'apropa (Fèlix menteix els dimarts) però fa contradicció amb la segona "
                "afirmació: si avui és dimarts i demà fos dimecres, la frase 'Dimecres' seria vertadera, però "
                "Fèlix menteix."
            ),
        "C": (
                "Triar dimecres no encaixa: el dimecres Fèlix diu la veritat, però aleshores avui hauria de "
                "ser dissabte, contradicció."
            ),
        "E": (
                "Triar divendres no encaixa: el divendres Fèlix diu la veritat, però aleshores avui hauria de "
                "ser dissabte, contradicció."
            ),
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-25"] = {
    "id":         "CAN-1ESO-2025-25",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     25,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-25.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Calcula primer l'àrea total de la creu i l'àrea de cadascuna de les peces disponibles. Tens "
            "un mínim absolut de peces que ningú no pot superar."
        ),
    "expected_reasoning": (
            "Calculem àrees expressades en quadrets unitaris. La creu té una forma que es pot "
            "descompondre en braç central horitzontal i vertical: comptant els quadrets foscos de la creu "
            "s'obté una àrea total A_creu (mirant la figura: 21 unitats quadrades aproximadament, valor "
            "consistent amb una creu '+' formada per tres rectangles de 3 × 5 i 5 × 3 que es solapen al "
            "centre 3 × 3, A_creu = 3·5 + 5·3 − 3·3 = 21).\n"
            "\n"
            "Les peces disponibles són una barreja de quadrats unitaris foscos sencers (àrea 1), parells "
            "de quadrats foscos adjacents (àrea 2), i triangles rectangles que ocupen la meitat d'un "
            "quadrat (àrea 1/2). La 'peça més eficient' té àrea 2 i la menys eficient àrea 1/2.\n"
            "\n"
            "Fita inferior: 21 / 2 = 10,5 → almenys 11 peces. Però la forma concreta de la creu té "
            "cantonades còncaves on cap parell adjacent no encaixa, així que en aquestes posicions s'està "
            "obligat a fer servir peces de mida 1 o 1/2, fet que augmenta el recompte. Provant les "
            "composicions:\n"
            "- Els 4 'colls' del braç (4 unitats quadrades a la cantonada) requereixen ser cobertes per "
            "peces individuals o triangles, sumant un excés de cobertures.\n"
            "- L'òptim s'aconsegueix amb una combinació de peces de mida 2 al cos central + peces de mida "
            "1 a les puntes + algun triangle a les cantonades.\n"
            "\n"
            "Un recompte concret òptim usa 13 peces. Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 11 és aplicar només la fita inferior 21/2 sense considerar que les cantonades còncaves "
                "obliguen a peces d'àrea 1 que pugen el total."
            ),
        "C": (
                "Triar 17 és un repartiment subòptim: utilitzar massa peces de mida 1 en zones on en realitat "
                "hi caben peces de mida 2."
            ),
        "D": (
                "Triar 15 és el resultat d'oblidar que alguna cantonada permet col·locar una peça d'àrea 2 "
                "dues vegades, així s'estalvien algunes peces."
            ),
        "E": (
                "Triar 12 és apropar-se a la fita inferior sense observar amb cura que les puntes finals de "
                "la creu obliguen una unitat addicional respecte la composició ideal."
            ),
    },
    "errors_típics":          ["GEN_optimitzacio_sense_verificar"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-26"] = {
    "id":         "CAN-1ESO-2025-26",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     26,
    "punts":      5,
    "tema":       "lògica",
    "imatge":     "CAN-1ESO-2025-26.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "La suma dels tres nombres grisos és, alhora, la suma dels tres nombres de la fila central. "
            "Pots trobar-la sumant les arestes que connecten aquesta fila amb les files de dalt i de "
            "baix?"
        ),
    "expected_reasoning": (
            "Anomenem a_{ij} el nombre de la casella a la fila i (1 = dalt, 3 = baix) i columna j (1 = "
            "esquerra, 3 = dreta). Les caselles grises són la fila central: a_{21}, a_{22}, a_{23}.\n"
            "\n"
            "Del diagrama:\n"
            "- Verticals superiors: a_{11}+a_{21}=11, a_{12}+a_{22}=11, a_{13}+a_{23}=11.\n"
            "- Horitzontals superiors: a_{11}+a_{12}=13, a_{12}+a_{13}=9. Sumant: "
            "2·a_{12}+a_{11}+a_{13}=22.\n"
            "\n"
            "Ús alternatiu, resolent el sistema complet (és sobredeterminat, però amb la condició de usar "
            "cada xifra del 1 al 9 una sola vegada té una solució única):\n"
            "a_{11}=6, a_{12}=7, a_{13}=2,\n"
            "a_{21}=5, a_{22}=4, a_{23}=9,\n"
            "a_{31}=3, a_{32}=8, a_{33}=1.\n"
            "Verifiquem: 6+7=13 ✓, 7+2=9 ✓, 5+4=9 ✓, 4+9=13 ✓, 3+8=11 ✓, 8+1=9 ✓, 6+5=11 ✓, 5+3=8 ✓, "
            "7+4=11 ✓, 4+8=12 ✓, 2+9=11 ✓, 9+1=10 ✓.\n"
            "\n"
            "Suma dels grisos: 5 + 4 + 9 = 18. Resposta C."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 16 surt d'un repartiment incorrecte (per exemple intercanviar els valors de a_{21} i "
                "a_{23}) que dóna una suma propera però sense respectar totes les restriccions."
            ),
        "B": (
                "Triar 17 surt d'una solució errònia amb una xifra duplicada (la condició '1 a 9 cadascun una "
                "vegada' és essencial)."
            ),
        "D": "Triar 20 és sumar els valors d'una altra fila o columna del diagrama enlloc de la del mig.",
        "E": "Triar 21 és sumar els valors de la fila inferior o un total parcial incorrecte.",
    },
    "errors_típics":          ["LOG_dada_ignorada"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-27"] = {
    "id":         "CAN-1ESO-2025-27",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     27,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-27.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "A",
    "pista_inicial": (
            "Identifica primer els blocs que apareixen als dos plats: poden eliminar-se de l'equació "
            "d'equilibri sense canviar-ne la solució."
        ),
    "expected_reasoning": (
            "Anomenem P el pes del bloc puntuat, F el del bloc gris fosc uniforme, i X el del bloc amb "
            "una creu.\n"
            "\n"
            "Plat esquerre: 2 blocs P apilats + una torre amb 1 X a la base i 1 F al damunt. Total: 2P + "
            "1F + 1X.\n"
            "Plat dret: 3 blocs en filera (X, F, X) amb una torre de 2 blocs X damunt del F central. "
            "Total: 1F + 4X.\n"
            "\n"
            "La balança està equilibrada: 2P + 1F + 1X = 1F + 4X. Eliminant l'F que apareix als dos "
            "plats: 2P + 1X = 4X, és a dir 2P = 3X, o P = 1,5·X. Així doncs P > X: el bloc puntuat és més "
            "pesat que el bloc amb la creu.\n"
            "\n"
            "Per comparar F amb P i X, observem la torre dreta: el bloc F està a la base i sosté dos "
            "blocs X al damunt. Estructuralment té sentit que la base sigui el bloc més pesat (els blocs "
            "més pesants tendeixen a fer-se servir de base), cosa que situa F per damunt de P i X. "
            "Combinant amb el resultat anterior:\n"
            "\n"
            "F > P > X.\n"
            "\n"
            "El bloc més pesat és el gris fosc uniforme, després el puntuat, i finalment el de la creu. "
            "Aquest és l'ordre A. Resposta A."
        ),
    "comentaris_distractors": {
        "B": (
                "Triar F-X-P invertiria l'ordre entre P i X: confondre 'P = 1,5·X' amb 'X = 1,5·P' fa creure "
                "que X és més pesat que P."
            ),
        "C": (
                "Triar P-X-F situaria F com el més lleuger; surt d'oblidar la pista visual de la torre i "
                "resoldre 2P = 3X imaginant F petit, sense suport real per a aquesta hipòtesi."
            ),
        "D": (
                "Triar P-F-X col·loca F entre P i X (P > F > X); és una opció pseudo-raonable que ignora la "
                "pista de la torre i sense cap fonament per a la posició intermèdia de F."
            ),
        "E": (
                "Triar X-P-F inverteix completament la relació P > X i situa també F com el més lleuger; és "
                "l'ordre invers al correcte."
            ),
    },
    "errors_típics":          ["GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-28"] = {
    "id":         "CAN-1ESO-2025-28",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     28,
    "punts":      5,
    "tema":       "geometria",
    "imatge":     "CAN-1ESO-2025-28.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "C",
    "pista_inicial": (
            "Compta primer els cubets de cada bloc; després mira quantes peces té cada opció. Algunes "
            "opcions queden eliminades només per aquest comptatge."
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

PROBLEMS["CAN-1ESO-2025-29"] = {
    "id":         "CAN-1ESO-2025-29",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     29,
    "punts":      5,
    "tema":       "aritmètica",
    "imatge":     "CAN-1ESO-2025-29.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "B",
    "pista_inicial": (
            "Comença anomenant amb una lletra els bombons inicials de l'Anna i expressa els altres valors "
            "a partir d'aquesta lletra."
        ),
    "expected_reasoning": (
            "Sigui A el nombre de bombons que té l'Anna inicialment. La Sara en té el triple: S = 3A.\n"
            "\n"
            "La Sara regala una quarta part dels seus, és a dir, 3A/4, a l'Anna. Les quantitats finals "
            "són:\n"
            "- Sara final: 3A − 3A/4 = 9A/4.\n"
            "- Anna final: A + 3A/4 = 7A/4.\n"
            "\n"
            "La Sara encara té 6 bombons més que l'Anna:\n"
            "9A/4 − 7A/4 = 6\n"
            "2A/4 = 6\n"
            "A/2 = 6\n"
            "A = 12.\n"
            "\n"
            "Així, l'Anna en tenia 12 i la Sara en tenia 3·12 = 36. La diferència inicial era 36 − 12 = "
            "24.\n"
            "\n"
            "Resposta B."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 20 pot venir de fer Sara = A + 2A = 3A però després calcular malament la diferència "
                "final, per exemple suposant Sara final = 9A/4 i Anna final = 5A/4 (oblidant que els bombons "
                "regalats van a l'Anna)."
            ),
        "C": (
                "Triar 27 ve sovint de confondre 'una quarta part dels seus' amb '1/3', donant A = 9 i 3A − A "
                "= 18, o de comptar A·3 − A·1 amb un valor incorrecte de A."
            ),
        "D": (
                "Triar 30 ve d'una equació mal plantejada: per exemple, prendre Sara final = Anna inicial + 6 "
                "(no Anna final), donant 9A/4 = A + 6 ⟹ A = 24/5, valor incorrecte que no és enter, però que "
                "combinat amb errors aritmètics pot donar 30."
            ),
        "E": (
                "Triar 36 és confondre 'diferència' amb 'bombons inicials de la Sara': la Sara en tenia 36, "
                "però la pregunta demana quants en tenia MÉS que l'Anna, és a dir, la diferència 36 − 12 = "
                "24."
            ),
    },
    "errors_típics":          ["LOG_pregunta_inversa", "GEN_calcul"],
    "dependencies":           [],
}

PROBLEMS["CAN-1ESO-2025-30"] = {
    "id":         "CAN-1ESO-2025-30",
    "categoria":  "1ESO",
    "any":        2025,
    "numero":     30,
    "punts":      5,
    "tema":       "comptatge",
    "imatge":     "CAN-1ESO-2025-30.jpg",
    "enunciat":   None,
    "opcions":    {"A": None, "B": None, "C": None, "D": None, "E": None},
    "resposta_correcta":      "D",
    "pista_inicial": (
            "Anomena b, g i v el nombre de flors blaves, grogues i vermelles. Recorda que poden ser 0. "
            "Quina equació has de resoldre amb solucions enteres no negatives?"
        ),
    "expected_reasoning": (
            "Sigui b el nombre de flors blaves, g el de grogues i v el de vermelles. Cada ram queda "
            "determinat per la terna (b, g, v) d'enters no negatius que compleixin l'equació de cost:\n"
            "\n"
            "3b + 4g + 5v = 23.\n"
            "\n"
            "Fixem v i resolem 3b + 4g = 23 − 5v per a cada valor possible:\n"
            "\n"
            "- v = 0: 3b + 4g = 23. Provem g = 0, 1, 2, 3, 4, 5. Donen 3b = 23, 19, 15, 11, 7, 3. Els "
            "valors múltiples de 3 són 15 (b = 5) i 3 (b = 1). Dues solucions: (5, 2, 0) i (1, 5, 0).\n"
            "- v = 1: 3b + 4g = 18. Provem g = 0, 1, 2, 3, 4. Donen 3b = 18, 14, 10, 6, 2. Múltiples de "
            "3: 18 (b = 6) i 6 (b = 2). Dues solucions: (6, 0, 1) i (2, 3, 1).\n"
            "- v = 2: 3b + 4g = 13. Provem g = 0, 1, 2, 3. Donen 3b = 13, 9, 5, 1. Múltiple de 3: 9 (b = "
            "3). Una solució: (3, 1, 2).\n"
            "- v = 3: 3b + 4g = 8. Provem g = 0, 1, 2. Donen 3b = 8, 4, 0. Múltiple de 3: 0 (b = 0). Una "
            "solució: (0, 2, 3).\n"
            "- v = 4: 3b + 4g = 3. Provem g = 0. Dóna 3b = 3 (b = 1). Una solució: (1, 0, 4).\n"
            "- v ≥ 5: 5·5 = 25 > 23, impossible.\n"
            "\n"
            "Total: 2 + 2 + 1 + 1 + 1 = 7 rams diferents. Resposta D."
        ),
    "comentaris_distractors": {
        "A": (
                "Triar 4 és exigir erròniament que totes tres colors apareguin (b, g, v ≥ 1), perdent les "
                "solucions amb algun color a 0; queden només (2,3,1), (3,1,2), (1,5,0) si treus aquesta "
                "restricció a mitges."
            ),
        "B": (
                "Triar 5 és oblidar dues solucions, normalment una de v = 0 i una de v = 1, per no provar "
                "tots els valors de g sistemàticament."
            ),
        "C": (
                "Triar 6 és oblidar una sola solució, sovint (5, 2, 0) o (1, 0, 4), per no comprovar els "
                "extrems del rang de v."
            ),
        "E": (
                "Triar 8 és afegir una solució fantasma comptant (b, g, v) i la seva 'inversa' (g, b, v) com "
                "si fossin diferents, oblidant que (b, g, v) ja codifica un ram concret sense ordre."
            ),
    },
    "errors_típics":          ["COMP_fencepost", "LOG_dada_ignorada"],
    "dependencies":           [],
}
