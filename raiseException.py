
class NegativeValueException(Exception):
    pass

def calculAge(annee):

    try:
        annee = int(annee)
        print("valeur ok")
        if(annee <= 0):
            print(annee)
            raise NegativeValueException("valeur negative")

    except ValueError as err:
        print(err)



calculAge(200)
