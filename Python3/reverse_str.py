'''abc=reversed('hello');
print(abc)
print(type(abc))


xyz =[(ch) for ch in abc]
print(xyz)



name = ''.join(reversed('hello'))
print(name)


def rever(string):
    return string[::-1]

rever('hello');

'''



s='aaaabbcca'
print(s.count('a',6,1))


ss = 'String'
print(ss.ljust(30, '*' ))
print(ss.rjust(30,"$" ))



str = "This is a string.";
'''print(str.startswith(" T"))
print(str.startswith("Th"))
print(str.startswith("a"))
print(str.startswith("t"))
'''

print(str.startswith("is" , 2))
print(str.startswith(" is",2 ))
print(str.startswith("T " ))


print(str.startswith(("b","a")))



s = b'\xc2\xa9 abc'
print(type(s));
u = s.decode('utf-8');
print(u)

z = u.encode('utf-8')
print(z)
