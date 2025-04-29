from interface_graphique.creer_graph import creer_graph
from graphes.integer_graph import interactions_integer_graph as i_ig

def ouvrir_canvas_integer_graph(root):
    creer_graph(root, {
        'is_connected': i_ig.is_connected,
        'get_type_graphe': i_ig.get_type_graphe,
    })
