with open('poem.txt','r') as f:
    a=f.read()
if 'Twinkle' in a:
    print('It is present')
else:
    print('It is not present')