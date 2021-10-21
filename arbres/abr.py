
from tkinter import *
from math import *

# =============================================================================
#                                       La classe
# =============================================================================

class Noeud:

    # Le constructeur
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None


    # Méthode qui permet d'afficher la valeur
    # de la racine avec la fonction print
    def __repr__(self):
        return str(self.value)

    def estFeuille(self):
        if not self.left and not self.right:
            return True
        else:
            return False

    def insert(self, valeur):
        if valeur < self.value:
            if self.left is None:
                self.left = Noeud(valeur)
                self.left.parent = self
            else:
                self.left.insert(valeur)
        elif valeur > self.value:
            if self.right is None:
                self.right = Noeud(valeur)
                self.right.parent = self
            else:
                self.right.insert(valeur)
    def parcours_infixe(self):
        if self:
            if self.left:
                self.left.parcours_infixe()
            print(self.value, end=' ')
            if self.right:
                self.right.parcours_infixe()

    def parcours_prefixe(self):
        if self:
            print(self.value, end=' ')
            if self.left:
                self.left.parcours_prefixe()
            if self.right:
                self.right.parcours_prefixe()

    def parcours_suffixe(self):
        if self:
            if self.left:
                self.left.parcours_suffixe()
            if self.right:
                self.right.parcours_suffixe()
            print(self.value, end=' ')


# =============================================================================
#                               Représentation graphique
# =============================================================================


# ------------------- cercle-------------------#
def cercle(canv,x,y,r,col,colf):
    """dessine un cercle graphique sur le canvas de centre (x,y) de rayon r de
    couleur col et de couleur de fond colf"""
    canv.create_oval(x-r,y-r,x+r,y+r,outline=col, fill=colf)
# ------------------- dessinenoeud-------------------#
def dessinenoeud(canv,x,y,r,noeud):
    """ dessine un noeud graphique : un cercle rempli avec un texte la dedans la valeur du noeud"""
    cercle(canv,x,y,r,"black","white")
    canv.create_text(x,y,text=noeud.value,fill="black")
# ------------------- centresuivant-------------------#
def centresuivant(x,y,r,m,dir):
    """ calcule la position de noeud suivant :
        on calcule a et b les décalages par rapport a la position actuelle x,y
        dir permet de spécifier:
             si c'est un fils gaucheon retranche le a
             Si c'est un fils droit  on ajoute le a  a x
             pour y on ajoute toujours b dans les deux cas.
              le m la distance entre les cercles : le noeud
        et ses descedants.
         """
    a=(2*r+m)*sin(pi/4)     # calcule le decalage sur l'axe des x : coordonnées polaire vers
                            #cordonnées cartesiennes
    b=(2*r+m)*cos(pi/4)     # de meme pour le decalage sur y l'angle d'ouverture est 45 °
    if dir=="l":            # dir pour left ou right cad fils gauche ou fils droit
        x1,y1=x-a,y+b       # on decale vers la gauche donc on retranche a de x et
                            # on ajoute b a y on descend vers le bas
    else:
        x1,y1=x+a,y+b       # on decale vers la droite donc on ajoute a de x
    return x1,y1
# ------------------- tracearbre-------------------#
def tracearbre(canv,x,y,r,m,noeud):
    """ trace l'arbre graphique recursivement"""
    pas=25                          # ce pas change permettant de reduire la distance entre les noeuds
                                    # autrement on aura des noeuds qui se superposent

    if noeud.estFeuille()==False:    # si le noeud n'est pas une feuille
        if noeud.right==None and noeud.left!=None :  # si il a un fils gauche mais pas de fils droit
            x1,y1=centresuivant(x,y,r,m,"l")         #recupération de la position du noeud fils
            canv.create_line(x,y,x1,y1,fill="black") # tracé d'une droite entre x,y et x1,y1
                                                        #cette fonction est dans la bibilothèque tkinter
            tracearbre(canv,x1,y1,r,m-pas,noeud.left)    #appel recursive pour traiter ce fils
        elif noeud.right!=None and  noeud.left==None :   #si il a un fils droit mais pas de fils gauche
            x1,y1=centresuivant(x,y,r,m,"r")             #recupération de la position du noeud fils
            canv.create_line(x,y,x1,y1,fill="black")     # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.right)   #appel recursive pour traiter ce fils
        else:                                            #si il a un fils gauche et un fils droit
            x1,y1=centresuivant(x,y,r,m,"l")            #recupération de la position du noeud fils gauche
            canv.create_line(x,y,x1,y1,fill="black")    # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.left)   #appel recursive pour traiter ce fils gauche
            x1,y1=centresuivant(x,y,r,m,"r")            #recupération de la position du noeud fils droit
            canv.create_line(x,y,x1,y1,fill="black")    # tracé d'une droite entre x,y et x1,y1
            tracearbre(canv,x1,y1,r,m-pas,noeud.right)  #appel recursive pour traiter ce fils droit
    dessinenoeud(canv,x,y,r,noeud)                      #tracé du noeud courant

# ------------------- graphicarbre-------------------#
def graphicarbre(noeud):
    """ fonction de tracée graphique d'un arbre """
    cwidth=650              # la largeur du canvas graphique
    cheight=400             # la hauteur du canvas
    couleurs=["red","green","bleu","white","black","cyan","magenta","yellow"]
    # fen est l'objet fenetre herité de la bibliotheque tkinter
    fen=Tk()
        # creation d'un bouton avec la commande fermer(quit) attaché Ã  la fenetre
    btn=Button(fen, text="Quitter",command=fen.destroy)
        # placement du bouton en bas de la fenetre
    btn.pack(side="bottom")
    #creation d'un panneau dans lequel on affichera l'arbre
    pan=LabelFrame(fen)
    # placement de ce panneau en faut de la fenetre
    pan.pack(side="top")
    # creation du canva graphique dans ce panneau
    canv=Canvas(pan,width=cwidth,height=cheight)
    #placement de ce canva en haut du panneau graphique
    canv.pack(side="top")
    #appel de la fonction de tracé graphique de l'arbre créer ci haut
    tracearbre(canv,cwidth//2,100,12,90,noeud)
    # actualisation de l'affichage graphique
    fen.mainloop()


# =============================================================================
#                                       création de l'arbre
# =============================================================================

bst = Noeud(6)
bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(9)
bst.insert(2)
bst.insert(7)
bst.insert(5)
graphicarbre(bst)