import sqlite3

def afficher_menu():
    """ première étape : afficher un menu """

    print(" 1. Consulter les informations d'un élément chimique ")
    print(" 2. Ajouter un élément chimique ")
    print(" 3. Modifier un élément chimique ")
    print(" 0. Quitter ")
    print(" Quel est votre choix ? ")

def lire_action():
    """ deuxième étape : saisir le choix

    Returns
    -------
    reponse : entier
    """
    reponse = 10
    while reponse not in (0, 1, 2, 3):
        afficher_menu()
        choix = input()
        reponse = int(choix)
    return reponse

def appli():
    """ troisième étape : on oriente en fonction du choix

    Returns
    -------
    None.

    """
    action = 10
    while action != 0:
        action = lire_action()
        if action == 1:
            print("Quelle est le nom de la base de données (n'oubliez pas l'extension)")
            base = input()
            action_afficher(base)
        elif action == 2:
            print("Quelle est le nom de la base de données (n'oubliez pas l'extension)")
            base = input()
            action_ajouter(base)
        elif action == 3:
            print("Quelle est le nom de la base de données (n'oubliez pas l'extension)")
            base = input()
            action_modifier(base)

def menu_attributs(nom_base, relation):
    """
    renvoie la liste des attributs dans une relation.

    Parameters
    ----------
    nom_base : str
        nom de la base de données.
    relation : str
        nom de la relation à explorer.

    Returns
    -------
    None.

    """
    connexion = sqlite3.connect(nom_base)
    curseur = connexion.execute('PRAGMA table_info(%s);' %relation)

    print(f"Les attributs de la table {relation} pouvant être affichés sont : ")

    for tuple in curseur:
        donnee = list(tuple)
        print(donnee)

    connexion.close()

def action_afficher(nom_base):
    """
    affiche une liste des informations correspondant à une requête

    Parameters
    ----------
    nom_base : str
        nom de la base de données.

    Returns
    -------
    None.

    """
    print("Quelle est votre requête ? ")
    requete = input()

    connexion = sqlite3.connect(nom_base)
    curseur = connexion.execute(requete)

    print("Les valeurs sont : ")

    for tuple in curseur:
        donnee = list(tuple)
        print(donnee)

    connexion.close()

def action_ajouter(nom_base):
    """
    ajoute un enregistrement à la relation d'une base de données

    Parameters
    ----------
    nom_base : str
        nom de la base de données.

    Returns
    -------
    None.

    """


def action_modifier(nom_base):
    """
    modifie un enregistrement dans la relation d'une base de données

    Parameters
    ----------
    nom_base : str
        nom de la base de données.

    Returns
    -------
    None.

    """

