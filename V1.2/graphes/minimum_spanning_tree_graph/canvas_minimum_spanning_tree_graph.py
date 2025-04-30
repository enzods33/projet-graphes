from interface_graphique.creer_graph import creer_graph
from graphes.minimum_spanning_tree_graph import interactions_minimum_spanning_tree_graph as i_mst

def ouvrir_canvas_minimum_spanning_tree_graph(root):
    creer_graph(root, {
        'is_connected': i_mst.is_connected,
        'get_type_graphe': i_mst.get_type_graphe,
    })
