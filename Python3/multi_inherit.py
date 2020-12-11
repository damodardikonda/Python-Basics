class A:

    def __init__(self):
        print("Parent class Constructor")

    def m1(self):
        print("Parent Instance Method")

    @classmethod
    def m2(cls):
        print("Cklass Method")

    @staticmethod
    def m3():
        print("Parent Static method")

class B(A):

    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


    @staticmethod
    def mmm(cls):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


    def mm(cls):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def m(cls):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


b = B()
b.mmm()
b.m()
B.mm()
