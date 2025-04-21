"""
Module 'menu_fichier' : gère les opérations de sauvegarde et de chargement 
de points depuis un fichier texte.

Ajoute un menu 'Fichier' dans la fenêtre principale de l'application, avec :
- une option pour sauvegarder les sommets affichés sur le canvas,
- une option pour charger un nuage de points depuis un fichier .txt.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
import interface_graphique.interactions_canvas as ic
import outils_canva.fonction_math as fm

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
        Charge des points à partir d’un fichier texte.

        Le fichier doit contenir une ligne par point : x y
        Les lignes vides ou commençant par '#' sont ignorées.
        Les points sont recréés sur le canvas, et les arêtes mises à jour si nécessaire.
        """
        messagebox.showinfo(
            "Format attendu",
            "Le fichier doit contenir une ligne par point : x y\n\n"
            "Chaque ligne correspond à un sommet.\n"
            "Exemple :\n120 200\n150.5 180\n\n"
            "Les lignes vides et les lignes commençant par '#' sont ignorées."
        )        
        filepath = filedialog.askopenfilename(
            filetypes=[("Fichiers texte", "*.txt")],
            title="Charger un nuage de points"
        )
        if filepath:
            ic.reset()
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    x_str, y_str = line.split()
                    x, y = float(x_str), float(y_str)
                    point = ic.create_point(x, y)
                    ic.sommets.append(point)
            if ic.edge_update_function:
                ic.edge_update_function()

    # Création du menu
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)
    menu_fichier.add_command(label="Sauvegarder", command=sauvegarder_points)
    menu_fichier.add_command(label="Charger", command=charger_points)
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)