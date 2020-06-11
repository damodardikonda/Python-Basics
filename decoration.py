

#decoration is nothing  but passing an argument of function to the function and returning another function
def outer(message):
    msg=message

    def inner():
        print(msg)

        return inner

mydata=outer('heyyyyyy');
by_fun=outer('byyy');

mydata()
by_fun()
