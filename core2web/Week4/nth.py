'''Write a Program to print sum of series up to the nth entered number.
 Series is: 9, 99, 999, 9999, 9999 . . .. n.
Input: Nth Element in series: 5
Output: the sum of: 9 + 99 + 999 + 9999 + 99999 = 111105
'''

n = int(input("n : "))
num = 0
s = 0
for i in range(n):
    num = num * 10 + 9
    s += num
    if(i < n - 1):
        print(num, " + ", end = "")
    else:
        print(num, " = ", end = "")
print(s, end = "")
