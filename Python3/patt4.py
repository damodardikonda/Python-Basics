

'''
Pattern31
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1


'''
rows=5
num = 1
for i in range(1, rows+1):
    for j in range(1,i):
        print(" " , end=" ")
    for k in range(i,rows+1):
        print(num ,end=" ")
        num+=1
    print()
    num = 1

'''

Pattern32
E E E E E
  D D D D
    C C C
      B B
        A

'''

num = 5
ch = 64

rows=5

for i in range(1, rows+1):
    for j in range(1,i):
        print(" " , end=" ")

    for k in range(i,rows+1):
        print(chr (ch+num) , end=" ")

    print()
    num-=1

'''

Pattern33
A B C D E
  A B C D
    A B C
      A B
        A
'''
ch = 64
num = 1
rows = 5
for i in range(1,rows+1):
    for j in range(1,i):
        print(" " , end=" ")
    for k in range(i,rows+1):
        print(chr(ch+num) , end=" ")
        num+=1
    print()
    num = 1


'''

Pattern34
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


'''
rows=5
m = (2*rows)-2
for i in range(0,rows):
    for j in range(0,m):
        print(end=" ")

    m=m-1

    for k in range(0,i+1):
       print("*" ,end=" ")

    print()

'''

Pattern35
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5


'''
rows=5
n= 1
m = (2 * rows)-2
for i in range(0,rows):
    for j in range(0,m):
        print(end=" ")

    m= m-1

    for k in range(0,i+1):
        print(n , end=" ")

    print()
    n+=1


'''
Pattern36
        1
      3 3 3
    5 5 5 5 5
  7 7 7 7 7 7 7
9 9 9 9 9 9 9 9 9

'''

rows=5
n=1
m = (2 * rows)-2

for i in range(0,rows):
    for j in range(0,m):
        print(end = " ")

    m= m-1

    for k in range(0,i+1):
        print(n , end=" ")

    print()
    n+=2

'''

Pattern37
        A
      B B B
    C C C C C
  D D D D D D D
E E E E E E E E E


'''
rows=5
n=1
ch=64
m=(2*rows)-2
for i in range(0,rows):
    for j in range(0,m):
        print(end=" ")
    m=m-1

    for k in range(0,i+1):
        print(chr(ch+n) , end=" ")
    n+=1
    print()


'''

Pattern38
        A
      C C C
    E E E E E
  G G G G G G G
I I I I I I I I I
'''


ch = 64
num = 1

r = 5

m =(2 * r)-2

for i in range(0,r):
    for j in range(0,m):
        print(end =" ")
    m-=1

    for j in range(0,i+1):
        print(chr (ch+num) ,end=" ")

    num+=2
    print()

'''

Pattern39
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9


'''

n = 1
r= 5
m=(2*r)-1
for i in range(0,r):
    for j in range(0,m):
        print(end=" ")
    m-=1

    for k in range(0,i+1):
        print(n , end=" ")
        n+=1
    n=1
    print()

'''

Pattern40
        1
      3 2 1
    5 4 3 2 1
  7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1


'''

r= 5
m=(2*r)-1
for i in range(0,r):
    n=1
    for j in range(0,m):
        print(end=" ")
    m-=1

    for k in range(0,i+1):
        for l in range(i+i+1,i,-1):
            print(l , end=" ")


    print()
