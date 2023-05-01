### Teacher Joel Peltonen
### 20.04.2023
### Py Intro day 4


                        ### Functions ###
'''

- Functions are awesome
- We have already used many
- print(), max(), input()

- A functions defines a block of code
    - that you can call when you need to

'''

# My first function!

print('\n------------------------\n')

def lucky_number():
    print('\nFeeling lucky?')
    print(777, '\n')


# Here we call that function

lucky_number()

def greet(name):
    print('Hello', name, '!!')

greet('VEERA')
greet('ROMA')

print('\n------------------------\n')

def triple(x):
    return x * 3

result = triple(9)
print(result)

my_test = triple('--Hello--')
print(my_test)

print('\n------------------------\n')

import random
money = 100

def double_or_nothing(bet):
    lucky = random.randint(0,1)
    if lucky == 1:
        return +bet
    else:
        return -bet
    
money = money + double_or_nothing(50)
print(money)
