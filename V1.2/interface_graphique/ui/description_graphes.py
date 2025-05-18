import tkinter as tk
from outils_canva.constantes import MAX_NB_POINTS, RAYON_MIN_Udg, RAYON_MAX_Udg, K_MAX_Neighbors, K_MAX_Yao

def create_description_window(root, nom):
    description = texte_descriptions.get(nom)

    fenetre_infos = tk.Toplevel(root)
    fenetre_infos.title(f"Description - {nom}")
    fenetre_infos.geometry("500x400")
    fenetre_infos.configure(bg="#f0f0f0")

    titre = tk.Label(fenetre_infos, text=nom, font=("Helvetica", 20, "bold"), bg="#f0f0f0")
    titre.pack(pady=10)

    label = tk.Label(
        fenetre_infos,
        text=description,
        font=("Helvetica", 20),
        bg="#ffffff",
        wraplength=440,
        justify="center",
        anchor="center"
    )
    label.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

def create_a_propos_window(root):

    fenetre_a_propos = tk.Toplevel(root)
    fenetre_a_propos.title(" À propos ")
    fenetre_a_propos.geometry("500x400")
    fenetre_a_propos.configure(bg="#f0f0f0")

    titre = tk.Label(fenetre_a_propos, text="À propos", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
    titre.pack(pady=10)


    cadre_a_propos = tk.Frame(fenetre_a_propos)
    cadre_a_propos.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(cadre_a_propos)
    scrollbar.pack(side="right", fill="y")

    texte_widget = tk.Text(
        cadre_a_propos, wrap="word", yscrollcommand=scrollbar.set,
        font=("Helvetica", 18), bg="#ffffff"
    )
    texte_widget.insert("1.0", texte_a_propos)
    texte_widget.config(state="disabled")  
    texte_widget.pack(side="left", fill="both", expand=True)

    scrollbar.config(command=texte_widget.yview)

texte_descriptions = {
    "Delaunay triangulation graph": 
        "La triangulation de Delaunay relie un ensemble de points de sorte qu'aucun point ne se trouve à l'intérieur du cercle circonscrit d'aucun triangle. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",

    "Gabriel graph":
        "Le graphe de Gabriel relie deux points si et seulement si le cercle dont le segment qu'ils forment est le diamètre ne contient aucun autre point. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",
        
    "Integer graph": 
        "Le graphe entier connecte deux points si ils sont situés à une distance entière l'un de l'autre. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",

    "K closest neighbors graph": 
        "Le graphe des k vosins les plus proches relie chaque point à ses k plus proches voisins. \n "
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS} \n"
        f"Le nombre maximum de voisins les plus proches calculé est actuellement de {K_MAX_Neighbors}",

    "Minimum spanning tree graph": 
        "L'arbre couvrant de poids minimal relie tous les points sans former de cycle, avec la longueur totale la plus petite possible. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",

    "Nearest neighbor graph": 
        "Le graphe de plus proche voisin relie chaque point uniquement à son voisin le plus proche. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",

    "Relative neighborhood graph": 
        "Le graphe de voisinage relatif relie deux points seulement si aucun autre point n'est plus proche des deux à la fois. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS}",

    "Unit disk graph": 
        "Le graphe de disque unitaire relie deux points si la distance entre eux est inférieure au rayon choisi. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS} \n"
        f"Le rayon est actuellement compris entre {RAYON_MIN_Udg} et {RAYON_MAX_Udg}",
        
    "Yao graph": 
        "Le graphe yao divise l'espace autour de chaque point en secteurs angulaires, puis connecte le nouveau point à son plus proche voisin dans chaque secteur. \n"
        f"Le nombre maximum de sommets est actuellement de : {MAX_NB_POINTS} \n"
        f"Le nombre maximum de secteurs angulaires est actuellement de {K_MAX_Yao}",

    }

texte_a_propos = ( 
        "Ce projet permet d'explorer différents types de graphes géométriques de manière interactive.\n\n"
        "Fonctionnalités principales :\n"
            "- Ajouter, déplacer et supprimer des sommets sur le canevas. \n"
            "- Réinitialisation du graphe lancé (suppression de tous les sommets et arêtes). \n"
            "- Générer dynamiquement les arêtes selon le type de graphe sélectionné. \n"
            "- Modification des paramètres des graphes (rayon, nombre de voisins...) et actualisation instantannée du graphe. \n"
            "- Zoomer et se déplacer dans l'espace graphique. \n"
            "- Réinitialisation de la vue (recentrage + zoom x1). \n"
            "- Afficher les distances, les connexions et autres propriétés selon le graphe. \n"
            "- Option de création d'un nuage de point aléatoire à partir d'un terminal. \n"
            "- Possibilité de sauvegarder un nuage de point sur l'ordinateur. \n"
            "- Possibilité de charger un nuage de point précédemment sauvegardé et l'ouvrir dans son état de sauvegarde (position + zoom inchangés). \n"
            "- Enregistrement d'un nuage de point, ou graphe, sous forme d'une image. \n"
            "- Génération d'un nuage de n points aléatoires en lignes de commandes dans un terminal. \n"
            "- Description des fonctionnalités de chaque graphe et limites des paramètres. \n\n"

        "A tout moment, l'utilisateur peut modifier les valeurs du module 'constantes' (\V1.2\outils_canva\constantes) " \
        "afin d'appliquer les paramètres qu'il souhaite pour ses graphes, comme : \n"
            "- les dimensions des canvas \n"
            "- le nombre maximum de sommets \n"
            "- les valeurs minimales et maximales du rayon \n"
            "- le nombre maximum de voisin pour les graphes de voisinages \n"
            "- la taille et la couleur des sommets et des arêtes \n"
            "- les facteurs zoom et la limite du zoom"
        )
