n=int(input("saisir n :\n"))
print((((n,"Fizz")[n%3==0],"Buzz")[n%5==0],"FizzBuzz")[n%15==0])
