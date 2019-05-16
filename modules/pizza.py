class Pizza(object):
    def __init__(self, name):
        self.name = name
        self.prix = 0
        self.ingredients = []
        self.qte = 0

    def getName(self):
        return self.name

    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def removeIngredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def fixerPrix(self, prix):
        self.prix = prix

    def addQuantite(self, qte):
        self.qte += qte

    def getQuantite(self):
        return self.qte

    def __repr__(self):
        return f"Pizza : {self.name} {self.ingredients} prix: {self.prix} euros"
