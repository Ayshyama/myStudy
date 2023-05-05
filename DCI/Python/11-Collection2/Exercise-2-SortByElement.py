#### TASK 2 ####

## Exercise (sort by second element):
# Write a Python program that sorts a list of tuples based on the second element of each tuple.
# The program should take a list of tuples as input from the user,
# Sort the tuples by the second element using the sort() method with a custom function
# print the sorted list of tuples

# print('#### TASK 2 ####')

# # func
# def sort_helper(tuple):
#     return tuple[1]


# # sort
# tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)]
# tuple_list.sort(key=sort_helper)

# # print
# print(tuple_list)


 
print('#### TASK 2 ver.2 ####')
# (2, 5);(1, 7);(4, 3);(6, 100);(3, 8)

my_input = input("Enter original list of tuples. Use ';' as separator: ")
my_new_list = my_input.split(';')

def get_int(tuple_str, pos):
    return tuple_str[1:-1].split(',')[pos]



# my_int_list = [(int(tuple_str[1:-1].split(',')[0]),int(tuple_str[1:-1].split(',')[0])) for tuple_str in my_new_list]
print(my_int_list)

def sorting_helper(my_tuple):
    # print(my_tuple[1])
    return my_tuple[1]

my_int_list.sort(key=sorting_helper)
print(my_new_list)





# print('#### TASK 2 BONUS ####')

# tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)]
# tuple_list.sort(key=lambda x: x[1])

# print(tuple_list)