a=["Vinit",2,True,"p",3.6,"Krsna"]
print(a[1:3])
print(a[:5:2])
print(a[-1:]) # prints only the last element
print(a[-3:])
print(a[-3:-1])


import numpy as np
l=np.array([[1, 2],[1.5, 1.8],[5, 8],[8, 8],[1, 0.6],[9, 11]])
print(l[:,0])
print(l[:,1])
print(l[-1:,0])
# Thus all methods of string slicing are applicable over here too.
