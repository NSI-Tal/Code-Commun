from math import inf

graphe = {
    'A': {'B': 3, 'E': 3, 'C': 3, 'D': 2},
    'B': {'A': 3, 'C': 5, 'D': 4, 'E': 2},
    'C': {'A': 3, 'B': 5, 'D': 2, 'S': 2},
    'D': {'A': 2, 'B': 4, 'C': 2, 'S': 2},
    'E': {'A': 3, 'B': 2},
    'S': {'C': 2, 'D': 2}
}

inf = 1.7976931348623157e+308


def dijkstraCours():
    depart = 'E'
    arrivee = 'S'

    marque = {}

    for sommet in graphe:
        marque[sommet] = inf
    marque[depart] = 0

    non_selectionnes = [sommet for sommet in graphe]

    pere = {depart: None}

    while non_selectionnes:
        marquePlusPetite = inf

        for s in non_selectionnes:
            if marque[s] < marquePlusPetite:
                marquePlusPetite = marque[s]
                sommetPlusPetit = s

        if sommetPlusPetit == arrivee:
            break

        non_selectionnes.remove(sommetPlusPetit)
        voisinAVisiter = [
            sommet for sommet in graphe[sommetPlusPetit] if sommet in non_selectionnes]

        for sommet in voisinAVisiter:
            p = marque[sommetPlusPetit] + graphe[sommetPlusPetit][sommet]
            if p < marque[sommet]:
                marque[sommet] = p
            pere[sommet] = sommetPlusPetit

    print("La distance de {} a {} est de longueur {}".format(
        depart, arrivee, marque[arrivee]))

    chemin = arrivee
    sommet = arrivee

    while pere[sommet] != None:
        chemin = pere[sommet] + ' - ' + chemin
        sommet = pere[sommet]

    print()
    print("Le chemin de {} a {}: {}".format(depart, arrivee, chemin))


def mini(listeSommet, marque):
    sommetPlusPetit = ''
    marqueLaPlusPetite = inf

    for sommet in listeSommet:
        if marque[sommet] < marqueLaPlusPetite:
            marqueLaPlusPetite = marque[sommet]
            sommetPlusPetit = sommet

    return str(sommetPlusPetit)


def dijkstra(graphe, depart, arrivee):

    non_selectionnes = [sommet for sommet in graphe]
    pere = {depart: None}

    marque = {sommet: inf for sommet in graphe}
    marque[depart] = 0

    while non_selectionnes != {}:

        # Selection du plus petit
        sommetPlusPetit = mini(non_selectionnes, marque)

        if sommetPlusPetit == arrivee:
            break

        print(sommetPlusPetit)
        print(non_selectionnes)
        non_selectionnes.remove(sommetPlusPetit)


dijkstra(graphe, "A", "S")
