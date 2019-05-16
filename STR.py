class SrtMultiplicationException(Exception):
    pass
class Str(str):
    def __mul__(self, other):
        if(type(other) is int):
            raise SrtMultiplicationException("Multiplication Interdite")

s = Str("toto2")
s2 = Str("toto2")
print(s==s2)

#print(s*2)
