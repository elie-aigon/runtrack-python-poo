import math
class Cercle:
    def __init__(self):
        self.rayon = 3

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon
    
    def afficherInfos(self):
        print('rayon : ', self.rayon, "diametre : ", self.diametre(), "circonférence : ", self.circonférence(), "aire : ", self.aire())

    def circonférence(self):
        return  2 * math.pi * self.rayon

    def aire(self):
        return self.rayon * self.rayon * math.pi

    def diametre(self):
        return  self.rayon * 2

cercle = Cercle()
cercle.afficherInfos()
cercle.changerRayon(5)
cercle.afficherInfos()