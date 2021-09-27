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
    
    def swap(self):
        x1=self.depiler()
        x2=self.depiler()
        self.empiler(x1)
        self.empiler(x2)
        return self

    
class File:
    def __init__(self):
        self.L=[]
    def vide(self):
        return self.L==[]
    def defile(self):
        return self.L.pop(0)
    def file(self,n):
        return self.L.append(n)
    def __repr__(self):
        return str(self.L)
    def taille(self):
        return len(self.L)
    def sommet(self):
        return self.L[0]