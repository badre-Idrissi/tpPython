class Menu(object):
    def __init__(self):
        self.pizzas = []

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def removePizza(self, pizza_name):
        for pizza in self.pizzas:
            if pizza.getName() == pizza_name:
                self.pizzas.remove(pizza)

    def getPizza(self, pizzaname):
        for pizza in self.pizzas:
            if pizza.getName() == pizzaname:
                return pizza


    def __repr__(self):
        s = "___ Menu ___\n\n"
        for pizza in self.pizzas:
            s += "\t" + str(pizza) + "\n"
        s += "___________"
        return s


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

menu = Menu()


def saveMenu(file_path, menu):
    ##sauvegarder le menu dans le fichier file_path
    fichier = open(file_path, 'w')
    fichier.write("menu :\n")
    fichier.write(str(menu))
    fichier.close()


def getMenuFromFile(file_path):
    ##recuperer le menu du fichier file_path
    print("getMenu")


def helpAdmin():
    print(""" Help :
				- addPizza pizzaName (ajouter une pizza au menu)
				- addIngredient pizzaName ingredient (ajouter un ingrédient à une pizza)
				- addPrix pizzaName prix (ajouter un prix à une pizza)
				- addQte pizzaName qte (ajouter une qte à une pizza)
				- exit (sortir du menu admin)
		""")


def addPizza(option):
    global menu
    _, pizzaName = option.split(" ")
    menu.addPizza(Pizza(pizzaName))


def addIngredient(option):
    global menu
    _, pizzaname, ingredient = option.split(" ")
    menu.getPizza(pizzaname).addIngredient(ingredient)


def addPrix(option):
    global menu
    _, pizzaname, prix = option.split(" ")
    menu.getPizza(pizzaname).fixerPrix(int(prix))


def addQte(option):
    global menu
    _, pizzaname, quantite = option.split(" ")
    menu.getPizza(pizzaname).addQuantite(int(quantite))


def helpClient():
    print(""" Help :
				- menu (afficher le menu)
				- manger pizzaName (manger une pizza)
				- exit (sortir du restaurant)
			""")


def displayMenu():
    global menu
    print(menu)


def manger(action):
    global menu
    _, pizza = action.split(" ")
    if menu.getPizza(pizza).getQuantite()>0:
        print("bonap")
        menu.getPizza(pizza).addQuantite(-1)
    else:
        print("pizza non disponible")


while True:
    login = input("login : ")
    if login == "exit":
        break
    if login == "admin":
        while True:
            option = input("choisir une option : ")
            if option == "exit":
                break
            if option == "help":
                helpAdmin()
            # Traiter les commandes admin
            if option.startswith("addPizza"):
                addPizza(option)
            if option.startswith("addIngredient"):
                addIngredient(option)
            if option.startswith("addPrix"):
                addPrix(option)
            if option.startswith("addQte"):
                addQte(option)
            if option.startswith("saveMenu"):
                saveMenu("./menu.txt", menu)

    if login == "client":
        while True:
            action = input("que voulez vous faire : ")
            if action == "exit":
                print("Au revoir")
                break
            if action == "help":
                helpClient()
            if action == "menu":
                displayMenu()
            if action.startswith("manger"):
                manger(action)

        # Traiter les commandes client
