class Test():

    def __init__(self):
        print("This is a Constructor ")

    def __init__(self , x):
        print("his is a method " )
        self.x=x
        print("Value of x is " , x)
            
b = Test(10)
a = Test()
