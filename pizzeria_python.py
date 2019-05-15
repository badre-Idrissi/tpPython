menu={"Napo":[["anchois"],12,2]}

def saveMenu(file_path, menu) :
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
	menu[pizzaName] = [[], 0, 0]
def addIngredient(option):
	global menu
	_, pizza, ingredient = option.split(" ")
	if not pizza in menu:
		menu[pizza] = [[], 0, 0]
	menu.get(pizza)[0].append(ingredient)

def addPrix(option):
	global menu
	_, pizza, prix = option.split(" ")
	if pizza in menu:
		menu.get(pizza)[1] = int(prix)
def addQte(option):
	global menu
	_, pizza, quantite = option.split(" ")
	if pizza in menu:
		menu.get(pizza)[2] += int(quantite)

def helpClient():
	print(""" Help :
				- menu (afficher le menu)
				- manger pizzaName (manger une pizza)
				- exit (sortir du restaurant)
			""")
def displayMenu():
	global menu
	print(menu)
def manger():
	global menu
	_, pizza = action.split(" ")
	if pizza in menu and menu.get(pizza)[2] > 0:
		print("bonap")
		menu.get(pizza)[2] -= 1
	else:
		print("pizza non disponible")


while True:
	login = input("login : ")
	if login == "exit":
		break
	if login=="admin":
		while True:
			option = input("choisir une option : ")
			if option == "exit":
				break
			if option == "help":
				helpAdmin()
		#Traiter les commandes admin
			if option.startswith("addPizza"):
				addPizza(option)
			if option.startswith("addIngredient"):
				addIngredient(option)
			if option.startswith("addPrix"):
				addPrix(option)
			if option.startswith("addQte"):
				addQte(option)
			if option.startswith("saveMenu"):
				saveMenu("./menu.txt",menu)
		
	if login=="client":
		while True:
			action = input("que voulez vous faire : ")
			if action == "exit":
				print("Au revoir")
				break
			if action == "help":
				helpClient()
			if action =="menu":
				displayMenu()
			if action.startswith("manger"):
				manger(action)
				
			#Traiter les commandes client

