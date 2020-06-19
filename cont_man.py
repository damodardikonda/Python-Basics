

class Open_file():

    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open('self.filename',self.mode)
        return self.mode

    def __exit__(self,exe_type,exe_value,traceback):
        self.file.close()


print("this called context manager")

with Open_file('sample.txt','w')as f:
    f.write("This is Testing file")

print(f.close)
