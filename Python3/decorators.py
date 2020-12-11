'''

def decor(fun):
  def inner(name):
    if name == "Damodar":
        print("Kingggggg")
    else:
        fun(name)
    return inner

@decor
def wish(name):
    print("Lavdya" , name)


wish("Damodar")
wish("Rushi")
wish("Adi")
wish("Raj")


def decor(fun):
  def inner(name):
    if name == "Damodar":
        print("Kingggggg")
    else:
        fun(name)
    return inner


def wish(name):
    print("Lavdya" , name)

decorr = decor(wish)

decorr("Damodar")
decorr("Rushi")
decorr("Adi")
decorr("Raj")

'''


def sdiv(func):
  def innwe(a,b):
    if b == 0:
        print("Bhaag Bhosadike")
    else:
        return func(a,b)
    return inner

@sdiv
def divide(a,b):
    return a/b

print(divide(20,10))
print(divide(10,0))
