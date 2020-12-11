class Parent:

    def m1(self):
        print("this is Parent Method")

class Child(Parent):

    def m2(self):
        print("this is child method")

class GrandChild(Child):

    def m3(self):
        print("this is GrandChild method")


cc = GrandChild()
cc.m1()
cc.m2()
cc.m3()

c = Child()
c.m2()
c.m1()
#c.m3() ---> Not Allowed


p = Parent()
p.m1()
#p.m2() ---> Not Allowed
#p.m3() ---> Not Allowed
