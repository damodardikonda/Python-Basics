class Outer:

    def __init__(self):
        print(" Outer Class")

    class Inner:

        def __init__(self):
            print("Inner Class")

        def m1(self):
            print(" Inner class method")

'''
o = Outer()
i = Outer().Inner()
i.m1()
'''

Outer().Inner().m1()
