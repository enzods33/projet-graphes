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

def is_connected(idx1, idx2):
    """
    Une arête fait partie de la triangulation de Delaunay s'il existe un cercle passant par
    idx1, idx2, et un autre point, tel que ce cercle ne contient aucun autre sommet.
    """
    p1 = ic.sommets.points[idx1]
    p2 = ic.sommets.points[idx2]

    if len(ic.sommets.points) <= 3:
        return True

    for i in range(len(ic.sommets.points)):
        if i in (idx1, idx2):
            continue
        p3 = ic.sommets.points[i]

        center = geo.center_of_circle(p1, p2, p3)
        if center is None:
            continue

        radius = geo.radius_of_circle(center, p1)
        cercle_vide = True

        for j in range(len(ic.sommets.points)):
            if j in (idx1, idx2, i):
                continue
            p = ic.sommets.points[j]
            if math.dist(center, p) < radius - 1e-10:
                cercle_vide = False
                break

        if cercle_vide:
            return True

    return False