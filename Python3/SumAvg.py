'''
class Test:

    def avg(self,list):
        self.list = list
        sum=0
        for i in self.list:
            sum=sum+i

        print(sum)
t = Test()
t.avg([10,20,30 ,40])


x = 1000
class Test:
    x=20
    def m1(self):
        print(x)
        print(self.x)

    def m2(self):
        print(x)
        print(Test.x)


t = Test()
t.m1()
t.m2()


'''


x = 1000
class Test:
    x=20
    def m1(self):
        x=500
        global y
        y=30000
        print(x)
        print(self.x)

    def m2(self):
        print(x)
        print(Test.x)


t = Test()
t.m1()
print(y)
