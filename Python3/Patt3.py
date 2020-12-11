'''

Pattern21
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
rows = 5;
num = 5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(num , end = " ");
        num-=1
    print()
    num = 5

'''
Pattern22
E E E E E
D D D D
C C C
B B
A
'''

num = 5;
rows = 5;
ch = 64
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(chr(ch+i) , end = " ")
    print()

'''

Pattern23
E D C B A
E D C B
E D C
E D
E

'''
r = 5
ch = 70

for i in range(r,0,-1):
    for k in range(1,i+1):
        print(chr(ch-k) , end=" ")

    print()

'''

Pattern23
E D C B A
E D C B
E D C
E D
E


Pattern24
         *
       * *
     * * *
   * * * *
 * * * * *
'''
row = 5
for i in range(1,row+1):
    for j in range(rows-1,i-1,-1):
        print(" " , end=" ")
    for k in range(1,i+1):
        print("*" , end=" ")
    print()

'''

Pattern25
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5


'''

row=5
num=1
for i in range(1,row+1):
    for j in range(rows-1,i-1,-1):
        print(" " , end=" ")
    for k in range(1,i+1):
        print(num,end=" ")
    num=num+1
    print()

'''
Pattern26
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''

rows = 5
num = 1
for i in range(1,rows+1):
    for j in range(rows-1, i-1,-1):
        print(" " , end=" " );
    for k in range(1,i+1):
        print(num , end=" ")
        num+=1
    print()
    num=1


'''


Pattern27
         A
       B B
     C C C
   D D D D
 E E E E E
'''

row=5
ch = 64
num=1

for i in range(1,row+1):
    for j in range(rows,i,-1):
        print(" " , end=" ")
    for j in range(1,i+1):
        print(chr (ch + num) , end =" ")
        num+=1
    print()
    num=1

'''
Pattern28
         A
       A B
     A B C
   A B C D
 A B C D E
'''
rows=5
ch = 64

for i in range(1,rows+1):
    for j in range(rows,i,-1):
        print(" " , end=" ")
    for k in range(1,i+1):
        print(chr (ch + k) , end=" ")
    print()


'''
Pattern29
 * * * * *
   * * * *
     * * *
       * *
         *
'''
rows=5
for i in range(1, rows+1):
    for j in range(1,i):
        print(" " , end= " ")
    for k in range(i,rows+1):
        print("*" , end=" ")
    print()

'''
Pattern30
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1


'''
rows = 5
num = 5
for i in range(1, rows+1):
    for j in range(1,i):
        print(" " , end=" ")
    for k in range(i,rows+1):
        print(num , end=" ")
    print()
    num-=1
