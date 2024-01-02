class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self,):
        afficherX = self.x
        afficherY = self.y

        print(afficherX, afficherY)
    
    def changerX(self, x,):
        self.x = x

        print("la nouvelle position de x est : ", self.x)

    def changerY(self, y,):
        self.y = y
        print("la nouvelle position de y est : ", y)


point = Point(10, 20)

point.afficherLesPoints()

point.changerX(30)

point.afficherLesPoints()

point.changerY(40)

point.afficherLesPoints()