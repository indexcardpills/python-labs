'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

numbers = [20, 50, 2222, 35, 5555, 60, 8888]
gen=(x for x in numbers if x%1111==0)
for x in gen:
    print(x)