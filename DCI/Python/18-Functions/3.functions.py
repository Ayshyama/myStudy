## 1. referring to a function by a variable name,

def greet():
    a = 1
    b = 2
    return 'hello', a+b

# assigning the function greet to the new variable hello
# print(greet) 
# print(greet()) #Hello
hello1 = greet   # Type: function
hello2 = greet() # Type:  tuple
# print(type(hello1))
# print(type(hello2))
# hello() 

#### pass functions as input arguments to other functions ####

def  add_numbers(a,b):
    return a + b

def mult_numbers(a,b):
    return a * b

def math_operation(func, x, y):
    result = func(x, y)
    return result

result_add = math_operation(add_numbers, 2, 3)
result_mult = math_operation(mult_numbers, 2, 3)
print(result_add)
print(result_mult)


#### return functions as output from a function. ######
def  add_numbers(a,b):
    return a + b

def mult_numbers(a,b):
    return a * b

def math_operation(operation):
    if operation == 'add':
        return add_numbers
    elif operation == 'mult':
        return mult_numbers
    return None

# print(add_numbers)  # function object
# print(add_numbers(1,2)) # prints integers

result_add_func = math_operation('add')
# print(type(result_add_func)) # Type? function
# print(result_add_func(1,2))

result_add = math_operation('add')(1, 2)
# print(result_add)

##### Closures ######

def make_averager():
    series = [] ### free variable

    def averager(new_value):
        series.append(new_value)
        print(series)
        total = sum(series)
        return total/len(series)
    
    return averager

#print(make_averager()(10))

# avg = make_averager() # what type is avg: Function
# print(avg)
# print(avg(10))
# print(avg(1))

def outer_function(my_parameter1):

    def print_parameter1(value1):
        # print(my_parameter1)
        # print(value1)

        def most_inner(value2):
            print(my_parameter1) # free variable
            print(value1)  # free variable
            print(value2) # local variable

        return most_inner

    return print_parameter1

inner_func = outer_function('BLA') # Function
inner_func('Hello world')

outer_function('BLA')('')('again')



def outer_function(my_parameter1):

    def print_parameter1(value1):
        print(my_parameter1)
        print(value1)
        return value1

    return print_parameter1 #### returns a function


print(type(outer_function('BLA'))) ### function
print(type(outer_function('BLA')(100))) ### integer

