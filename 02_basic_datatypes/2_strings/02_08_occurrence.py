'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
string=input("type some words: ")
first_letter=input("type a letter found in the words: ")
index=string.find(first_letter)
print("the first occurence of that letter is: ", index)
