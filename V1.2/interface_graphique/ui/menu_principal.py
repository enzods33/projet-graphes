"""
Module d'interface utilisateur pour la sélection et le chargement de graphes.
Gère l'affichage d'un menu de sélection de graphe
"""

import tkinter as tk
from graphes import graphes_disponibles
from outils_canva.gestion_fichier import load_graph
from gen_cloud import explications
from interface_graphique.chargement_utils import apply_graph_state

etat_chargement = {
    "points": [],
    "type": None,
    "parametres": {},
    "facteur_global": 1.0,
    "scroll_x": 0,
    "scroll_y": 0
}
frame_contenu = None

def open_menu(root):
    """ouvre le menu principal de selection de graphe"""
    global frame_contenu

    if frame_contenu:
        frame_contenu.destroy()
        frame_contenu = None 

    root.config(menu=None)

    setup_menu(root)

    frame_contenu = tk.Frame(root)
    frame_contenu.pack(fill=tk.BOTH, expand=True)

    setup_interface_selection(frame_contenu)

def setup_menu(root):
    """
    configure la barre de menu
    option pour charger un fichier
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Charger un fichier", command=lambda: load_file_action(root))
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def setup_interface_selection(parent):
    """
    construit l'interface pour permettre à l'utilisateur de sélectionner un type de graphe disponible
    Paramètre: parent: widget où placer les composants
    """
    global frame_menu, listbox

    frame_principal = tk.Frame(parent, bg="#f0f0f0")  
    frame_principal.pack(fill=tk.BOTH, expand=True)

    frame_menu = tk.Frame(frame_principal, bg="#f0f0f0")  
    frame_menu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16), bg="#f0f0f0") 
    titre.pack(pady=20)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 20), bg="#f0f0f0", justify="center") 
    for nom in graphes_disponibles.keys():
        listbox.insert(tk.END, nom)
    listbox.pack(pady=10, ipadx=30)

    btn_choisir = tk.Button(frame_menu, text="Choisir", font=("Helvetica", 12), command=lambda: select_graph(parent.winfo_toplevel()))
    btn_choisir.pack(pady=20)
    
    btn_nuage = tk.Button(frame_menu,text="Générer un nuage",command=explications,font=("Helvetica", 12))
    btn_nuage.pack()

def load_file_action(root):
    """charge un graphe depuis un fichier et propose de l'ouvrir dans son type d'origine"""
    type_graphe, facteur_global, parametres, points, scroll_x, scroll_y = load_graph()

    if type_graphe is None:
        return

    etat_chargement["points"] = points
    etat_chargement["type"] = type_graphe
    etat_chargement["parametres"] = parametres
    etat_chargement["facteur_global"] = facteur_global
    etat_chargement["scroll_x"] = scroll_x
    etat_chargement["scroll_y"] = scroll_y

    if type_graphe == "Nuage Aleatoire":
        tk.messagebox.showinfo(
            "Nuage aléatoire chargé",
            "Le graphe chargé est un nuage généré aléatoirement.\n\nVeuillez choisir un type de graphe pour le charger."
        )
        # Et on ne lance pas open_original_graph, car ce n'est pas un vrai graphe !

    else:
        reponse = tk.messagebox.askyesno(
            "Ouvrir avec le graphe d'origine ?",
            f"Le fichier chargé correspond au graphe {type_graphe}.\n\nVoulez-vous l'ouvrir directement ?"
        )

        if reponse:
            open_original_graph(root)

def open_original_graph(root):
    """ouvre le graphe précédemment chargé en utilisant son type d'origine si possible"""
    global frame_contenu

    type_graphe = etat_chargement["type"]
    points = etat_chargement["points"]
    parametres = etat_chargement["parametres"]
    facteur_global = etat_chargement["facteur_global"]
    scroll_x = etat_chargement["scroll_x"]
    scroll_y = etat_chargement["scroll_y"]

    if type_graphe in graphes_disponibles:
        if frame_contenu:
            frame_contenu.destroy()
            frame_contenu = None

        graphes_disponibles[type_graphe](root)
        apply_graph_state(points, facteur_global, parametres, scroll_x, scroll_y)
        reset_loading_state()
    else:
        tk.messagebox.showerror("Erreur", f"Graphe inconnu : {type_graphe}")

def select_graph(root):
    """ouvre l'interface pour le graphe séléctionné par l'utilisateur"""
    global frame_contenu

    selection = listbox.curselection()
    if selection:
        nom = listbox.get(selection[0])

        if frame_contenu:
            frame_contenu.destroy()
            frame_contenu = None 

        graphes_disponibles[nom](root)

        apply_graph_state(
            etat_chargement["points"],
            etat_chargement["facteur_global"],
            etat_chargement["parametres"],
            etat_chargement["scroll_x"],
            etat_chargement["scroll_y"],

        )

        reset_loading_state()

def reset_loading_state():
    """Réinitialise complètement l'état de chargement temporaire"""
    etat_chargement["points"] = []
    etat_chargement["type"] = None
    etat_chargement["parametres"] = {}
    etat_chargement["facteur_global"] = 1.0
    etat_chargement["scroll_x"] = 0
    etat_chargement["scroll_y"] = 0