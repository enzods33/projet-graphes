import tkinter as tk
from tkinter import filedialog, messagebox
import interface_graphique.interactions_canvas as ic
import utils.fonction_math as fm

def ajouter_menu_fichier(root):
    """
    Ajoute un menu 'Fichier' avec options de sauvegarde et chargement.
    """
    def sauvegarder_points():
        """
        Sauvegarde les coordonnées des sommets dans un fichier texte.
        Chaque ligne contiendra : x y
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
        Charge un fichier texte contenant des points au format : x y (un point par ligne).
        Recrée les sommets sur le canvas et met à jour les arêtes si besoin.
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