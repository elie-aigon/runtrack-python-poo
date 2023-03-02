class Tache:
    def __init__(self, titre, descipt, status):
        self.titre = titre
        self.descipt = descipt
        self.status = status

class ListeDeTaches:
    def __init__(self, taches):
        self.taches = taches

    def afficherListe(self):
        for tache in self.taches:
            print("Titre = ", tache.titre, "Status = ", tache.status)
    
    def ajouterTache(self, tache):
        if tache not in self.taches:
            self.taches.append(tache)

    def marquerCommeFinie(self, tache):
        tache.status = "Terminer"

    def filtreListe(self):
        à_faire = []
        terminer = []
        for tache in self.taches:
            if tache.status == "à faire":
                à_faire.append(tache)
            else:
                terminer.append(tache)
        print("à faire: ")
        for element in à_faire:
            print("Titre = ", element.titre, "Status = ", element.status)
        print("Terminer: ")
        for element in terminer:
            print("Titre = ", element.titre, "Status = ", element.status)


tache1 = Tache("tache1", "", "à faire")
tache2 = Tache("tache2", "", "à faire")
tache3 = Tache("tache3", "", "terminer")
tache4 = Tache("tache4", "", "à faire")
tache5 = Tache("tache5", "", "terminer")

liste = ListeDeTaches([tache1, tache2, tache3, tache4])
liste.filtreListe()
liste.ajouterTache(tache5)
liste.marquerCommeFinie(tache1)
print("#############")
liste.filtreListe()