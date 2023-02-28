class commande:
    def __init__(self, num_commande, liste_plat, status):
        self.__num_commande = num_commande
        self.__liste_plat = liste_plat
        self.__status = status
        self.cout_plat = {"entre": 3, "plat": 5, "boisson": 2}
        
    def modif_status(self):
        self.__status = input("new status: ")

    def add_plat(self):
        new_plat = input("new plat: ")
        if new_plat in self.cout_plat:
            self.__liste_plat[new_plat] += 1

    def __calcul_total(self):
        self.total = 0
        for element in self.__liste_plat:
            self.total += self.cout_plat[element] * self.__liste_plat[element]
        return self.total
    
    def __calculTVA(self):
        self.__TVA = 0.2
        self.__partTVA = self.total * self.__TVA
        return self.__partTVA

    def showInfos(self):
        print("listes plats: ", self.__liste_plat)
        print("Total: ", self.__calcul_total())
        print("part TVA: ", self.__calculTVA(), "avec TVA: ", self.__TVA)
        print("status: ", self.__status)

cmd1 = commande(1, {"boisson": 2, "plat": 3, "entre": 1}, "en cours")
cmd1.add_plat()
cmd1.showInfos()