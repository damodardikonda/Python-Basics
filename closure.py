#closure


#def outer():
#    msg='hii'

#        print(msg)

#        return inner()

#outer()



def outer():
    msg='hii'

    def inner():
        print(msg)

        return inner

mydata=outer()


print(mydata)
print(mydata)
print(mydata)
print(mydata.__name__)
