class Operation:
    nombre1 = 12
    nombre2 = 3

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le resultat est : " + str(resultat))


affichage = Operation()

affichage.addition()