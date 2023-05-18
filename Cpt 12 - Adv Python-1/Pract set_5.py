a=int(input('Enter the number:'))
b=[a*i for i in range(1,11)]
print(str(b))k
with open('Table.txt','a') as f:
    f.write(str(b))
    f.write('\n')
