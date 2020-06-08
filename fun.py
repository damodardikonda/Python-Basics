
def hello_fun():
    print('hello_function')

#executing 4 times
hello_fun()
hello_fun()
hello_fun()
hello_fun()


# if we return a value then print value where they called

def hello():
   return "hello"


print(hello().upper())


#hello() is an string


def h(greeting,name='Damo'):
    print('{} {} world'.format(greeting,name))



h('hellooo',)

#*arg= it is used to printing an list tuple set etc.arg is an variable we cn us anything
#**kwarg = it is used for dictionary

def student(*arg,**kwarg):
    print(arg)
    print(kwarg)

student('math','science','history',name='damodar',mob=11738758)
