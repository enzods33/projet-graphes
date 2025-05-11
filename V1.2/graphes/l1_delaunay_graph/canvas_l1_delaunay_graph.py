from graphes.l1_delaunay_graph import interactions_l1_delaunay_graph as i_ld
from interface_graphique.creer_graph import create_graph

def open_l1_delaunay_graph_canvas(root):
    """
    Ouvre le canvas pour le L1-Delaunay Graph.
    """
    create_graph(
        root,
        {
            "is_connected": i_ld.is_connected,
            "get_graph_type": i_ld.get_graph_type,
        },
        graph_name=i_ld.get_graph_type()
    )