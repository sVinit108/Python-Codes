letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
Name=input("Enter your name\n")
Date=input("Enter the date\n")
letter=letter.replace("<|NAME|>",Name)
letter=letter.replace("<|DATE|>",Date)
print(letter)


