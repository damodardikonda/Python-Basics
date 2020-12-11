class Op_Overloading:

    def __init__(self , page):
        self.page = page

    def __add__(self , other):
        return self.page + other.page

    def __sub__(self , other):
        return self.page - other.page

    def __mul__(self , other):
        return self.page * other.page
'''
    def __div__(self , other):
        return self.page / other.page

'''
b1 = Op_Overloading(100)
b2 = Op_Overloading(200)

print(b1+b2)
print(b2-b1)
#print(b2/b1)
print(b1*b2)
