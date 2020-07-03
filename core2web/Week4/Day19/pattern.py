''' Write a Program to Print following Pattern.
 A C E G
 B D F
 C E
 D
 '''
'''

n=0
inner=0
ascii=chr(65)
for outer in range(4
    print(ascii+n)
    for inner in range(outer,outer-inner):

           print(ascii+inner,end="")
           print()
           inner+=1
           n+=1
    if n==3:
'''
inc=0
for i in range(4):
    inc=0
    for j in range(4-i):
        print(chr(65)+i+inc , end=" ")
        inc+=2
    print()
