# Python Object Oriented 4th  video

class  Employee:
  def __init__(self,first,last,pay):
     self.first=first
     self.last=last
     self.pay=pay
     self.email=first+'.'+last+'@gmail.com'

  def fullname(self):
      return 'My name is {} {}'.format(self.first,self.last) # it takes every object as an argument


class Developer(Employee): # it is an inheritance we are passing Employee which is inherited by Developer
    pass





dev_1 = Developer('Damodar','Dikonda',500000);#creating object of an Developer class and calling dev_1
dev_2 = Developer('dams','Dikonda',300000);


#print(dev_1.email)
#print(dev_2.pay)

print(help(Developer))
