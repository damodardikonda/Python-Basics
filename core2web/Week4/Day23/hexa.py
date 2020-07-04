''' Write a Program to Convert entered Decimal Number to Hexadecimal Number
Input: Decimal Number: 43
Output: Hexadecimal Number: 2B
'''

'''i=int(input("Enter the Number:-\t"));
print(hex(i))
'''

n=int(input("Enter the Number"));
p=list()

i=0
while(n!=0):
    p.append(chr(n%16+48)) if (n%16<=9) else p.append(chr(n%16+55))
    n=n
    i=i+1


i=-1
while(i!=0):
      p.append(p[i],end=" ")
      i=i-1
