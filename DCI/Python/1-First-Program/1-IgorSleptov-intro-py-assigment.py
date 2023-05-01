### Task 1 - printing single object

print(123)

print(43.23)

print(4 - 1j)

print("How are you?")

print(True)


# ### Task 2 - printing type of given value

print(123, 'is type of', type(123), sep=" ")

print(43.23, 'is type of', type(43.23), sep=" ")

print(4 - 1j, 'is type of', type(4 - 1j), sep=" ")

print('How are you?', 'is type of', type("qwe"), sep=" ")

print(True, 'is type of', type(False), sep=" ")


### Task 3 - checking type of value

# integer -True
number = 123
print(isinstance(number, int))  

# float - False
number = 43.23
print(isinstance(number, int))  

# complex - True
number = 4 - 1j
print(isinstance(number, complex))

# string - True
string = "Hello, world!"
print(isinstance(string, str))  

# boolean - False
boolean = 'True'
print(isinstance(boolean, bool)) 


### Task 4 - checking type of value (version 2)

# integer -True
number = 123
print('Is', number, 'an instance of int?:', isinstance(number, int))  

# float - False
number = 43.23
print('Is', number, 'an instance of bool?:', isinstance(number, int))  

# complex - True
number = 4 - 1j
print("Is", number, "an instance of complex?:", isinstance(number, complex))

# boolean - False
boolean = True
print("Is", boolean, "an instance of bool?:", isinstance(boolean, bool))

# string - True
string = 123
print("Is", string, "an instance of str?:", isinstance(string, str))  


### Task 5 - using comments in code

# This program calculates the average of two numbers and prints it to the console

# Block comment explaining the purpose of the program

# Get the first number from the user
number1 = float(input("Enter the first number: "))  # Inline comment explaining the purpose of this line

# Get the second number from the user
number2 = float(input("Enter the second number: "))  # Another inline comment

# Calculate the average of the two numbers
average = (number1 + number2) / 2

# Print the average to the console
print("The average of", number1, "and", number2, "is:", average)  # Another inline comment

"""
This is a multiline comment.
Here, we are using triple quotes to comment on the structure of the output statement.
The output statement uses string concatenation to join multiple values and a colon to separate the label and the value.
"""



