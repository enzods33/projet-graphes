"""
⚠️⚠️ATTENTION LES DOCSTRINGS A COMPLETER !!!!⚠️⚠️ car je gere pas les input
ce module regroupe les fonctions qui vont demander des saisies manuelles à l'utilisateur
"""

from outils_canva.constantes import MAX_NB_POINTS

def ask_float(message, valeur_par_defaut, min=None, max=None):
    """
    dans la console, demande à l'utilisateur une valeur comprise entre min et max
    
    Paramètres:
        message: message texte affiché dans la console par le programme
        valeur_par_défaut:
        min: valeur minimum possible du nombre demandé à l'utilisateur
        max: valeur maximum possible du nombre demandé à l'utilisateur 
        
    retours:
        valeur: la valeur rentrée par l'utilisateur si elle respecte tous les critères
    """
    while True:
        valeur_str = input(message)

        if valeur_str == "":
            return float(valeur_par_defaut)

        valeur_str = valeur_str.replace(",", ".")  # Remplacer la virgule par un point

        # Vérifie qu'on a bien une seule valeur sans espace
        if " " in valeur_str:
            print("❌ Entrez une seule valeur numérique sans espaces.")
            continue

        # Vérifie que c'est un nombre
        if not valeur_str.replace(".", "", 1).isdigit():
            print("❌ Veuillez entrer un nombre valide (ex: 2.5 ou 2,5).")
            continue

        valeur = float(valeur_str)

        if min is not None and valeur < min:
            print(f"❌ La valeur doit être supérieure ou égale à {min}.")
            continue
        if max is not None and valeur > max:
            print(f"❌ La valeur doit être inférieure ou égale à {max}.")
            continue

        return valeur


def ask_interval(message_min, message_max, valeur_min_defaut, valeur_max_defaut, min_global=None, max_global=None):
    """
    Demande à l'utilisateur les intervalles de coordonnées sur lesquels il souhaite que le nuage de points aléatoire se génère
    Cet intervalle ne doit évidemment pas dépasser les dimensions du canva
    Paramètres:
        message_min:
        message_max: 
        valeur_min_défaut:
        valeur_max_défaut:
        min_global:
        max_global:
    Retours:
        vmin:
        vmax:
    """

    while True:
        vmin = ask_float(message_min, valeur_min_defaut, min=min_global, max=max_global)

        if max_global is not None and vmin >= max_global:
            print(f"❌ Erreur : la valeur minimale ({vmin}) doit être strictement inférieure à la borne maximale ({max_global}). Réessayez.")
            continue

        vmax = ask_float(message_max, valeur_max_defaut, min=min_global, max=max_global)

        if vmin < vmax:
            return vmin, vmax
        else:
            print(f"❌ Erreur : la valeur minimale ({vmin}) doit être strictement inférieure à la valeur maximale ({vmax}). Réessayez.")


def ask_nb_points(message):
    """
    Demande à l'utilisateur le nombre de points qu'il souhaite générer aléatoirement
    Cette valeur doit être comprise entre 1 et 100.
    Paramètres:
        message: message texte affiché dans la console par le programme
    retour: 
        valeur: le nombre de ponits choisi par l'utilisateur si il respecte les critères
    """
    max_nb_points = MAX_NB_POINTS
    while True:
        valeur_str = input(message)
        if valeur_str == "":
            valeur = 100
        elif valeur_str.isdigit():
            valeur = int(valeur_str)
        else:
            print("❌ Veuillez entrer un nombre entier valide.")
            continue

        if valeur > max_nb_points:
            print(f"❌ Trop de points ({valeur}) pour la limite maximale ({max_nb_points}). Réessayez.")
        elif valeur <= 0:
            print("❌ Le nombre de points doit être strictement positif. Réessayez.")
        else:
            return valeur


def ask_cloud_parameters(largeur, hauteur):
    """renvoie les intervalles de coordonnées x et y dans lesquels le nuage aléatoire va se générer
    ainsi que le nombre de point a créer.
    Ces valeurs ont étés choisies par l'utilisateur, en respectant des critères.
    Paramètres:
        largeur: largeur du canva
        hauteur: hauteur du canva
    Retour:
        l'intervalle de coordonéés pour générer le nuage et le nombre de points à générer
    """
    print(" Paramètres pour X :")
    xmin, xmax = ask_interval(
        "Valeur minimale pour x : ",
        "Valeur maximale pour x : ",
        valeur_min_defaut=0,
        valeur_max_defaut=largeur,
        min_global=0,
        max_global=largeur
    )

    print(" Paramètres pour Y :")
    ymin, ymax = ask_interval(
        "Valeur minimale pour y : ",
        "Valeur maximale pour y : ",
        valeur_min_defaut=0,
        valeur_max_defaut=hauteur,
        min_global=0,
        max_global=hauteur
    )

    npoints = ask_nb_points( "Nombre de points à générer : " )

    return xmin, xmax, ymin, ymax, npoints

