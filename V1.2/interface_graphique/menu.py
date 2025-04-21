import tkinter as tk
from tkinter import filedialog
from graphes import graphes_disponibles

def ouvrir_menu(root):
    """
    Affiche le menu principal de sélection des graphes.

    Cette interface propose :
    - un menu pour charger un fichier de points,
    - une liste des types de graphes disponibles à lancer,
    - un bouton pour valider le choix.

    Paramètres :
        root : fenêtre principale Tkinter dans laquelle insérer le menu.
    """
    for widget in root.winfo_children():
        widget.destroy()
    root.config(menu=None)

    points_charges = []

    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    def charger_fichier():
        """
        Ouvre un fichier texte contenant des coordonnées de points (format : x y).

        Les lignes vides ou débutant par '#' sont ignorées.
        Les points valides sont stockés dans la liste locale 'points_charges',
        qui sera utilisée pour initialiser le graphe si l'utilisateur en sélectionne un ensuite.
        """
        nonlocal points_charges
        filepath = filedialog.askopenfilename(
            filetypes=[("Fichiers texte", "*.txt")],
            title="Charger un nuage de points"
        )
        if filepath:
            points_charges.clear()
            with open(filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    x_str, y_str = line.split()
                    x, y = float(x_str), float(y_str)
                    points_charges.append((x, y))

    menu_fichier.add_command(label="Charger un fichier", command=charger_fichier)
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

    frame_menu = tk.Frame(root)
    frame_menu.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16))
    titre.pack(pady=10)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 14))
    noms_graphes = list(graphes_disponibles.keys())
    for nom in noms_graphes:
        listbox.insert(tk.END, nom)
    listbox.pack(fill=tk.BOTH, expand=True)

    def choisir_graphe():
        """
        Lance l'affichage du graphe sélectionné dans la liste.

        Détruit le menu actuel, puis appelle la fonction 'ouvrir_canvas' du graphe choisi,
        en lui passant les points chargés s'il y en a.
        """
        selection = listbox.curselection()
        if selection:
            nom = listbox.get(selection[0])
            frame_menu.destroy()
            graphes_disponibles[nom](root, points=points_charges if points_charges else None)

    btn_choisir = tk.Button(frame_menu, text="Choisir", command=choisir_graphe)
    btn_choisir.pack(pady=10)