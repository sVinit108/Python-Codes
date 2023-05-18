with open('Q4.txt') as f:
    a=f.read()
a=a.replace('the','****')
with open('Q4.txt','w') as f:
    f.write(a)


