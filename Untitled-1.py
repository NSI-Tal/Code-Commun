'''
def vide():
    return None
def cons(x,L):
    return(x,L)
def ajouteEnTete(L,x):
    return cons(x,L)
def supprEnTete(L):
    return (L[0],L[1])
def estVide(L):
    return L is None
def compte(L):
    if estVide(L):
        return 0
    return 1 + compte(L[1])
'''

class Cellule:
    def __init__(self, tete, queue):
        self.car = tete
        self.cdr = queue
class Liste:
    def __init__(self,c):
        self.cellule= c
    def estVide(self):
        return self.cellule is None
    def car(self):  # sourcery skip: de-morgan
        assert not (self.cellule is None), 'Liste vide'
        return self.cellule.car
    def cdr(self):  # sourcery skip: de-morgan
        assert not(self.cellule is None),'Liste est vide'
        return self.cellule.cdr
def cons(tete,queue):
    return Liste(Cellule(tete,queue))

nil =Liste(None)
L = cons(5,cons(4,cons(3, cons(2,cons(1,cons(0,nil))))))
print (L.estVide())

            
