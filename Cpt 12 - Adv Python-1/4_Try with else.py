try:
    a=int(input('Enter the number: '))
    b=1/a
except Exception as e:
    print(e)
else:                           # if the code has successfully executed else will run else it won't.
    print('We were successful')
