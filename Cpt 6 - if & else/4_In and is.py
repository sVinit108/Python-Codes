a=None
if(a is None):
    print("Yes")
else:
    print("No")

b=[25,35,45]
print(45 in b)

# is vs ==
l=[1,2,3]

a=l#[1,2,3]
b=l#[1,2,3]

print(a is b) # is - True if a&b point exact same memory location
print(a==b)   # == - True if values of a&b is identical.