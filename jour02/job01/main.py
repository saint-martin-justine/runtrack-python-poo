class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec longueur 20 et largeur 10
rectangle = Rectangle(20, 10)

# Afficher des attributs initiaux
print("Longueur :", rectangle.get_longueur()) 
print("Largeur :", rectangle.get_largeur()) 

# Modification de la longueur et de la largeur
rectangle.set_longueur(10)
rectangle.set_largeur(2)

# Afficher des attributs modifiés
print("Longueur :", rectangle.get_longueur()) 
print("Largeur :", rectangle.get_largeur()) 

