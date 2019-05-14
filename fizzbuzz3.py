while True :
    n=input("saisir n :\n")
    if n=="exit":
		break
    n=int(n)  
    print((((n,"Fizz")[n%3==0],"Buzz")[n%5==0],"FizzBuzz")[n%15==0])
