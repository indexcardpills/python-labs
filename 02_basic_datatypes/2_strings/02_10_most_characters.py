'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
string_one=input("type a word: ")
string_two=input("type another word: ")
string_three=input("type another word: ")
print(len(string_one), string_one)
print(len(string_two), string_two)
print(len(string_three), string_three)
