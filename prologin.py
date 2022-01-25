def listMax(l1, l2):
    if(len(l1) == len(l2)):
        return [l1, l2] if sum(l1) >= sum(l2) else [l2, l1]
    else:
        return [l1, l2] if len(l1) > len(l2) else [l2, l1]


def resoudre(x, n, l):
    """
    :param x: le nombre magique
    :type x: int
    :param n: la longueur du code la Matriks
    :type n: int
    :param l: le code de la Matriks
    :type l: list[int]
    """
    sub = []
    best = [[], []]
    for i in range(n+1):
        for j in range(i + 1, n + 1):
            if(x % sum(l[i:j]) == 0):
                sub.append(l[i:j])
    print(sub)
    for i in range(len(sub)):
        for j in range(len(sub)):
            if(sum(sub[i]) * sum(sub[j]) == x):
                if(len(sub[i]) + len(sub[j]) > len(best[0]) + len(best[1])):
                    best = listMax(sub[i], sub[j])

    if(best == [[], []]):
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x) for x in best[0]))
        print(" ".join(str(x) for x in best[1]))
    pass


resoudre(105, 5, [1, 2, 3, 4, 5])
