'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

daniel = (x+'f' for x in "hello")
for x in daniel:
    print(x)
