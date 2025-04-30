from interface_graphique.creer_graph import create_graph
from graphes.urquhart_graph import interactions_urquhart_graph as i_ug

def open_urquhart_graph_canvas(root):
    create_graph(
        root, 
        {
        'is_connected': i_ug.is_connected,
        'get_type_graphe': i_ug.get_type_graphe,
        }
    )
