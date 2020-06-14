'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
sum_number=0
first_number = 5
second_number = 9
range_numbers = range(first_number, second_number+1)
for x in range_numbers:
    print(sum_number+first_number)
    if sum_number == second_number+1:
        break
# I think I'm getting closer? But now I don't know what else to do. I initialized a variable outside
# the for loop, but beyond that, I don't know what to do with it exactly. With this I just get 5 printed
# 5 times.

