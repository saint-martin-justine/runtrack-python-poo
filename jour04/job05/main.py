class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        import math
        return math.pi * self.radius**2

rectangle1 = Rectangle(largeur=5, hauteur=3)
cercle1 = Cercle(radius=4)

resultat_aire_rectangle = rectangle1.aire()
resultat_aire_cercle = cercle1.aire()

print("L'aire du rectangle est:", resultat_aire_rectangle)
print("L'aire du cercle est:", resultat_aire_cercle)