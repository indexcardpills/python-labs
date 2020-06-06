'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_one = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = list(dict.fromkeys(list_one))
print(unique_list)
#still have values that have duplicates printed once. same as my attempt below.
'''
unique_set = set(list_one)
unique_list = list(unique_set)
print(unique_list)
still have values that have duplicates printed once.....
'''