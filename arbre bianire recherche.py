# Créé par .H., le 12/01/2022 en Python 3.7

class Noeud:

    def __init__(self,valeur):
        self.valeur = valeur
        self.e_g = None
        self.e_d = None
##je définie mon objet avec c'est caracteristique mon objet ici est un noeud
    def get_valeur(self):
        return(self.valeur)

    def get_enfant_g(self):
        return(self.e_g)

    def get_enfant_d(self):
        return(self.e_d)

##creation de mon arbre
racine = Noeud(14)
racine.e_g = Noeud(7)
racine.e_g.e_g = Noeud(4)
racine.e_g.e_d = Noeud(9)
racine.e_g.e_g.e_g = Noeud(8)
racine.e_g.e_g.e_d = Noeud(11)
racine.e_g.e_g.e_g.e_g = Noeud(10)
racine.e_g.e_g.e_g.e_d = Noeud(13)

racine.e_d = Noeud(24)
racine.e_d.e_g = Noeud(20)
racine.e_d.e_g.e_g = Noeud(18)
racine.e_d.e_g.e_d = Noeud(22)
racine.e_d.e_d = Noeud(30)
racine.e_d.e_d.e_g = Noeud(25)
racine.e_d.e_d.e_d = Noeud(38)
racine.e_d.e_d.e_d.e_g = Noeud(35)
racine.e_d.e_d.e_d.e_d = Noeud(40)

##fonction de recherche
def recherche(arbre,k):
    if arbre != None:
        if arbre.valeur == k:
            return True
        if arbre.valeur<k:
            return recherche(arbre.get_enfant_g(), k)
        if arbre.valeur>k:
            return recherche(arbre.get_enfant_d(), k)
    else:
        return False

##commande de recherche
k=3
print("il y a", k, "dans", recherche(racine,k))

##affiche mon arbre
def affiche(arbre):
    if arbre != None:
        return(arbre.get_valeur(), affiche(arbre.get_enfant_g()), affiche(arbre.get_enfant_d()))
print(affiche(racine))
