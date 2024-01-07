class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur
        
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def getHauteur(self):
        return self.__hauteur
    
    def setHauteur(self, nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur
    
    def volume(self):
        return self.surface() * self.getHauteur()

rectangle1 = Rectangle(longueur=5, largeur=3)

parallelepipede1 = Parallelepipede(longueur=5, largeur=3, hauteur=2)

print("Longueur du Rectangle:", rectangle1.getLongueur())
print("Largeur du Rectangle:", rectangle1.getLargeur())

rectangle1.setLongueur(8)
rectangle1.setLargeur(4)

print("Périmètre du Rectangle:", rectangle1.perimetre())
print("Surface du Rectangle:", rectangle1.surface())

print("Longueur du Parallélépipède:", parallelepipede1.getLongueur())
print("Largeur du Parallélépipède:", parallelepipede1.getLargeur())
print("Hauteur du Parallélépipède:", parallelepipede1.getHauteur())

parallelepipede1.setLongueur(8)
parallelepipede1.setLargeur(4)
parallelepipede1.setHauteur(3)

print("Périmètre du Parallélépipède:", parallelepipede1.perimetre())
print("Surface du Parallélépipède:", parallelepipede1.surface())

print("Volume du Parallélépipède:", parallelepipede1.volume())