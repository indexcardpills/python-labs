'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]
no_duplicates=list(dict.fromkeys(list_))
print(no_duplicates)
#I just looked this up...