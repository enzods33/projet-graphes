from interface_graphique.creer_graph import create_graph
from graphes.unit_disk_graph import interactions_unit_disk_graph as i_udg
from interface_graphique.ui.boutons import add_plus_minus_buttons
from outils_canva.constantes import RAYON_MODIFICATION

def open_unit_disk_graph_canvas(root):
    """créé le graphe en enregistrant les carcateristiques propres a ce graphe"""
    create_graph(
        root,
        {
            'is_connected': i_udg.is_connected,
            'get_graph_type': i_udg.get_graph_type,
            'get_parameters': i_udg.get_parameters,
            'set_parameters': i_udg.set_parameters,
            'reset': i_udg.specific_reset,
        },
        ajouter_boutons_specifiques=lambda frame_buttons: add_plus_minus_buttons(
            frame_buttons,
            lambda: i_udg.adjust_radius(RAYON_MODIFICATION),
            lambda: i_udg.adjust_radius(-RAYON_MODIFICATION),
            i_udg.get_radius,
            i_udg.set_lbl_rayon
        ),
        graph_name = i_udg.get_graph_type()
    )
