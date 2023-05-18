# Concatenating/Adding of two strings
greeting="Hare krsna , "
name="Vinit"
print(greeting + name)

name2="Krishna"
# print(name2[1]) # Counting starts from 0 and not 1.
print(name2[1:5]) # THis is known as str slicing .It will print only element 1 to  and not 5.
# print(name2[:5]) # same as [0:5]
# print(name2[1:]) # same as [1:5]
print(name2[-5:-1]) # same as [3:7]

name3="HareKrsna"
print(name3[0::2]) # by this it will print  alternate elements
