class Animal:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        print("L'age de l'animal ", age, " ans")

    def vieillir(self):
        self.age += 1
        print("L'age de l'animal ", self.age, " ans")
    
    def nommer(self, nom):
        self.nom = nom
        print("Le nom de l'animal est : ", self.nom)
    
animal = Animal()

animal.vieillir()

animal.nommer("Luna")