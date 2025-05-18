#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique import interactions_canvas as ic
from graphes.k_closest_neighbors import compute_all_neighbors

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

nearest_neighbor_cache = {}
last_points_hash = None

def is_connected(idx1, idx2):
    """
    Deux points sont connectés si l'un est le plus proche voisin de l'autre.
    """
    global last_points_hash, nearest_neighbor_cache

    points = ic.sommets.points
    current_hash = hash(tuple(points))

    if current_hash != last_points_hash:
        last_points_hash = current_hash
        # On réutilise compute_all_neighbors avec k=1
        voisins = compute_all_neighbors(points, 1)
        nearest_neighbor_cache = {i: voisins[i][0] for i in voisins}

    return (
        nearest_neighbor_cache.get(idx1) == idx2 or
        nearest_neighbor_cache.get(idx2) == idx1
    )