import sys

class CMD:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def disp(self):
        print("Value of a is = " , a)
        print("Value of b is = " , b)


    def add(self):
        self.ans = self.a + self.b
        print("The Answer is = " , self.ans)


a = int(sys.argv[1])
b = int(sys.argv[2])

c= CMD(a,b)
c.disp()
c.add()
