import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = self.initialiser_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def initialiser_paquet(self):
        valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def tirer_carte(self):
        return self.paquet.pop()

    def distribuer_cartes_initiales(self):
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]

    def calculer_score(self, main):
        score = sum(carte.valeur for carte in main)
        as_present = any(carte.valeur == 11 for carte in main)

        while score > 21 and as_present:
            for carte in main:
                if carte.valeur == 11:
                    carte.valeur = 1
                    break
            score = sum(carte.valeur for carte in main)
            as_present = any(carte.valeur == 11 for carte in main)

        return score

    def jouer(self):
        self.distribuer_cartes_initiales()

        while True:
            score_joueur = self.calculer_score(self.main_joueur)
            score_croupier = self.calculer_score(self.main_croupier)

            print(f"Votre main : {[str(carte) for carte in self.main_joueur]}, Score : {score_joueur}")
            print(f"Carte visible du croupier : {self.main_croupier[0]}")

            if score_joueur == 21:
                print("Blackjack ! Vous gagnez.")
                break
            elif score_joueur > 21:
                print("Vous avez dépassé 21. Vous perdez.")
                break

            action = input("Voulez-vous prendre une carte supplémentaire ? (O/N): ").lower()
            
            if action == 'o':
                self.main_joueur.append(self.tirer_carte())
            else:
                break

        while score_croupier < 17:
            self.main_croupier.append(self.tirer_carte())
            score_croupier = self.calculer_score(self.main_croupier)

        print(f"Votre main : {[str(carte) for carte in self.main_joueur]}, Score : {score_joueur}")
        print(f"Main du croupier : {[str(carte) for carte in self.main_croupier]}, Score : {score_croupier}")

        if score_joueur > 21:
            print("Vous avez dépassé 21. Vous perdez.")
        elif score_croupier > 21 or score_joueur > score_croupier:
            print("Votre main Gagne !")
        elif score_joueur == score_croupier:
            print("Partie nul.")
        else:
            print("La main du croupier gagne.")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()

print(f"Votre main : {[str(carte) for carte in jeu.main_joueur]}, Score : {jeu.calculer_score(jeu.main_joueur)}")
print(f"Main du croupier : {[str(carte) for carte in jeu.main_croupier]}, Score : {jeu.calculer_score(jeu.main_croupier)}")