from interface_graphique.creer_graph import creer_graph
from graphes.nearest_neighbor_graph import interactions_nearest_neighbor_graph as i_nng

def ouvrir_canvas_nearest_neighbor_graph(root):
    creer_graph(root, {
        'is_connected': i_nng.is_connected,
        'get_type_graphe': i_nng.get_type_graphe,
    })
