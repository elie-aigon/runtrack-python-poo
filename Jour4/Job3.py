class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longeur = longueur
        self.__largeur = largeur

    def périmètre(self):
        return 2 * (self.__largeur + self.__longeur)

    def surface(self):
        return self.__longeur * self.__largeur

    def getLongeur(self, valeur):
        if isinstance(valeur, int):
            self.__setLongeur(valeur)

    def getLargeur(self, valeur):
        if isinstance(valeur, int):
            self.__setLargeur(valeur)

    def __setLongeur(self, valeur):
        self.__longeur = valeur

    def __setLargeur(self, valeur):
        self.__largeur = valeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur

bidule = Parallélépipède(5, 4, 3)
print('périmètre = ', bidule.périmètre(), "m")
print('surface = ', bidule.surface(), "m2")
print('volume = ', bidule.volume(), "m3")

bidule.getLargeur(8)
bidule.getLongeur(13)

print('périmètre = ', bidule.périmètre(), "m")
print('surface = ', bidule.surface(), "m2")
print('volume = ', bidule.volume(), "m3")