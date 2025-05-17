#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique import interactions_canvas as ic

def open_relative_neighborhood_graph(root):
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
        },
        None,
        graph_name=get_graph_type()
    )

#Fonctions d'intégration du graphe

def get_graph_type():
    return "Relative neighborhood graph"

#Algorithme principal du graphe Relative Neighborhood

def is_connected(idx1, idx2):
    """
    Deux sommets sont connectés dans le graphe de voisinage relatif s'il n'existe aucun troisième
    sommet qui soit plus proche à la fois de idx1 et de idx2 que la distance qui les sépare.
    """
    dist_1_2 = ic.get_real_distance(idx1, idx2)

    for idx_i in range(len(ic.sommets.points)):
        if idx_i != idx1 and idx_i != idx2:
            dist_1_i = ic.get_real_distance(idx1, idx_i)
            dist_2_i = ic.get_real_distance(idx2, idx_i)
            if dist_1_i < dist_1_2 and dist_2_i < dist_1_2:
                return False

    return True