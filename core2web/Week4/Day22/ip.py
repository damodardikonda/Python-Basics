'''
Write a Program that accepts 5 integer values from user and
compares two consecutive inputs and if the second of them is lesser that the
previous one then the code exits out of loop and prints the unexpected input.
{Note: Use Break Statement}
Input: 1 3 5 4
Output: Loop is exited with input 4. '''

n1,n2,n3,n4,n5=[int(i) for i in input("Enter the number").split()]

if n1<n2 and n2<n3  and n3<n4  and n4<n5:
    print(n1,n2,n3,n4,n5)
else:
    print("not")
