from interface_graphique.creer_graph import create_graph
from graphes.relative_neighborhood_graph import interactions_relative_neighborhood_graph as i_rng

def open_relative_neighborhood_graph_canvas(root):
    create_graph(
        root,
        {
        'is_connected': i_rng.is_connected,
        'get_type_graphe': i_rng.get_type_graphe,
        },
        None,
        graph_name = i_rng.get_type_graphe()
    )
