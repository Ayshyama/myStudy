# PEP 8
def calculate_sum(a, b):
    result = a + b
    return result


# Black
def calculate_sum(a, b):
    result = a + b
    return result


# PEP 8
def long_function_name(parameter1, parameter2, parameter3, parameter4):
    result = parameter1 + parameter2 + parameter3 + parameter4
    return result


# Black
def long_function_name(
        parameter1, parameter2, parameter3, parameter4,
):
    result = parameter1 + parameter2 + parameter3 + parameter4
    return result


# PEP 8
def function1():
    statement1 = "Hello"
    statement2 = "World"

    return statement1 + " " + statement2


def function2():
    statement = "This is another function"

    return statement


# Black
def function1():
    statement1 = "Hello"
    statement2 = "World"

    return statement1 + " " + statement2


def function2():
    statement = "This is another function"

    return statement
