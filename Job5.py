class Voiture:
    def __init__(self, marque, modèle, année, km):
        self.__marque = marque
        self.__modele = modèle
        self.__annee = année
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50

    def showInfos(self):
        print("marque = ", self.__marque)
        print("modele = ", self.__modele)
        print("année = ", self.__annee)
        print("km = ", self.__km)
        print("status = ", self.__en_marche)

    def __setMarque(self, input_):
        self.__marque = input_
    def __setModel(self, input_):
        self.__modele = input_
    def __setAnnee(self, input_):
        self.__annee = input_
    def __setKm(self, input_):
        self.__km = input_
    def __set_en_marche(self, input_):
        self.__en_marche = input_


    def getMarque(self):
        self.__setMarque(input("marque: "))
    def getModel(self):
        self.__setModel(input("modele: "))
    def getAnnee(self):
        self.__setAnnee(input("année: "))
    def getKm(self):
        self.__setKm(input("km: "))
    def geten_marche(self):
        new_en_marche = input("status: ")
        if isinstance(new_en_marche, bool):
            self.__set_en_marche(new_en_marche)

    def démarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
    
    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        if self.__reservoir > 5:
            return True
        else: 
            return False
audi = Voiture("audi", "A3", 2010, 200)
audi.showInfos()
audi.getMarque()
audi.showInfos()
audi.démarrer()
audi.showInfos()
audi.arreter()
audi.showInfos()