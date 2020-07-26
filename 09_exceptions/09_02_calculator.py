'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    x = int(input("enter a number: "))
    y = int(input("enter another number: "))
    print(x/y)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("must enter a number")
