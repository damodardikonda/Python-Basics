#e.g:-__init__().these 2 underscore called as dunder
# when object is created then it implicitly calls a dunder method


class  Employee:
  def __init__(self,first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument

  def __repr__(self):
      return "Employee('{}','{}','{}'')".format(self.first,self.last,self.pay)

  def __str__(self):
      return '{}-{}'.format(self.fullname(),self.email)

  def __add__(self, other):
      return self.pay+other.pay

  def __len__(self):
      return len(self.fullname())



emp_1 = Employee('Damodar','Dikonda',500000);
emp_2 = Employee('dams','Dikonda',300000);#emp_1 and emp_2 is an object of class

print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1+emp_2)

print(1+2)

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(str.__add__('1','2'))

print('length of object is')
print(len(emp_1))
