'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

for dictionary in office:
    name = dictionary["full_name"]
    item = dictionary["item"].capitalize()
    list_names = name.split()
    last_names = list_names[1].upper()
    first_names = list_names[0]
    if (len(name)) == 10:
        print(f"{last_names}, {first_names:<20}{item}")
    if (len(name)) == 11:
        print(f"{last_names}, {first_names:<19}{item}")
    if (len(name)) == 12:
        print(f"{last_names}, {first_names:<18}{item}")
    if (len(name)) == 13:
        print(f"{last_names}, {first_names:<17}{item}")
    if (len(name)) == 14:
        print(f"{last_names}, {first_names:<16}{item}")
    if (len(name)) == 15:
        print(f"{last_names}, {first_names:<15}{item}")

#how do I get the items to align? I've tried putting the spacing in with the item variable and it still
#doesn't work...