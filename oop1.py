# Python Object Oriented 1 st video

class  Employee: #Employee is an blueprint of class
    #pass # it indicates that you want to skip it for now
  def __init__(self,first,last,pay):# init as like constructor and self indicates the object itself i.e. self=emp_1 or emp_2
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument







emp_1 = Employee('Damodar','Dikonda',500000);
emp_2 = Employee('dams','Dikonda',300000);#emp_1 and emp_2 is an object of class

print(emp_1.fullname())
#print(emp_2.fullname())
print(Employee.fullname(emp_2))# if we use an class name to call then pass an instance emp_1 as an argument. it works in background
# output is
#<__main__.Employee object at 0x0000017B4E714F88>
#<__main__.Employee object at 0x0000017B4E70EF48>
# here we can see both object has different memory location
