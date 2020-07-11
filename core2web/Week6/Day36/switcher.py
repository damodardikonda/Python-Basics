
'''
num=int(input("Enter 1 for Binary,2 for hexa and 3 for octal"));

if num==1:
    print(bin(num));
elif num==2:
    print(hex(num));
elif num==3:
    print(oct(num))

    '''


def numbers(num):
    switcher={
      0:    print(bin(num));
      1:    print(hex(num));
      3:    print(oct(num))


    }

    return switcher.get(num,"nothing")

if __name__ == "__main__":
num=int(input("Enter 1 for Binary,2 for hexa and 3 for octal"));
    print numbers_to_strings(num)
