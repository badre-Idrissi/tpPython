n=int(input("saisir n :\n"))
if n % 15==0:
    print("FizzBuzz")
elif n % 5==0:
    print("Buzz")
elif n % 3==0:
    print("Fizz")
else:
    print(n)

