class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts_marques += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        print("Statistiques pour le joueur", self.nom)
        print("Numéro :", self.numero)
        print("Position :", self.position)
        print("Buts marqués :", self.buts_marques)
        print("Passes décisives :", self.passes_decisives)
        print("Cartons jaunes :", self.cartons_jaunes)
        print("Cartons rouges :", self.cartons_rouges)


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        print("Statistiques pour l'équipe", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()
    
    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts_marques=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts_marques
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges


# Création des joueurs
joueur1 = Joueur("Robert Lewandowski", 9, "Attaquant")
joueur2 = Joueur("Karim Benzema", 9, "Attaquant")
joueur3 = Joueur("Ousmane Dembele", 7, "Attaquant")
joueur4 = Joueur("Luka modric", 10, "Attaquant")

# Création des équipes
equipe1 = Equipe("FC Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques des joueurs avant le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur3.recevoirUnCartonJaune()
joueur2.recevoirUnCartonRouge()
joueur4.recevoirUnCartonJaune()

# Mise à jour des statistiques des joueurs
equipe1.mettreAJourStatistiquesJoueur("Robert Lewandowski", buts_marques=1, passes_decisives=1)
equipe1.mettreAJourStatistiquesJoueur("Ousmane Dembele", cartons_jaunes=1)

equipe2.mettreAJourStatistiquesJoueur("Karim Benzema", cartons_rouges=1)
equipe2.mettreAJourStatistiquesJoueur("Luka Modric", cartons_jaunes=1)

# Affichage des statistiques des joueurs après le match
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()




