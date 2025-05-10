from interface_graphique.creer_graph import create_graph
from graphes.theta_graph import interactions_theta_graph as i_tg
from interface_graphique.ui.boutons import add_theta_button

def open_theta_graph_canvas(root):
    create_graph(
        root,
        {
            'is_connected': i_tg.is_connected,
            'get_graph_type': i_tg.get_graph_type,
            'get_parameters': i_tg.get_parameters,
            'set_parameters': i_tg.set_parameters,
        },
        ajouter_boutons_specifiques = lambda frame: add_theta_button(
            frame,
            i_tg.augmenter_k,
            i_tg.diminuer_k,
            i_tg.get_lbl_text,
            i_tg.set_lbl_k
        ),
        graph_name=i_tg.get_graph_type()
    )
