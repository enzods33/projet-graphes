import interface_graphique.interactions_canvas as ic
import outils_canva.fonction_math as fm
import tkinter as tk

rayon = 100
lbl_rayon = None

def left_click(event):
    """
    Gère le clic gauche sur le canvas.

    Ajoute un point à la position cliquée et crée les arêtes avec les sommets voisins,
    selon le rayon courant. Ce point est aussi ajouté à la liste globale des sommets.
    
    Paramères :
        event : événement Tkinter contenant les coordonnées du clic.
    """
    global rayon
    point = ic.create_point(event.x, event.y)
    create_edges(point, rayon)
    ic.sommets.append(point)

def create_edges(new_point, rayon):
    """
    Crée des arêtes entre un nouveau point et les points existants proches.

    Deux points sont connectés par une arête si la distance entre eux est inférieure
    au rayon donné.

    Paramètres :
        new_point : identifiant du point nouvellement créé sur le canvas.
        rayon : distance maximale pour créer une arête.
    """
    new_coords = ic.canva.coords(new_point)
    new_center = fm.get_center(new_coords)
    nearby_points = fm.find_nearby_points(new_center, ic.sommets, ic.canva.coords, rayon)

    for som in nearby_points:
        som_coords = ic.canva.coords(som)
        som_center = fm.get_center(som_coords)
        ic.canva.create_line(new_center[0], new_center[1], som_center[0], som_center[1], fill="yellow", width=2)

def reafficher_les_arêtes():
    """
    Recalcule et réaffiche toutes les arêtes en fonction du rayon courant.

    Supprime d'abord toutes les arêtes actuelles (lignes sur le canvas),
    puis recrée celles qui respectent la condition de proximité.
    """
    global rayon
    for item in ic.canva.find_all():
        if ic.canva.type(item) == "line":
            ic.canva.delete(item)

    for point in ic.sommets:
        create_edges(point, rayon)

def augmenter_rayon(event=None):
    """
    Augmente le rayon de connexion de 10 unités.

    Met à jour l'affichage du label de rayon et redessine les arêtes.
    
    Paramètres :
        event : paramètre optionnel pour compatibilité avec les binds clavier.
    """
    global rayon
    rayon += 10
    maj_label()
    reafficher_les_arêtes()

def diminuer_rayon(event=None):
    """
    Diminue le rayon de connexion de 10 unités, sans descendre en dessous de 10.

    Met à jour le label et redessine les arêtes en conséquence.

    Paramètres :
        event : paramètre optionnel pour compatibilité avec les binds clavier.
    """
    global rayon
    if rayon > 10:
        rayon -= 10
        maj_label()
        reafficher_les_arêtes()

def maj_label():
    """
    Met à jour le label affichant la valeur du rayon courant sur l'interface.
    
    Ne fait rien si le label n'a pas encore été créé.
    """
    if lbl_rayon:
        lbl_rayon.config(text=f"Rayon : {rayon}")

def reset_specifique():
    """
    Réinitialise le rayon à sa valeur par défaut (100) et met à jour le label.
    """
    global rayon
    rayon = 100
    maj_label()

def add_controls(frame):
    """
    Ajoute les contrôles spécifiques au graphe UDG dans un frame d'interface.

    Ajoute :
    - un bouton "+" pour augmenter le rayon,
    - un bouton "-" pour le diminuer,
    - un bouton "Reset" pour réinitialiser le rayon et les points.

    Paramètres :
        frame : le conteneur Tkinter dans lequel les boutons seront placés.
    """
    global lbl_rayon
    # Boutons +/-
    frame_pm = tk.Frame(frame, bg="#f0f0f0")
    frame_pm.pack(pady=10)

    btn_plus = tk.Button(frame_pm, text="+", command=augmenter_rayon)
    btn_plus.pack(side=tk.RIGHT, padx=5)

    lbl_rayon = tk.Label(frame_pm, text=f"Rayon : {rayon}", bg="#f0f0f0")
    lbl_rayon.pack(side=tk.RIGHT)

    btn_moins = tk.Button(frame_pm, text="-", command=diminuer_rayon)
    btn_moins.pack(side=tk.RIGHT, padx=5)

    # Bouton reset
    btn_reset = tk.Button(frame, text="Reset", command=lambda: [ic.reset(), reset_specifique()])
    btn_reset.pack(pady=10)