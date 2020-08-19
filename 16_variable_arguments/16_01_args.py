'''
Write a script with a function that demonstrates the use of *args.

'''

def tennis_score(*args):
    for x in args:
        print(x)


tennis_score('love', 15, 30, 40, 'deuce', 'advantage')