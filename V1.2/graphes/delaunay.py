# L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
import math
from interface_graphique import interactions_canvas as ic
from outils_canva import outils_geometrie as geo

def open_delaunay_triangulation_graph(root):
    """
    Crée l'interface du graphe de Delaunay et enregistre ses callbacks propres.
    """
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
        },
        ajouter_boutons_specifiques=None,
        graph_name=get_graph_type()
    )

# Fonctions d'intégration du graphe

def get_graph_type():
    """
    Retourne le nom du graphe utilisé pour l'affichage et la sauvegarde.
    """
    return "Delaunay triangulation graph"

# Algorithme principal du graphe Delaunay

delaunay_edges = set()
last_hash = None

def is_connected(idx1, idx2):
    """
    Une arête est valide si elle appartient à la triangulation de Delaunay
    (condition du cercle vide).
    """
    global delaunay_edges, last_hash

    points = ic.sommets.points
    if len(points) <= 3:
        return True

    current_hash = hash(tuple(points))
    if current_hash != last_hash:
        last_hash = current_hash
        delaunay_edges = compute_delaunay_edges(points)

    return tuple(sorted((idx1, idx2))) in delaunay_edges

def compute_delaunay_edges(points):
    """
    Calcule toutes les arêtes de la triangulation de Delaunay
    selon la condition du cercle vide.
    """
    edges = set()
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            for k in range(n):
                if k in (i, j):
                    continue

                p3 = points[k]
                center = geo.center_of_circle(p1, p2, p3)
                if center is None:
                    continue

                radius = geo.radius_of_circle(center, p1)
                cercle_vide = True

                for l in range(n):
                    if l in (i, j, k):
                        continue
                    if math.dist(center, points[l]) < radius - 1e-10:
                        cercle_vide = False
                        break

                if cercle_vide:
                    edges.add(tuple(sorted((i, j))))
                    break 

    return edges