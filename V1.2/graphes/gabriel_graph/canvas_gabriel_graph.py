from interface_graphique.creer_graph import create_graph
from graphes.gabriel_graph import interactions_gabriel_graph as i_gg

def open_gabriel_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""

    create_graph(
        root,
        {
        'is_connected': i_gg.is_connected,
        'get_graph_type': i_gg.get_graph_type,
        },
        None,
        graph_name = i_gg.get_graph_type()
    )
