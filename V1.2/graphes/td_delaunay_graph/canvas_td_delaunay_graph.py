from interface_graphique.creer_graph import create_graph
from graphes.td_delaunay_graph import interactions_td_delaunay_graph as i_tdg

def open_td_delaunay_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_tdg.is_connected,
        'get_graph_type': i_tdg.get_graph_type,
        }
    )
