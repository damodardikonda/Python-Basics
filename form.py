dict={'name':'Damodar','age':21}

pri='my name is {} and i am {} year old'.format(dict['name'],dict['age'])
print(pri)


prin='my name is {0} and i am {1} year old'.format(dict['name'],dict['age'])
print(prin)


tag='h1'
text='this is headline'
sen='<{0}><{1}></{0}>'.format(tag,text)
print(sen)


#class person():
#     def__init__(self,n,a):
#       self.n=n
#       self.a=a


#obj=new person('damodar','21')

#sent='my name is {0.n} and i am {1.m} years old'.format(obj)
#print(sent)

obj={'name':{'damu','dikonda'},'age':23}
sent='my name is {name} and i am {age} years old'.format(**obj)
print(sent)

for i in range(0,11):
    msg='value is{}'.format(i);
    print(msg)


import datetime
my_date=datetime.datetime(2017,4,29,22)

sente='{:%B, %d %y}'.format(my_date)
print(sente)
