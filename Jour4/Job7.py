import random
from time import sleep
class Cartes:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    
class Jeu:
    def __init__(self):
        self.init_game()
        # game states
        self.game_on = False

    def genPaquets(self):
        self.paquets = []
        couleur = ["Carreau", "Coeur", "Pique", "Trèfle"]
        valeur = {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 10, "Dame": 10, "Roi": 10}
        for i in couleur:
            for y in valeur:
                self.paquets.append(Cartes(i, y))

    def tirer_carte(self, joueur):
        card = random.choice(self.paquets)
        joueur.append(card)
        self.paquets.remove(card)

    def gen_2Cards(self):
        self.card_joueur = []
        self.card_croupier = []
        running = True
        while running:
            card = random.choice(self.paquets)
            if len(self.card_croupier) < 2:
                self.card_croupier.append(card)
            elif len(self.card_joueur) < 2:
                self.card_joueur.append(card)
            else:
                running = False
            self.paquets.remove(card)
        
    def init_game(self):
        self.genPaquets()
        self.gen_2Cards()
    
    def display(self):
        print("################")
        if self.game_on:
            print("Ta main: ")
            for card in self.card_joueur:
                print(card.valeur, "de ", card.couleur)
            print("La main tu croupier: ")
            print(self.card_croupier[0].valeur, "de", self.card_croupier[0].couleur)
            print("hide ")

    def action_joueur(self):
        print('Tu peux tirer une carte ou te coucher, (choisis en tappant "tirer" ou "fold")')
        choice = input()
        if choice.lower() == "tirer":
            self.tirer_carte(self.card_joueur)
        elif choice.lower() == "fold":
            self.game_on = False
            print("The BANK win !")
        else:
            self.action_joueur_croupier()
        
    def action_croupier(self):
        for element in self.card_croupier:
            
        
jeu = Jeu()
i = 0
run = True
print(jeu.card_croupier[0].valeur)
    

    