class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.__disponible = True  # attribut privé

    def vérification(self):
        return self.__disponible  # renvoie la valeur de l'attribut privé

    def emprunter(self):
        if self.__disponible:  # vérifie si le livre est disponible
            self.__disponible = False  # rend le livre indisponible
            print(f"Le livre \"{self.titre}\" a été emprunté.")
        else:
            print(f"Désolé, le livre \"{self.titre}\" n'est pas disponible pour le moment.")

    def rendre(self):
        if not self.__disponible:  # vérifie si le livre a été emprunté
            self.__disponible = True  # rend le livre disponible
            print(f"Le livre \"{self.titre}\" a été rendu avec succès.")
        else:
            print(f"Le livre \"{self.titre}\" n'a pas été emprunté auparavant.")
# création d'un livre
livre1 = Livre("Les Misérables ", "Victor Hugo")

# vérifier la disponibilité
print(livre1.vérification())  

# emprunt du livre
livre1.emprunter()  

# vérifier la disponibilité
print(livre1.vérification()) 

# rendre le livre
livre1.rendre()  

# vérifier la disponibilité
print(livre1.vérification())  
