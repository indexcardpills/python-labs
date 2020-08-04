'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

import os
warpeace=[]
with open ("books\war_and_peace.txt", "r", encoding="utf8") as store:
    warpeace.append(store.readlines())
print(warpeace[0])
with open ("books\crime_and_punishment.txt", "w") as overwrite:
     overwrite.write("")

for book in os.listdir(r"books\\"):
    #print(f"books\\{book}")
    with open (f"books\\{book}", "r", encoding="utf8") as x:
        first_line=x.readline()
        print(first_line[:0])






