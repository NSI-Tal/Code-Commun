def fuite_de_clavier(n, k, chaine):
    """
    :param n: taille de la chaîne
    :type n: int
    :param k: taille du mot de passe
    :type k: int
    :param chaine: la chaîne contenant le mot de passe
    :type chaine: list[str]
    """
    strMin = "abcdefghijklmnopqrstuvwxyz"
    strMaj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    strNb = "1234567089"
    strSpe = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" + '"'
    print(strSpe)
    
    possible = []
    for char in range(len(chaine) - k + 1):
        chaineDeK = ""
        for i in range(char, char + k):
            chaineDeK += chaine[i]
        if(
            any(x in chaineDeK for x in strSpe) and
            any(x in chaineDeK for x in strMin) and
            any(x in chaineDeK for x in strNb) and
            any(x in chaineDeK for x in strMaj)
            ):
            possible.append(chaineDeK)
    print(len(possible))

    pass


fuite_de_clavier(10, 4, "!84cDc1s_p")
