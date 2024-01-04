class Tache:
    def __init__(self, titre, description, statut='A faire'):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquer_comme_finie(self):
        self.statut = 'Terminée'


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def afficher_liste(self):
        for tache in self.taches:
            print(f"{tache.titre} - {tache.description} - {tache.statut}")

    def filter_liste(self, statut):
        filtered_taches = []
        for tache in self.taches:
            if tache.statut == statut:
                filtered_taches.append(tache)
        return filtered_taches
# Création des tâches
tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs")
tache2 = Tache("Nettoyer la maison", "Passer l'aspirateur et laver les sols")
tache3 = Tache("Appeler le médecin", "Prendre rendez-vous pour la semaine prochaine")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

# Afficher la liste des tâches
print("Liste des tâches :")
liste_taches.afficher_liste()

# Supprimer une tâche
liste_taches.supprimer_tache(tache2)

# Afficher  la liste des tâches mise à jour
print("Liste des tâches après suppression :")
liste_taches.afficher_liste()

# Marquage d'une tâche comme terminée
tache1.marquer_comme_finie()

# Affichage de la liste des tâches à faire
print("Liste des tâches à faire :")
taches_a_faire = liste_taches.filter_liste('A faire')
for tache in taches_a_faire:
    print(f"{tache.titre} - {tache.description}")
