class Joueur:
    def __init__(self, nom, numero, poste, buts, passe_d, jaunes, rouges):
        self.nom = nom
        self.numero = numero
        self.poste = poste
        self.buts = buts
        self.passe_d = passe_d
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1

    def effectuerPasseD(self, buteur):
        self.passe_d += 1
        buteur.marquerUnBut()

    def recevoirJaune(self):
        self.jaunes += 1

    def recevoirRouge(self):
        self.rouges += 1
    
    def afficherStats(self):
        print("nom = ", self.nom)
        print("Numero = ", self.numero)
        print("Poste = ", self.poste)
        print("Buts = ", self.buts)
        print("Passe D = ", self.passe_d)
        print("Jaunes = ", self.jaunes)
        print("Rouges = ", self.rouges)


class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    def ajouterJoueur(self, joueur):
        if joueur not in self.joueurs:
            self.joueurs.append(joueur)
    
    def afficherStatsJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStats()
    
    def mettreAJourStatsJoueur(self):
        pass


elie = Joueur("Elie", 4, "gardien", 10, 5, 1, 0)
yoann= Joueur("yoann", 5, "défenseur", 15, 3, 8, 1)
aurore = Joueur("aurore", 6, "attaquant", 35, 14, 3, 5)

om = Equipe("OM", [elie, yoann, aurore])

hugo = Joueur("hugo", 1, "gardien", 10, 5, 1, 0)
remi= Joueur("remi", 3, "défenseur", 15, 3, 8, 1)
leo = Joueur("leo", 9, "attaquant", 35, 14, 3, 5)

paris = Equipe("PSG", [hugo, remi, leo])


paris.afficherStatsJoueurs()
print("###############################################")
om.afficherStatsJoueurs()

aurore.marquerUnBut()
elie.recevoirJaune()

hugo.recevoirRouge()
yoann.recevoirRouge()
yoann.marquerUnBut()

paris.afficherStatsJoueurs()
print("###############################################")
om.afficherStatsJoueurs()