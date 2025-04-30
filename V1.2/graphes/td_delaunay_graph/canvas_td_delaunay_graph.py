from interface_graphique.creer_graph import create_graph
from graphes.td_delaunay_graph import interactions_td_delaunay_graph as i_tdg

def ouvrir_canvas_td_delaunay_graph(root):
    create_graph(root, {
        'is_connected': i_tdg.is_connected,
        'get_type_graphe': i_tdg.get_type_graphe,
    })
