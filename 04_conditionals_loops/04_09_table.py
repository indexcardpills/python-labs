'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
'''
single_digits = range(0, 10)
teens = range(10, 20)
for x in single_digits:
    print(x)
for y in teens:
    print(y)
#how do I make it print on different lines to create a table?
'''

for x in range(0,50):
    if (x+1)%10 == 0:
        end_char = "\n"
    else:
        end_char = " "
    print(x, end=end_char)
#had to look this up. I think I get it, but I'm not sure what the end part on the last line is for, does that
#just end the loop?