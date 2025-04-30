from interface_graphique.creer_graph import create_graph
from graphes.integer_graph import interactions_integer_graph as i_ig

def open_integer_graph_canvas(root):
    create_graph(
        root,
        {
        'is_connected': i_ig.is_connected,
        'get_type_graphe': i_ig.get_type_graphe,
        },
        None,
        graph_name = i_ig.get_type_graphe()
    )
