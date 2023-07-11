def calculate_fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci_number(n - 1) + calculate_fibonacci_number(n - 2)


number = 20
result = calculate_fibonacci_number(number)
print(f"The   Fibonacci    numberr   at   inndex    {number}   is: {result}  . ")

fruits = ["apple", "banana", "orange"]
if "kiwi" not in fruits:
    print("Kiwi is not in the list of fruits!")
