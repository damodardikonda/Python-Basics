'''
str,ch,age,marks = [ eval(i) for i in input(" Enter String, char , INT , Float").split()]


print(str)
print(ch)
print(age)
print(marks)


for i in range(1,4):

    str,ch,age,marks = [eval(i) for i in input("Enter 4 ") .split()]
    print(str)
    print(ch)
    print(age)
    print(marks)

'''

i=1

while i < 4:

    str,ch,age,marks = [eval(i) for i in input("Enter 4 ") .split()]
    print(str)
    print(ch)
    print(age)
    print(marks)
    i+=1
    
