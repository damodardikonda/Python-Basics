class Employee:

     def __init__(self , eno , ename , esal):
          self.eno = eno
          self.ename = ename
          self.esal = esal

     def display(s):
         print("Employee Number is " , s.eno)
         print("Employee Name is " , s.ename )
         print("Employee salary is " , s.esal )


class Owner:

    def m1(emp):
        emp.esal = emp.esal + 10000;
        emp.display()

e = Employee(1 ,"Damodar" ,999999)
Owner.m1(e)
