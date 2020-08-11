import string as str


a=str.ascii_lowercase

print(a)
print(type(a))


b= str.ascii_letters

print(b)
print(type(b))

c= str.ascii_uppercase
print(c)
print(type(c))
print(id(a))
print(id(b))


d=str.digits
print(d)
print(type(d))




e=str.hexdigits
print(e)
print(type(e))




'''
f=str.octaldigits
print(f)
print(type(f))
'''


x="A".lower()

y="A".upper().lower()
print(x);
print(id(x))
print(id(y))

print(y)
