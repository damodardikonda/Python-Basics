# Python Object Oriented 2nd video

class  Employee: #Employee is an blueprint of class
  raise_amt=1.4
  def __init__(self,first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

     Employee.no_of_emp+=1

  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument

  def apply_raise(self):# if you dont call raise_amt with instance varible or class name then it will give an error
      self.pay=int(self.pay*self.raise_amt)



print(Employee.no_of_emp)# it printout 0

emp_1 = Employee('Damodar','Dikonda',500000);
emp_2 = Employee('dams','Dikonda',300000);#emp_1 and emp_2 is an object of class

print(Employee.no_of_emp)

print(emp_1.fullname())
#print(emp_2.fullname())
print(Employee.fullname(emp_2))# if we use an class name to call then pass an instance emp_1 as an argument. it works in background

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

print(emp_1.__dict__)# it does not have an raise_amt

emp_1.raise_amt=1.9# it will change only value of that perticular object
print(emp_1.__dict__)# here it has an raise_amt
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
