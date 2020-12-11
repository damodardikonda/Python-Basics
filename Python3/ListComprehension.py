print([x*x for x in (1,2,3,4)])

ch = [s.upper() for s in ("hwllo World")]
print(ch)

ch1=[x if x in 'aeiou' else '*' for x in 'apple']
print(ch1)

ch2 = [ x if x in 'd' else '*' for x in 'damodar']
print(ch2)
'''foo=[1,2,3,4,5]
y=[ str(x) for i in range(3) for j in foo(i) ]
print(y)
''
abc=[sorted(x) for x in [[3,1,2],[5,3,4],[6,4,2]]]
print(abc)

[print(x) for x in(1,2,3)]

a = [1,2,3,4,5]
b= [1,3,5]

[print(x) for x in a if x not in b]


[print(y) if y not in b else '*' for y in range(10) ]

[print(x) for x in 'human']


s=[x if x % 2 == 0 else " it is odd number" for x in range(20)]
print(s)

even = [x for x in range(20) if x % 2 == 0]
print(even)

num = [x for x in range(50) if x % 5==0 if x % 2 ==0]
print(num)

num1 = [ x  for x in range(50) if x % 5 == 0  elif x % 2==0]
print(num1)
''
xx=[1,2,3,4,5,6,7,8,9]
num=[2*(if x % 2 == 0 else -1)+1 for x in xx ]
print(num)
''

ss = [x if x > 2 else '*' for x in range(10) if x % 2 == 0]


v= [v for v in (f(x) for x in range(100)) if v > 10]
print(v)
''


a=[f(x) for x in range(1000) if f(x) > 10]
print(a)
'''
r=(x**2 for x in xrange(10))
print(r.next())
