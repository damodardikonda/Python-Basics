''': Write a Program to print series of Deficient Numbers up to nth element. Where n is number entered by user.

'''



num = int(input("Enter the number"))



for jtr in range(1,num):
    sum1 = 0
    for itr in range(1,(jtr/2)+1):
        if jtr%itr == 0:
            sum1 = sum1+itr
    if sum1 < jtr:
        print(jtr)
