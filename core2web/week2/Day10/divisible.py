'''Write a Program to print all the numbers ranging between 1 to 100 that are divisible by 3 or 5.
Output: 3 5 6 9 10 . . .. 99 100. '''

#for i in range(3,101):
#    if i%3==0 and i%5==0:
#        print(i,"is divisible by 3 and 5")
#    else:
#        print(i,"is not divisible by 3 and 5")



for i in range(3,101):
    if i%3==0 :
        print(i,"is divisible by 3 ")
    elif i%5==0:
        print(i,"is divisible by 5")

    else:
       print(i,"is not divisible by 3 and 5")


#for i in range(101):
#    if (i+1)%3==0 and (i+1)%5==0:
#        print(i,"is divisible by 3 and 5")
#    else:
#        print(i,"is not divisible by 3 and 5")
