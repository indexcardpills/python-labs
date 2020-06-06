'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
script = "hi dan"
list_of_words = str.split(script)
first_word_tuple = tuple(list_of_words[0])
second_word_tuple = tuple(list_of_words[1])
list_of_tuples=[first_word_tuple, second_word_tuple]
print(list_of_tuples)
#what would I do if there was more than 2 words inputted by the user?


#tuple_of_letters_0 = tuple(list_of_words[0])
#list_of_tuples_0 = list(tuple_of_letters_0)
#tuple_of_letters_1 = tuple(list_of_words[1])
#list_of_tuples_1 = list(tuple_of_letters_1)
#print(list_of_tuples_0+list_of_tuples_1)
#print(tuple_of_letters_0+tuple_of_letters_1)


