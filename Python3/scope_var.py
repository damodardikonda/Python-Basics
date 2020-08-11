'''x = 'global'

def f1():
     global x
     x= 'local'
     x= x*2

     print(x)
     print(x)

print(" global var = " ,x)
f1()
print(" global var = " ,x)

'''

a = 5

def f1():

    global a
    a = 10
    print("Local var" , a)

print("gloabal var = " , a)
f1()

print("gloabal var = " , a)

'''
foo = 1
def func():

  foo = 2




print("global " ,globals()['foo']) # prints 1
print("local",locals()['foo'])
''
foo = 1
def func():

 foo = 2
 print(foo)
 print(globals()['foo'])
 print(locals()['foo'])


func()

''
a = 1
def func():

 a = 7 # global foo is modified
 print(a)
 print(globals()['a'])
 global a
 print(a) 

func()
''

foo = 1
def func():
 # This function has a local variable foo, because it is defined down below.
 # So, foo is local from this point. Global foo is hidden.
# print(foo) # raises UnboundLocalError, because local foo is not yet initialized
 foo = 7

 print(foo)
 print(globals()['foo'])

func()
'''
a = 1
def func():
 # In this function, foo is a global variable from the beginning



 global foo # this could be anywhere within the function

 print(foo) # 7
# print(locals()['foo']) # 1
 foo = 7 # global foo is modified
 print(foo) # 7

func()
