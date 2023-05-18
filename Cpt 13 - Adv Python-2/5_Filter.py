# Filter syntax: list(filter(function,list/tuple/set)) , function can be a lambda
from typing import List


def greater_than_5(n):
    if n>5:
        return True
    return False
g10 = lambda n:n>10
l=[1,2,3,7,8,456,78,99,455]  
print(list(filter(greater_than_5,l)))
print(list(filter(g10,l)))

# to remove all occurance of an element from a list
l=[1,2,3,1,4,5]
l1=list(filter(lambda a:a!=1,l))
print(l1)