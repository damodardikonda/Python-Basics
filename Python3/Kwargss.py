


def display( **Kwargs):
    print(type(Kwargs))

    for k , v in Kwargs.items():
        print( k , "........" , v)


display( name = " Damodar" , Age = 21 , mob = 899252586 , marks =90)
display(name = " Dikonda " , gf = " single" , friends="Alot")
display(education = " BEC" , clg =" Bhikarda")
