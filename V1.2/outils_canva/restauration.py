"""
Module de restauration de l'état d'un graphe sur le canevas Tkinter. Il permet de recharger un état complet
sauvegardé d'un graphe (positions, zoom, paramètres, vue).
Ce module n'a aucune dépendance vis-à-vis de la structure de fenêtre Tkinter (pas de Frame ou Button).
"""
from interface_graphique import interactions_canvas as ic

def apply_graph_state(points, facteur_global, parametres=None, scroll_x=0, scroll_y=0):
    """
    Cette fonction effectue les opérations suivantes :
    - Réinitialise le canvas et les structures internes.
    - Applique le zoom global.
    - Recharge les sommets (points).
    - Applique les paramètres spécifiques du graphe.
    - Redessine les éléments graphiques.
    - Restaure la position de la vue (scroll).
    """
    ic.reset()
    ic.apply_intial_global_factor(facteur_global)
    ic.sommets.points = [(x, y) for (x, y) in points]
    ic.apply_parameters_if_possible(parametres)
    ic.redraw_canvas()
    ic.refresh_scrollregion()
    ic.canvas_init.canva.xview_moveto(scroll_x)
    ic.canvas_init.canva.yview_moveto(scroll_y)