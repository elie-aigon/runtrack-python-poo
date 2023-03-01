class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde, decouvert):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("num compte =  ", self.__num_compte)
        print("Nom = ", self.__nom)
        print("Prenom = ", self.__prenom)
        print("Solde = ", self.__solde) 

    def afficherSolde(self):
        print("Solde = ", self.__solde) 

    def versement(self, montant):
        self.__solde += montant

    def virement(self, montant, destinataire):
        if self.__solde >= montant:
            self.__solde -= montant
            destinataire.versement(montant)

    def retrait(self, montant):
        if self.__solde >= montant and self.__decouvert:
            self.__solde -= montant

    def agios(self):
        self.taux = 0.1
        if self.__solde < 0:
            self.__solde += self.__solde * self.taux

compte1 = CompteBancaire(1, "elie", "aigon", 500, False)
compte2 = CompteBancaire(2, "mahel", "aigon", -200, True)

compte1.afficher()
compte2.afficher()

compte2.agios()
compte1.virement(220, compte2)

compte1.afficher()
compte2.afficher()