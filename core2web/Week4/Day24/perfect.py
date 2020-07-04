'''
 Write a Program to that skips the occurrence of perfect
 numbers using continue statement.
 Print this sequence up to 100.
 Output:  1 2 3 4 5 7 8 9.
 '''

a=0
 for i in range(1,101):
     for j in range(1,i):
         if i%2==0:
             a=a+i;

if a==i:
    continue
else:
    print(a)
