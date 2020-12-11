result = 0
def fact(n):
    if n == 0 :
        result = 1
    else :
        result = n * fact(n-1)
    return result


print(fact(4))
print(fact(5))
print(fact(10))
