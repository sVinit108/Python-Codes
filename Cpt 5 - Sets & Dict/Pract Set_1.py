mydict = {
    "name":"नाम",
    "house": "मकान",
    "water": "पानी",
}
print("The options are: ",mydict.keys())
a=input("Enter the word: ")
print("The hindi trans of the word is: ",mydict.get(a))

