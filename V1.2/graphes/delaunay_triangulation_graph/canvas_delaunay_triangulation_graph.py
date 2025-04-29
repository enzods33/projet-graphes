from interface_graphique.creer_graph import creer_graph
from graphes.delaunay_triangulation_graph import interactions_delaunay_triangulation_graph as i_dtg

def ouvrir_canvas_delaunay_triangulation_graph(root):
    creer_graph(root, {
        'is_connected': i_dtg.is_connected,
        'get_type_graphe': i_dtg.get_type_graphe,
    })
