'''

Write a Program to Print following Pattern
*
* *
* * *
* * * *
'''

for i in range(1,5):
    for j in range(1,i+1):
        print('*', end=" ")
        i=i+1
        print()


#for i in range(1,5):
#    for j in range(1,i+1):
#        print('*', end=" ")
#        i=i+1
#        print()
