# Print Formatting method (clg)
# a='This a method: {}'.format('I am using the format method')
# b='This a method: %s' %'I am using the format method'
# print(a)
# print(b)

# f formatting
c='thomas'
d=33
print(f"last night {c} scored {d} pts")

# if we want to print only till 2nd decimal
price=17.1234
print(f'Price:- {price:.2f}')

# if we want to print f-string as f-string
print(f'this is a f-string - {{hello}}')


# or concatenation
c='thomas'
d=33
e='Last night, '+c+' socred '+str(d)+' pts'
print(e)

x,y = 'vint' , '19'
print("The name of the student is %s and his age is %s"%(x,y))

