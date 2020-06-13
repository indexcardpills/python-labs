'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
number = int(input("enter a number: "))
if number == 1:
    print("January")
if number == 2:
    print("February")
if number == 3:
    print("March")
if number == 4:
    print("April")
if number == 5:
    print("May")
if number == 6:
    print("June")
if number == 7:
    print("July")
if number == 8:
    print("August")
if number == 9:
    print("September")
if number == 10:
    print("October")
if number == 11:
    print("November")
if number == 12:
    print("December")
if number > 12:
    print("Other")