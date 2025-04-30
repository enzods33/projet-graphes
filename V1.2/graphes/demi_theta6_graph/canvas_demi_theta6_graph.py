from interface_graphique.creer_graph import create_graph
from graphes.demi_theta6_graph import interactions_demi_theta6_graph as i_dtg

def ouvrir_canvas_demi_theta6_graph(root):
    create_graph(root, {
        'is_connected': i_dtg.is_connected,
        'get_type_graphe': i_dtg.get_type_graphe,
    })
