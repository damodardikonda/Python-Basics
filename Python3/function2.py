'''
def fun():
  print("Damodar Dikonda")

print(fun())


def Arith(x,y):
    add = x+y
    sub = x-y
    mul = x * y
    return add , sub, mul

(a,b,c) = Arith(20,10)

print("Addition is  " , a)
print("Subtraction is " , b)
print("Multiplicaton is " , c)

''

def Arith1(x,y):
    add = x+y
    sub = x-y
    mul = x * y
    return add , sub, mul

[a,b,c] = Arith1(20,10)

print("Addition is  " , a)
print("Subtraction is " , b)
print("Multiplicaton is " , c)



def Arith2(x,y):
    add = x+y
    sub = x-y
    mul = x * y
    return add , sub, mul
s=set()
a,b,c= Arith2(20,10)

print("Addition is  " , a)
print("Subtraction is " , b)
print("Multiplicaton is " , c)
'''   


def Arith3(x,y):
    add = x+y
    sub = x-y
    mul = x * y
    return add , sub, mul

l = Arith3(20,10)
print(type(l))
for x in l :
    print(x)
