'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
# fish_list=[]
# for x in fish_tuple:
#     if x.endswith('fish'):
#         fish_list.append(x)
# print(fish_list)
fish_list=[x for x in fish_tuple if x.endswith('fish')]
print(fish_list)


