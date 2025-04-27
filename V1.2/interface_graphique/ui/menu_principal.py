import tkinter as tk
from tkinter import messagebox
from graphes import graphes_disponibles
from outils_canva.gestion_fichier import charger_graphe
import interface_graphique.interactions_canvas as ic
from outils_canva.generateur_nuage import generer_nuage_aleatoire
from outils_canva.saisie_utilisateur import demander_float, demander_intervalle

# Variables globales pour stocker l'état chargé
points_charges = []
type_graphe_charge = None
parametres_charges = None

def ouvrir_menu(root):
    global points_charges, type_graphe_charge, parametres_charges, frame_boutons

    # Réinitialiser l'affichage de la fenêtre principale
    for widget in root.winfo_children():
        widget.destroy()
    root.config(menu=None)

    # Menu fichier
    setup_menu(root)

    # Créer l'interface de sélection de graphe
    setup_interface_selection(root)

    # Créer un frame pour les boutons
    frame_boutons = tk.Frame(root)
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    # Ajouter tous les boutons dans le frame (par exemple le bouton "Générer un nuage")
    ajouter_bouton_nuage_aleatoire(frame_boutons) 

def setup_menu(root):
    """
    Crée et configure la barre de menu, avec les options 'Fichier' et 'Quitter'.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Charger un fichier", command=lambda: action_charger_fichier(root))
    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def setup_interface_selection(root):
    """
    Crée l'interface de sélection de graphe, avec une liste de graphes disponibles.
    """
    global frame_menu, listbox

    frame_menu = tk.Frame(root)
    frame_menu.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    titre = tk.Label(frame_menu, text="Choisissez un type de graphe :", font=("Helvetica", 16))
    titre.pack(pady=10)

    listbox = tk.Listbox(frame_menu, font=("Helvetica", 14))
    noms_graphes = list(graphes_disponibles.keys())
    for nom in noms_graphes:
        listbox.insert(tk.END, nom)
    listbox.pack(fill=tk.BOTH, expand=True)

    btn_choisir = tk.Button(frame_menu, text="Choisir", command=lambda: choisir_graphe(root))
    btn_choisir.pack(pady=10)

def action_charger_fichier(root):
    """
    Action de chargement depuis le menu principal.
    Charge un fichier JSON, propose d'ouvrir directement, sinon stocke pour plus tard.
    """
    charger_graphe(lambda type_graphe, parametres, points: callback_chargement(root, type_graphe, parametres, points))

def callback_chargement(root, type_graphe, parametres, points):
    """
    Callback appelé après le chargement du fichier JSON.
    Stocke les informations et demande si l'utilisateur veut ouvrir directement avec le graphe d'origine.
    """
    global points_charges, type_graphe_charge, parametres_charges

    points_charges = points
    type_graphe_charge = type_graphe
    parametres_charges = parametres

    reponse = messagebox.askyesno(
        "Ouvrir avec le graphe d'origine ?",
        f"Le fichier est un {type_graphe}.\nVoulez-vous l'ouvrir avec ce graphe ?"
    )
    if reponse:
        ouvrir_graphe_origine(root, type_graphe, parametres_charges, points_charges)

def ouvrir_graphe_origine(root, type_graphe, parametres, points):
    """
    Ouvre directement le graphe d'origine avec les paramètres chargés.
    """
    if type_graphe in graphes_disponibles:
        frame_menu.destroy()
        graphes_disponibles[type_graphe](root, points=points)
        ic.appliquer_parametres_si_disponible(parametres)
    else:
        messagebox.showerror("Erreur", f"Graphe inconnu : {type_graphe}")

def choisir_graphe(root):
    """
    Lance le graphe choisi par l'utilisateur dans la liste.
    Applique les paramètres si c'est le graphe d'origine chargé.
    """
    global points_charges, type_graphe_charge, parametres_charges

    selection = listbox.curselection()
    if selection:
        nom = listbox.get(selection[0])
        frame_menu.destroy()

        graphes_disponibles[nom](root, points=points_charges if points_charges else None)

        if type_graphe_charge == nom:
            ic.appliquer_parametres_si_disponible(parametres_charges)

def ajouter_bouton_nuage_aleatoire(frame_boutons):
    """
    Ajoute un bouton permettant de générer un nuage de points aléatoires.
    """
    def generer_et_sauvegarder():
        largeur = 600
        hauteur = 600

        # Demander à l'utilisateur le nombre de points (en utilisant la fonction demander_points)
        npoints = demander_float("Combien de points voulez-vous générer ?", 100, min=1, max=min(largeur, hauteur))
        if npoints is None:
            return  # Si l'utilisateur annule, on ne fait rien

        # Demander les intervalles pour X et Y
        print("🔵 Paramètres pour X :")
        xmin, xmax = demander_intervalle(
            "Valeur minimale pour x : ",
            "Valeur maximale pour x : ",
            valeur_min_defaut=0,
            valeur_max_defaut=largeur,
            min_global=0,
            max_global=largeur
        )

        print("🟢 Paramètres pour Y :")
        ymin, ymax = demander_intervalle(
            "Valeur minimale pour y : ",
            "Valeur maximale pour y : ",
            valeur_min_defaut=0,
            valeur_max_defaut=hauteur,
            min_global=0,
            max_global=hauteur
        )

        # Appeler la fonction pour générer et sauvegarder le nuage
        generer_nuage_aleatoire(largeur, hauteur, npoints, xmin, xmax, ymin, ymax)

    # Créer un bouton qui appelle la fonction pour générer un nuage
    btn_nuage = tk.Button(frame_boutons, text="Générer un nuage", command=generer_et_sauvegarder)
    btn_nuage.pack(pady=20)