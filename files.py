from Pile import *
from File import *

f1 = File()
f1.L = [0, 1, 1, 0, 1]

f2 = File()
f2.L = [2]


def croisement(f1, f2):
    f3 = File()
    while not (f1.vide() or f2.vide()):
        if f1.sommet() == 0:
            if f2.sommet() == 0:
                _extracted_from_croisement_10(f3, 0, f2, f1)
            else:
                _extracted_from_croisement_10(f3, 2, f2, f1)
        else:
            f3.file(1)
            f1.defile()

    if f1.vide():
        for _ in range(f2.taille()):
            f3.file(f2.defile())
    elif f2.vide():
        for _ in range(f1.taille()):
            f3.file(f1.defile())
    return f3

def _extracted_from_croisement_10(f3, arg1, f2, f1):
    f3.file(arg1)
    f2.defile()
    f1.defile()

def merge(f1, f2):
    while not f1.vide():
        f2.file(f1.defile())

    return f2

def impair_pair(f1):
    pair = File()
    impair = File()
    while not f1.vide():
        if f1.sommet() % 2 == 0:
            pair.file(f1.defile())
        else:
            impair.file(f1.defile())

    return merge(pair, impair)

f1 = File()
f1.L = [1, 5, 7, 3, 8, 10, 4, 6, 24, 35]
print(impair_pair(f1))