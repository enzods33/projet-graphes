from interface_graphique.creer_graph import creer_graph
from graphes.urquhart_graph import interactions_urquhart_graph as i_ug

def ouvrir_canvas_urquhart_graph(root):
    creer_graph(root, {
        'is_connected': i_ug.is_connected,
        'get_type_graphe': i_ug.get_type_graphe,
    })
