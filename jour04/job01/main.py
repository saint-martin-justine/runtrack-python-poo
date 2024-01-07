class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
        print(f"la personne à {nouvel_age} ans.")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def bonjour(self):
        print("Bonjour")


class Professeur(Personne):
    def __init__(self, matiere_enseignee, age=30):
        super().__init__(age)
        self.__matiereEnseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer.")

    def afficherAge(self):
        print(f"J'ai {self.age} ans et j'enseigne la matière {self.__matiereEnseignee}.")


eleve1 = Eleve()
eleve1.afficherAge()
eleve1.bonjour()
eleve1.allerEnCours()

professeur1 = Professeur(matiere_enseignee="La programmation en OO")
professeur1.afficherAge()
professeur1.bonjour()
professeur1.enseigner()