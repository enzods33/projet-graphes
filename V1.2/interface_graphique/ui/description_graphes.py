import tkinter as tk
from outils_canva.constantes import MAX_NB_POINTS, RAYON_MIN_Udg, RAYON_MAX_Udg, K_MAX_Neighbors, K_MAX_Yao

def create_description_window(root, nom):
    description = descriptions.get(nom)

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


descriptions = {
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


