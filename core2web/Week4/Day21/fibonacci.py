'''
: Write a Program to print Fibonacci Series of 5 Elements.
{Note: In Fibonacci series next element is sum of previous two elements}
Output: 0 1 1 2 3.
 '''

num=int(input("Enter the number"));
n=0

while(i<num):
    prev=i
    next=i+1
    next=next+prev
    print(next)


'''
a = 0
b = 1
c = 0

print("Febonacci series")

print(a,end="\t")

print(b,end="\t")

for itr in range(0,3):
    c= a+b
    print(c,end="\t")

    a=b
    b=c
'''
