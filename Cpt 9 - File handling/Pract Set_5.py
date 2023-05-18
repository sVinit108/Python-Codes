word=['in','the']
with open('Q4.txt') as f:
    a=f.read()
for word in word: 
    a=a.replace(word,'****')
with open('Q4.txt','w') as f:
    f.write(a)