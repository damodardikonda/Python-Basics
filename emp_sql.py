class  Employee: #Employee is an blueprint of class
    #pass # it indicates that you want to skip it for now
  def __init__(self,first,last,pay):# init as like constructor and self indicates the object itself i.e. self=emp_1 or emp_2
     self.first=first
     self.last=last
     self.pay=pay

  @property
  def email(self):
     return ('{}.{}@gmail.com').format(self.first,self.last)


  @property
  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument


  def __repr__(self):
      return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
