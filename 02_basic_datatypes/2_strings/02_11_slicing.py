'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
name=input("What's your name: ")
first_letter=name[0]
first_letter_removed=(name[1:])
first_letter_moved_to_end=first_letter_removed+first_letter
pig_latin=first_letter_moved_to_end+"ay"
print(pig_latin)
#print(name)
#don't think this has been covered yet in course?