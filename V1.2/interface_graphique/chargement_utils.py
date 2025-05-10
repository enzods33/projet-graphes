"""
Module de gestion et de mise à jour de l'état graphique du canevas.
"""

from interface_graphique import interactions_canvas as ic

def apply_graph_state(points, facteur_global, parametres=None, scroll_x=0, scroll_y=0):
    """
    Recharge complètement l'état d'un graphe dans l'interface.

    Cette fonction :
    - Réinitialise complètement le canvas et les variables internes.
    - Applique le facteur de zoom global sauvegardé.
    - Recharge tous les sommets à partir de leurs coordonnées logiques (non zoomées).
    - Applique les paramètres spécifiques du graphe (ex: rayon, k, etc.) si disponibles.
    - Redessine tous les points et arêtes avec l'échelle du zoom appliqué.
    - Recalcule et ajuste correctement la zone de défilement (scrollregion) en fonction du zoom.
    - Restaure la position de la vue sauvegardée (scroll_x et scroll_y) pour retrouver la caméra initiale.

    Paramètres :
        points (list[tuple[float, float]]): Liste des sommets à recharger.
        facteur_global (float): Facteur de zoom global à appliquer.
        parametres (dict, optionnel): Paramètres spécifiques du graphe.
        scroll_x (int, optionnel): Position horizontale du scroll à restaurer.
        scroll_y (int, optionnel): Position verticale du scroll à restaurer.
    """
    ic.reset()
    ic.apply_intial_global_factor(facteur_global)
    ic.sommets = [(x, y) for (x, y) in points]
    ic.apply_parameters_if_posible(parametres)
    ic.redraw_canvas()
    ic.refresh_scrollregion()
    ic.canva.xview_moveto(scroll_x)
    ic.canva.yview_moveto(scroll_y)