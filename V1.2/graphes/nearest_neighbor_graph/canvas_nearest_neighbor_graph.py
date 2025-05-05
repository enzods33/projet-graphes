from interface_graphique.creer_graph import create_graph
from graphes.nearest_neighbor_graph import interactions_nearest_neighbor_graph as i_nng

def open_nearest_neighbor_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""

    create_graph(
        root,
        {
        'is_connected': i_nng.is_connected,
        'get_graph_type': i_nng.get_graph_type,
        },
        None,
        graph_name = i_nng.get_graph_type()
    )
