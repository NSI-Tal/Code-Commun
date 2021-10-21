import sqlite3

connexion = sqlite3.connect('ludotheque.db')
connexion.execute("PRAGMA foreign_keys = ON")

curseur = connexion.execute("SELECT * FROM Editeur")

for tuple in curseur:
    print(tuple)

connexion.commit()

connexion.close()
