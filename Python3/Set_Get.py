
class Student:

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self,marks=100):
       self.marks = marks

    def getMarks(self):
        return self.marks


n = int( input (" Enter number of Student"))

for i in range(n):
    name = input("Enter Name = " )
    marks = float( input( " Enter Marks = "))
    s = Student()
    s.setName(name)
    s.setMarks(marks)

    print("Hey" , s.getName())
    print("Your Marks is = " , s.getMarks())
    print('*' * 20)
