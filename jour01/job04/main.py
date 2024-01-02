class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def sePresenter(self):
        print("Je suis ",self.nom + " " + self.prenom)


personne2 = Personne("John", "Doe")

personne2.sePresenter()
personne = Personne("Jean", "Dupond")

personne.sePresenter()
