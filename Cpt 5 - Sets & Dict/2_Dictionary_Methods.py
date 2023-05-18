My_Dictionary = {
    "Fast": "To move in a quick manner" ,
    "Slow": "To not move in a quick manner" , 
 "Medium" : " To move with in an average manner" ,
   "Marks": [1,2,3,4,5] ,
   "Vivaan": "Student",
 "another_Dict": {"Sam":"A coder"},
            1: 2
}
# Dictionary Methods
print(list(My_Dictionary.keys())) # Prints the keys of the dictionary
print(My_Dictionary.keys()) # Prints lists the keys of the dictionary
print(My_Dictionary.values())  # Prints lists the values of the dictionary
print(My_Dictionary.items()) # Prints the tuple of (key, value) for all contents of the dictionary

print(My_Dictionary)
uDicionary={
    "Rohan":"Friend",
    "Vivaan": "Graduate"
}
My_Dictionary.update(uDicionary)
print(My_Dictionary)  # Updates the dictionary by adding key-value pairs from updateDict

print(My_Dictionary.get("Vivaan")) # Prints value associated with key "harry"
print(My_Dictionary["Vivaan"]) # Prints value associated with key "harry"

# The difference between .get and [] sytax in Dictionaries?
print(My_Dictionary.get("harry2")) # Returns None as harry2 is not present in the dictionary
#print(My_Dictionary["harry2"]) # throws an error as harry2 is not present in the dict

# we can also perform arithmetic operations
My_Dict={'key1':'1,2,3','key2':'Hello','key3':100}
My_Dict['key3']=My_Dict['key3']- 123
print(My_Dict['key3'])

# crearing an empty dict & keys and values to it
d={}
d['Animals']='Dog'
d['Marks']=25
print(d)

d={'marks':12,'name':'vint'}
del d['marks']
print(d)
d1=d.copy()
print(d1)
d2={'a':12}
d1.update(d2)
print(d1)

sampleDict={
    "Name":"Kelly",
    "Age": 25,
    "Salalry": 8000,
    "City": "New york",
}
print(sampleDict)
sampleDict['Location']=sampleDict['City']
del sampleDict['City']
print(sampleDict)

# converting 2 lists into a dictionary
l1=['a','b','c']
l2=[1,2,3]
res=dict(zip(l1,l2))
print(res)


# To get key from value
dic = {'Java':100, 'python':200, 'C++':300}
value = {i for i in dic if dic[i]==300}
print(value)