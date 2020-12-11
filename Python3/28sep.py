'''
name , roll , interest = [ eval(x) for x in input("Enter Name , roll , field of interest ").split()]

print("Hey , My name is " , name , " and my roll no is " , roll , " interest " , interest);
'''
'''
s1 ,s2 = (str(x) for x in input("Enter 2 string").split())

print(s1," " ,s2)



strid ,intid = (eval(x) for x in input("Enter two numbers").split())
print(strid,intid, "@gmail.com")
'''

for i in range(1,6):
    for j in range(1,6):
        if(j%2==0):
           print("1", end=" ")
        else:

            print("0" , end=" ")

    print()
