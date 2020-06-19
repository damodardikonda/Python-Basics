from contexlib import contextmanager

@contextmanager
def Open_file(file , mode):
    f=open(file , mode)
    yield f  # here all statement of with is going to run..
    f.close()


with open('sample1.text','w') as f:
    f.write("this is an testing file so lets check")


print(f.close)
