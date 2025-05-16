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

    C'est-à-dire : pour tout autre sommet idx_r, on doit avoir
    d(idx1, idx_r) ≥ d(idx1, idx2) ou d(idx2, idx_r) ≥ d(idx1, idx2)
    """
    d_ab = ic.get_real_distance(idx1, idx2)

    for idx_r in range(len(ic.sommets.points)):
        if idx_r != idx1 and idx_r != idx2:
            d_ar = ic.get_real_distance(idx1, idx_r)
            d_br = ic.get_real_distance(idx2, idx_r)
            if d_ar < d_ab and d_br < d_ab:
                return False

    return True