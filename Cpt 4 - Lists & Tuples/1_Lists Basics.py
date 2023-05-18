# Create a list using []
a=[0,1,2,34,5]
print(a)

# Changes the value at 1 or the value of list using
a[1]=99  
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])

# We can create a list with items of different types
c = [45, "Krsna", False, 6.9]
print(c)

# 
l=[1,2,3]
m=l
m[0]=0
print(l,m) # both l & m will change since m is not a new list but a reference to l.
# but if we do
l=[1,2,3]
m=l.copy()
m[0]=0
print(l,m)