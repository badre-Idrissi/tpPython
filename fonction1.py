def cap_(s):
    s1 = str(s[0]).upper()
    s2 = str(s[1:]).lower()
    return s1+s2
def cap(s):
    result=""
    for elem in s.split("."):
        result = result + "."+cap_(elem)
    return str(result[1:])

def operation(*args):
    liste_int = [x for x in args if type(x) is int]
    if len(liste_int) == 0:
        return ("Liste vide","Liste vide","Liste vide","Liste vide")
    val_max=liste_int[0]
    val_min=liste_int[0]
    val_somme=0;
    for x in liste_int :
        val_somme+=x
        if x > val_max:
            val_max = x
        if x < val_min:
            val_min = x

    val_moy = val_somme / len(liste_int)
    return (val_somme,val_max, val_min, val_moy)

somme,max,min,moy = operation(1,2,3,4,"chaine", True)
print("somme = ",somme)
print("max = ",max)
print("min = ",min)
print("moy = ",moy)

#var = cap("chaine1.chaine2")
#print(var)
