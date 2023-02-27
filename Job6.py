class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

loup = Animal()
print(loup.age, loup.prenom)
loup.vieillir()
loup.nommer("loulou")
print(loup.age, loup.prenom)