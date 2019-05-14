menu={"Napo":["anchois",12,2]}
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
				print(""" Help :
				- addPizza pizzaName (ajouter une pizza au menu)
				- addIngredient pizzaName ingredient (ajouter un ingrédient à une pizza)
				- addPrix pizzaName prix (ajouter un prix à une pizza)
				- addQte pizzaName qte (ajouter une qte à une pizza)
				- exit (sortir du menu admin)
				""")
		#Traiter les commandes admin
			if option.startswith("addPizza"):
				_,pizzaName = option.split(" ")
				menu[pizzaName]=[[],0,0]
			if option.startswith("addIngredient"):
				_,pizza,ingredient=option.split(" ")
				if not pizza in menu :
					menu[pizza]=[[],0,0]
				menu.get(pizza)[0].append(ingredient)
			if option.startswith("addPrix"):
				_,pizza,prix=option.split(" ")
				if pizza in menu :
					menu.get(pizza)[1]=int(prix)
			if option.startswith("addQte"):
				_,pizza,quantite=option.split(" ")
				if pizza in menu:
					menu.get(pizza)[2]+=int(quantite)
		
	if login=="client":
		while True:
			action = input("que voulez vous faire : ")
			if action == "exit":
				print("Au revoir")
				break
			if action == "help":
				print(""" Help :
				- menu (afficher le menu)
				- manger pizzaName (manger une pizza)
				- exit (sortir du restaurant)
				""")
			if action =="menu":
				print(menu)
			if action.startswith("manger"):
				_,pizza = action.split(" ")
				if pizza in menu and menu.get(pizza)[2]>0:
					print("bonap")
					menu.get(pizza)[2]-=1
				else:
					print("pizza non disponible")
				
			
			
			#Traiter les commandes client
	
		
