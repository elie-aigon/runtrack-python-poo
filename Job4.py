class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def Sepresenter(self):
        print("Je suis ", self.prenom, self.nom)

personne1 = Personne("aigon", "elie")
personne2 = Personne("Fermaud", "Yoann")

personne1.Sepresenter()
personne2.Sepresenter()