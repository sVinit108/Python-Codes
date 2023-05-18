import this
# PEP 8 - Python enhancement proposal

def funct(a):
    '''This fun prints the sqaure of the number'''
    return a*a
a=int(input('Enter the number:'))
print(funct.__doc__)  # this will print the comment inside the function.
print(funct(a))

