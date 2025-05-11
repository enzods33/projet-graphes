from graphes.td_delaunay_graph import interactions_td_delaunay_graph as i_td
from interface_graphique.creer_graph import create_graph

def open_td_delaunay_graph_canvas(root):
    """
    Ouvre un canvas pour manipuler un TD Delaunay Graph.
    """
    create_graph(
        root,
        {
            "is_connected": i_td.is_connected,
            "get_graph_type": i_td.get_graph_type,
        },
        graph_name=i_td.get_graph_type()
    )
