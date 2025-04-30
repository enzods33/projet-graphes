from interface_graphique.creer_graph import create_graph
from graphes.l1_delaunay_graph import interactions_l1_delaunay_graph as i_ldg

def open_l1_delaunay_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_ldg.is_connected,
        'get_type_graphe': i_ldg.get_type_graphe,
        }
    )
