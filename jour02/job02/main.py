class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: le nombre de pages doit être un nombre entier positif")
# Création d'un livre avec titre, auteur et nombre de pages
livre1 = Livre("Les Misérables", "Victor Hugo", 1500)

# Afficher les attributs initiaux
print("Titre :", livre1.get_titre()) 
print("Auteur :", livre1.get_auteur()) 
print("Nombre de pages :", livre1.get_nombre_de_pages()) 

# Modification du nombre de pages avec une valeur invalide
livre1.set_nombre_de_pages(-100) 

# Afficher le nombre de pages modifié
print("Nombre de pages :", livre1.get_nombre_de_pages()) 

