# Python Object Oriented 3rd video

class  Employee: #Employee is an blueprint of class
  raise_amt=1.4
  def __init__(self,first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

     #Employee.no_of_emp+=1

  def fullname(self):# this i an instance method
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument

  @classmethod
  def classesmethod(cls,amount):#this is an class method not instance method
    cls.raise_amt= amount

  @classmethod
  def from_string(cls,emp_str):
      first,last,pay=emp_str.split('-')
      return cls(first,last,pay)

  @staticmethod
  def is_weekday(day):
      if day.weekday()==5 or day.weekday()==6:
          return False
      return True

emp_1 = Employee('Damodar','Dikonda',500000);
emp_2 = Employee('dams','Dikonda',300000);#emp_1 and emp_2 is an object of class


import datetime
my_date=datetime.date(2017 , 6 ,10)
print(Employee.is_weekday(my_date))


Employee.classesmethod(100)

emp_str_1='damodar-dikonda-900000'
emp_str_2='dams-dikonda-40000'
emp_str_3='d-d-20000'

new_str=Employee.from_string(emp_str_1)

print(new_str.email)
print(new_str.pay)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


#print(emp_1.fullname())
#print(emp_2.fullname())
#print(Employee.fullname(emp_2))# if we use an class name to call then pass an instance emp_1 as an argument. it works in background



#print(emp_1.__dict__)# it does not have an raise_amt

#emp_1.raise_amt=1.9# it will change only value of that perticular object
#print(emp_1.__dict__)# here it has an raise_amt
#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)
