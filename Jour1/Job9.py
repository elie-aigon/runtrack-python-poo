class Produit:
    def __init__(self, nom, prix, TVA):
        self.nom = nom
        self.prixHT = prix
        self.TVA = TVA

    def CalculerPrixTTC(self):
        self.prixTTC = self.prixHT + (self.TVA * self.prixHT)
        return self.prixTTC
    
    def afficher(self):
        list_aff = [self.nom, self.prixHT, self.TVA]
        return list_aff

    def change_name(self, new_name):
        self.nom = new_name

    def change_prix(self, new_prix):
        self.prixHT = new_prix

    def return_name(self):
        return self.nom

    def return_prixht(self):
        return self.prixHT

kebab = Produit("kebab", 6, 0.15)

for element in kebab.afficher():
    print(element)

print(kebab.return_name())
print(kebab.return_prixht())
print(kebab.CalculerPrixTTC())
kebab.change_name("kebab XL")
kebab.change_prix(8)
for element in kebab.afficher():
    print(element)
print(kebab.CalculerPrixTTC())

print('#################################')
souris = Produit("souris", 80, 0.2)
for element in souris.afficher():
    print(element)
print(souris.CalculerPrixTTC())
print(souris.return_name())
print(souris.return_prixht())
souris.change_name("souris XXL")
souris.change_prix(110)
for element in souris.afficher():
    print(element)

print(souris.CalculerPrixTTC())
