'''x='This is a String'.split()
print(type(x))

print(x[2:0:-1])
'''

str = 'This is a String'.split(' ')
print(str)

str = 'This is a sentense'.split('e')
print(str)

str='this is a strings'.split('s')
print(str)

str = 'This is a Sentense'.split('e' , maxsplit=-1);
print(str)

str = 'This is a string'.split('e', maxsplit = 2)
print(str)

str = 'this is a sentense'.split('None' , maxsplit  = 100)
print(str)


str1 = 'abcdbb'.rsplit('b',maxsplit=1)
print(str1)

str1 = ' abcdbb'.rsplit('b',maxsplit = 2)
print(str1)

str1 = 'abcdbb'.split('b',maxsplit=-1)
print(str1)

str1 = 'abcdbb'.rsplit('b',maxsplit=-1)
print(str1)


str1 = 'abcdbb'.rsplit('b',maxsplit=0)
print(str1)

str2 = 'abcdddddeee'.replace('d','e',1)
print(str2);
