"""
Module de gestion et de mise à jour de l'état graphique du canevas.
"""

from interface_graphique import interactions_canvas as ic

def apply_graph_state(points, facteur_global, parametres=None, scroll_x=0, scroll_y=0):
    """
    Recharge complètement un graphe :
    - reset le canvas
    - crée les points
    - applique le facteur de zoom
    - applique les paramètres spécifiques
    - repositionne la vue si besoin
    """

    ic.reset()

    # Appliquer le facteur de zoom global
    ic.apply_intial_global_factor(facteur_global)

    # Créer les points avec facteur_global appliqué
    for x, y in points:
        # Appliquer le facteur de zoom aux coordonnées
        x_zoom = x * facteur_global
        y_zoom = y * facteur_global

        # Créer le point sur le canevas
        point = ic.create_point(x_zoom, y_zoom)  # Vérifier si cette méthode crée correctement les points
        ic.sommets.append(point)

    # Appliquer les paramètres spécifiques au graphe (si nécessaire)
    ic.apply_parameters_if_posible(parametres)
    
    # Mettre à jour les arêtes (si nécessaire)
    ic.update_edge()

    # On force Tkinter à finir d'afficher le canvas tout de suite (taille, scrollregion, etc.)
    # Sinon, il attend la prochaine boucle mainloop() pour le faire,
    # et les scrolls (xview_scroll/yview_scroll) ne marchent pas encore si le canvas vient juste d'être créé.
    ic.canva.update_idletasks()

    # Appliquer la position de scroll sauvegardée pour centrer la vue
    if scroll_x != 0:
        ic.canva.xview_scroll(scroll_x, "units")
    if scroll_y != 0:
        ic.canva.yview_scroll(scroll_y, "units")

    # Mettre à jour les variables de défilement
    ic.unite_scroll_x = scroll_x
    ic.unite_scroll_y = scroll_y