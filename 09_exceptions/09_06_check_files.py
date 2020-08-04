'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

with open ('integers.txt', 'r') as fin:
    try:
        x=int(fin.readline())+1
    except IOError:
        print("that's an input-output error")
    except ValueError:
        print("that's a value error")
    else:
        print(x)



