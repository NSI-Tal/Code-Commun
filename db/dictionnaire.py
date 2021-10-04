# -*- coding: utf-8 -*-

# =============================================================================
# Import des modules
# =============================================================================

import doctest
import copy

# =============================================================================
# Définition des constantes
# =============================================================================

liste_a_tester_1 = [{"auteur": "Maupassant", "titre": "Bel-Ami", "dispo": True},
                  {"auteur": "Balzac", "titre": "Eugénie Grandet", "dispo": True}]
bibliotheque = [{"nom_auteur": "Bussi",
                 "prenom_auteur": "Michel",
                 "titre": "On La Trouvait Plutôt Jolie",
                 'nbre_pages': 544,
                 "editeur": "Pocket",
                 "annee": 2018,
                 "type": "Roman",
                 "dispo": True},
                {"nom_auteur": "Bussi",
                 "prenom_auteur": "Michel",
                 "titre": "J'ai Dû Rêver Trop Fort",
                 'nbre_pages': 480,
                 "editeur": "Presses De La Cité",
                 "annee": 2019,
                 "type": "Roman",
                 "dispo": True},
                {"nom_auteur": "Bussi",
                 "prenom_auteur": "Michel",
                 "titre": "Le Temps est Assasin",
                 'nbre_pages': 400,
                 "editeur": "Presses De La Cité",
                 "annee": 2016,
                 "type": "Roman",
                 "dispo": True},
                {"nom_auteur": "Houellebecq",
                 "prenom_auteur": "Michel",
                 "titre": "La Carte Et Le Territoire",
                 'nbre_pages': 496,
                 "editeur": "Flammarion",
                 "annee": 2016,
                 "type": "Roman",
                 "dispo": True}]
cles_bibliotheque = ['nom_auteur', 'prenom_auteur', 'titre', 'nbre_pages', 'editeur', 'annee', 'type', 'dispo']

# =============================================================================
# Définition des fonctions
# =============================================================================

def recherche(liste_dico, ensemble):
    """
    Renvoie la liste des dictionnaires contenant l'ensemble clé/valeur
    et une liste vide sinon.

    Parameters
    ----------
    liste_dico : une liste de dictionnaires
        les dictionnaires dans lequel on fait la recherche.
    ensemble : un tuple
        la clé de recherche et la valeur associée

    Returns
    -------
    resultat : une liste de dictionnaires
        les dictionnaires associés à l'ensemble clé / valeur
        ou une liste vide si la clé ou la valeur n'existe pas.

    Exemples
    --------
    >>> recherche(liste_a_tester_1, ("titre", "Bel-Ami"))
    [{'auteur': 'Maupassant', 'titre': 'Bel-Ami', 'dispo': True}]
    >>> recherche(liste_a_tester_1, ("titre", "Le père goriot"))
    []
    """
    resultat = []
    # On s'affranchit des majuscules/minuscules lors de la frappe
    item_recherche = (ensemble[0].lower(), ensemble[1].title())

    for dico in liste_dico:
        print(resultat)
    return resultat

def emprunt(liste_dico, ensemble):
    """

    Modifie le dictionnaire pour indiquer que l'ouvrage n'est plus disponible
    à l'emprunt'

    Parameters
    ----------
    liste_dico : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.
    ensemble : un tuple
        la clé de recherche et la valeur associée

    Returns
    -------
    nouvelle_liste : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.

    Exemple
    -------
    >>> emprunt([{'titre': 'Bel-Ami', 'dispo': True}, {'titre': 'Eugénie Grandet', 'dispo': True}], ("titre", "Bel-Ami"))
    [{'titre': 'Bel-Ami', 'dispo': False}, {'titre': 'Eugénie Grandet', 'dispo': True}]
    """
    nouvelle_liste = []
    for dico in liste_dico:
        for element in dico.items():
            if element == ensemble:
                dico["dispo"] = False
        nouvelle_liste.append(dico)
    return nouvelle_liste

def saisie(liste_dico, liste_cles, liste_valeurs):
    """
    Ajoute un nouvel ouvrage à la liste

    Parameters
    ----------
    liste_dico : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.
    liste_cles : une liste de chaînes de caractères
        La liste des clés du dictionnaire.
    liste_valeurs : une liste
        l'ensemble des valeurs associées aux clés.

    Returns
    -------
    nouvelle_liste : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.

    Exemple
    -------
    >>> saisie([{'auteur': 'Maupassant', 'titre': 'Bel-Ami', 'dispo': False}], ['auteur', 'titre', 'dispo'], ['Bernard Minier', 'la vallée', True])
    [{'auteur': 'Maupassant', 'titre': 'Bel-Ami', 'dispo': False}, {'auteur': 'Bernard Minier', 'titre': 'La Vallée', 'dispo': True}]

    """
    dico = {}
    nouvelle_liste = copy.deepcopy(liste_dico)
    for i in range(len(liste_cles)):
        if isinstance(liste_valeurs[i], str):
            ma_valeur=liste_valeurs[i].title()
        else:
            ma_valeur = liste_valeurs[i]
        dico[liste_cles[i]] = ma_valeur
    nouvelle_liste .append(dico)
    return nouvelle_liste

def supprime(liste_dico, ensemble):
    """
    supprime un dictionnaire de la liste de dictionnaires

    Parameters
    ----------
    liste_dico : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.
    ensemble : un tuple
        la clé de recherche et la valeur associée

    Returns
    -------
    nouvelle_liste : une liste de dictionnaires
        les dictionnaires associés aux ouvrages.

    Exemple
    -------
    >>> supprime([{'auteur': 'Maupassant', 'dispo': False}, {'auteur': 'Minier', 'dispo': True}], ('auteur', 'Maupassant'))
    [{'auteur': 'Minier', 'dispo': True}]
    """
    nouvelle_liste = []
    item_recherche = (ensemble[0].lower(), ensemble[1].title())
    for dico in liste_dico:
        est_present = True
        for element in dico.items():
            if element == item_recherche:
                est_present = False
        if est_present:
            nouvelle_liste.append(dico)
    return nouvelle_liste




def fonction(dicto):
    for i in dicto.items():
        dicto[i[0]]=str(i[1])
