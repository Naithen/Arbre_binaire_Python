class noeud():
    def __init__(self,nom):
        self.name=nom
        self.enfant_gauche_objet= None
        self.enfant_droit_objet=None

    def get_enfant_gauche(self):
        return self.enfant_gauche_objet
    def get_enfant_droit(self):
        return self.enfant_droit_objet
    def set_enfant_gauche(self,objet):
        self.enfant_gauche_objet=objet
    def set_enfant_droit(self,objet):
        self.enfant_droit_objet=objet

##############Creation de l'arbre##############

racine = noeud("A")
b = noeud("B")
c = noeud("C")
d = noeud("D")
e = noeud("E")
f = noeud("F")
racine.enfant_gauche_objet = b
racine.enfant_droit_objet = c
b.enfant_droit_objet = d
b.enfant_gauche_objet = f
c.enfant_droit_objet = e

##print(racine.get_enfant_gauche().name)
##print(racine.enfant_gauche_objet.name)

###############parcours profondeur infix (recursif)##############

def parcours_infixe(arbre):
    if arbre != None:
        parcours_infixe(arbre.enfant_gauche_objet)
        print(arbre.name)
        parcours_infixe(arbre.enfant_droit_objet)

print("parcours infixe")
parcours_infixe(racine)

###############parcours profondeur prefix (recursif)##############

def parcours_prefix(arbre):
    if arbre != None:
        print(arbre.name)
        parcours_prefix(arbre.enfant_gauche_objet)
        parcours_prefix(arbre.enfant_droit_objet)

print("parcours prefix")
parcours_prefix(racine)

###############parcours profondeur suffixe (recursif)##############

def parcours_suffixe(arbre):
    if arbre != None:
        parcours_suffixe(arbre.enfant_gauche_objet)
        parcours_suffixe(arbre.enfant_droit_objet)
        print(arbre.name)

print("parcours suffixe")
parcours_suffixe(racine)