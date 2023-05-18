def greatest(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
         if n2>n3:
            return n2
         else:
            return n3
print(greatest(4,6,3))

