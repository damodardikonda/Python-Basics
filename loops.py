num=[1,2,8,5,10]

#for loop

for n in num:
    print(n)
    if n==3:
        print('lets beake')
        break

#inner loops

for nn in num:
    for le in 'abc':
        print(nn,le)

print('\n\n')

#range function
for i in range(10):
    print(i)

print('\n\n while loop ')

x=0

while x<6:
    print(x)
    x=x+1
