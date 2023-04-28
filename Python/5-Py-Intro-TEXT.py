### Teacher Joel Peltonen
### 21.04.2023
### Py Intro day 5 


                        ### TEXT DAY ###


            ## **Yesterday**
'''
- 'while' loops
- 'for' loops
- 'functions'
'''


            ## **Today**
'''
- Fibonacci task demo
- Methods!
    - What's a method?
    - String methods
    - One list method
'''

            ## **Fibonacci**
'''
- Print out the first 50 numbers of the Fibonacci series
- A classic programming puzzle, common in coding challenges when applying for jobs
- The Fibonacci series is a series of numbers starting with 1, 1, 2, 3, 5...
- Each new number is the sum of the previous two numbers
- You can use a `for` loop and the `range` function, but you don't have to :)
'''

'''
prevprev = 0
prev = 1
current = 1

for i in range(1000):                   # using 'i' is a convention, could stand for iteration, index, integer....
                                              #  Measure-Command {py 5-Py-Intro-day-Text-day.py}
    prevprev = prev
    prev = current
    current = prev + prevprev

print(prev)

'''

            ## **Methods**
'''
- Methods are special kinds of functions
    - We have used many functions
    - We even created our own functions

- Methods are functions that are associated with an object
    - More on objects later
    - we will focus on two kinds of methods
        - String methods
        - List methods

- String methods are functions that we call on individual string
'''

'''
my_text = 'is TEST'

print(my_text.upper())
print(my_text.capitalize())
print(my_text.lower())
print(my_text.isalpha()) # alpha = part of Alphabet
'''

text = 'Rauli\n\tStrength: 3\n\tInt: 2\n\tHP: 7'
print(text)

print('\n--------------------------\n')

print(len('caramel ice'))
print(len(['wat', 'snow', 'ice']))

my_list = ['apple', 'banana', 'cherry']
my_list.insert(1, 'hello')
print(my_list)