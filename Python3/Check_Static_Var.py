class Test:

    a = 10

    def __init__(self):

        print(" Inside The Constructor")
        print(self.a)
        print(Test.a)

    def m1(self):

        print("Inside Method")
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print("Inside class method")
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print("Inside static method")
        print(Test.a)


t = Test()
t.m1()
t.m2()
t.m3()

print("By using object outside the class")
print(t.a)

print("By using class name outside the class")
print(Test.a)
