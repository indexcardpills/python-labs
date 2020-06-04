'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
original_ten="1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
new_list=original_ten.split()
print(new_list[0][0], new_list[0][1])
#I've saved the string into a list, but when I try to print the items in the list, they come out as characters, why?


'''
a=input("enter a number: ")
int(a)
b=input("enter a number: ")
int(b)
c=input("enter a number: ")
int(c)
d=input("enter a number: ")
int(d)
e=input("enter a number: ")
int(e)
f=input("enter a number: ")
int(f)
g=input("enter a number: ")
int(g)
h=input("enter a number: ")
int(h)
i=input("enter a number: ")
int(i)
j=input("enter a number: ")
int(j)
list_of_numbers=[a, b, c, d, e, f, g, h, i, j]
print(f"{b}, {d}, {f}, {h}, {j}, {i}, {g}, {e}, {c}, {a}")
#can i do this faster by getting all of the numbers in one input and making that into a list?
'''
