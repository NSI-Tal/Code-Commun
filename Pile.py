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