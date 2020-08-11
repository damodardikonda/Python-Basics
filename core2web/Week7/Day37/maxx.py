num=int(input("ENter the Number"));


rem=0
while(num!=0):
    if(num%10 >= rem):
       rem=num%10;
    num=int(num/10)
print("Maximum Number:",rem)
'''

num = int(input("Enter num : "))
m = 0
while(num != 0):
    if(num % 10 >= m):
        m = num % 10;
    num = int(num / 10)
print("max : ", m)
'''
