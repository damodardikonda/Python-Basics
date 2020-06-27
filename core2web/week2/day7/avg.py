''' Write a Progr am to accept 10 integers from user and prin t s the  sum &  average of entered   numbers .
Input:  1  2 3 4 5 6 7 8 9  10   '''

num = input("Enter the number : ")
sum1 = 0
for itr in range(1,num+1):
    sum1 = sum1 + itr

print("The Sum of number upto "+str(num)+" : "+str(sum1))   
