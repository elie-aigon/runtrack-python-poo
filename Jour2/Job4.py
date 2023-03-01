class Students:
    def __init__(self, nom, prénom, studNb):
        self.__nom = nom
        self.__prénom = prénom
        self.__studNb = studNb
        self.__credNb = 0
        self.__studentEval()

    def student_info(self):
        print("nom = ", self.__nom)
        print("prenom = ", self.__prénom)
        print("id = ", self.__studNb)
        print("lvl = ", self.__lvl)

    def add_credits(self):
        incrément = float(input("Combien voulez vous ajouter: "))
        if incrément > 0:
            self.__credNb += incrément
            self.__studentEval()
        print(self.__prénom, self.__nom, "points: ", self.__credNb, "points")
        
    def __studentEval(self):
        if int(self.__credNb) >= 90:
            self.__lvl = "Excellent"
        elif self.__credNb >= 80:
            self.__lvl = "TB"
        elif self.__credNb >= 70:
            self.__lvl = "bien"
        elif self.__credNb >= 60:
            self.__lvl = "passale"
        else:
            self.__lvl = "insuffisant"
        
JD = Students("Doe", "Jhon", 145)
JD.student_info()
JD.add_credits() 
JD.student_info()