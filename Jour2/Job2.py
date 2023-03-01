class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def __setInfos(self):
        self.titre = input("Titre: ")
        self.auteur = input("Auteur: ")
        self.nb_page_check = round(float(input("NB de pages: ")))
        if self.nb_page_check > 0:
            self.nb_pages = self.nb_page_check
    
    def getInfos(self):
        self.__setInfos()
        print("Titre: ", self.titre, "auteur: ", self.auteur, "nb de pages: ", self.nb_pages)

hp = Livre("harry potter", "JK", 10000)
print("Titre: ", hp.titre, "auteur: ", hp.auteur, "nb de pages: ", hp.nb_pages)
hp.getInfos()

