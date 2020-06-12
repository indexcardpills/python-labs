'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
while True:
    number = int(input("Enter a number between 0 and 1,000,000,000: "))
    x = 7
    if number < x:
        print("no, higher")
    if number > x:
        print("no, lower")
    if number == x:
        print("correct")
        break
