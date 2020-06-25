'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]
for dictionary in famous_quotes:
    name= dictionary["full_name"]
    last_first=', '.join(reversed(name.split()))
    quotes=dictionary["quote"]
    print(f'\"{quotes}\" - {last_first}')



'''
first_item = famous_quotes[0]
first_name=first_item["full_name"]
name_one=', '.join(reversed(first_name.split()))
first_quote=first_item["quote"]
second_item=famous_quotes[1]
second_name=second_item["full_name"]
name_two=', '.join(reversed(second_name.split()))
second_quote=second_item["quote"]
third_item=famous_quotes[2]
third_name=third_item["full_name"]
name_three=', '.join(reversed(third_name.split()))
third_quote=third_item["quote"]
fourth_item=famous_quotes[3]
fourth_name=fourth_item["full_name"]
name_four=', '.join(reversed(fourth_name.split()))
fourth_quote=fourth_item["quote"]
fifth_item=famous_quotes[4]
fifth_name=fifth_item["full_name"]
name_five=', '.join(reversed(fifth_name.split()))
fifth_quote=fifth_item["quote"]
sixth_item=famous_quotes[5]
sixth_name=sixth_item["full_name"]
name_six=', '.join(reversed(sixth_name.split()))
sixth_quote=sixth_item["quote"]
seventh_item=famous_quotes[6]
seventh_name=seventh_item["full_name"]
name_seven=', '.join(reversed(seventh_name.split()))
seventh_quote=seventh_item["quote"]
print(f'\"{first_quote}\" - {name_one}\n\"{second_quote}\" - {name_two}\n\"{third_quote}\" - {name_three}\n\
\"{fourth_quote}\" - {name_four}\n\"{fifth_quote}\" - {name_five}\n\"{sixth_quote}\" - {name_six}\n\
\"{seventh_quote}\" - {name_seven}')
'''

