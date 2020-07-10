''' Write a Program that takes a number as input from
user and prints only perfect digits if it have any
else prints appropriate message.
Input: 24
Output: The number 24 does not have any digit, which is perfect in nature.
'''

num=int(input("Enter the Numbers:="));

for i in range(1,num):
    if num%i==0:
        print(num,"Is Perfect Number");
    else:
        print("num is not a Perfect number");
