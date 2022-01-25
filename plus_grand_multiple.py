# -*- coding: utf-8 -*-
# plus grand multiple de a inférieur à b

## vérification de la table de a

def sousmultiple(a,b):
    n=0 # premier multiple de a
    while n<=b:
        n=n+a # balayage de la table de a
    return n-a # recul au premier multiple inférieur ou égal à b

## utilisation de la division euclidienne

def sousmultiple2(a,b):
    quotient = b//a # calcul du quotient
