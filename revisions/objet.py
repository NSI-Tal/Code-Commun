class Pile:
    def __init__(self):
        self.pile = []
        
    def est_vide(self):
        return self.pile == []
    
    def empiler(self, e):
        self.pile.append(e)
        
    def depile(self):
        return self.pile.pop()
    
    def nb_elements(self):
        return len(self.pile)
    
    def afficher(self):
        for i in range(self.nb_elements()):
            print(self.pile[i], end=" ")
            
def etendre(pile1, pile2):
    while not pile2.est_vide():
        x = pile2.depile()
        pile1.empiler(x)
    return pile1

pile1 = Pile()
pile1.empiler(7)
pile1.empiler(5)
pile1.empiler(2)
pile1.empiler(3)

pile2 = Pile()
pile2.empiler(1)
pile2.empiler(3)
pile2.empiler(4)

pile1.afficher()
pile2.afficher()