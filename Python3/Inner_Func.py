'''def fun1():

      def inner(a,b):

          print(" The Addition is = " , (a+b))
          print( " The Average is " , (a+b) / 2)

      inner(20,10)
      inner(40,60)
      inner(80,100)


#inner(10,20) ---> Not Allowed
fun1()


def outer():
    print("Outer Function started")

    def inner():
        print("Inner Function executed")

    print("Outer function executed")
    return inner


f1 = outer()
f1()
'''


def outer():
    print("Outer Function started")

    def inner():
        print("Inner Function executed")

    print("Outer function executed")
    return inner


f1 = outer
f1()
