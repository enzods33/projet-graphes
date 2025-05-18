#L'interface graphique

from interface_graphique.interface_graphe import build_graph_interface
from interface_graphique.ui.boutons_graphes import add_plus_minus_buttons
from interface_graphique import interactions_canvas as ic
from outils_canva.constantes import RAYON_MODIFICATION_Udg, RAYON_PAR_DEFAUT_Udg, RAYON_MAX_Udg

def open_unit_disk_graph(root):
    build_graph_interface(
        root,
        {
            'is_connected': is_connected,
            'get_graph_type': get_graph_type,
            'get_parameters': get_parameters,
            'set_parameters': set_parameters,
            'reset': reset_radius_unit_disk_graph,
        },
        ajouter_boutons_specifiques=lambda frame_buttons: add_plus_minus_buttons(
            frame_buttons,
            lambda: adjust_radius(RAYON_MODIFICATION_Udg),
            lambda: adjust_radius(-RAYON_MODIFICATION_Udg),
            get_radius_label_text,
            set_radius_label_widget
        ),
        graph_name=get_graph_type()
    )

#Fonctions d'intégration du graphe

rayon_affiche = RAYON_PAR_DEFAUT_Udg
lbl_rayon = None

def get_graph_type():
    return "Unit disk graph"

def get_parameters():
    return {"rayon": rayon_affiche}

def set_parameters(parametres):
    global rayon_affiche
    rayon_affiche = parametres.get("rayon", RAYON_PAR_DEFAUT_Udg)
    update_radius_label()

def reset_radius_unit_disk_graph():
    global rayon_affiche
    rayon_affiche = RAYON_PAR_DEFAUT_Udg
    update_radius_label()

#Contrôle de rayon et affichage du label

def adjust_radius(delta):
    global rayon_affiche
    nouveau_rayon = rayon_affiche + delta
    if 10 <= nouveau_rayon <= RAYON_MAX_Udg:
        rayon_affiche = nouveau_rayon
        update_radius_label()
        ic.redraw_canvas()

def get_radius_label_text():
    return f"Rayon : {round(rayon_affiche)}"

def update_radius_label():
    if lbl_rayon and lbl_rayon.winfo_exists():
        lbl_rayon.config(text=get_radius_label_text())

def set_radius_label_widget(label):
    global lbl_rayon
    lbl_rayon = label
    update_radius_label()

#Algorithme principal du graphe Unit Disk

def is_connected(point1, point2):
    return ic.get_real_distance(point1, point2) <= rayon_affiche