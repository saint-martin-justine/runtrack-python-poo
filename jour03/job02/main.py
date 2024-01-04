class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde_initial, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert = decouvert

    def afficher(self):
        print("Compte n°{} de {} {}: {} €".format(self.__numero, self.__prenom, self.__nom, self.__solde))

    def afficherSolde(self):
        print("Solde du compte n°{} : {} €".format(self.__numero, self.__solde))

    def versement(self, montant):
        self.__solde += montant
        print("Versement de {} € effectué sur le compte n°{}. Nouveau solde : {} €".format(montant, self.__numero, self.__solde))

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible : solde insuffisant")
        else:
            self.__solde -= montant
            print("Retrait de {} € effectué sur le compte n°{}. Nouveau solde : {} €".format(montant, self.__numero, self.__solde))

    def agios(self, taux):
        if self.__solde < 0:
            self.__solde -= self.__solde * taux
            print("Application des agios ({}%) sur le compte n°{}. Nouveau solde : {} €".format(taux*100, self.__numero, self.__solde))

    def virement(self, compte_dest, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Opération impossible : solde insuffisant")
        else:
            self.__solde -= montant
            compte_dest.versement(montant)
            print("Virement de {} € effectué du compte n°{} vers le compte n°{}".format(montant, self.__numero, compte_dest.getNumero()))

    def getNumero(self):
        return self.__numero
# Création du compte
compte1 = CompteBancaire("123456789", "Durand", "Jean", 1000)

# Afficher les informations du compte
compte1.afficher()
compte1.afficherSolde()

# Exemple de versement et retrait
compte1.versement(500)
compte1.retrait(200)

# Ajout de l'attribut découvert et test de la méthode retrait avec solde négatif autorisé
compte2 = CompteBancaire("987654321", "Dupont", "Marie", -500, True)
compte2.retrait(1000)

# Application des agios
compte2.agios(0.05)

# Virement entre deux comptes
compte1.virement(compte2, 300)
