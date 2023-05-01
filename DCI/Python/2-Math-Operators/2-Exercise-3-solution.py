#Task1

num1 = 5
num2 = 10

sum = 0

sum += num1
sum += num2

print("The sum is", sum)




#Task2

num1 = 2
num2 = 3
num3 = 4
num4 = 5

product = 1
product *= num1
product *= num2
product *= num3
product *= num4

print("The product is:", product)




#Task3

char1 = "H"
char2 = "e"
char3 = "l"
char4 = "l"
char5 = "o"
char6 = " "
char7 = "W"
char8 = "o"
char9 = "r"
char10 = "l"
char11 = "d"

reverse = ""
reverse += char11
reverse += char10
reverse += char9
reverse += char8
reverse += char7
reverse += char6
reverse += char5
reverse += char4
reverse += char3
reverse += char2
reverse += char1

print("The resulting string is:", reverse)



#Task4

str1 = "apple"
str2 = "banana"
str3 = "cherry"

concatenated = ""
concatenated += str1
concatenated += str2
concatenated += str3

print("The concatenated string is:", concatenated)






##### ---Math-operators Tasks--- #####

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
