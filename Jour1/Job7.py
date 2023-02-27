class Personnage:
    def __init__(self):
        self.x = 5
        self.y = 10

    def position(self):
        print(self.x, self.y)

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1    

elie = Personnage()
elie.position()
elie.droite()
elie.bas()
elie.position()