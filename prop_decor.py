


class Employee:

    def __init__(self,first,last):
        self.first= first
        self.last=last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first , self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    @fullname.setter
    def fullname(self,name):
      first, last =name.split(' ')
      self.first=first
      self.last=last

    @fullname.deleter
    def fullname(self):
      print("delete name")
      self.first=None
      self.last=None



emp_1=Employee('Damodar','Dikonda')
emp_2=Employee('Bhaskar','Dikonda')

emp_1.first='Karan';

emp_1.fullname = 'chirag oza'
print(emp_1.first)
#print(emp_1.email()) it will run but we want to treat like an attribute not a function
print(emp_1.email)# for that we required to add property decorator
print(emp_1.fullname)


del emp_1.fullname
