'''
Program 4: Write a Program to Print following Pattern.
      A
    B A
  C B A
 D C B A
'''
ch="A"
for i in range(4):
    for j in range(4):
        if j<3-j:
            print("",end="\t")
        else:
            print(ch,end="")
            ch=(chr(ord(ch))-1)
    print()
    ch=(chr(ord('A'))+j+1)
