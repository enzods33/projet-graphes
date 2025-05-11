from interface_graphique.creer_graph import create_graph
from graphes.urquhart_graph import interactions_urquhart_graph as i_ug

def open_urquhart_graph_canvas(root):
    """Crée le canvas pour le graphe Urquhart."""

    create_graph(
        root,
        {
            'is_connected': i_ug.is_connected,
            'get_graph_type': i_ug.get_graph_type,
            'reset': i_ug.reset_specific
        },
        graph_name=i_ug.get_graph_type(),
    )
