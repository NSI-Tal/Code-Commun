def est_vide(l):
    return l is None

def tete(l):
    if est_vide(l):
        raise IndexError("Liste vide")
    return l[0]

def queue(l):
    if est_vide(l):
        raise IndexError("Liste vide")
    return l[1]
    
def cons(valeur, liste):
    return (valeur, liste)

def approche_recursive(l):
    if est_vide(l):
        raise IndexError("Liste vide")
    else:
        print(tete(l))
        return approche_recursive(l[1])
    
def approche_iterative(l):
    l1 = l
    while not est_vide(l):
        t = tete(l)
        print(t)
        l = queue(l)
        
def longueur(l):
    if est_vide(l):
        return 0
    count = 0
    while not est_vide(l):
        count += 1
        l = queue(l)
    return count
            
def appartient(v, l):
    if est_vide(l):
        return False
    while not est_vide(l):
        if l[0] == v:
            return True
        l = queue(l)
    return False

def n_ieme(i, l):
    if est_vide(l):
        raise IndexError("Liste vide")
    index = 0
    while not est_vide(l):
        if l[0] == i:
            return index
        index += 1
        l = queue(l)
    raise IndexError("Indice non trouvé")
