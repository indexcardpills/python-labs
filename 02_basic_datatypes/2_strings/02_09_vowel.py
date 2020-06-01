'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
#string=input("write a sentence: ")
string="the dog ate the cat"
a=string.count("a")
e=string.count("e")
i=string.count("i")
o=string.count("o")
u=string.count("u")
print(a+e+i+o+u)
