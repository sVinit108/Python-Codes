a = 8

# 1. if-elif-else ladder in Python
# if(a<3): 
#     print("The value of a is greater than 3")
# elif(a>13):
#     print("The value of a is greater than 13")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>17):
#     print("The value of a is greater than 17")
# else:
#     print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:                                              # else statement is optional
    print("The value is not greater than 3 or 7")

print("Done")

# Shorthand  if-else
a=100
b=10
print('a<b') if a<b else print('a==b') if a==b else print('a>b')