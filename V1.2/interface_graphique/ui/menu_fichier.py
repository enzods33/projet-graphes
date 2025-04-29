import tkinter as tk
import interface_graphique.interactions_canvas as ic
from outils_canva.gestion_fichier import sauvegarder_graphe, charger_graphe
import outils_canva.geometrie as geo
from interface_graphique.chargement_utils import appliquer_etat_graphe

def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' avec options Sauvegarder et Charger.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Sauvegarder Graphe", command=action_sauvegarder_graphe)
    menu_fichier.add_command(label="Charger Graphe", command=action_charger_graphe)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def action_sauvegarder_graphe():
    """
    Sauvegarde l'état actuel du graphe dans un fichier JSON.
    """
    type_graphe = ic.callbacks["get_type_graphe"]()
    facteur_global = ic.facteur_global
    scroll_x_units = ic.scroll_x_units
    scroll_y_units = ic.scroll_y_units
    points = []
    for point in ic.sommets:
        coords = ic.canva.coords(point)
        center_x, center_y = geo.get_center(coords)

        real_x = center_x / facteur_global
        real_y = center_y / facteur_global

        points.append((real_x, real_y))

    parametres = ic.callbacks["get_parametres"]() if ic.callbacks.get("get_parametres") else {}

    sauvegarder_graphe(type_graphe, parametres, points, facteur_global, scroll_x_units, scroll_y_units)

def action_charger_graphe():
    type_graphe, facteur_global, parametres, points, scroll_x, scroll_y = charger_graphe()

    if type_graphe is None or not points:
        return

    appliquer_etat_graphe(points, facteur_global, parametres, scroll_x, scroll_y)
