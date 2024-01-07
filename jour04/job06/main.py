class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        return f'Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}'

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes
    
    def informationsVehicule(self):
        info_generales = self.informationVehicule()
        return f'{info_generales}\nNombre de portes : {self.portes}'

    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} a démarre. ~bruit de moteur...~!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue
    
    def informationsVehicule(self):
        info_generales = self.informationVehicule()
        return f'{info_generales}\nNombre de roues : {self.roue}'

    def demarrer(self):
        print(f"La moto {self.marque} {self.modele} a démarre. ~bruit de moteur...~")

voiture1 = Voiture(marque="Dodge", modele="Demond", annee=2018, prix=38000)
moto1 = Moto(marque="Yamaha", modele="Tmax", annee=2015, prix=12500)

info_voiture = voiture1.informationsVehicule()
print(info_voiture)

info_moto = moto1.informationsVehicule()
print(info_moto)

voiture1.demarrer()
moto1.demarrer()