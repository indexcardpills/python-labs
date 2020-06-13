'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
numbers = "7, 6, 8, 9"
numbers_without_spaces = numbers.replace(" ", "")
list_of_numbers = [numbers_without_spaces]
numbers_sorted=sorted(list_of_numbers)
print(numbers_sorted)
#why is this not sorting?