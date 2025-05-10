from graphes.yao_4_linfity_graph import interactions_yao_4_linfity_graph as i_y4l
from interface_graphique.creer_graph import create_graph

def open_yao_4_linfity_graph_canvas(root):
    create_graph(
        root,
        {
            'is_connected': i_y4l.is_connected,
            'get_graph_type': i_y4l.get_graph_type,
            # 'get_parameters': i_y4l.get_parameters,  # Décommente si tu ajoutes paramètres
            # 'set_parameters': i_y4l.set_parameters,
        }
    )
