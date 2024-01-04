class Commande:
    
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"
    
    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "status": "en cours"}
    
    def annuler_commande(self):
        self.__statut_commande = "annulée"
        for plat in self.__plats_commandes.values():
            plat["status"] = "annulé"
    
    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            if plat["status"] == "en cours":
                total += plat["prix"]
        return total
    
    def afficher_commande(self):
        total = self.__calculer_total()
        commande_str = f"Commande n°{self.__numero_commande} ({self.__statut_commande}) :\n"
        for nom_plat, plat in self.__plats_commandes.items():
            commande_str += f"- {nom_plat} : {plat['prix']} euros ({plat['status']})\n"
        commande_str += f"Total à payer : {total} euros (TVA incluse)"
        return commande_str
    
    
    def calculer_tva(prix_ht, taux_tva):
        return prix_ht * taux_tva / 100
    
    # Création d'une commande
commande1 = Commande("001")

# Ajout de plats à la commande
commande1.ajouter_plat("Pizza Royal", 8)
commande1.ajouter_plat("Salade césar", 6)
commande1.ajouter_plat("Tiramisu", 4)

# Affichage de la commande avec le total à payer
print(commande1.afficher_commande())




    