from interface_graphique.creer_graph import create_graph
from graphes.yao_graph import interactions_yao_graph as i_yg

def ouvrir_canvas_yao_graph(root):
    create_graph(root, {
        'is_connected': i_yg.is_connected,
        'get_type_graphe': i_yg.get_type_graphe,
    })
