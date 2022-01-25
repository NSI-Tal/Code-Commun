def forceBrute(objets, w):
    """
    Résolution du problème du sac à dos par force brute
    objets est une liste d'objets du type (poids,valeur)
    w est le poids maximum entrant dans le sac
    Un nombre en binaire permet d'indiquer quels objets sont sélectionnés.
    """
    combinaison = -1
    n = len(objets)
    valeurmax = 0
    combinaisonmax = 0
    for i in range(2**n):
        poids = 0
        valeur = 0
        combinaison += 1
        combiBinaire = bin(combinaison)[2:]
        combiBinaire = (n-len(combiBinaire))*'0' + \
            combiBinaire  # avec n chiffres
        for j in range(n):
            if combiBinaire[j] == '1':
                poids += objets[j][1]
                if poids > w:
                    break
                valeur += objets[j][0]
        else:
            if valeur > valeurmax:
                valeurmax = valeur
                combinaisonmax = combiBinaire
    contenuSac = []
    for j in range(n):
        if combinaisonmax[j] == '1':
            contenuSac.append(objets[j])
    return valeurmax, contenuSac


"""
Programmation dynamique
"""


def tableau_kp_dynamique(objets, w):
    """
    Résolution du problème du sac à dos par programmation dynamique
    >>> tableau_kp_dynamique([(3, 2), (8, 10), (2, 2), (8, 1), (4, 6), (6, 6)], 10)
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 8],
    [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 8],
    [0, 8, 8, 11, 11, 13, 13, 13, 13, 13, 13],
    [0, 8, 8, 11, 11, 13, 13, 13, 13, 15, 15],
    [0, 8, 8, 11, 11, 13, 13, 14, 14, 17, 17]]
    """
    T = [[0]*(w + 1) for i in range(len(objets))]

    liste = []

    for i in range(len(objets)):
        v, p = objets[i]
        for j in range(w + 1):
            T[i][j] = T[i - 1][j] if j < p else max(T[i - 1][j], v + T[i - 1][j - p])
    return T


def kp_dynamique(objets, w):
    
    """
    Renvoie la valeur maximale et une liste d'objets réalisant cette valeur
    en utilisant le tableau renvoyé par la fonction tableau_kp_dynamique
    """
    tab = tableau_kp_dynamique(objets, w)
    lobj = []
    vmax = tab[len(objets) - 1][w]
    i = len(objets) - 1
    j = w
    while(i >= 0):
        if(tab[i - 1][j] == tab[i][j]):
            i -= 1
        else:
            lobj.append(objets[i])
            i -= 1
            j = j - objets[i][1]
    return lobj
print(kp_dynamique([(3, 2), (8, 10), (2, 2), (8, 1), (4, 6), (6, 6)], 10))
            
