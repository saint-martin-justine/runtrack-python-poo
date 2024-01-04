class Voiture:
    def __init__(self, marque, modele, annee, km):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._km = km
        self._en_marche = False
        self._reservoir = 50

    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_km(self, km):
        self._km = km

    def set_en_marche(self, en_marche):
        self._en_marche = en_marche

    def set_reservoir(self, reservoir):
        self._reservoir = reservoir

    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_km(self):
        return self._km

    def get_en_marche(self):
        return self._en_marche

    def get_reservoir(self):
        return self._reservoir

    def demarrer(self):
        if self._verifier_plein() > 5:
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("Le réservoir est presque vide, la voiture ne peut pas démarrer.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    def _verifier_plein(self):
        return self._reservoir

# Instancier un objet voiture
voiture = Voiture("Peugeot", "208", 2018, 50000)

# Utiliser les mutateurs pour changer les attributs
voiture.set_marque("Renault")
voiture.set_modele("Clio")
voiture.set_annee(2020)
voiture.set_km(20000)
voiture.set_reservoir(30)

# Utiliser les assesseurs pour récupérer les attributs
print("Marque :", voiture.get_marque())
print("Modèle :", voiture.get_modele())
print("Année :", voiture.get_annee())
print("Kilométrage :", voiture.get_km())
print("Réservoir :", voiture.get_reservoir())

# Utiliser les méthodes demarrer et arreter
voiture.demarrer()
voiture.arreter()