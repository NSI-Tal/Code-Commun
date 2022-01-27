class Cellule:
    
    def __init__(self, valeur, suivant):
        self.valeur = valeur
        self.suivant = suivant
        
class Liste:
    
    def __init__(self, cellule):
        self.cellule = cellule
        
    def __str__(self):
        if self.est_vide():
            raise IndexError("Liste vide")
        l = self.cellule
        while not self.est_vide():
            print(str(l.valeur) + "-> ", end="")
            l = l.suivant
              
    def est_vide(self):
        return self.cellule is None
        
    def tete(self):
        if self.est_vide():
            raise IndexError("Liste vide")
        return self.cellule.valeur
        
    def queue(self):
        return self.cellule.suivant
        
def cons(v, l):
    return Liste(Cellule(v, l.cellule))

l1 = Liste(Cellule(3, Cellule(2, Cellule(4, Cellule(7, None)))))
print(l1)