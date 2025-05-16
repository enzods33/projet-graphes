#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique import interactions_canvas as ic

def open_minimum_spanning_tree_graph(root):
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
    return "Minimum spanning tree graph"

#Algorithme principal du graphe Minimum Spanning Tree

mst_edges = []
_last_points_hash = None

def is_connected(idx1, idx2):
    global mst_edges, _last_points_hash

    points = ic.sommets.points
    if len(points) < 2:
        mst_edges = []
        return False

    # On calcule un nombre entier unique (ou presque) qui représente le "l'identité" de l’objet (liste = pas hashable, mais tuple oui).
    # Pour éviter de recalculer mst_edges si la position n'a pas changé
    current_hash = hash(tuple(points)) 
    if current_hash != _last_points_hash:
        _last_points_hash = current_hash
        edges = ic.get_all_edges()
        edges.sort()
        parent = {i: i for i in range(len(points))}
        mst_edges = []

        for dist, u, v in edges:
            if find(u, parent) != find(v, parent):
                union(u, v, parent)
                mst_edges.append((u, v))

    return (idx1, idx2) in mst_edges or (idx2, idx1) in mst_edges

def find(s, parent):
    """
    Trouve la racine de l'ensemble contenant s avec compression de chemin.
    """
    while parent[s] != s:
        parent[s] = parent[parent[s]]
        s = parent[s]
    return s

def union(a, b, parent):
    """
    Fusionne les ensembles contenant a et b.
    """
    parent[find(a, parent)] = find(b, parent)