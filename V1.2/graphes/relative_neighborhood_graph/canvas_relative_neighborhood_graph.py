from interface_graphique.creer_graph import creer_graph
from graphes.relative_neighborhood_graph import interactions_relative_neighborhood_graph as i_rng

def ouvrir_canvas_relative_neighborhood_graph(root):
    creer_graph(root, {
        'is_connected': i_rng.is_connected,
        'get_type_graphe': i_rng.get_type_graphe,
    })
