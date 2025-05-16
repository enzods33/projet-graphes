# L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
import math
import interface_graphique.interactions_canvas as ic

def open_gabriel_graph(root):
    """
    Crée l'interface du graphe de Gabriel et enregistre ses callbacks propres.
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
    return "Gabriel graph"

# Algorithme principal du graphe Gabriel Graph

def is_connected(idx1, idx2):
    """
    Deux sommets sont connectés s'il n'existe aucun autre sommet à l'intérieur
    du cercle dont ils forment le diamètre (Gabriel Graph).
    """
    if idx1 >= len(ic.sommets.points) or idx2 >= len(ic.sommets.points):
        return False

    p1 = ic.sommets.points[idx1]
    p2 = ic.sommets.points[idx2]

    if p1 == p2:
        return False

    # Centre du cercle
    disk_center = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    disk_radius = math.dist(p1, p2) / 2

    for i in range(len(ic.sommets.points)):
        if i in (idx1, idx2):
            continue
        p = ic.sommets.points[i]
        if math.dist(p, disk_center) < disk_radius - 1e-10:
            return False

    return True