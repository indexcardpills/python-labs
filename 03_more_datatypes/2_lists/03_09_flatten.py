'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [starting_list[0][0], starting_list[0][1], starting_list[0][2], starting_list[0][3],
                  starting_list[1][0], starting_list[1][1], starting_list[2][0], starting_list[2][1],
                  starting_list[2][2]]
print(flattened_list)
