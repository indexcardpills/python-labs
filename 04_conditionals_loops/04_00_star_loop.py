'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
numbers = range(6)
for x in numbers:
    if x == 1:
        print("*")
    if x == 2:
        print("**")
    if x == 3:
        print("***")
    if x == 4:
        print("****")
    if x == 5:
        print("*****")

#Is there a more efficient way of doing this? Also, the initial n variable on line 13 was already provided
#here in the lab so I didn't take it out.
