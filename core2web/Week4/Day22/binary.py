'''

Write a Program to Convert entered Decimal Number to Binary
Number
Input: Binary Number: 35
Output: Octal Number: 100011 '''



b = ""
dec = int(input("Enter decimal num : "))
while(True):
    quo = int(dec / 2)#17
    rem = dec % 2 #1
    dec = quo#17
    if(rem == 1):
            b = b + "1"
    elif(rem == 0):
            b = b + "0"
    if(quo == 0):
            break

for i in range(len(b) - 1, -1, -1):
    print(b[i], end = "")
