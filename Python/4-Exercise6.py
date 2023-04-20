import random

### TASK 1
'''
number = random.randint(1, 100000)
guess = 0
guess_counter = 0

while guess != number:
    guess = int(input('Guess a number between 1 and 100000: '))
    guess_counter += 1

    if guess < number:
        print('It is too low! Try again. ')
    
    elif guess > number:
        print('It is too high! Try again.')
    
    else:
        print('Cool! You guessed the number! Your total number of attempts is: ', guess_counter)

'''

### TASK 2

num1 = 0
num2 = 1
for i in range(1000):
    print(num2, end='  ')
    remember = num1 + num2
    num1 = num2
    num2 = remember



