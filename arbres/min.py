def noeud(nom, fg=None, fd=None):
    return {"racine": nom, "fg": fg, "fd": fd}


# création des noeuds
k = noeud("k")
f = noeud("f")
e = noeud("e", k, None)
b = noeud("b", e, f)
m = noeud("m")
j = noeud("j", m, None)
i = noeud("i")
d = noeud("d", i, j)
h = noeud("h")
c = noeud("c", None, h)
a = noeud("a", c, d)
racine = noeud("r", a, b)

# création de l"arbre
def construit(arbre):
    if arbre is None:
        return []
    else:
        return [arbre["racine"], construit(arbre["fg"]), construit(arbre["fd"])]
arbre1 = construit(racine)
print(arbre1)
