import sys
import json
import importlib
import matplotlib.pyplot as plt
from interface_graphique import interactions_canvas as ic


def load_points_from_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    points = [tuple(p) for p in data["points"]]  # Assure que les points sont hashables
    return points, data["type"], data.get("parametres", {})


def draw_graph(points, is_connected, chemin_de_sortie):
    """
    Dessine un graphe à partir des points et d'une fonction is_connected,
    puis sauvegarde l'image dans le fichier output_path.
    """
    plt.figure(figsize=(6, 6))                           # Crée une figure matplotlib carrée
    xs, ys = zip(*points)                                # Sépare les x et y pour affichage
    plt.scatter(xs, ys, facecolors='yellow', edgecolors='black', marker='s')       # Affiche les sommets en noir

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if is_connected(i, j):
                x1, y1 = points[i]
                x2, y2 = points[j]
                plt.plot([x1, x2], [y1, y2], color='yellow')  # Trace l'arête

    plt.axis("off")                                     # Supprime les axes pour un rendu propre
    plt.gca().invert_yaxis()                            # Inverse l'axe Y pour correspondre à Tkinter
    plt.savefig(chemin_de_sortie, bbox_inches='tight')  # Sauvegarde l'image sans marges
    plt.close()                                         # Ferme la figure


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python3 gen_image.py test.json sortie.png")
        sys.exit(1)

    json_file = sys.argv[1]
    output_image = sys.argv[2]

    # Chargement des points, du type de graphe et des paramètres
    points, graph_type, parametres = load_points_from_json(json_file)

    # Injection dans ic.sommets pour compatibilité avec les fichiers de graphes
    ic.sommets.points = points

    # Pré-remplissage du cache de distances
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ic.get_real_distance(i, j)

    # Mappage type de graphe -> chemin de module
    type_to_module = {
        "Theta graph": "graphes.theta",
        "Relative neighborhood graph": "graphes.relative_neighborhood",
        "Minimum spanning tree graph": "graphes.minimum_spanning_tree",
        "Unit disk graph": "graphes.unit_disk",
        "Integer graph": "graphes.integer_",
        "Gabriel graph": "graphes.gabriel",
        "Delaunay triangulation graph": "graphes.delaunay_triangulation",
        "K closest neighbors graph": "graphes.k_closest_neighbors",
        "Nearest neighbor graph": "graphes.nearest_neighbor",
    }

    if graph_type not in type_to_module:
        print(f"Erreur : type de graphe inconnu : '{graph_type}'")
        sys.exit(1)

    module_path = type_to_module[graph_type]
    module = importlib.import_module(module_path)

    # Appliquer les paramètres seulement pour certains graphes
    if graph_type == "Unit disk graph":
        module.set_parameters(parametres)
    elif graph_type == "K closest neighbors graph":
        module.set_parameters(parametres)
    elif graph_type == "Theta graph":
        module.set_parameters(parametres)

    is_connected = lambda i, j: module.is_connected(i, j)

    draw_graph(points, is_connected, output_image)
    print(f"Image enregistrée dans {output_image}")