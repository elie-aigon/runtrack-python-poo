class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print("j'ai ", self.age, "ans")

    def bonjour(self):
        print('Hello')

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print('je vais en cours')

class Professeur(Personne):
    def __init__(self, matière):
        self.__matière = matière

    def enseigner(self):
        print('le cours va commencer')

prof = Professeur("python")
prof.modifierAge(40)
prof.bonjour()
prof.enseigner()


stud1 = Eleve()
stud1.bonjour()
stud1.allerEnCours()
stud1.modifierAge(15)
stud1.afficherAge()



