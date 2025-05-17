"""
Module de création de l'interface graphique principale pour afficher et gérer un graphe.

Ce module définit la structure visuelle de l'application de visualisation de graphes :
- Création d'une fenêtre Tkinter avec un canevas scrollable pour dessiner les sommets et arêtes.
- Intégration des boutons de commande communs (zoom, réinitialisation, changement de graphe).
- Intégration des boutons spécifiques selon le graphe choisi.
- Liaison des événements souris (clic, drag, molette) pour l'interaction utilisateur.
- Ajout d'un menu Fichier permettant la sauvegarde et le chargement d'un graphe.
"""

import tkinter as tk
from interface_graphique import interactions_canvas as ic
from interface_graphique.ui.boutons_graphes import add_common_buttons
from interface_graphique.ui.description_graphes import create_description_window
from outils_canva.gestion_fichier import save_graph, load_graph
from outils_canva.restauration import apply_graph_state
from outils_canva.constantes import CANVAS_LARGEUR, CANVAS_HAUTEUR, CANVAS_COULEUR, SCROLLX1, SCROLLX2, SCROLLY1, SCROLLY2

def build_graph_interface(root, config_callbacks, ajouter_boutons_specifiques=None, graph_name=''):
    """
    Crée l'interface de graphe générique avec tous les éléments communs.
    Paramètres :
        root : fenêtre principale
        config_callbacks : dictionnaire {nom_callback: fonction}
        ajouter_boutons_specifiques : fonction(frame_boutons) -> ajoute les boutons spécifiques à ce graphe
        le nom du graphe
    """
    # Réinitialiser la fenêtre
    for widget in root.winfo_children():
        widget.destroy()

    # Frame principale générale
    frame_global = tk.Frame(root)
    frame_global.pack(fill=tk.BOTH, expand=True)

    # Frame pour la partie canvas + scrollbars
    frame_canvas = tk.Frame(frame_global)
    frame_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbars
    xscrollbar = tk.Scrollbar(frame_canvas, orient="horizontal")
    yscrollbar = tk.Scrollbar(frame_canvas, orient="vertical")

    # Canvas
    canvas = tk.Canvas(frame_canvas, width=CANVAS_LARGEUR, height=CANVAS_HAUTEUR,
                       background=CANVAS_COULEUR,
                       xscrollcommand=xscrollbar.set,
                       yscrollcommand=yscrollbar.set)
    canvas.config(scrollregion=(SCROLLX1, SCROLLY1, SCROLLX2, SCROLLY2))

    # Placement avec grid pour le canvas + scrollbars
    canvas.grid(row=0, column=0)
    xscrollbar.grid(row=1, column=0, sticky="ew")
    yscrollbar.grid(row=0, column=1, sticky="ns")

    # Configuration d'expansion
    frame_canvas.grid_rowconfigure(0, weight=1)
    frame_canvas.grid_columnconfigure(0, weight=1)

    # Définir le canvas pour l'interaction
    ic.set_canvas(canvas)

    # Frame pour les boutons à droite
    frame_boutons = tk.Frame(frame_global, bg="#f0f0f0")
    frame_boutons.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    if graph_name:
        label_graph = tk.Label(frame_boutons, text=f"Graphe: \n {graph_name}", font=("Helvetica", 8), bg="#f0f0f0")
        label_graph.pack()

    if ajouter_boutons_specifiques:
        ajouter_boutons_specifiques(frame_boutons)

    add_common_buttons(frame_boutons, root)

    btn_description = tk.Button(frame_boutons, text="Description", font=("Helvetica", 8), command=lambda: create_description_window(root, graph_name))
    btn_description.pack(side='bottom')

    # Lier les scrollbars
    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)

    # Menu fichier
    add_file_menu(root)

    for nom, fonction in config_callbacks.items():
        ic.save_callback(nom, fonction)

    # Événements souris
    canvas.bind('<Button-1>', ic.is_drag)
    canvas.bind('<Button-3>', ic.on_right_click)
    canvas.bind('<B1-Motion>', ic.on_drag_motion)
    canvas.bind('<ButtonRelease-1>', ic.on_drag_end)
    
def add_file_menu(root):
    """
    Ajoute un menu 'Fichier' avec options Sauvegarder et Charger.
    """
    menubar = tk.Menu(root)
    menu_fichier = tk.Menu(menubar, tearoff=0)

    menu_fichier.add_command(label="Sauvegarder Graphe", command=save_graph_action)
    menu_fichier.add_command(label="Charger Graphe", command=load_graph_action)

    menubar.add_cascade(label="Fichier", menu=menu_fichier)
    root.config(menu=menubar)

def save_graph_action():
    """
    Sauvegarde l'état actuel du graphe dans un fichier JSON.
    """
    type_graphe = ic.canvas_init.callbacks["get_graph_type"]()
    parametres = ic.canvas_init.callbacks["get_parameters"]() if ic.canvas_init.callbacks.get("get_parameters") else {}
    points = [(x, y) for (x, y) in ic.sommets.points]
    facteur_global = ic.sommets.facteur_global
    scroll_x_fraction = ic.canvas_init.canva.xview()[0] 
    scroll_y_fraction = ic.canvas_init.canva.yview()[0] 

    save_graph(type_graphe, parametres, points, facteur_global, scroll_x_fraction, scroll_y_fraction)

def load_graph_action():
    """charge un graphe sauvegardé depuis un fichier JSON"""
    type_graphe, facteur_global, parametres, points, scroll_x, scroll_y = load_graph()

    if type_graphe is None or not points:
        return None

    apply_graph_state(points, facteur_global, parametres, scroll_x, scroll_y)