"""
Script de génération d'un nuage de points aléatoires et sauvegarde dans un fichier JSON.
Utilisation :
    python3 gen_nuage.py <xmin> <xmax> <ymin> <ymax> <nombre_de_points> <nom_fichier.json>
"""

import sys
import json
import random
from tkinter import filedialog
from outils_canva.constantes import SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2, MAX_NB_POINTS, ZOOM_MIN


def is_float(value):
    """
    Vérifie si une chaîne représente un nombre flottant valide.
    """
    value = value.replace(",", ".")
    if value.startswith("-"):
        value = value[1:]
    return value.replace(".", "", 1).isdigit()


def is_valid_args(argv):
    """
    Valide les arguments en ligne de commande.
    """
    if len(argv) != 7:
        print("Ligne de commande incorrecte, Réessayez")
        explications()
        return None

    x1, x2, y1, y2, nb_str, nom_fichier = argv[1:]

    if not all(is_float(v) for v in [x1, x2, y1, y2]):
        print("Erreur : Les coordonnées doivent être des nombres valides.")
        return None

    if not nb_str.isdigit():
        print("Erreur : Le nombre de points doit être un entier positif.")
        return None

    xmin = float(x1.replace(",", "."))
    xmax = float(x2.replace(",", "."))
    ymin = float(y1.replace(",", "."))
    ymax = float(y2.replace(",", "."))
    nb = int(nb_str)

    if nb > MAX_NB_POINTS:
        print(f"Erreur : le nombre de points ne doit pas dépasser {MAX_NB_POINTS}.")
        return None

    if not (xmin < xmax and ymin < ymax):
        print("Erreur : xmin doit être < xmax, et ymin < ymax.")
        return None

    if not (SCROLLX1 <= xmin <= SCROLLX2 and SCROLLX1 <= xmax <= SCROLLX2):
        print(f"Erreur : xmin et xmax doivent être entre {SCROLLX1} et {SCROLLX2}.")
        return None

    if not (SCROLLY1 <= ymin <= SCROLLY2 and SCROLLY1 <= ymax <= SCROLLY2):
        print(f"Erreur : ymin et ymax doivent être entre {SCROLLY1} et {SCROLLY2}.")
        return None

    if not nom_fichier.endswith(".json"):
        nom_fichier += ".json"

    return xmin, xmax, ymin, ymax, nb, nom_fichier


def generate_cloud_points(xmin, xmax, ymin, ymax, nb):
    """
    Génère un nuage de points aléatoires dans une zone rectangulaire.
    """
    return [(random.uniform(xmin, xmax), random.uniform(ymin, ymax)) for _ in range(nb)]


def save_cloud(points, nom_initial):
    """
    Sauvegarde un nuage de points dans un fichier JSON via une boîte de dialogue.
    """
    fichier_sortie = filedialog.asksaveasfilename(
        initialfile=nom_initial,
        defaultextension=".json",
        filetypes=[("Fichier JSON", "*.json")],
        title="Enregistrer le nuage de points"
    )

    if not fichier_sortie:
        print("Sauvegarde annulée.")
        return

    data = {
        "type": "Nuage Aleatoire",
        "facteur_global": ZOOM_MIN,
        "parametres": {},
        "points": points,
        "scroll_x": 0.5,
        "scroll_y": 0.5
    }

    with open(fichier_sortie, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Nuage sauvegardé dans {fichier_sortie}")


def generate_cloud():
    """
    Fonction principale : lit les arguments, génère un nuage et propose une sauvegarde.
    """
    args = is_valid_args(sys.argv)
    if args is None:
        return

    xmin, xmax, ymin, ymax, nb, nom_fichier = args
    points = generate_cloud_points(xmin, xmax, ymin, ymax, nb)
    save_cloud(points, nom_fichier)

def explications():
    """
    Affiche dans la console les instructions pour exécuter correctement le script.
    """
    print("Pour générer un nuage de points aléatoires, ouvrez un terminal (cmd, PowerShell ou terminal de VS Code)\n" \
    "Placez-vous dans le dossier du projet avec la commande cd.\n" \
    "Usage: python3 gen_nuage.py <xmin> <xmax> <ymin> <ymax> <nombre de points> <nom du fichier>\n" \
    "Exemple : python3 gen_nuage.py 0 200 0 200 50 nuage.json")


if __name__ == "__main__":
    generate_cloud()