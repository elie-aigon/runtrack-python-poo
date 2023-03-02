from time import sleep

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.degats = 10
        
    def attaquer(self, enemi):
        enemi.vie -= self.degats

    def showInfos(self):
        print("Nom = ", self.nom, "; HP = ", self.vie)

class Jeu:
    def __init__(self):
        self.lancerJeu()
        self.game_end = False

    def choisirNiveau(self):
        lvl = input("Chosis le niveau : ")
        if lvl in ["facile", "normal", "hard"]:
            self.niveau = lvl
        else:
            self.choisirNiveau()

    def lancerJeu(self):
        self.choisirNiveau()
        self.players = [Personnage("Joueur"), Personnage("Enemi")]
        if self.niveau == "hard":
            self.players[1].vie = 200
        elif self.niveau == "facile":
            self.players[1].vie = 50
        
    def checkWin(self):
        for personnage in self.players:
            if personnage.vie <= 0:
                print(personnage.nom, "à perdu ! ")
                self.game_end = True

    def showInfosPlayers(self):
        for player in self.players:
            player.showInfos()
        self.checkWin()

taken = Jeu()

i = 0
while True:
    print("Round", i + 1)
    taken.showInfosPlayers()
    if i % 2 == 0:
        taken.players[0].attaquer(taken.players[1])
    else:
        taken.players[1].attaquer(taken.players[0])
    if taken.game_end:
        break
    sleep(1)
    i += 1
    