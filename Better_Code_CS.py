# 1
'''
condition = True
if condition:
    x=1
else:
    x=0
print(x)
'''
# or
condition = True
x = 1 if condition else 0
print(x)

# 2
'''
num1 = 10000000000
num2 = 100000000
total = num1+num2
print(total)
'''
# or
num1 = 10_000_000_000
num2 = 100_000_000
total = num1+num2
print(f'{total:,}')

# 3
'''
letters = ['a','b','c','d']
index = 1
for letter in letters:
    print(index,letter)
    index+=1
'''
# or
letters = ['a','b','c','d']
for index,letter in enumerate(letters,start=1):
    print(index,letter)

# 4
'''
person = ['vinit','vivaan','vijay']
profession = ['student','student','teacher']
for index,letter in enumerate(person):
    prof = profession[index]
    print(f'{person} is actually {prof}')
'''
# or
person = ['vinit','vivaan','vijay']
profession = ['student','student','teacher']
for person,prof in zip(person,profession):
    print(f'{person} is actually {prof}')

# 5
#Unpacking
a,b = (1,2)
print(a) #1
print(b) #2

a,_=(1,2) # _ is added to avoid value-error
print(a) #1

a,b,*c = (1,2,3,4,5) # * will assign all remaining values to c.
print(a) #1
print(b) #2
print(c) #[3,4,5]

a,b,*c,d = (1,2,3,4,5) # * will assign all remaining values to c except for last val which will be asigned to d.
print(a) #1
print(b) #2
print(c) #[3,4,5]
print(d) #5

#6
# setattr() & getattr()
