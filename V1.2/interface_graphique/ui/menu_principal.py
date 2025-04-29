import tkinter as tk
from graphes import graphes_disponibles
from interface_graphique import interactions_canvas as ic
from outils_canva.gestion_fichier import charger_graphe
from interface_graphique.ui.boutons import ajouter_bouton_nuage_aleatoire
from interface_graphique.chargement_utils import appliquer_etat_graphe

etat_chargement = {
    "points": [],
    "type": None,
    "parametres": {},
    "facteur_global": 1.0,
}
frame_contenu = None

def ouvrir_menu(root):
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
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Charger un fichier", command=lambda: action_charger_fichier(root))
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def setup_interface_selection(parent):
    global frame_menu, listbox

    frame_principal = tk.Frame(parent, bg="#f0f0f0")  
    frame_principal.pack(fill=tk.BOTH, expand=True)

    frame_menu = tk.Frame(frame_principal, bg="#f0f0f0")  
    frame_menu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16), bg="#f0f0f0") 
    titre.pack(pady=10)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 14), bg="#f0f0f0", highlightthickness=0, borderwidth=0) 
    for nom in graphes_disponibles.keys():
        listbox.insert(tk.END, nom)
    listbox.pack(fill=tk.BOTH, expand=True)

    btn_choisir = tk.Button(frame_menu, text="Choisir", command=lambda: choisir_graphe(parent.winfo_toplevel()))
    btn_choisir.pack(pady=10)

    # Frame pour les boutons à droite
    frame_boutons = tk.Frame(frame_principal, bg="#f0f0f0")
    frame_boutons.pack(side=tk.RIGHT, fill=tk.Y, padx=20, pady=20)

    ajouter_bouton_nuage_aleatoire(frame_boutons)

def action_charger_fichier(root):
    type_graphe, facteur_global, parametres, points = charger_graphe()

    if type_graphe is None:
        return

    etat_chargement["points"] = points
    etat_chargement["type"] = type_graphe
    etat_chargement["parametres"] = parametres
    etat_chargement["facteur_global"] = facteur_global

    reponse = tk.messagebox.askyesno(
        "Ouvrir avec le graphe d'origine ?",
        f"Le fichier chargé correspond au graphe {type_graphe}.\n\nVoulez-vous l'ouvrir directement ?"
    )

    if reponse:
        ouvrir_graphe_origine(root)

def ouvrir_graphe_origine(root):
    global frame_contenu

    type_graphe = etat_chargement["type"]
    points = etat_chargement["points"]
    parametres = etat_chargement["parametres"]
    facteur_global = etat_chargement["facteur_global"]

    if type_graphe in graphes_disponibles:
        if frame_contenu:
            frame_contenu.destroy()
            frame_contenu = None

        graphes_disponibles[type_graphe](root)
        appliquer_etat_graphe(points, facteur_global, parametres)
        reset_etat_chargement()
    else:
        tk.messagebox.showerror("Erreur", f"Graphe inconnu : {type_graphe}")

def choisir_graphe(root):
    global frame_contenu

    selection = listbox.curselection()
    if selection:
        nom = listbox.get(selection[0])

        if frame_contenu:
            frame_contenu.destroy()
            frame_contenu = None 

        graphes_disponibles[nom](root)

        appliquer_etat_graphe(
            etat_chargement["points"],
            etat_chargement["facteur_global"],
            etat_chargement["parametres"],
        )

        reset_etat_chargement()

def reset_etat_chargement():
    """
    Réinitialise complètement l'état de chargement temporaire.
    """
    etat_chargement["points"] = []
    etat_chargement["type"] = None
    etat_chargement["parametres"] = {}
    etat_chargement["facteur_global"] = 1.0