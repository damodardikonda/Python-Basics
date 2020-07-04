''' Write a Program to that skips the occurrence of numbers
that are divisible by 7 using continue statement.
 Print this sequence up to 100.
  Output:  1 2 3 4 5 6 8 9 10 11 12 13 15
'''


i=0
while(i<100):
    if i%7==0:
        continue
    else:
        print(i) 
