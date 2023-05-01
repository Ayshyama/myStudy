## Tasks

"""

### Task 1 - basic math operations

# Operation: addition (+)
######## Integers
a = 5
b = 10
print(a + b)

c = -25
d = 10
print(c + d)

######## Floats
a = 25.5
b = 10.25
print(round(a+b, 1))
print(a + b)

c = -25.775
d = 10.5
print(round(c + d, 1))
print(round(c + d, 2))
print(round(c + d, 3))
print(round(c + d, 4))
print(round(c + d, 5))
print(c + d)

######## Complex numbers
a = 2 + 3j
b = 1 + 2j
print(a + b)

c = -3 - 2j
d = 5 + 1j
print(c + d)

######## Booleans
a = True
b = False
print(a + b)

c = True
d = True
print(c + d) 

# Operation: Subtraction (-)
a = 5
b = 10
print(a - b)

c = -8
d = 12 
print(c - d)

# Operation: Multiplication (*)
print(a * b)
print(2.5 * 1.25)
print(round(5.5 * 1.133, 2))
print((2 + 3j) * (1 + 2j))
print(True * False)

####### ZeroDivisionError:
a = 5
b = 0
# print(a / b)

"""



### Task 2 - basic math functions

# abs() - returns the absolute value of a number
print(abs(-23)) # 23
print(abs(3.1415)) # 3.1415
abs(4 - 3j) # = sqrt(4^2 + (-3)^2)
            # = sqrt(16 + 9)
            # = sqrt(25)
            # = 5

# pow() - returns the value of x to the power of y
print(pow(2, 3)) # 8
print(pow(2.5, 2))  # 6.25

# max() - returns the largest of the given arguments
print(max(1, 2, 3, 4, 5))  # 5
print(max(-2, -5, -1))  # -1
print(max(True, False))
# min() - returns the smallest of the given arguments
print(min(1, 2, 3, 4, 4, 4 ,5 ,10))
print(min(-2, -5, -1))  # -5

# divmod() - returns the quotient and the remainder when dividing two numbers
print(divmod(9, 4))  # (2, 1)
print(divmod(10.5, 2.5))  # (4.0, 0.5)

# complex() - returns a complex number with the specified real and imaginary parts
print(complex(2, 3))  # (2+3j)
print(complex(-2.5, 4.1))  # (-2.5+4.1j)

# bool() - returns a boolean value, True or False
print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True
print(bool(3.14))  # True
print(bool(""))  # False
print(bool("hello"))  # True