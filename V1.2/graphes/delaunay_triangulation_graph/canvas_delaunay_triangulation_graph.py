from interface_graphique.creer_graph import create_graph
from graphes.delaunay_triangulation_graph import interactions_delaunay_triangulation_graph as i_dtg

def ouvrir_canvas_delaunay_triangulation_graph(root):
    create_graph(root, {
        'is_connected': i_dtg.is_connected,
        'get_type_graphe': i_dtg.get_type_graphe,
    },
    graph_name = i_dtg.get_type_graphe())
