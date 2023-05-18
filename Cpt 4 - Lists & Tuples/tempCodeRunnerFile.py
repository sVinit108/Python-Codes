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