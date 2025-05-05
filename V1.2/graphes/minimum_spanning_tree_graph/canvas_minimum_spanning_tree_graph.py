from interface_graphique.creer_graph import create_graph
from graphes.minimum_spanning_tree_graph import interactions_minimum_spanning_tree_graph as i_mstg

def open_minimum_spanning_tree_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""

    create_graph(
        root,
        {
        'is_connected': i_mstg.is_connected,
        'get_graph_type': i_mstg.get_graph_type,
        },
        None,
        graph_name = i_mstg.get_graph_type()
    )
