with open('abc.txt','w') as f:
    a=f.write('Hello world')
    f.tell()
print(a)