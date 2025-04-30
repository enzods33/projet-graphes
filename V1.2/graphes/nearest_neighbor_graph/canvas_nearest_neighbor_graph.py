from interface_graphique.creer_graph import create_graph
from graphes.nearest_neighbor_graph import interactions_nearest_neighbor_graph as i_nng

def ouvrir_canvas_nearest_neighbor_graph(root):
    create_graph(
        root,
        {
        'is_connected': i_nng.is_connected,
        'get_type_graphe': i_nng.get_type_graphe,
        },
        None,
        graph_name = i_nng.get_type_graphe()
    )
