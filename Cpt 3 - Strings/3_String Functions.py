story = "once upon a time there was a youtuber named Harry who uploaded python course with notes Harry "
# String Functions
print(len(story)) # prints the length of the strings.
print(story[0:25])
print(story.endswith("notes")) # true if story ends with notes or else false
print(story.count("c")) # counts the total occurance of any character. can be used for words too.
print(story.capitalize()) # capitalizes the 1st letter of the string. 
print(story.find("upon")) # Finds the 1st occurance of the word in the string. -1 means false , its not there.
print(story.replace("Harry", "CodeWithHarry")) # this replaces the old word with the new word in the entire string.

