### Teacher Joel Peltonen
### 19.04.2023
### Py Intro day 3

'''
# check the name
my_name = input("What's your name?: ")
my_age = int(input("How old are you?: "))      ## cast the result of input to an integer
score = 0 

if (my_age <= 17):
    if (my_name == "Vera"):                 ## Conditional statement
        print("Hi Vera")                    ## Indentation is critical in Py!
        print("Looking goof!")
        score = 10
        print("Your score is: ", score)
    elif (my_name == "Raul"):
        print('Heyyyyyyyy Raul!')
        score = 20
        print("Your score is: ", score)
    else:
        print('I dont know you.')
        print("Bye!")
else:
    print("Nope. Just for kidz!")
'''

import random

lucky = random.randint(0, 5)
player = input("Welcome to casino Py! What can I call you? ")
password = input("Enter password: ")

if password != "Swordfish":
    print("Access denied") 
else:
    if player == "James Blond":
        print("Absolutely not. Access denied")
    else:
        if (lucky == 5):
            print('You win big!')
        elif (lucky >= 3):
            print("You win small")
        elif lucky == 0:
            print("You lose big")
        else:
            print("You lose a bit")


