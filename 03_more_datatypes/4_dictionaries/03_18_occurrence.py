'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
string = "Write a script that takes a string from the user and creates a dictionary of letter that exist\
in the string and the number of times they occur. For example:"
result = {}
for letter in string:
    if letter=="a":
        continue
    if letter in result:
        result[letter] += 1
    else:
        result[letter]=1

print(result)



#tuple = tuple(string)
#print(tuple)
#occurences = tuple.count(string)
