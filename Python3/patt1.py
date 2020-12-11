
for i in range(5):
    for j in range(5):
        print("*" , end=' ')
    print()

for j in range(3):
    for k in range(7):
        print("1" , end=' ')

    print()

num =1
for k in range(5):
    for i in range(5):
        print(num , end=' ')
        num+=1
    print()

#pattern2
num=1;
for i in range(5):
    for j in range(5):
        print(num, end=' ')
    num+=1
    print()

'''
pattern3
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
num = 1
for i in range(5):
    for j in range(5):
        print(num,end =' ' )
        num+=1
    print()
    num = 1


print()
print()

'''


A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
ch =65
num =0
for i in range(5):
    for  j in range(5):
        print(chr(ch+num) ,end=' ')
    num+=1
    print()

'''

Pattern5
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''


ch = 65


for i in range(5):
    for j in range(5):
        print(chr (ch+j) , end = ' ')

    ch = 65
    print()


print()
print()

'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''

for i in range(5,0,-1):
    for j in range(5):
        print(i , end=' ')
    print()


'''
pattern6
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''

for i in range(5):
    for j in range(5,0,-1):
        print(j , end = ' ')
    print()


'''

Pattern8
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
'''
ch = 64
num = 5
for i in range(5):
    for j in range(5):
        print(chr(ch+num) , end =' ')

    num-=1
    print()


'''

Pattern9
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
'''

ch = 64

for i in range(5):
    for j in range(5,0,-1):
        print(chr(ch+j) , end=' ')
    print()


'''

Pattern10
*
* *
* * *
* * * *
* * * * *

'''

for i in range(0,5):
    for j in range(0,i+1):
        print("* " , end = ' ')
    print()
