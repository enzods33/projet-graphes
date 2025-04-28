import tkinter as tk

from graphes import graphes_disponibles
from interface_graphique import interactions_canvas as ic
from outils_canva.gestion_fichier import charger_graphe
from interface_graphique.ui.boutons import ajouter_bouton_nuage_aleatoire

# Etat global pour stocker les informations de chargement
etat_chargement = {
    "points": [],
    "type": None,
    "parametres": None
}

def ouvrir_menu(root):
    """
    Ouvre le menu principal : réinitialise la fenêtre, configure le menu, l'interface de sélection et les boutons.
    """
    for widget in root.winfo_children():
        widget.destroy()
    root.config(menu=None)

    setup_menu(root)
    setup_interface_selection(root)

def setup_menu(root):
    """
    Crée et configure la barre de menu, avec l'option 'Charger un fichier'.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Charger un fichier", command=lambda: action_charger_fichier(root))
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def setup_interface_selection(root):
    """
    Crée l'interface de sélection du type de graphe et les boutons secondaires.
    """
    global frame_menu, listbox

    frame_menu = tk.Frame(root)
    frame_menu.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16))
    titre.pack(pady=10)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 14))
    for nom in graphes_disponibles.keys():
        listbox.insert(tk.END, nom)
    listbox.pack(fill=tk.BOTH, expand=True)

    btn_choisir = tk.Button(frame_menu, text="Choisir", command=lambda: choisir_graphe(root))
    btn_choisir.pack(pady=10)

    frame_boutons = tk.Frame(root)
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    ajouter_bouton_nuage_aleatoire(frame_boutons)

def action_charger_fichier(root):
    """
    Action de chargement depuis le menu : ouvre un fichier JSON et traite son contenu.
    """
    charger_graphe(lambda type_graphe, parametres, points: callback_chargement(root, type_graphe, parametres, points))

def callback_chargement(root, type_graphe, parametres, points):
    """
    Callback appelé après le chargement d'un fichier JSON.
    """
    etat_chargement["points"] = points
    etat_chargement["type"] = type_graphe
    etat_chargement["parametres"] = parametres

    if type_graphe is None:
        tk.messagebox.showinfo(
            "Chargement réussi",
            f"Nuage de {len(points)} points chargé.\n\nAucun type de graphe détecté.\n\nVeuillez choisir manuellement le type de graphe."
        )
    else:
        reponse = tk.messagebox.askyesno(
            "Ouvrir avec le graphe d'origine ?",
            f"Le fichier est un {type_graphe}.\nVoulez-vous l'ouvrir avec ce graphe ?"
        )
        if reponse:
            ouvrir_graphe_origine(root, type_graphe, parametres, points)

def ouvrir_graphe_origine(root, type_graphe, parametres, points):
    """
    Ouvre directement le graphe d'origine avec les paramètres chargés.
    """
    if type_graphe in graphes_disponibles:
        frame_menu.destroy()
        graphes_disponibles[type_graphe](root, points=points)
        ic.appliquer_parametres_si_disponible(parametres)
    else:
        tk.messagebox.showerror("Erreur", f"Graphe inconnu : {type_graphe}")

def choisir_graphe(root):
    """
    Lance le graphe choisi par l'utilisateur dans la liste.
    """
    selection = listbox.curselection()
    if selection:
        nom = listbox.get(selection[0])
        frame_menu.destroy()

        # Réinitialiser les callbacks avant de charger le nouveau graphe
        ic.reset_callbacks()
        
        graphes_disponibles[nom](root, points=etat_chargement["points"] if etat_chargement["points"] else None)

        if etat_chargement["type"] == nom:
            ic.appliquer_parametres_si_disponible(etat_chargement["parametres"])

