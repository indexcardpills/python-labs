'''
Print out every prime number between 1 and 100.

'''
for number in range(1,100):
   if number > 1:
       for i in range(2,number):
           if (number % i) == 0:
               break
       else:
           print(number)

    #had to look this up. I still don't really understand the for loops part of this...