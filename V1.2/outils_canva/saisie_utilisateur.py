def demander_float(message, valeur_par_defaut, min=None, max=None):
    """
    Demande à l'utilisateur de saisir un nombre réel via la ligne de commande.

    - Accepte les nombres avec un point (.) ou une virgule (,) comme séparateur décimal.
    - Vérifie que l'entrée est bien un seul nombre sans espace.
    - Vérifie que la valeur est comprise entre les bornes min et max si elles sont définies.
    - Si l'utilisateur appuie sur Entrée sans rien saisir, utilise la valeur par défaut.

    Paramètres :
        message (str) : Message affiché à l'utilisateur.
        valeur_par_defaut (float) : Valeur utilisée si l'utilisateur n'entre rien.
        min (float, optionnel) : Valeur minimale autorisée (None pour sans limite).
        max (float, optionnel) : Valeur maximale autorisée (None pour sans limite).

    Retour :
        float : La valeur saisie et validée par l'utilisateur.
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
            print("❌ Veuillez entrer un nombre valide (ex: 3.14 ou 3,14).")
            continue

        valeur = float(valeur_str)

        if min is not None and valeur < min:
            print(f"❌ La valeur doit être supérieure ou égale à {min}.")
            continue
        if max is not None and valeur > max:
            print(f"❌ La valeur doit être inférieure ou égale à {max}.")
            continue

        return valeur


def demander_intervalle(message_min, message_max, valeur_min_defaut, valeur_max_defaut, min_global=None, max_global=None):
    """
    Demande un intervalle valide [vmin, vmax] tel que vmin < vmax.
    Redemande vmin si nécessaire pour garantir un vrai intervalle.
    """
    while True:
        vmin = demander_float(message_min, valeur_min_defaut, min=min_global, max=max_global)

        if max_global is not None and vmin >= max_global:
            print(f"❌ Erreur : la valeur minimale ({vmin}) doit être strictement inférieure à la borne maximale ({max_global}). Réessayez.")
            continue

        vmax = demander_float(message_max, valeur_max_defaut, min=min_global, max=max_global)

        if vmin < vmax:
            return vmin, vmax
        else:
            print(f"❌ Erreur : la valeur minimale ({vmin}) doit être strictement inférieure à la valeur maximale ({vmax}). Réessayez.")
      
def demander_points(message, max_points):
    """
    Demande à l'utilisateur un nombre entier de points.
    Redemande tant que l'entrée est invalide ou hors limite.
    """
    while True:
        valeur_str = input(message)
        if valeur_str == "":
            valeur = 100
        elif valeur_str.isdigit():
            valeur = int(valeur_str)
        else:
            print("❌ Veuillez entrer un nombre entier valide.")
            continue

        if valeur > max_points:
            print(f"❌ Trop de points ({valeur}) pour la limite maximale ({max_points}). Réessayez.")
        elif valeur <= 0:
            print("❌ Le nombre de points doit être strictement positif. Réessayez.")
        else:
            return valeur

def demander_parametres_nuage(largeur, hauteur):
    """
    Demande à l'utilisateur les paramètres du nuage de points : intervalles X, Y, nombre de points.

    Paramètres :
        largeur : largeur maximale autorisée pour X
        hauteur : hauteur maximale autorisée pour Y

    Retourne :
        (xmin, xmax, ymin, ymax, npoints)
    """

    print("🔵 Paramètres pour X :")
    xmin, xmax = demander_intervalle(
        "Valeur minimale pour x : ",
        "Valeur maximale pour x : ",
        valeur_min_defaut=0,
        valeur_max_defaut=largeur,
        min_global=0,
        max_global=largeur
    )

    print("🟢 Paramètres pour Y :")
    ymin, ymax = demander_intervalle(
        "Valeur minimale pour y : ",
        "Valeur maximale pour y : ",
        valeur_min_defaut=0,
        valeur_max_defaut=hauteur,
        min_global=0,
        max_global=hauteur
    )

    npoints = demander_points(
        "Nombre de points à générer : ",
        max_points=min(largeur, hauteur)
    )

    return xmin, xmax, ymin, ymax, npoints