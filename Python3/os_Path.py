import os

print(os.getcwd())

#op:=C:\py4e\prac\gitt\Python3

os.chdir("C:\py4e\prac\gitt")

print(os.getcwd())

#os.chdir("C:\py4e\prac\gitt")
#print(os.getcwd())

#print(os.listdir())

print(os.stat('checking.txt'))

print(os.stat('checking.txt').st_size)
