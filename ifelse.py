language='python'

if language=='java':
   print('language is java')
elif language=='python':
    print("language is python")
elif language=='javascript':
    print("language is javascript")

else:
    print("language is not java")


user='damodar'
logged=False

if user=='damodar' and logged:
    print('logged in')
else:
    print('sorry')

if user=='damodar' or logged:
    print('logged in')
else:
    print('sorry')

if not logged:
    print("please locked in")
else:
    print('locked in')

# is =used for check that object are same or not

a=[1,2,3]
b=[1,2,3]

print(a)
print(b)

if(a is b):
    print('object ar same')
else:
    print('object are not same')

print(id(b))


print('\n None')
cond=None

if cond:
    print("condition is true")
else:
    print("condition is false")

#(zero or more number)

con=-10
if con:
    print('condition is true')
else:
    print('condition is flse')


c=[]
if c:
    print('condition is true')
else:
    print('condition is flse')


co={}
if con:
    print('condition is true')
else:
    print('condition is flse')
