def puissance():
    n = 0
    u = 1
    while u < 5:
        n = n + 1
        u = u + 1
    return "n = {}, et u = {}".format(n, u)

def premier(n):
    reponse = True
    for i in range(2, 10):
        if n %vd i == 0:
            reponse = False
    return reponse

print(premier(16))