n=int(input("saisir un nombre"))
i=2
while(i<n):
	j=2
	while(j<=i):
		if(i%j==0):
			break;
		else :
			j+=1
	if(j==i):
		print(i)
	i+=1