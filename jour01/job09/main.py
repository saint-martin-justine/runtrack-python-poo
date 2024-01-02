class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def calculerPrxTTC(self):
        return self.prixHT * (1 + self.TVA)
    
    def afficher(self):
        return "Le nom du produit est : ", self.nom , "Le prix HT est : ", self.prixHT,  "Le TVA est : ", self.TVA, "Le prx TTC est : ", self.calculerPrxTTC()
    
vélo = Produit("Vélo", 1000, 0.2)
print(vélo.afficher())
