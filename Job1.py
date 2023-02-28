class Rectangle:
    def __init__(self):
        self.longueur = 8
        self.largeur = 4
    
    def __setRect(self):
        self.longueur = input("Longueur: ")
        self.largeur = input("Largeur: ")

    def getRect(self):
        self.__setRect()
        print("longeur: ", self.longueur, "largeur: ", self.largeur)

rect = Rectangle()
print("longeur: ", rect.longueur, "largeur: ",rect.largeur)
rect.getRect()