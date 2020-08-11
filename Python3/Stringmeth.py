'''s= 'Dammy'
print(id(s))
 s1=s.replace('mm','xx')
print(id(s1))
print(s1)


''
s2='abb$$$bfc'.replace('$','DAms')
print(s2)
''


S = 'xxxxxxSPAMSxxxxSPAMSxxxx'
where = S.find('dd') # Search for position
print(where)
'

s3= 'Damdaamdaamdam'
s2=s3.replace('d','y',1)
print(s2)
''
s4 = 'dams'
s5='$'.join(s4)
print(s5)
print(id(s4))
print(id(s5))
''

s4 = (['d','a','m','s'])
s5='%'.join(s4)
print(s5)
print(id(s4))
print(id(s5))
''

s3= 'Dam,daam,daam,dam'
s2=s3.split(',')
print(s2)

''

x='abcAAAA'.casefold()
print(x)
''

str='This is a string'
str1 = str.lower();
print(str1)
print(id(str))
print(id(str1))
''

str='This is a string'
str1 = str.upper();
print(str1)
print(id(str))
print(id(str1))

''
str='This is a string'
str1 = str.title();
print(str1)
print(id(str))
print(id(str1))
'''


zz='abcabaca'
ss=zz.find('hh')
print(ss)
