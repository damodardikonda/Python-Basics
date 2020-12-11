'''
with open('fred.txt', 'w') as outfile:
 s = "I'm Not Dead Yet!"
 print(s) # writes to stdout
 print(s, file = outfile) # writes to outfile
 myfile = None
 print(s, file = myfile) # writes to stdout
 print(s, file = None) # writes to stdout
''

import mmap
with open('abc.txt', 'r') as fd:
 # 0: map the whole file
 mm = mmap.mmap(fd.fileno(), 0)
 # print characters at indices 5 through 10
 print(mm[5:10])

 print(mm.readline())

 mm[10]='a'
 print(mm[10])

 print(mm.seek())
'''
with open('abc.txt','r') as f:

    line = f.read()

    replace_str=line.replace('tomatoes' ,'onions')

    wf=f.write(replace_str)

with open('abc.txt' , 'r+')as f:
    print(f.read())
