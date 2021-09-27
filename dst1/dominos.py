from random import randint

class Dominos:

    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def affiche_points(self):
        print("Face A: ", self.pointA, "Face B: ", self.pointB)

    def valeur(self):
        return(self.pointA + self.pointB)


def cree_pioche(n: int):
    return [Dominos(randint(1, 6), randint(1, 6)) for i in range(n)]
T

def domino_max(lst: list):
    max = lst[0]
    for i in lst:
        if i.valeur() > max.valeur():
            max = i
    return max

l= cree_pioche(7)
for i in l:
    print(i.affiche_points())

