from interface_graphique.creer_graph import create_graph
from graphes.demi_theta6_graph import interactions_demi_theta6_graph as i_dtg

def open_demi_theta6_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_dtg.is_connected,
        'get_graph_type': i_dtg.get_graph_type,
        }
    )
