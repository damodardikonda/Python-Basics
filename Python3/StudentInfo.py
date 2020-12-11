
class Student():

    def __init__(self , roll , name):
        self.name=name
        print("name " , name)

        self.roll = roll

    def run(self):
        self.id = 1000
        print("Name is " , self.name)
        print("Roll no is " ,self.roll)
#        print("name " , name) it is not gonna print

    def DispId(self):
        print(" id is " , self.id)
'''
s = Student(10,"Damodar")
print(s.name)
print(s.roll)
s.run();
'''


s1 = Student(200 , "Damodarrrrrrrrrrrr")
print(s1.run())
s1.DispId()
