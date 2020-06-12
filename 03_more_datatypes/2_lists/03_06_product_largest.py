'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

numbers=(input("enter ten single digit numbers: "))
list_of_numbers=list(numbers)
max_in_list=max(list_of_numbers)
print(max_in_list)
#It's just giving me the highest single digit, what am I doing wrong? Below i did each number as a separate variable
'''
first_number=input("enter a number: ")
int(first_number)
second_number=input("enter a number: ")
int(second_number)
third_number=input("enter a number: ")
int(third_number)
fourth_number=input("enter a number: ")
int(fourth_number)
fifth_number=input("enter a number: ")
int(fifth_number)
sixth_number=input("enter a number: ")
int(sixth_number)
seventh_number=input("enter a number: ")
int(seventh_number)
eighth_number=input("enter a number: ")
int(eighth_number)
ninth_number=input("enter a number: ")
int(ninth_number)
tenth_number=input("enter a number: ")
int(tenth_number)
list_of_numbers=[first_number, second_number, third_number, fourth_number, fifth_number, sixth_number,
                 seventh_number, eighth_number, ninth_number, tenth_number]
largest_number=max(list_of_numbers)
print(largest_number)
#could I have saved all the numbers into one variable and created a list out of that?

'''