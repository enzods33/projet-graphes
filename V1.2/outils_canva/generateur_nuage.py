import json
import random
import json
import random

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
    points = []
    for _ in range(int(npoints)):
        x = random.uniform(xmin, xmax)
        y = random.uniform(ymin, ymax)
        points.append([x, y])

    # Sauvegarder le nuage de points dans le fichier JSON
    nuage_data = {
        "points": points
    }

    # Ouvrir et écrire dans le fichier JSON
    with open(nom_fichier, "w") as json_file:
        json.dump(nuage_data, json_file, indent=4)

    print(f"Nuage sauvegardé dans {nom_fichier}")