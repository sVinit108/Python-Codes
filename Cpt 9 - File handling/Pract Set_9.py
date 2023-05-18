with open('poem.txt') as f:
    f1=f.read()

with open('Q8(1).txt') as f:
    f2=f.read()
if f1==f2:
    print('Files are identical')
else:
    print('Files are not identical')