
import datetime

first='Damodar'
last='Dikonda'

sentence='my name is {} {}'.format(first,last)
sent=f'my name is {first.upper()} {last}'
print(sentence)
print(sent)


print('for index')
person={'name':'Damodar','age':21}

s='My name is {} and I am {} years old'.format(person['name'],person['age'])
print(s)

sf=f"my name is {person['name']} and I am {person['age']} years old"
print(sf)

print('we can do a clculation in f string')
calc=f" 4 times 11 is { 4 * 11} "
print(calc)

print('for loops')

for n in range(1,10):
    sentencess=f'the valueof n is {n:04}'
    print(sentencess)

pie=3.141592653589793238
val=f'the value of pi is {pie:.4f}'
print(val)

print('for dates')
date=datetime.datetime(1999,4,3 ,9,0,0)
d=f'my bday is {date}'
print(d)
