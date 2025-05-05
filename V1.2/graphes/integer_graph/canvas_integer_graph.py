from interface_graphique.creer_graph import create_graph
from graphes.integer_graph import interactions_integer_graph as i_ig

def open_integer_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""

    create_graph(
        root,
        {
        'is_connected': i_ig.is_connected,
        'get_graph_type': i_ig.get_graph_type,
        },
        None,
        graph_name = i_ig.get_graph_type()
    )
