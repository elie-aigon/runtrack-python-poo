class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque = ", self.marque)
        print("Model = ", self.model)
        print("Année = ", self.annee)
        print("Prix = ", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix):
        super().__init__( marque, model, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Portes = ", self.portes)

class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix):
        super().__init__(marque, model, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Roues = ", self.roues)
    
    def demarrer(self):
        super().demarrer()
        print('et je BOMBARDE!')

audi = Voiture("Audi", "A3", 2010, 35000)
audi.informationsVehicule()
print('#####################')
yamaha = Moto("Yamaha", "Bip", 2003, 25000)
yamaha.informationsVehicule()
print('#####################')
audi.demarrer()
yamaha.demarrer()