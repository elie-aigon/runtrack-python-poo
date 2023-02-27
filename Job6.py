class Point:
    def __init__(self):
        self.x = 5
        self.y = 6

    def affLesPoints(self):
        print(self.x, self.y)

    def affX(self):
        print(self.x)

    def affY(self):
        print(self.y)

    def changeX(self, new_X):
        self.x = new_X

    def changeY(self, new_Y):
        self.y = new_Y

point = Point()
point.affLesPoints()
point.affX()
point.affY()
point.changeX(4)
point.affX()
point.changeY(9)
point.affY()