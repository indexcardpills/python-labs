'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def tennis_score(**kwargs):
    for x in kwargs.items():
        print(x)
tennis_score(zero='love', one=15, two=30, three=40)

