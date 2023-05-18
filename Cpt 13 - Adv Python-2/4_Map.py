def sqaure(num):
    return num**2
l=[1,2,3]

# Method-1
l2=[]
for i in l:
    l2.append(sqaure(i))
print(l2)

# Method-2
print(list(map(sqaure,l)))