try:
    a=int(input('Enter the number: '))
    b=1/a
except Exception as e:
    print(e)
finally:                             # finally will be executed if code is succesfull or not 
    print('We were Done')
