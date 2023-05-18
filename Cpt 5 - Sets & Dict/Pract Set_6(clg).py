# Write a Python program to count the number of characters (character frequency) in a string
a=input("Enter the string: ")
d={}
for i in a:
    if i in d:
       d[i] += 1
    else:
       d[i] = 1
print(d)

c={}
c['marks']=2
print(c)
c['marks']=c['marks']+1
print(c)



