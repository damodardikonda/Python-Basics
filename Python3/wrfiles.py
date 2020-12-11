
with open('abc.txt','w') as fileobj:
    fileobj.write('tomatoes eggs chicken\ncarrot\n whiskey  \n beer \n rum')


#print(fileobj)


with open('abc.txt','r') as r:

    list = r.readlines();

    print(list)
    print(type(list))



with open('a.txt','r') as r:

    list1 = r.readlines();

    print(list1)
    print(type(list1))



with open('abc.txt','r') as r:

    content = r.read();

    print(content)
    print(type(content  ))
