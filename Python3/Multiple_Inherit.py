class Parent:

    def m1(self):
        print("P1 method")

class Child1():

    def m1(self):
        print("P2 Method")

class Child2(Parent , Child1):

    pass


c = Child2()
c.m1() # ---> P1 method


class Child3(Child1 ,Parent):
    pass

cc = Child3()
cc.m1() # ----> P2 method


class c4(Parent , Child1):
    def m1(self):
        print("C4 Method")

ccc = c4()
ccc.m1()
