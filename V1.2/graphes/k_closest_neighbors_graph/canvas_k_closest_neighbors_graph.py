from interface_graphique.creer_graph import creer_graph
from graphes.k_closest_neighbors_graph import interactions_k_closest_neighbors_graph as i_kcng

def ouvrir_canvas_k_closest_neighbors_graph(root):
    creer_graph(root, {
        'is_connected': i_kcng.is_connected,
        'get_type_graphe': i_kcng.get_type_graphe,
    })
