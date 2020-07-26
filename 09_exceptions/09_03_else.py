'''
Write a script that demonstrates a try/except/else.

'''

try:
    x = int(input("enter a number: "))
    y = int(input("enter another number: "))
    print(x/y)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("must enter a number")
else:
    print("no errors")