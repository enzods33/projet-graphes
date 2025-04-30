from interface_graphique.creer_graph import create_graph
from graphes.theta_graph import interactions_theta_graph as i_tg

def ouvrir_canvas_theta_graph(root):
    create_graph(root, {
        'is_connected': i_tg.is_connected,
        'get_type_graphe': i_tg.get_type_graphe,
    })
