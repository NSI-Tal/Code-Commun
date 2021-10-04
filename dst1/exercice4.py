def apartient(val, liste):
    if val==liste[0]:
        return True
    if len(liste)==0:
        return False 
    else: 
        return appartient(val,liste)

def nbr_de_chiffres(n):
    mot = str(n)

    if mot == "":
        return 0
        
    return 1+ nbr_de_chiffres(mot[1:])

nb1 = 0
def nbr_de_bit(n):
    global nb1

    def binaire(nb):
        global nb1

        if nb == 0:
            return""

        nb1 = nb1+1
        
        return binaire(nb//2)+str(nb%2)

    binaire(n)

    return nb1

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste[1])