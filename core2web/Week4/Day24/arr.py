''' Write a Program that takes an array as input from user
and prints the array in reverse order.
Input: 1 2 3 4 5 6 7 8
 Output: 8 7 6 5 4 3 2 1 '''

print("Enter numbers:")
p = list()

for i in range(1,10):
     p.append(int(input()))
p.reverse()

print(p)
