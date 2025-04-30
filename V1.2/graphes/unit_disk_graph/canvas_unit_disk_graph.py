from interface_graphique.creer_graph import create_graph
from graphes.unit_disk_graph import interactions_unit_disk_graph as i_udg
from interface_graphique.ui.boutons import add_udg_button
from outils_canva.constantes import RAYON_MODIFICATION

def open_unit_disk_graph_canvas(root):
    create_graph(
        root,
        {
            'is_connected': i_udg.is_connected,
            'get_type_graphe': i_udg.get_type_graphe,
            'get_parametres': i_udg.get_parametres,
            'set_parametres': i_udg.set_parametres,
            'reset': i_udg.reset_specifique,
        },
        ajouter_boutons_specifiques=lambda frame: add_udg_button(
            frame,
            augmenter_cb=lambda: i_udg.ajuster_rayon(RAYON_MODIFICATION),
            diminuer_cb=lambda: i_udg.ajuster_rayon(-RAYON_MODIFICATION),
            get_lbl_text=lambda: f"Rayon : {i_udg.get_rayon()}",
            set_lbl_rayon_cb=i_udg.set_lbl_rayon
        ),
        graph_name = i_udg.get_type_graphe()
    )
