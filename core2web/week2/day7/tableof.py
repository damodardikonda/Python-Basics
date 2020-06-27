'''Write a Program that accepts an integer from user and print table of that number.
Input: 4
Output: 4 8 12 16 20 24 28 36 40 '''

n=int(input("Enter the number"));
for i in range(10):
    #print(n*i end=" ");
   print((i+1)*n)
