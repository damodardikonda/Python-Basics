'''

Pattern11
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

'''
for i in range(1,6):
    for j in range(i):
        print(i , end=" ");

    print();


'''

Pattern12
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j , end=" ");

    print();

'''


Pattern13
A
B B
C C C
D D D D
E E E E E
'''
ch = 65;
for i in range(5):
    for j in range(i+1):
        print(chr(ch) , end=" ")
    print();
    ch+=1;


'''
Pattern14
A
A B
A B C
A B C D
A B C D E
'''

ch = 65
for i in range(5):
    for j in range(i+1):
        print(chr(ch+j),end=" ");
    print()


'''
Pattern15
* * * * *
* * * *
* * *
* *
*
'''
rows = 5
for i in range(rows+1 , 0 , -1):
    for j in range(0,i-1):
        print("* " , end= " ")
    print()


'''

Pattern16
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
rows=5
num =1
for i in range( rows+1,0,-1):
    for j in range(1,i+1):
        print(num , end=" ")
    print()
    num+=1


'''
Pattern17
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
rows=5
for i in range(  rows+1,1,-1):
    for j in range(1,i):
        print(j ,end=" ")

    print()
'''

Pattern18
A A A A A
B B B B
C C C
D D
E


'''
ch=65;
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(chr(ch) , end=" " )
    print()
    ch+=1;

'''
Pattern19
A B C D E
A B C D
A B C
A B
A

'''
ch=64;
rows = 6
for i in range(rows-1,0,-1):
    for j in range(1,i+1):
        print(chr(ch+j) , end=" ")
    print();


'''

Pattern20
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

'''
rows=4
for i in range(rows+1,0,-1):
    for j in range(1,i+1):
        print(i , end=" ")
    print()
