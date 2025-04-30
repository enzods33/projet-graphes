from interface_graphique.creer_graph import create_graph
from graphes.theta_graph import interactions_theta_graph as i_tg

def open_theta_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_tg.is_connected,
        'get_graph_type': i_tg.get_graph_type,
        }
    )
