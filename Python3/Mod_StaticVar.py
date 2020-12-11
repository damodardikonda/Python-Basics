class Test:
    a=10

    def __init__(self):
        Test.a=20

    def m1(self):
        Test.a = 50

    @classmethod
    def m3(cls):
        Test.a = 100
        cls.a = 200

    @staticmethod
    def m4():
        Test.a = 500


t = Test()
t.m1()
t.m3()
t.m4()
print(t.a)
Test.a = 10000

print(Test.a)
