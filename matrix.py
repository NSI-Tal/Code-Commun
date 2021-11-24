g = dict()
g["a"] = ["b", "c"]
g["b"] = ["a", "d", "e"]
g["c"] = ["a", "d"]
g["d"] = ["b", "c", "e"]
g["e"] = ["b", "d", "f", "g"]
g["f"] = ["e", "g"]
g["g"] = ["e", "f", "h"]
g["h"] = ["g"]

A1 = [[0, 1, 1, 0, 0, 0, 0, 0],
      [1, 0, 0, 1, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 0],
      [0, 1, 1, 0, 1, 0, 0, 0],
      [0, 1, 0, 1, 0, 1, 1, 0],
      [0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 1, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 0]]

def deg_sommet(G, s):
    return len(G[s])

def plusGrandSommet(G):
    lsa = G.keys()
    maxiNbr = 0
    maxiI = ""
    for keys in G.keys():
        maxiNbr = max(deg_sommet(G, keys), maxiNbrp)
        maxiI = keys
    return keys

print(plusGrandSommet(g))