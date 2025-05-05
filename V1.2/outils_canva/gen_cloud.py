"""
Module regroupant les fonctions utiles à la génération d'un nuage de point aléatoire
et à sa sauvegarde
"""

import json
import sys
from outils_canva.geometrie import generate_points_cloud

def generate_random_cloud():
    """
    Génère un nuage de points aléatoires dans les intervalles spécifiés et les sauvegarde en JSON.

    Paramètres :
    - largeur : la largeur du canvas (limite des coordonnées x)
    - hauteur : la hauteur du canvas (limite des coordonnées y)
    - npoints : le nombre de points à générer
    - xmin, xmax : intervalles pour les coordonnées x
    - ymin, ymax : intervalles pour les coordonnées y
    """

    if (len(sys.argv) != 8):
        print("Ligne de commande incorrecte, Réessayez")
        print("Usage: python3 gen_cloud.py <xmin> <xmax> <ymin> <ymax> <nombre de points> <nom du fichier>")
        print("Exemple: python3 mgen_cloud.py 0 200 0 200 5 test.json")
        return
    
    xmin=sys.argv[1]
    xmax=sys.argv[2]
    ymin=sys.argv[3]
    ymax=sys.argv[4]
    nb=sys.argv[5]
    nom_fichier=sys.argv[6]

    if not nom_fichier.endswith(".json"):
        # Si l'extension .json n'est pas présente, l'ajouter
        nom_fichier += ".json"

    # Générer les points aléatoires
    points = generate_points_cloud(xmin, xmax, ymin, ymax, nb)

    # Sauvegarder le nuage de points dans le fichier JSON
    nuage_data = {
    "type": "Nuage Aleatoire",
    "facteur_global": 1.0,
    "parametres": {},
    "points": points,
    "scroll_x": 0,
    "scroll_y": 0
    }

    # Ouvrir et écrire dans le fichier JSON
    with open(nom_fichier, "w") as json_file:
        json.dump(nuage_data, json_file, indent=4)

    print(f"Nuage sauvegardé dans {nom_fichier}")

def explications():
    print("Usage: python3 gen_cloud.py <xmin> <xmax> <ymin> <ymax> <nombre de points> <nom du fichier>")
    print("Exemple: python3 mgen_cloud.py 0 200 0 200 5 test.json")


generate_random_cloud()