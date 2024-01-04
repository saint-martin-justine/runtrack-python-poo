class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nom(self):
        return self.__nom

    def get_nb_habitants(self):
        return self.__nb_habitants

    def ajouter_population(self):
        self.__nb_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    def ajouter_population(self):
        self.__ville.ajouter_population()


# Créer un objet "Ville" avec comme arguments "Paris" et 1000000.
paris = Ville("Paris", 1000000)

# Afficher le nombre d'habitants de la ville de Paris sur la console .
print(f"Il y a {paris.get_nb_habitants()} habitants à {paris.get_nom()}.")

# Créer un autre objet "Ville" avec comme arguments "Marseille" et 861635.
marseille = Ville("Marseille", 861635)

# Afficher  le nombre d'habitants de la ville de Marseille sur la console.
print(f"Il y a {marseille.get_nb_habitants()} habitants à {marseille.get_nom()}.")

# Créer les objets suivants :
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajouter les nouvelles personnes à leur ville.
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# Afficher le nombre d'habitants de Paris et de Marseille après l'arrivée de ces nouvelles personnes.
print(f"Il y a maintenant {paris.get_nb_habitants()} habitants à {paris.get_nom()}.")
print(f"Il y a maintenant {marseille.get_nb_habitants()} habitants à {marseille.get_nom()}.")