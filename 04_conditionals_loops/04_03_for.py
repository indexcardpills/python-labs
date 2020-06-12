'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
numbers = range(1, 100)
for odd_numbers in numbers:
    if odd_numbers % 2:
        print(odd_numbers)