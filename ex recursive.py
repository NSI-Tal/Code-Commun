# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:04:39 2021

@author: Admin
"""

#ex1:
    
def somme(m,n):
    if n==0:
        return m
    return somme(m,n-1)+1

#ex2
def longueur(mot):
    if mot=="":
        return 0
    return 1+ longueur(mot[1:])

#ex4

def binaire(nb):
    if nb==0:
        return""
    return binaire(nb//2)+str(nb%2)

#ex 7
def appartient(valeur, liste, indice):
    assert(type(liste)==list), "La liste n'est pas une liste"

    if len(liste)<indice:
        return False
    return True if valeur == liste[indice-1] else appartient(valeur,liste,indice+1)





def pyramide(chaine, n):
    for i in range(1,n+1):
        chaine =chaine*i
        print(chaine)

def syracus(u_n):

    if u_n>1:

        if u_n%2==0:
            print(u_n/2)
            syracus(u_n/2)
        else:
            print (3*u_n +1)
            syracus(3*u_n +1)



def u_n(n):
    return 1 if n==0 else ((2*(v_n(n-1))+u_n(n-1)))
    

def v_n(n):
    return -1 if n==0 else (2*u_n(n-1))+v_n(n-1)







        
    
