#### TASK 1 ####

## Exercise (Vowel Sort):
# Write a Python program that sorts a list of strings based on the number of vowels they contain.
# The program should take a list of strings as input from the user.
# Sort the strings by the number of vowels they contain using the sort() method with a custom function.
# Print the sorted list of strings.

# my_strings = ['blaaa', 'bla', 'blaa'] --> ['bla', 'blaa', 'blaaa']
print('#### TASK 1 ####')

# input
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

my_strings = input("Write some strings to the list, separate it by a comma: ").split(',')

# sorting
my_strings.sort(key=count_vowels)

# print
print("Sorted list of strings based on number of vowels:")
print(my_strings)

