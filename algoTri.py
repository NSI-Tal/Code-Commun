import random
import time
import matplotlib.pyplot as plt

def genere_tableau(n):
    return [ random.random() for _ in range(n) ]

def temps_tri(t, algo_tri):
    debut = time.time()
    algo_tri(t)
    return time.time() - debut

def triSelection(l):
    for i in range(len(l) - 1):
        k = i
        for j in range(i + 1, len(l)):
            if l[j] < l[k]:
                k = j
        l[i], l[k] = l[k], l[i]
    return l

def triInsertion(l):
    for i in range(2, len(l)):
        j = i
        while(j > 1 and l[j - 1] > l[j]):
            l[j - 1], l[j] = l[j], l[j - 1]
            j = j - 1
    return l

def recuTriFusion(l):
    if(len(l) <= 1):
        return l
    midLenList = int(len(l) / 2)
    l1 = l[:midLenList]
    l2 = l[midLenList:]

    return recFusion(recTriFusion(l1), recTriFusion(l2))

def recFusion(l1, l2):
    if(l1 == []):
        return l2
    if(l2 == []):
        return l1
    if(l1[0] < l2[0]):
        return [ l1[0] ] + recFusion(l1[1:], l2)
    else:
        return [ l2[0] ] + recFusion(l1, l2[1:])

def fusion(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    l = [] * (n1 + n2)
    i1 = 0
    i2 = 0
    while(l1 != [] and l2 != []):
        if(l1[i1] < l2[i2]):
            l[i1 + i2] = l1[i1]
            i1 += 1
        else:
            l[i1 + i2] = l2[i2]
            i2 += 1
    while l1 != []:
        l[i1 + i2] = l1[i1]
        i1 += 1
    while l2 != []:
        l[i1 + i2] = l2[i2]
        i2 += 1
    return l


def triFusion(l):
    n = len(l)
    if n > 1:
        l1 = [ l[i] for i in range(0, n//2) ]
        l2 = [ l[i] for i in range(0, n//2) ]
        return fusion(l1, l2)
    else:
        return tab


