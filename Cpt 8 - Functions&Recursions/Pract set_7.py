# Strip Function
# a='   hello world   '
# print(a)
# print(a.strip())
l1=['Vinit','Vivaan','Deepak','Seema']
a=input('Enter the word: ')
def replace(a):
    if a in l1:
        l1.remove(a) 
        return (l1)
        
    else:
       return print('Word not found ')
print(replace(a))
