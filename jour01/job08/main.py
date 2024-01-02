class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    
    def change_rayon(self,rayon):
        self.rayon = rayon
    
    def afficherInfo(self):
        print("le diamètre de ce cercle est : ", self.diamètre())
        print("Le circonférence de ce cercle est : ", self.circonférence())
        print("Les aires de ce cercle sont : ", self.aires())
    
    def circonférence(self):
        return 3.14 * self.rayon * self.rayon
    
    def aires(self):
        return 2 * 3.14 * self.rayon
    
    def diamètre(self):
        return self.rayon * 2
    

cercle = Cercle(4)
cercle.afficherInfo()

cercle2 = Cercle(7)
cercle2.afficherInfo()