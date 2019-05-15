dict_ = {"cle":12,"cle2":13}

def ouvrirFichier ():
    try:
        fichier = open("menu.txt",'r')
        lines = fichier.readlines()
    except FileNotFoundError:
        return (False, "erreur")
    else:
        print("aucune exception n'est declanché")
        return (True, lines)

success, result = ouvrirFichier()
if(success) :
    print(result)
else :
    print(result)

exit()


while True:
    try:
        cle = input("lire clé : ")

        print(dict_[cle])
        a = 10 / 0

    except KeyError:
        print("la cle n'existe pas")
    except ZeroDivisionError:
        print ("division par 0")

