"""
Module de gestion et de mise à jour de l'état graphique du canevas.
"""

from interface_graphique import interactions_canvas as ic

def apply_graph_state(points, facteur_global, parametres=None, scroll_x=0, scroll_y=0):
    """
    Recharge complètement l'état d'un graphe dans l'interface.

    Cette fonction :
    - Réinitialise le canvas et l'état interne.
    - Applique le facteur de zoom global sauvegardé.
    - Recharge les sommets à partir des coordonnées logiques (x, y).
    - Applique les paramètres spécifiques du graphe (ex: rayon, k, etc).
    - Redessine tous les sommets et arêtes avec les paramètres mis à jour.
    - Recentre la vue et restaure la position de défilement sauvegardée.

    Paramètres :
        points (list[tuple[float, float]]): Liste des sommets à recharger.
        facteur_global (float): Facteur de zoom global à appliquer.
        parametres (dict, optionnel): Paramètres spécifiques du graphe.
        scroll_x (int, optionnel): Position horizontale du scroll à restaurer.
        scroll_y (int, optionnel): Position verticale du scroll à restaurer.
    """

    ic.reset()

    # Appliquer le facteur de zoom global
    ic.apply_intial_global_factor(facteur_global)

    # Charger les points logiques directement
    ic.sommets = [(x, y) for (x, y) in points]

    # Appliquer les paramètres spécifiques au graphe (si nécessaire)
    ic.apply_parameters_if_posible(parametres)

    # Redessiner tous les points et toutes les arêtes
    ic.redraw_canvas()

    # Forcer la mise à jour graphique immédiate
    ic.canva.update_idletasks()

    # Appliquer la position de scroll sauvegardée pour centrer la vue
    if scroll_x != 0:
        ic.canva.xview_scroll(scroll_x, "units")
    if scroll_y != 0:
        ic.canva.yview_scroll(scroll_y, "units")

    # Mettre à jour les variables de défilement internes
    ic.unite_scroll_x = scroll_x
    ic.unite_scroll_y = scroll_y