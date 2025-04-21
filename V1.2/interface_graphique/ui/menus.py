"""
Module 'menu_fichier' : gère les opérations de sauvegarde et de chargement 
de points depuis un fichier texte.

Ajoute un menu 'Fichier' dans la fenêtre principale de l'application, avec :
- une option pour sauvegarder les sommets affichés sur le canvas,
- une option pour charger un nuage de points depuis un fichier .txt.
"""
import tkinter as tk
from tkinter import filedialog
import interface_graphique.interactions_canvas as ic
import outils_canva.fonction_math as fm
from interface_graphique.ui.chargement import charger_fichier_points


def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' à la fenêtre Tkinter principale.

    Ce menu contient deux options :
    - 'Sauvegarder' : enregistre les sommets actuels dans un fichier texte.
    - 'Charger' : importe un fichier texte contenant des coordonnées de points.
    
    Paramètres :
        root : la fenêtre principale de l'application (objet Tkinter).
    """
    def sauvegarder_points():
        """
        Sauvegarde les coordonnées actuelles des sommets dans un fichier texte.
        
        Chaque ligne contient les coordonnées x y du centre d'un point.
        Le fichier est enregistré via une boîte de dialogue.
        """
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichier texte", "*.txt")]
        )
        if filepath:
            with open(filepath, "w") as f:
                for point in ic.sommets:
                    cx, cy = fm.get_center(ic.canva.coords(point))
                    f.write(f"{cx} {cy}\n")

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

    # Création du menu
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)
    menu_fichier.add_command(label="Sauvegarder", command=sauvegarder_points)
    menu_fichier.add_command(label="Charger", command=charger_points)
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)