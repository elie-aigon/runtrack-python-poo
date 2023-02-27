import math
class Cercle:
    def __init__(self):
        self.rayon = 3

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    
    def afficherInfos(self):
        print(self.rayon)

    def circonférence(self):
        print("circ: ", 2 * math.pi * self.rayon)

    def aire(self):
        print('aire: ', self.rayon * self.rayon * math.pi)

    def diametre(self):
        print("diametre : ", self.rayon * 2)

cercle = Cercle()
cercle.afficherInfos()
cercle.aire()
cercle.circonférence()
cercle.diametre()
cercle.changerRayon(5)
cercle.afficherInfos()