# Python Object Oriented 4th  video

class  Employee:
  raise_a= 1.04

  def __init__(self,first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument


  def raise_amnt(self):
      self.pay=int(self.pay * self.raise_a)

class Developer(Employee): # it is an inheritance we are passing Employee which is inherited by Developer

   raise_a=1.10

   def __init__(self,first,last,pay,p_lang):
        super().__init__(first,last,pay)# it is used for calling parents class init method
        #Employee.__init__(self,first,last,pay) used for calling super class init Method

        self.p_lang=p_lang


class Manager(Employee):
   def __init__(self,first,last,pay,Emp=None):
        super().__init__(first,last,pay)# it is used for calling parents class init method
        if Emp is None:
            self.Emp=[]
        else:
            self.Emp=Emp

   def add_emp(self,e):
       if e not in self.Emp:
           self.Emp.append(e)

   def del_emp(self,e):
       if e  in self.Emp:
           self.Emp.remove(e)

   def print_emp(self):
       for em in Emp:
           print('-->',em)



dev_1 = Developer('Damodar','Dikonda',500000,'Python');#1.creating object of an Developer class and calling dev_1, 2. it will take an raise_a value of developer calss
#dev_1 = Employee('Damodar','Dikonda',500000):- it will take raise_a from Employee xclass
dev_2 = Developer('dams','Dikonda',300000,'java');

man_1=Manager('vaishnav','gaikwad','300000',[dev_1])
print(man_1.email)
man_1.add_emp(dev_2)
man_1.del_emp(dev_1)

print(isinstance(man_1,Manager))#it shows that man_1 is instance of manager class or not
print(isinstance(man_1,Developer))# it will print out false

print(issubclass(Developer,Employee))# it will print out True if Developer is subclass of Employee\
print(isinstance(Manager,Employee))# it will print out True
print(isinstance(Developer,Manager))# it will print out false becaue Developer is not subclassof Manager

#print(dev_1.email)
#print(dev_1.p_lang)
#print(dev_2.email)
#print(dev_2.p_lang)

#print("printing raise amount")
#print(dev_1.pay)
#dev_1.raise_amnt()
#print(dev_1.pay)


























#print(help(Developer))
#output:==class Developer(Employee)
 #|  Developer(first, last, pay)
 #|
 #|  Method resolution order: it runs first and these are thre method where python searches for method and attribute
 #|      Developer:-1st search here
 #|      Employee:-then here
 #|      builtins.Object:- every class in python is inherit from object
 #|
 #|  Methods inherited from Employee:
 #|
 #|  __init__(self, first, last, pay)
 #|      Initialize self.  See help(type(self)) for accurate signature.
 #|
 #|  fullname(self)
 #|
 #|  ----------------------------------------------------------------------
 #|  Data descriptors inherited from Employee:
 #|
 #|  __dict__
 #|      dictionary for instance variables (if defined)
 #|
 #|  __weakref__
 #|      list of weak references to the object (if defined)
