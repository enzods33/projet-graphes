"""
Module de gestion du menu Fichier pour l'application de graphe 
les fonction permettent: 
- l'ajout d'un menu 'Fichier' à l'interface principale.
- la sauvegarde de l'état du graphe dans un fichier JSON.
- le chargement d'un graphe (précédemment sauvegardé)dans son état de sauvegarde
"""

import tkinter as tk
import interface_graphique.interactions_canvas as ic
from outils_canva.gestion_fichier import save_graph, load_graph
import outils_canva.geometrie as geo
from interface_graphique.chargement_utils import apply_graph_state

def add_file_menu(root):
    """
    Ajoute un menu 'Fichier' avec options Sauvegarder et Charger.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Sauvegarder Graphe", command=save_graph_action)
    menu_fichier.add_command(label="Charger Graphe", command=load_graph_action)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def save_graph_action():
    """
    Sauvegarde l'état actuel du graphe dans un fichier JSON.
    """
    type_graphe = ic.callbacks["get_type_graphe"]()
    facteur_global = ic.facteur_global
    scroll_x_units = ic.unite_scroll_x
    scroll_y_units = ic.unite_scroll_y
    points = []
    for point in ic.sommets:
        coords = ic.canva.coords(point)
        center_x, center_y = geo.get_center(coords)

        real_x = center_x / facteur_global
        real_y = center_y / facteur_global

        points.append((real_x, real_y))

    parametres = ic.callbacks["get_parametres"]() if ic.callbacks.get("get_parametres") else {}

    save_graph(type_graphe, parametres, points, facteur_global, scroll_x_units, scroll_y_units)

def load_graph_action():
    """charge un graphe sauvegardé depuis un fichier JSON"""
    type_graphe, facteur_global, parametres, points, scroll_x, scroll_y = load_graph()

    if type_graphe is None or not points:
        return None

    apply_graph_state(points, facteur_global, parametres, scroll_x, scroll_y)
