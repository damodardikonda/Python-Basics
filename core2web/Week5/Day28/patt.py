''' Write a Program to Print following Pattern.
         A3
      B3 A4
   C3 B4 A5
D3 C4 B5 A6

'''
'''

a=65

for i in range(4):
    a=i+1
    for j in range(4):

        if j<4-j:
            print(end="\t")
        else:
            print(chr(a)+""+str(i+j), end="\t")
            ch=ch-1

    print()


'''



ch = 65


for itr in range(4):
    ch = 65+itr
    for jtr in range(4):
        if jtr<3-itr:
            print("\t",end="")
        else:
            print(chr(ch)+""+str(itr+jtr),end="\t")
            ch=ch-1

    print("")
