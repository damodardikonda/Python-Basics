

#try:
#    f=open('new_name.csv')
#    var=bad
#except FileNotFoundError:
#    print('Sorry file does not exist')
#except Exception as e:
#    print(e)



try:
    f=open('new.csv')
    if f.name=='new.csv':
        raise Exception #manual Exception
except FileNotFoundError:
    print('Sorry file does not exist')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Execute these at any cost');
