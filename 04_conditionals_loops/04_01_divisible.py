'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
number = int(input("enter a number between 1 an 1,000,000,000: "))
if number % 3 == 0:
    print("the number is divisible by 3")
else:
    print("the number is not divisible by 3")