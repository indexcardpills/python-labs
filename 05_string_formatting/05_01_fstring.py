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
first_item = famous_quotes[0]
first_name=first_item["full_name"]
first_quote=first_item["quote"]
second_item=famous_quotes[1]
second_name=second_item["full_name"]
second_quote=second_item["quote"]
third_item=famous_quotes[2]
third_name=third_item["full_name"]
third_quote=third_item["quote"]
fourth_item=famous_quotes[3]
fourth_name=fourth_item["full_name"]
fourth_quote=fourth_item["quote"]
fifth_item=famous_quotes[4]
fifth_name=fifth_item["full_name"]
fifth_quote=fifth_item["quote"]
sixth_item=famous_quotes[5]
sixth_name=sixth_item["full_name"]
sixth_quote=sixth_item["quote"]
seventh_item=famous_quotes[6]
seventh_name=seventh_item["full_name"]
seventh_quote=seventh_item["quote"]
print(f'\"{first_quote}\" - {first_name}\n\"{second_quote}\" - {second_name}\n\"{third_quote}\" - {third_name}\n\
\"{fourth_quote}\" - {fourth_name}\n\"{fifth_quote}\" - {fifth_name}\n\"{sixth_quote}\" - {sixth_name}\n\
\"{seventh_quote}\" - {seventh_name}')
# How would I make it print Lastname, Firstname?
# Also, is there a faster/more efficient way of doing this? Or do I have to break it down into variables the
# way I did here?

