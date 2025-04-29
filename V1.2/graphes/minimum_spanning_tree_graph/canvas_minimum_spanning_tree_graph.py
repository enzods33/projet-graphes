from interface_graphique.creer_graph import creer_graph
from graphes.minimum_spanning_tree_graph import interactions_minimum_spanning_tree_graph as i_mstg

def ouvrir_canvas_minimum_spanning_tree_graph(root):
    creer_graph(root, {
        'is_connected': i_mstg.is_connected,
        'get_type_graphe': i_mstg.get_type_graphe,
    })
