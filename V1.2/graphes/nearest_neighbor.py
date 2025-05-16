#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique import interactions_canvas as ic
from graphes.k_closest_neighbors import find_neighbors

def open_nearest_neighbor_graph(root):
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
    return "Nearest neighbor graph"

#Algorithme principal du graphe Nearest Neighbor

def is_connected(idx1, idx2):
    """
    Deux points sont connectés si l'un est le plus proche voisin de l'autre.
    """
    # On force le remplissage du cache pour cette paire
    ic.get_real_distance(idx1, idx2)
    voisins1 = find_neighbors(idx1, 1)[0]
    if voisins1 == idx2:
        return True

    voisins2 = find_neighbors(idx2, 1)[0]
    return voisins2 == idx1