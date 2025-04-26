"""
Module 'menu_fichier' : gère les opérations de sauvegarde et de chargement 
de points depuis un fichier texte.

Ajoute un menu 'Fichier' dans la fenêtre principale de l'application, avec :
- une option pour sauvegarder les sommets affichés sur le canvas,
- une option pour charger un nuage de points depuis un fichier .txt.
"""
import tkinter as tk
import interface_graphique.interactions_canvas as ic
from outils_canva.gestion_fichier import sauvegarder_points_dans_fichier, charger_fichier_points


def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' à la fenêtre principale Tkinter.

    Le menu propose deux options :
    - 'Sauvegarder' : convertit les sommets actuels du canvas en coordonnées (x, y) 
    et les enregistre dans un fichier texte sélectionné par l'utilisateur.
    - 'Charger' : importe un fichier texte contenant des coordonnées de points
    et affiche ces points sur le canvas.

    Paramètres :
        root : la fenêtre principale de l'application (objet Tkinter).
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    points = [ic.get_center(ic.canva.coords(point)) for point in ic.sommets]    #les coordonnées des sommets 
    menu_fichier.add_command(label="Sauvegarder", command=lambda: sauvegarder_points_dans_fichier(points))

    def charger_points():
        """
        Charge un fichier de points (.txt) et les affiche sur le canvas.

        Réinitialise le canvas, place les points et met à jour les arêtes si nécessaire.
        """
        def afficher_sur_canvas(points):
            ic.reset()
            for x, y in points:
                point = ic.create_point(x, y)
                ic.sommets.append(point)
            if ic.callbacks["update_edges"]:
                ic.callbacks["update_edges"]()
        charger_fichier_points(afficher_sur_canvas) 
    menu_fichier.add_command(label="Charger", command=charger_points)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)