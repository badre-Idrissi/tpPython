def calcul(a,b):
    try :
        fichier = open("menu.txt",'r')
        lines = fichier.readlines()
        x = a/b
        if x==0:
            print("zero")
        else :
            pass
        return lines
    except ZeroDivisionError:
        pass
        print("apres pass")

    finally:
        fichier.close()
        print("traitement continue")

    print("traitment hors try")


print(calcul(1,0))