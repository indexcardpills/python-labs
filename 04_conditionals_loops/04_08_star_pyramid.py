'''
Write a script that takes in a number from the user as input and prints the following structure.

Suppose the input is 5, you will output
*
* *
* * * 
* * * *
* * * * * 
i.e. number of rows will be 5, 1st row will have 1 star, 2nd row will have 2 stars, 3rd row 3 stars, 4th row will have 4 stars and 5th row will have 5 stars.

Another example: if input is 3, you will output
*
* *
* * *

Hint: Think of nested for loops

'''
number = int(input("enter a number: "))
rows = range(1, number+1)
for x in rows:
    if number ==

# I'm stuck. This is similar to the first star loop lab, but in this one I need to take an input so I can't
# just assign a number to the number variable and print however many rows and stars I assign.