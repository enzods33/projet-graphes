from interface_graphique.creer_graph import create_graph
from graphes.yao4_linf_graph import interactions_yao4_linf_graph as i_ylg

def ouvrir_canvas_yao4_linf_graph(root):
    create_graph(root, {
        'is_connected': i_ylg.is_connected,
        'get_type_graphe': i_ylg.get_type_graphe,
    })
