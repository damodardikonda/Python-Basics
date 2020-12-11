'''
s = lambda n : n*n
print(s(4))
print(s(8))
print(s(18))


x = lambda a, b : a+b
print(x(10,20))
print(x(50,100))




x = lambda a, b ,c,d,r,v,g,t,h : a+b+c+d+r+v+g+t+h

print(x(10,20,30,40,50,60,70,80,90))
print(x(50,100,150,200,250,300,350,400,450))



lam = lambda 10,20,30 : 10+20+30
print(lam())



ll = lambda a,b,c : a+b+int(c)
print(ll(10,20,30.5))



fun = lambda a,b : a if a>b else b
print(" b is greater" , fun(5,10))

'''
'''
Filter()

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

l1 = [1,2,3,4,5,6,7,8,9,10,12,16,18,90,67]

print(type(filter(isEven , l1)))
l2 = list(filter(isEven , l1))
print(l2)

print(type(l2))


l1=[2,3,4,5,6,7,8,9,0,12,14,13,15,45,31,50]
l2 = list( filter( lambda x : x%2==0 , l1 ) )
print(l2)

l3 = tuple( filter(lambda x: x% 2 == 1 , l1))
print(l3)

'''


'''
map()


def Doub(x):
    return x*2
l=[5,10,34,12,14,38,65]
l1=list( map(Doub,l))
print(l1)



l=[4,5,78,6,9,7,23,87]
l1 = list(map(lambda s : s*2  , l ))
print(l1)


l1=[4,5,78,6,9,7,23,87]
l2=[2,3,4,5,6,7,8,9]
l3 = list(map(lambda s,y : s*y  , l1 ,l2 ))
print(l3)



l1=[4,5,78,6,9,7,23,87]
l2=(02,3,4,5,6,7,8,9)
l3 = list(map(lambda s,y : s*y  , l1 ,l2 ))
print(l3)


'''
import functools

l=[1,2,3,4,5,6,7,8,9,12,1,3,54]
s = functools.reduce(lambda x , a : x + a , l )
print(s)
