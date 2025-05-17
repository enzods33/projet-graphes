"""
Module canvas_init.py

Responsable de l'initialisation du canvas, de la gestion des callbacks,
et de la remise à zéro complète du graphe.
"""

# Variables globales du canvas et des callbacks
canva = None
callbacks = {
    "reset": None,
    "is_connected": None,
    "get_parameters": None,
    "set_parameters": None,
    "get_graph_type": None,
}
label_compteur = None
label_facteur_zoom = None

def set_canvas(canvas):
    """Associe le canvas principal aux interactions."""
    global canva
    canva = canvas

def save_callback(nom, fonction):
    """Enregistre un callback spécifique (connexion, paramètres, reset, etc.)."""
    callbacks[nom] = fonction

def reset_callbacks():
    """Réinitialise tous les callbacks enregistrés."""
    for key in callbacks:
        callbacks[key] = None

def reset():
    """Réinitialise complètement le canvas, les points, le zoom, la position, et les labels."""
    from interface_graphique.interactions_canvas import sommets, zoom, cache_distance

    sommets.points.clear()
    sommets.facteur_global = 1.0
    if canva:
        canva.delete("all")
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)
        zoom.refresh_scrollregion()

    if label_compteur and label_compteur.winfo_exists():
        label_compteur.config(text="Sommets : 0\nArêtes : 0")
    if label_facteur_zoom and label_facteur_zoom.winfo_exists():
        label_facteur_zoom.config(text="Zoom : x1.00")

    cache_distance.distance_cache.clear()

    if callbacks["reset"]:
        callbacks["reset"]()

def set_counter_label(label):
    """Définit le label qui affiche le nombre de sommets/arêtes."""
    global label_compteur
    label_compteur = label

def set_zoom_label(label):
    """Définit le label qui affiche le facteur de zoom."""
    global label_facteur_zoom
    label_facteur_zoom = label

def full_reset_view():
    """Réinitialise complètement la vue : zoom à 1 et recentre le canvas."""
    from interface_graphique.interactions_canvas import sommets, zoom

    sommets.facteur_global = 1.0
    zoom.update_zoom_label()
    if canva:
        canva.xview_moveto(0.5)
        canva.yview_moveto(0.5)
    sommets.redraw_canvas()
    zoom.refresh_scrollregion()

def apply_parameters_if_possible(parametres):
    """Applique les paramètres sauvegardés si la fonction set_parameters est disponible."""
    if parametres and callbacks.get("set_parameters"):
        callbacks["set_parameters"](parametres)

def change_graph(root):
    """Change de graphe et réinitialise complètement le canvas."""
    from interface_graphique.ui import menu_principal as mp

    reset()
    set_canvas(None)

    for widget in root.winfo_children():
        widget.destroy()

    root.config(menu=None)

    mp.reset_loading_state()
    mp.open_menu(root)