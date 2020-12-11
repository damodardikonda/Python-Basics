class P :

    def m1(self):
        print("This is  Parent Method")


class C(P):

    def m2(self):
        print("This is Child Method")


c = C()
c.m1()
c.m2()


p = P()
p.m1()
#
p.m2() # nort allowed

c = P()
c.m1()
c.m2()
