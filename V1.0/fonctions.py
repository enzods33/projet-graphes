import tkinter as tk
import math 

def put_art(event, feuille, rayon: int, sommets: list):
    """ relie deux points par un trait si ils sont à une distance inférieure à rayon """
    for som in sommets:
        coords = feuille.coords(som)
        if math.dist(coords, (event.x-3, event.y-3, event.x+3, event.y+3))<=rayon:
            feuille.create_line(coords[0]+3, coords[1]+3, event.x, event.y, fill="yellow", width=2)

def put_point(event, feuille, sommets : list, rayon : int):
    """
    place un point aux coordonées définies par le clic gauche de la souris 
    si le canva possède au moins deux sommets (la liste sommets a donc au moins deux valeur), on appelle put_art pour voir si on relie les sommets
      """
    x,y = event.x, event.y
    if len(sommets)>=1:
        put_art(event, feuille, rayon, sommets)
    sommets.append(feuille.create_rectangle(x-3, y-3, x+3, y+3, fill="yellow"))
    print(sommets)


def remove_point(event, feuille, sommets):
    min = feuille.winfo_width()
    items = feuille.find_all()
    for item in items:        
        coords = feuille.coords(item)
        if math.dist(coords, (event.x-3, event.y-3, event.x+3, event.y+3))<min and feuille.type(item) == "rectangle":
            min = math.dist(coords, (event.x-3, event.y-3, event.x+3, event.y+3))
            item_del= item
    remove_art(feuille, item_del)
    feuille.delete(item_del)    
    sommets.remove(item_del)
    print(sommets)

def remove_art(feuille, som_del):
    items = feuille.find_all()
    for item in items: 
        if feuille.type(item) == "line":
            coords = feuille.coords(item)
            if (coords[0],coords[1])==(feuille.coords(som_del)[0]+3,feuille.coords(som_del)[1]+3) or (coords[2],coords[3])==(feuille.coords(som_del)[0]+3,feuille.coords(som_del)[1]+3):
                feuille.delete(item)
