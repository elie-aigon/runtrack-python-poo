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
        self.game_step = False
        
    def genPaquets(self):
        self.paquets = []
        couleur = ["Carreau", "Coeur", "Pique", "Trèfle"]
        self.valeur = {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Valet": 10, "Dame": 10, "Roi": 10}
        for i in couleur:
            for y in self.valeur:
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
        self.game_step = False
    
    def display(self):
        print("################")
        if  not self.game_step:
            print("Ta main: ")
            for card in self.card_joueur:
                print(card.valeur, "de ", card.couleur)
            print("###############")
            print("La main tu croupier: ")
            print(self.card_croupier[0].valeur, "de", self.card_croupier[0].couleur)
            print("hide ")
        elif self.game_step:
            print("Ta main: ")
            for card in self.card_joueur:
                print(card.valeur, "de ", card.couleur)
            print("La main tu croupier: ")
            for card in self.card_croupier:
                print(card.valeur, "de ", card.couleur)

    def action_joueur(self):
        print('Tu peux tirer une carte ou rester: (choisis en tappant "tirer" ou "stay")')
        choice = input()
        if choice.lower() == "tirer":
            self.tirer_carte(self.card_joueur)
            self.display()
            self.action_joueur()
        elif choice.lower() == "stay":
            self.game_step = True
        else:
            print('Pas compris')
            self.action_joueur()
        
    def action_croupier(self):
        valeur_croupier = 0
        for card in self.card_croupier:
            valeur_croupier += self.valeur[card.valeur]
        if valeur_croupier < 17:
            self.tirer_carte(self.card_croupier)
            self.action_croupier()
    
    def check_bust(self):
        valeur_croupier = 0
        valeur_joueur = 0
        for card in self.card_croupier:
            valeur_croupier += self.valeur[card.valeur]
        if valeur_croupier > 21:
            if "As" in  self.card_croupier:
                if valeur_croupier - 10 > 21:
                    print("Tu as gagnée!")
                    return False
                else:
                    pass
            else:
                print("Tu as gagnée! a")
                return False
        for card in self.card_joueur:
            valeur_joueur += self.valeur[card.valeur]
        if valeur_joueur > 21:
            if "As" in  self.card_joueur:
                if valeur_joueur - 10 > 21:
                    print("La bank a gagnée!")
                    return False
            else:
                print("La bank a gagnée!")
                return False
        return True

        
    def check_win(self):
        valeur_croupier = 0
        valeur_joueur = 0
        for card in self.card_croupier:
            valeur_croupier += self.valeur[card.valeur]
        for card in self.card_joueur:
            valeur_joueur += self.valeur[card.valeur]
        if valeur_croupier > valeur_joueur:
            print("La bank gagne!")
        elif valeur_joueur > valeur_croupier:
            print('Tu as gagné! ')
        else:
            print("Push")


    def play_again(self):
        print("Play again?(y/n)")
        choice = input()
        if choice.lower() == "y":
            self.init_game()
            return True
            
        else:
            return False


jeu = Jeu()

while True:
    jeu.display()
    jeu.action_joueur()
    jeu.action_croupier()
    jeu.display()
    if jeu.check_bust():
        jeu.check_win()
    jeu.play_again()




    

    