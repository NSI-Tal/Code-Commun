from copy import deepcopy
import matplotlib as plt

laby = [[0,1,0,0,0,0],
        [0,1,1,1,1,0],
        [0,1,0,1,0,0],
        [0,1,0,1,1,0],
        [0,1,1,0,1,0],
        [0,0,0,0,1,0]]

T = deepcopy(laby)
T[3][2] = 'hello'

for ligne in laby:
    print(ligne)
print("----------------")
for ligne in T:
    print(ligne)
lignes= len(laby)
colonnes = len(laby[0])

def voisins(T,v):  # sourcery skip: merge-nested-ifs
    V = []
    i,j = v[0],v[1]
    for a in (-1,1):
        if 0<= i + a < lignes:
            if T[i+a][j] == 1:
                V.append((i+a,j))
        if 0<= j + a <colonnes:
            if T[i][j+a] == 1:
                V.append((i,j+a))
    return V

print(voisins(laby,(0,0)))

