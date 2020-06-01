'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
original_sentence=input("type a sentence: ")
symbol=input("enter a symbol: ")
first=original_sentence[0]
print(original_sentence.replace(first, symbol))
