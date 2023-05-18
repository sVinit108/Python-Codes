while(True):
    print('Press q to exit')
    a=input('Enter the number: ')
    if a=='q':
        break
    try:
        print('Trying.....')
        a=int(a)
        if a>6:
            print('You have a number greater than 6')
    except Exception as e:
        print(f'Your input resulted in an error: {e}')
print('Thanks for the game')

