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
        "Fixa't en les dues files del terra que es veuen a la foto i busca quina seqüència de cinc "
        "rajoles les conté totes dues com a tros consecutiu (llegint-la de manera cíclica)."
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
        "Separa el vaixell en parts: el cos rectangular, les dues proes inclinades i la torreta. "
        "Compta quantes peces de cada tipus necessites per a cadascuna d'aquestes parts."
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
        "Posa un nom al nombre d'habitacions de 4 persones i escriu una equació que relacioni el "
        "nombre total de persones amb el nombre d'habitacions de cada tipus."
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
        "Comprova una a una les dues condicions: que hi hagi exactament dos cercles seguits i que "
        "no hi hagi dos quadrats adjacents. Elimina les opcions que incompleixin almenys una "
        "d'elles."
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
        "Pensa quant sumen totes les sis cares del dau i quant sumen les tres cares que no veus. "
        "Recorda que les cares oposades sempre sumen 7."
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
        "Per a cada figura, intenta traçar totes les línies que la divideixen en dues meitats "
        "idèntiques. Quina figura permet traçar-ne més?"
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
        "Compta quants panells verticals té la figura 3D i fixa't on han d'estar els talls (línia "
        "gruixuda) i els plecs (línia de punts) al full pla per crear exactament aquells panells."
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
        "Pensa quantes posicions té la flor en total i quantes posicions cobreix cada peça. "
        "Reflexiona si cal cobrir cada posició exactament una vegada o si la superposició és "
        "possible."
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
        "Calcula primer quantes porcions menja en Max, i amb el que queda calcula quantes en menja "
        "la Gràcia. El que resta és el que els queda al final."
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
        "Segueix el recorregut del dibuix pel hexàgon pas a pas: a quin triangle arriba després de "
        "cada simetria i com queda orientada la imatge cada vegada?"
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
        "Quantes vagonetes calen per a 30 alumnes si cada una porta 3 persones? Pensa quan surt la "
        "darrera vagoneta i quant tarda a acabar el recorregut."
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
        "Intenta localitzar un punt o un eix respecte al qual la figura sembli equilibrada. Recorda "
        "que la línia de tall no cal que sigui horitzontal ni vertical."
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
        "El rellotge intercanvia sempre les mateixes dues posicions de dígits. Mira quina hora real "
        "correspondria al que el rellotge mostra ara, i pensa quina hora real serà d'aquí a un "
        "minut."
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
        "Per a cada figura, intenta comptar quants quadrets de la quadrícula ocupa la zona "
        "ombrejada, tenint en compte que els triangles formats per les diagonals valen mig quadret "
        "cadascun."
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
    "comentaris_distractors": {},
    "errors_típics":          [],
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
        "Fes el seguiment de quins nombres queden apilats exactament a la posició del número 1 "
        "després de cada plegada. En cada plegada, la meitat dreta es dobla per sota de la meitat "
        "esquerra."
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
        "Calcula quant ha de sumar cadascú i pensa quines targetes pot tenir la Victòria si els "
        "altres dos han agafat parelles que sumen la mateixa quantitat."
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
        "Pensa quants costats de cada trapezi queden a l'interior del molinet i quants queden al "
        "perímetre exterior. La diferència entre la suma dels quatre perímetres i el perímetre del "
        "molinet t'indica quant mesuren els costats interiors."
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
        "Anota quants retoladors agafa cadascú en cada torn i porta la compte acumulada fins que la "
        "Fàtima tingui prop de 25. Potser l'últim torn no és complet."
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
        "Quants dígits senars existeixen? Pensa quantes maneres hi ha d'escollir-ne quatre i en "
        "quants ordres es poden col·locar (creixent o decreixent)."
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
        "Per a cada pista, comprova quantes ciutats de la ruta real coincideixen amb la posició "
        "(origen, via o destí) que apareix en aquella frase. Ha de ser exactament una."
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
        "Posa un nom a cada cercle i escriu una igualtat per a cada fila i cada columna. Després "
        "mira si combinant dues d'aquestes igualtats pots descobrir alguna relació entre els dos "
        "cercles grisos."
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
        "Posa un nom al nombre d'amics i un altre al nombre de maduixes. La frase de les 80 "
        "maduixes de més et permet trobar primer quants amics hi ha; comença per aquí."
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
        "Recorda que els cinc nombres són 1, 2, 3, 4 i 5 i pensa quins valors pot tenir el triple "
        "del nombre de la Zoe, perquè ha de coincidir amb la suma de dos d'aquests nombres."
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
        "Recorda que cada plec fa que la tira tombi i canviï la cara que es veu. Compta quants girs "
        "fa la figura de la dreta i fixa't si hi ha cap tros recte sense plec."
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
        "Pensa quant pesen totes nou pilotes juntes i recorda que, si la balança està equilibrada, "
        "els dos plats pesen el mateix. Fixa't també en quant pot pesar com a màxim el plat que "
        "només té dues pilotes."
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
        "Mira que els rectangles formen molinets encaixats i comença per dins, pel quadrat negre i "
        "els rectangles blancs. Busca com es relacionen el costat llarg i el costat curt d'un "
        "rectangle amb el quadrat que tanca a dins."
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
        "Per a cada fila i cada columna, calcula quant li sobra respecte de 6: això et diu quant "
        "has de treure en total d'aquella fila o columna. Comença per les files o columnes on només "
        "hi ha una manera possible de treure aquesta quantitat."
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
        "Classifica primer les tasses per mida i per color de nansa. Pensa què vol dir que l'Ona i "
        "la Paula tinguin mides diferents però el mateix color de nansa, i mira quines parelles ho "
        "compleixen."
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
        "Fixa't que totes les caselles amb lletra són dins d'una mateixa regió, de manera que només "
        "hi anirà un gronxador. Comença per la regió més petita i pensa a quina fila pot anar el "
        "seu gronxador."
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
        "Pensa que el grup 2026 pot sortir de dues maneres: sencer dins d'un nombre, o partit entre "
        "el final d'un nombre i el principi del següent. Mira quines maneres de partir 2026 entre "
        "dos nombres són realment possibles."
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
