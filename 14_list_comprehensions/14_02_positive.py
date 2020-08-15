'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
# positive_list=[]
# for x in numbers:
#     if x > 0:
#         positive_list.append(x)
# print(positive_list)
positive_list=[x for x in numbers if x > 0]
print(positive_list)
