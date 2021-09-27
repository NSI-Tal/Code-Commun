class File:
    def __init__(self):
        self.L = []

    def vide(self):
        return self.L == []

    def defile(self):
        return self.L.pop(0)

    def file(self, n):
        return self.L.append(n)

    def __repr__(self):
        return str(self.L)

    def taille(self):
        return len(self.L)

    def sommet(self):
        return self.L[0]
