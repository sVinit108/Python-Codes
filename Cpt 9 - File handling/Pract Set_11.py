import os
filename='sample2.txt'
with open(filename,) as f:
    content=f.read()
with open('renamed_by_python','w') as f:
    f.write(content)
os.remove(filename)