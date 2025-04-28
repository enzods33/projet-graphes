import json
from outils_canva.geometrie import generer_nuage_points
from outils_canva.saisie_utilisateur import demander_parametres_nuage
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR

def generer_nuage_aleatoire(largeur, hauteur, npoints, xmin=0, xmax=None, ymin=0, ymax=None):
    """
    Génère un nuage de points aléatoires dans les intervalles spécifiés et les sauvegarde en JSON.

    Paramètres :
    - largeur : la largeur du canvas (limite des coordonnées x)
    - hauteur : la hauteur du canvas (limite des coordonnées y)
    - npoints : le nombre de points à générer
    - xmin, xmax : intervalles pour les coordonnées x
    - ymin, ymax : intervalles pour les coordonnées y
    """
    # Utilisation des valeurs par défaut si non spécifiées
    if xmax is None:
        xmax = largeur
    if ymax is None:
        ymax = hauteur

    # Demander à l'utilisateur le nom du fichier
    nom_fichier = input("Nom du fichier de sauvegarde (ex: nuage.json) : ")
    
    # Si l'utilisateur n'entre rien, utiliser un nom par défaut avec l'extension .json
    if not nom_fichier:
        nom_fichier = "nuage.json"
    elif not nom_fichier.endswith(".json"):
        # Si l'extension .json n'est pas présente, l'ajouter
        nom_fichier += ".json"

    # Générer les points aléatoires
    points = generer_nuage_points(xmin, xmax, ymin, ymax, int(npoints))

    # Sauvegarder le nuage de points dans le fichier JSON
    nuage_data = {
        "points": points
    }

    # Ouvrir et écrire dans le fichier JSON
    with open(nom_fichier, "w") as json_file:
        json.dump(nuage_data, json_file, indent=4)

    print(f"Nuage sauvegardé dans {nom_fichier}")

def generer_et_sauvegarder():
    xmin, xmax, ymin, ymax, npoints = demander_parametres_nuage(CANVAS_LARGEUR, CANVAS_HAUTEUR)

    generer_nuage_aleatoire(CANVAS_LARGEUR, CANVAS_HAUTEUR, npoints, xmin, xmax, ymin, ymax)