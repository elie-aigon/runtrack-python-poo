class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages
        self.__dispo = True

    def aff(self):
        print("Titre: ", self.titre, "auteur: ", self.auteur, "nb de pages: ", self.nb_pages,"dispo: ", self.__dispo)

    def __setInfos(self):
        self.titre = input("Titre: ")
        self.auteur = input("Auteur: ")
        self.nb_page_check = round(float(input("NB de pages: ")))
        if self.nb_page_check > 0:
            self.nb_pages = self.nb_page_check
    
    def getInfos(self):
        self.__setInfos()
    
    def emprunter(self):
        if self.vérification():
            self.__dispo = False

    def rendre(self):
        if not self.vérification():
            self.__dispo = True

    def vérification(self):
        if self.__dispo:
            return True
        else:
            return False

hp = Livre("harry potter", "JK", 10000)
hp.aff()
hp.emprunter()
hp.aff()
hp.rendre()
hp.aff()