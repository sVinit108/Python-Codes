from os import close, write


f=open('a.txt','a')
f.write(' I am appending')
f.write(' I am appending')
f.write(' I am appending')
f.close()

