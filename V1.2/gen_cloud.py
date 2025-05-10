"""
Module regroupant les fonctions utiles à la génération d'un nuage de points aléatoires
et à sa sauvegarde dans un fichier JSON via une boîte de dialogue Tkinter.
"""

from tkinter import filedialog
import json
import random
import sys

from outils_canva.constantes import SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2, MAX_NB_POINTS

def read_command_args():
    """
    Lit et valide les arguments passés en ligne de commande.

    Retour :
        Tuple (xmin, xmax, ymin, ymax, nb_points, nom_fichier)
        ou None si les arguments sont invalides.
    """
    if len(sys.argv) != 7:
        print("Ligne de commande incorrecte, Réessayez")
        explications()
        return None

    x1 = sys.argv[1].replace(",", ".")
    x2 = sys.argv[2].replace(",", ".")
    y1 = sys.argv[3].replace(",", ".")
    y2 = sys.argv[4].replace(",", ".")
    nb_str = sys.argv[5]
    nom_fichier = sys.argv[6]

    if not (is_float(x1) and is_float(x2) and is_float(y1) and is_float(y2)):
        print("Les coordonnées doivent être des nombres valides.")
        return None

    if not nb_str.isdigit():
        print("Le nombre de points doit être un entier positif.")
        return None

    xmin = float(x1)
    xmax = float(x2)
    ymin = float(y1)
    ymax = float(y2)
    nb = int(nb_str)

    if nb > MAX_NB_POINTS:
        print("Le nombre de points doit être inférieur à: ", MAX_NB_POINTS)

    if not (xmin < xmax and ymin < ymax):
        print("xmin doit être strictement inférieur à xmax, et ymin à ymax.")
        return None

    if not (SCROLLX1 <= xmin <= SCROLLX2 and SCROLLX1 <= xmax <= SCROLLX2):
        print(f"xmin et xmax doivent être compris entre {SCROLLX1} et {SCROLLX2}.")
        return None

    if not (SCROLLY1 <= ymin <= SCROLLY2 and SCROLLY1 <= ymax <= SCROLLY2):
        print(f"ymin et ymax doivent être compris entre {SCROLLY1} et {SCROLLY2}.")
        return None

    if not nom_fichier.endswith(".json"):
        nom_fichier += ".json"

    return xmin, xmax, ymin, ymax, nb, nom_fichier

def is_float(val):
    """
    Vérifie si une chaîne représente un nombre flottant valide,
    en acceptant les virgules comme séparateur décimal et les signes négatifs.

    Retourne True si la valeur est un float valide, False sinon.
    """
    val = val.replace(",", ".")
    if val.startswith("-"):
        val = val[1:]
    return val.replace(".", "", 1).isdigit()

def generate_points_cloud(xmin, xmax, ymin, ymax, npoints):
    """
    Génère une liste de points aléatoires dans les intervalles de coordonnées donnés.
    """
    return [(random.uniform(xmin, xmax), random.uniform(ymin, ymax)) for _ in range(npoints)]

def save_cloud_to_file(points, nom_donne):
    """
    Ouvre une boîte de dialogue pour sauvegarder les points dans un fichier JSON.
    """
    nom_fichier = filedialog.asksaveasfilename(
        initialfile=nom_donne,
        defaultextension=".json",
        filetypes=[("Fichier JSON", "*.json")],
        title="Enregistrer le nuage de points"
    )

    if not nom_fichier:
        print("Sauvegarde annulée.")
        return

    nuage_data = {
        "type": "Nuage Aleatoire",
        "facteur_global": 1.0,
        "parametres": {},
        "points": points,
        "scroll_x": 0,
        "scroll_y": 0
    }

    with open(nom_fichier, "w") as json_file:
        json.dump(nuage_data, json_file, indent=4)

    print(f"Nuage sauvegardé dans {nom_fichier}")

def explications():
    """
    Affiche dans la console les instructions pour exécuter correctement le script.
    """
    print("Pour générer un nuage de points aléatoires, ouvrez un terminal (cmd, PowerShell ou terminal de VS Code).")
    print("Placez-vous dans le dossier du projet avec la commande cd.")
    print("Usage: python3 gen_cloud.py <xmin> <xmax> <ymin> <ymax> <nombre de points> <nom du fichier>")
    print("Exemple : python3 gen_cloud.py 0 200 0 200 50 nuage.json")

def generate_random_cloud():
    """
    Point d'entrée principal pour générer et sauvegarder un nuage de points aléatoires.
    """
    args = read_command_args()
    if args is None:
        return

    xmin, xmax, ymin, ymax, nb, nom_fichier = args
    points = generate_points_cloud(xmin, xmax, ymin, ymax, nb)
    save_cloud_to_file(points, nom_fichier)

if __name__ == "__main__":
    """
    Point d'entrée du script lorsqu'il est exécuté en ligne de commande.

    Exemple :
        python3 gen_cloud.py 0 100 0 100 50 nuage.json
    """
    generate_random_cloud()