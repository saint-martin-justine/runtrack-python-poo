import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, ennemi):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige {degats} points de dégâts.")
        ennemi.vie -= degats
        if ennemi.vie <= 0:
            print(f"{ennemi.nom} est vaincu !")
            return True
        else:
            return False


class Jeu:
    def __init__(self):
        self.niveau = 1
    
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez un niveau de difficulté (1, 2 ou 3) : "))
    
    def lancerJeu(self):
        if self.niveau == 1:
            vie_joueur = 50
            vie_ennemi = 30
        elif self.niveau == 2:
            vie_joueur = 40
            vie_ennemi = 40
        elif self.niveau == 3:
            vie_joueur = 30
            vie_ennemi = 50
        else:
            print("Niveau non valide.")
            return
        
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)
        print(f"Vous affrontez un ennemi de niveau {self.niveau} avec {vie_ennemi} points de vie.")
        
        while joueur.vie > 0 and ennemi.vie > 0:
            print(f"{joueur.nom} : {joueur.vie} points de vie.")
            print(f"{ennemi.nom} : {ennemi.vie} points de vie.")
            joueur_attaque = input("Voulez-vous attaquer ? (oui/non) : ")
            if joueur_attaque == "oui":
                if joueur.attaquer(ennemi):
                    print("Vous avez gagné !")
                    break
            else:
                print("Vous passez votre tour.")
            if ennemi.attaquer(joueur):
                print("Vous avez perdu...")
                break
        
        print("Fin de la partie.")
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()