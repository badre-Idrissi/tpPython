import datetime
class Personne(object):

    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance

    def saluer(self):
        print(f"Salut {self.nom}")
    def displayPersonne(self):
        print(f"Hello {self.nom}")
    def calculAge(self):
        this_year = datetime.datetime.now().year
        return this_year - self.dateNaissance
class Etudiant(Personne):
    def __init__(self, nom, prenom, date, numeroCarte):
        Personne.__init__(self, nom, prenom, date)
        self.numeroCarte = numeroCarte

class Employe(Personne):
    def __init__(self, nom, prenom, date, salaire):
        Personne.__init__(self, nom, prenom, date)
        self.salaire = salaire
    def saluer(self) :
        
        self.saluer()
        print("le salaire :", self.salaire)



etudiant = Etudiant("Felix","Lechat", 2005, "123NB22")
etudiant.saluer()
empl = Employe("Tom", "Cruz", 1965, 1200000)
empl.saluer()




