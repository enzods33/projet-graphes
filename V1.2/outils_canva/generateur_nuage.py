from outils_canva.saisie_utilisateur import demander_parametres_nuage
from outils_canva.fonction_math import generer_nuage_points
from outils_canva.gestion_fichier import sauvegarder_points_dans_fichier

def creer_nuage_aleatoire_et_sauvegarder(largeur, hauteur):
    """
    Génère un nuage aléatoire de points et le sauvegarde, avec largeur et hauteur reçues en paramètre.

    Demande :
    - un nom de fichier (utilisé comme proposition par défaut),
    - les intervalles x et y,
    - le nombre de points.

    Affiche ensuite une fenêtre pour choisir où enregistrer le fichier.
    """
    print("Création d'un nuage de points aléatoires")
    nom_fichier = input("Nom du fichier de sauvegarde (ex: nuage.txt) : ")
    if nom_fichier == "":
        nom_fichier = "nuage.txt"

    xmin, xmax, ymin, ymax, npoints = demander_parametres_nuage(largeur, hauteur)
    points = generer_nuage_points(xmin, xmax, ymin, ymax, npoints)
    
    print("📂 Une fenêtre va s'ouvrir pour choisir où enregistrer votre fichier. Veuillez sélectionner l'emplacement.")
    sauvegarder_points_dans_fichier(points, nom_fichier)

    print(f"✅ {npoints} points ont été enregistrés dans '{nom_fichier}' avec succès.")