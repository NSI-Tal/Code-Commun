def nombre_chiffres(n):
    return len(str(n))

def appartient(v, t, i=0):
    if i >= len(t):
        return False
    return True if (t[i] == v) else appartient(v, t, i + 1)

def coeff(n, p):
    return 1 if p in [0, n] else coeff(n - 1, p - 1) + coeff(n - 1, p)
    
    