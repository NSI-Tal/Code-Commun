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
def longueurListe(L):
    n = 0
    while not(L.estVide()):
        n += 1
        L = L.cdr()
    return n
def listeElements(L):
    t = []
    while not(L.estVide()):
        t.append(L.car())
        L = L.cdr()
    return t
def ajouteenTete(L,nb):
    L=cons(nb,L)
    return L
def supprEnTete(L):
    x=L.car()
    L=cons(L.cdr.car(),L.cdr().cdr())
    return(L)

nil =Liste(None)
L = cons(5,cons(4,cons(3, cons(2,cons(1,cons(0,nil))))))
x=L.car()
L=cons(L.cdr().car(),L.cdr().cdr())
