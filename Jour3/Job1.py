class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def showInfos(self):
        return self.__nb_habitants

    def ajouterPopulationBis(self):
        self.__nb_habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation(self.__ville)

    def ajouterPopulation(self, ville):
        ville.ajouterPopulationBis()

Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
print("Paris", Paris.showInfos())
print("Marseille: ", Marseille.showInfos())

Jhon = Personne("Jhon", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloe", 18, Marseille)


print("Paris", Paris.showInfos())
print("Marseille: ", Marseille.showInfos())