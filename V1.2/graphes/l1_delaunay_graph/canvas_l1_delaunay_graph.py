from interface_graphique.creer_graph import creer_graph
from graphes.l1_delaunay_graph import interactions_l1_delaunay_graph as i_ldg

def ouvrir_canvas_l1_delaunay_graph(root):
    creer_graph(root, {
        'is_connected': i_ldg.is_connected,
        'get_type_graphe': i_ldg.get_type_graphe,
    })
