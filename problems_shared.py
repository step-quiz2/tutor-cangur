"""
Tutor Cangur — shared catalogue.

Contains ERROR_CATALOG and DEPENDENCIES, shared across all level files.
Import this from problems_1eso.py, problems_2eso.py, etc.
"""
ERROR_CATALOG = {
    # ---- Aritmètics ----
    "ARI_ordre_operacions": (
        "Resol d'esquerra a dreta sense respectar la prioritat de multiplicació/divisió "
        "sobre suma/resta."
    ),
    "ARI_signes": (
        "Error de signe en una resta o quan apareix un nombre negatiu (típic a 1r ESO)."
    ),
    # ---- Geomètrics ----
    "GEO_perimetre_vs_area": (
        "Confon perímetre i àrea: suma costats quan l'enunciat demana àrea, o multiplica "
        "quan demana perímetre."
    ),
    "GEO_costats_oblidats": (
        "En calcular el perímetre, oblida sumar algun costat (típic en figures no rectangulars)."
    ),
    "GEO_unitats": (
        "Confon unitats lineals i quadrades (cm vs cm²) o no converteix unitats."
    ),
    # ---- Comptatge ----
    "COMP_fencepost": (
        "Error de comptatge per excés o defecte d'1 (fencepost error). Compta intervals "
        "com a pals, o pals com a intervals."
    ),
    "COMP_doble_recompte": (
        "Compta dues vegades el mateix element en una enumeració."
    ),
    # ---- Lògica / lectura de l'enunciat ----
    "LOG_pregunta_inversa": (
        "Respon a la pregunta inversa de la que es demana (p.ex. dóna el nombre de noies "
        "quan demanen el de nois)."
    ),
    "LOG_dada_ignorada": (
        "Ignora alguna dada de l'enunciat que era essencial per resoldre el problema."
    ),
    # ---- Genèrics ----
    "GEN_calcul": "Error puntual de càlcul (suma, resta, multiplicació) no atribuïble a cap concepte.",
    "GEN_endevina":  "Tria una lletra sense raonament documentat.",
    "GEN_condicions_no_verificades": (
        "Troba una solució parcial però no comprova que compleixi totes les condicions de l'enunciat alhora."
    ),
    "GEN_visualitzacio_espacial": (
        "Dificultat per imaginar girs, plecs o transformacions espacials sense manipular físicament l'objecte."
    ),
    "GEN_optimitzacio_sense_verificar": (
        "Troba una solució que sembla òptima però no comprova si n'hi ha una de millor (màxim/mínim)."
    ),
}


# ============================================================
# DEPENDÈNCIES (buit al MVP)
# ============================================================
# Es deixa buit deliberadament. Quan vulguem afegir mini-exercicis de
# reforç per a conceptes que fallen molt, poblarem aquesta estructura
# i activarem la lògica de retrocés a prerequisit (que ara ja no està
# al tutor.py per simplicitat).
DEPENDENCIES = {}


# ============================================================
# PROBLEMES
# ============================================================
# Catàleg de 30 problemes. ESTRUCTURA OBJECTIU:
#   - PRO-1ESO-2024-01 ... PRO-1ESO-2024-10  →  10 problemes de 3 punts
#   - PRO-1ESO-2024-11 ... PRO-1ESO-2024-20  →  10 problemes de 4 punts
#   - PRO-1ESO-2024-21 ... PRO-1ESO-2024-30  →  10 problemes de 5 punts
#
# COM AFEGIR ELS PROBLEMES:
# Avui el catàleg té DOS problemes d'exemple poblats (CAN-1ESO-2024-01,
# CAN-1ESO-2024-11) per il·lustrar el format complet. Els 28 restants
# són PLACEHOLDERS amb camps obligatoris a None: la UI els amaga
# automàticament (vegeu `get_available_problems()` més avall).
#
# A mesura que tinguis els enunciats reals, omple cada placeholder
# substituint els None per:
#   - "enunciat": el text del problema (string)
#   - "opcions": {"A": "...", "B": "...", "C": "...", "D": "...", "E": "..."}
#   - "resposta_correcta": una lletra "A".."E"
# Els camps "expected_reasoning", "comentaris_distractors", "errors_típics"
# es deixen None / dict buit / list buida i es poden anar omplint més
# endavant. La IA degrada elegantment quan no hi són.
PROBLEMS = {}
