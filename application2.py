nom = input("sasissez le nom : \n")
genre_val=input("saisir le genre :\n")
#genre= ("Monsieur" if genre_val=="1" else "Madame")
genre=("Monsieur", "Madame")[genre_val=="0"]
        
msg= "Bonjour {} {}"
print("Bonjour {} {}".format(genre,nom))
