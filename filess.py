

#f=open('text.txt',r)

#print("name of file is")
#print(f.name)

#print('mode of file is')
#print(f.mode)

with open('text.txt','r') as f:
    #f_content=f.read()
    #print(f_content)


    #f_readAll=f.readlines()
    #print(f_readAll)# it  print alll content in one list

    #f_read1=f.readline()# it print only 1st line
    #print(f_read1,end='')#end deleted unwanted line

    #f_read1=f.readline()# it print second line.
    #print(f_read1,end='')


   #for line in f:
    #   print(line,end='')

#    f_content=f.read(100)#it prints only first 100 character
#    print(f_content)

    size_of=10
    f_content=f.read(size_of)
    print(f.tail())#it gives 10 because we set 10 value 
#    while len(f_content)>0:
#            print(f_content,end='*')
#            f_content=f.read(size_of)




#print(f.closed) #now this file is closed

#print(f.read()) it gives erroe because file is not open yet
#f.close()
