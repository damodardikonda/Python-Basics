'''Write a Program to all the numbers ranging between 1 to 100 that are divisible by 4 and 7.
Output: 28 56 84
'''

for i in range(1,100):
    if i%4==0 and i%7==0:
        print(i,"is divisible by 4 and 7");
        
