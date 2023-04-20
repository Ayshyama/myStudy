### Teacher Joel Peltonen
### 20.04.2023
### Py Intro day 4


                        ### LOOPS ###
'''

- loops repeat code
- the simplest loop in Py is the 'while' loop
- the while loop is based on a conditional
    - kind of like an 'if'
    - the while runs a block of code until the condition

'''

number = 0
while (number > -1):
    number += 1
    
    print(number)
    break
print('Done')

import sys

print(sys.maxsize)

'''

- In Py 'for' loops go over some kind of sequence
    - like characters in a string
    - like items in a list
    - so what is a list???

- Lists store multiple items in a single variable
    - The items could be strings
    - The items could be numbers
    - List are 'indexed'
    - Indexes start from zero
    - Indexes are zero-based

'''
print('------------')

my_name = 'Igor'
foods = ['Banana', 'Coffee', 'Honey', 100]

print(foods[1])
print(foods[3])
print('------------')

for x in foods:
    print(x)

print('------------')

for pet in ['Cat', 'Dog', 'Rat']:
    print('I want a', pet)

print()

for char in 'Coffee':
    print(char)

print()

drink = 'Tea'
print(drink[0])
print()


'''

- Ranges are indexed

'''



my_range = range(2, 5)
print(my_range)
print()

for x in my_range:
    print(x)
    
print()

print(my_range[1])

print()
print('------------')
print()


fun_fruits = ['Rawberry', 'Cutecumber', 'Melown']

for f in fun_fruits:
    print(f)
    for char in f:
        print(char)

