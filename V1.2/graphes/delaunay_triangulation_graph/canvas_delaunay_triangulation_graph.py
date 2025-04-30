from interface_graphique.creer_graph import create_graph
from graphes.delaunay_triangulation_graph import interactions_delaunay_triangulation_graph as i_dtg

def open_delaunay_triangulation_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_dtg.is_connected,
        'get_graph_type': i_dtg.get_graph_type,
        },
        graph_name = i_dtg.get_graph_type()
    )
