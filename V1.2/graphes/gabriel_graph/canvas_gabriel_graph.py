from interface_graphique.creer_graph import create_graph
from graphes.gabriel_graph import interactions_gabriel_graph as i_gg

def open_gabriel_graph_canvas(root):
    create_graph(
        root,
        {
        'is_connected': i_gg.is_connected,
        'get_type_graphe': i_gg.get_type_graphe,
        },
        None,
        graph_name = i_gg.get_type_graphe()
    )
