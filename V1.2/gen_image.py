"""
Script de génération d'image de graphe à partir d'un fichier JSON de points.
Usage :
    python3 gen_image.py <fichier_points.json> <fichier_sortie.png>
"""

import sys
import os
import json
import importlib
import matplotlib.pyplot as plt
from interface_graphique import interactions_canvas as ic


def read_command_args():
    """
    Lit les arguments en ligne de commande et les valide.
    Retourne un tuple (chemin_json, chemin_image) ou None en cas d'erreur.
    """
    if len(sys.argv) != 3:
        print("Usage : python3 gen_image.py <fichier_points.json> <fichier_sortie.png>")
        return None

    fichier_json = sys.argv[1]
    fichier_image = sys.argv[2]

    if not os.path.isfile(fichier_json):
        print(f"Erreur : le fichier '{fichier_json}' n'existe pas.")
        return None

    if not fichier_image.endswith(".png"):
        print("Erreur : le fichier de sortie doit être une image PNG.")
        return None

    return fichier_json, fichier_image


def load_json_data(fichier_json):
    """
    Charge les données du fichier JSON et vérifie la présence des champs attendus.
    Retourne (points, type_graphe, parametres) ou None en cas d'erreur.
    """
    with open(fichier_json, "r") as f:
        contenu = f.read()

    if not contenu.strip().startswith("{"):
        print("Erreur : le fichier ne contient pas un JSON valide.")
        return None

    data = json.loads(contenu)

    if "points" not in data or "type" not in data:
        print("Erreur : le JSON doit contenir les champs 'points' et 'type'.")
        return None

    points = [(x, y) for (x, y) in data["points"]]
    type_graphe = data["type"]
    parametres = data.get("parametres", {})

    return points, type_graphe, parametres


def import_graphe_module(type_graphe):
    """
    Importe dynamiquement le module du graphe correspondant.
    Retourne le module ou None si le type est inconnu.
    """
    type_to_module = {
        "Yao graph": "graphes.yao",
        "Relative neighborhood graph": "graphes.relative_neighborhood",
        "Minimum spanning tree graph": "graphes.minimum_spanning_tree",
        "Unit disk graph": "graphes.unit_disk",
        "Integer graph": "graphes.integer_",
        "Gabriel graph": "graphes.gabriel",
        "Delaunay triangulation graph": "graphes.delaunay_triangulation",
        "K closest neighbors graph": "graphes.k_closest_neighbors",
        "Nearest neighbor graph": "graphes.nearest_neighbor",
    }

    if type_graphe not in type_to_module:
        print(f"Erreur : type de graphe inconnu : '{type_graphe}'")
        print("Types acceptés :", ", ".join(type_to_module.keys()))
        return None

    return importlib.import_module(type_to_module[type_graphe])


def draw_and_save_graph(points, is_connected, fichier_image):
    """
    Génère une image du graphe à partir des points et de la fonction de connexion.
    """
    plt.figure(figsize=(6, 6))
    xs, ys = zip(*points)
    plt.scatter(xs, ys, facecolors='yellow', edgecolors='black', marker='s')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if is_connected(i, j):
                x1, y1 = points[i]
                x2, y2 = points[j]
                plt.plot([x1, x2], [y1, y2], color='yellow')

    plt.axis("off")
    plt.gca().invert_yaxis()
    plt.savefig(fichier_image, bbox_inches='tight')
    plt.close()

    print(f"Image enregistrée dans {fichier_image}")


def generer_image_graphe():
    """
    Fonction principale appelée en ligne de commande.
    """
    args = read_command_args()
    if args is None:
        return

    fichier_json, fichier_image = args
    resultats = load_json_data(fichier_json)
    if resultats is None:
        return

    points, type_graphe, parametres = resultats
    module = import_graphe_module(type_graphe)
    if module is None:
        return

    # Préparer les données pour les fonctions canvas
    ic.sommets.points = points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ic.get_real_distance(i, j)

    if type_graphe in ["Unit disk graph", "K closest neighbors graph", "Yao graph"]:
        if "set_parameters" in dir(module):
            module.set_parameters(parametres)

    is_connected = lambda i, j: module.is_connected(i, j)

    draw_and_save_graph(points, is_connected, fichier_image)


if __name__ == "__main__":
    generer_image_graphe()