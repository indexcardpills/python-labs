'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
first_number = 5
second_number = 9
range_numbers = range(first_number, second_number)
for x in range_numbers:
    print(sum(range_numbers))
#I'm able to get the sum of all the numbers, but it prints it the amount of times equal to the range
#of the numbers... how do I get it to print once? Also, how do I include the 2nd number in the range?