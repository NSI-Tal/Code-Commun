class Point:

    nbr = 0
    
    def __init__(self,x:float, y:float, nom:str):
        self.x = x
        self.y = y
        self.nom = nom
        Point.nbr += 1

    def get_coordonnees(self):
        return self.x, self.y

    def set_coordonneess(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "{}({};{})".format(self.nom, self.x, self.y)

class Segment:

    def __init__(self, point1, point2):  
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return "[{};{}]".format(self.point1.nom, self.point2.nom)

    def longeur(self):
        return ((point1.x-point2.x)^2+ (point1.y-point2.y)^2)^0.5

class Cercle:

    def __init__(self, centre, rayon):
        self.centre = centre
        self.rayon = rayon

    def __repr__(self):
        return "C({};{})".format(self.centre, self.reyon)
        
    def contient(self, point):
        segment = Segment(self.centre, point)
        return segment.longueur() == self.rayon