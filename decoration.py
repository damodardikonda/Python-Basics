

#decoration is nothing  but passing an argument of function to the function and returning another function
def outer(message):
    msg=message

    def inner():
        print(msg)

        return inner

mydata=outer('heyyyyyy');
by_fun=outer('byyy');

#mydata()
#by_fun()



def decorate_fun(original_fun):
    def wrapper_fun():
        return original_fun()
        return wrapper_fun


def display():
    print("Hello World")

disp=decorate_fun(display)

disp()
