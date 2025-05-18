"""
Module d'interface utilisateur pour la sélection et le chargement de graphes.
Gère l'affichage d'un menu de sélection de graphe.
"""

import tkinter as tk
from graphes import graphes_disponibles
from outils_canva.gestion_fichier import load_graph
from gen_nuage import explications
from outils_canva.restauration import apply_graph_state
from interface_graphique.ui.description_graphes import create_description_window, create_a_propos_window


# Variables globales
etat_chargement = {
    "points": [],
    "type": None,
    "parametres": {},
    "facteur_global": 1.0,
    "scroll_x": 0.5,
    "scroll_y": 0.5
}
frame_contenu = None

# Fonctions principales du menu
def open_menu(root):
    """Ouvre le menu principal de sélection de graphe."""
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
    """Configure la barre de menu avec l'option pour charger un fichier."""
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Charger un fichier", command=lambda: load_file_action(root))
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def setup_interface_selection(parent):
    """Construit l'interface pour permettre à l'utilisateur de sélectionner un type de graphe."""
    global frame_menu, listbox

    frame_menu = tk.Frame(parent, bg="#f0f0f0")
    frame_menu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16), bg="#f0f0f0")
    titre.pack(pady=15, expand=True)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 15), bg="#f0f0f0", justify="center", height=len(graphes_disponibles))
    for nom in graphes_disponibles.keys():
        listbox.insert(tk.END, nom)
    listbox.pack(pady=10, ipadx=30, expand=True)

    btn_choisir = tk.Button(frame_menu, text="Choisir", font=("Helvetica", 12), command=lambda: select_graph(parent.winfo_toplevel()))
    btn_choisir.pack(expand=True)

    btn_nuage = tk.Button(frame_menu, text="Générer un nuage", command=explications, font=("Helvetica", 12))
    btn_nuage.pack( expand=True)

    btn_description = tk.Button(frame_menu, text="Description", font=("Helvetica", 12), command=lambda: give_infos(parent.winfo_toplevel()))
    btn_description.pack( expand=True)

    btn_a_propos = tk.Button(frame_menu, text="A propos", font=("Helvetica", 12), command=lambda: create_a_propos_window(parent.winfo_toplevel()))
    btn_a_propos.pack(side='bottom', expand=True)

# Gestion des actions de chargement
def load_file_action(root):
    """Charge un graphe depuis un fichier et propose de l'ouvrir dans son type d'origine."""
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
    else:
        reponse = tk.messagebox.askyesno(
            "Ouvrir avec le graphe d'origine ?",
            f"Le fichier chargé correspond au graphe {type_graphe}.\n\nVoulez-vous l'ouvrir directement ?"
        )

        if reponse:
            open_original_graph(root)

def open_original_graph(root):
    """Ouvre le graphe sauvegardé en utilisant son type d'origine si possible."""
    global frame_contenu

    type_graphe = etat_chargement["type"]
    points = etat_chargement["points"]
    parametres = etat_chargement["parametres"]
    facteur_global = etat_chargement["facteur_global"]
    scroll_x = etat_chargement["scroll_x"]
    scroll_y = etat_chargement["scroll_y"]

    if frame_contenu:
        frame_contenu.destroy()
        frame_contenu = None

    graphes_disponibles[type_graphe](root)
    apply_graph_state(points, facteur_global, parametres, scroll_x, scroll_y)
    reset_loading_state()

def select_graph(root):
    """Ouvre l'interface pour le graphe sélectionné par l'utilisateur."""
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

def give_infos(root):
    """Ouvre une fenêtre affichant la description du graphe sélectionné."""
    selection = listbox.curselection()
    if not selection:
        tk.messagebox.showinfo("Information", "Veuillez sélectionner un graphe dans la liste.")
        return

    nom_graphe = listbox.get(selection[0])

    create_description_window(root, nom_graphe)


def reset_loading_state():
    """Réinitialise complètement l'état de chargement temporaire."""
    etat_chargement["points"] = []
    etat_chargement["type"] = None
    etat_chargement["parametres"] = {}
    etat_chargement["facteur_global"] = 1.0
    etat_chargement["scroll_x"] = 0.5
    etat_chargement["scroll_y"] = 0.5