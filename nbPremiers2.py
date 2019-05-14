n=int(input("saisir un nombre"))
for nb in range(2,n) :
	premier=True
	for div in range(2,nb) :
		if nb%div==0 :
			premier=False
			break;
	if premier :
		print(nb)
