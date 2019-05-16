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