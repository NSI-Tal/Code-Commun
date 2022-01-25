class Pile:

    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def empiler(self, a):
        self.L.append(a)

    def depiler(self):
        return self.L.pop()

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[-1]
    
def creer_pile_vide():
    return Pile()

def est_vide(P):
    return P.L == [] 
    
def hauteur_pile(P):
    Q = Pile()
    n = 0
    while not est_vide(P):
        n += 1
        x = P.depiler()
        Q.empiler(x)
    while not est_vide(Q):
        x = Q.depiler()
        P.empiler(x)
    return n

def max_pile(P):
    Q = Pile()
    n = None
    while not est_vide(P):
        x = P.depiler()
        Q.empiler(x)
        if x > n:
            n = x
    while not est_vide(Q):
        x = Q.depiler()
        P.empiler(x)
    return n

def retourner(P, i):
    Q = creer_pile_vide()
    for i in range(hauteur_pile(P)):
        x = P.depiler()
        if i - j <= 0: # On arrive au i derniers elements
            Q.empiler(x)
            
 

pile = Pile()
pile.empiler(4)
pile.empiler(6)
pile.empiler(2)
pile.empiler(4)
pile.empiler(6)

print(hauteur_pile(pile))