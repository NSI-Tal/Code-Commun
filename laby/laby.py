from copy import deepcopy
from matplotlib.pyplot import *

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

laby=[[0,1,0,0,0,0],
      [0,1,0,1,1,0],
      [0,1,0,1,0,0],
      [0,1,0,1,1,0],
      [0,1,1,1,1,1],
      [0,0,0,0,1,0]]

lignes=len(laby[0])
colonne=(len(laby))

T=deepcopy(laby)


for ligne in laby:
    print(ligne)
print("---------------")
for ligne in T:
    print(ligne)

def voisins(T,v):
    """   
    Parameters
    ----------
        T: list
            Tableau representant le labyrinthe
        v: tuple
            coordonée de la position actuelle dans le labyrinthe

        retourne les coordonée des cases 1 autour de v
    """
    assert (type(v)==tuple),'mauvais coordoné'
    assert (type(T)==list),'mauvais tableau'
    V=[]
    i,j=v[0],v[1]
    for a in (-1,1):
        if 0<=i+a<lignes:
            if T[i+a][j]==1:
                V.append((i+a,j))
        if 0<=j+a<colonne:
            if T[i][j+a]==1:
                V.append((i, j+a))
    return V
#print(voisins(T,(0,1)))

def parcours(laby, entree, sortie):
    T=deepcopy(laby)
    p=Pile()
    v=entree
    vois=v
    T[v[0]][v[1]]=-1
    recherche=True
    while recherche==True:
        vois=voisins(T,v)
        if len(vois)==0:
            if p.taille()==0:
                return False
            else:
                v=p.depiler()
        else:
            p.empiler(v)
            v=vois[0]
            T[v[0]][v[1]]=-1
            if v==sortie:
                p.empiler(v)
                recherche=False
    return p

print(parcours(laby,(0,1),(5,4)))

def tracer(laby,p):
    if p==False:
        return('no way')
    fig, axes=subplots(nrows=1, ncols=2)
    axes[0].matshow(laby)
    axes[1].matshow(laby)
    for i in p.L:
        laby[i[0]][i[1]]=-1
    axes[1].matshow(laby)
    show()
print(tracer(laby,parcours(laby,(0,1),(5,4))))