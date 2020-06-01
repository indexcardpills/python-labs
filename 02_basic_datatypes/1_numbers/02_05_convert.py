'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
#1)
x=2
print(float(2))
#2)
y=3.5
print(int(y))
#3
z=6.5/2
print(z)
#4
first_number=input("enter any number: ")
second_number=input("enter another number: ")
print(float(first_number)*float(second_number))
