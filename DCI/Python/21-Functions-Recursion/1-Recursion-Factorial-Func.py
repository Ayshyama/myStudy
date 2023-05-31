def factorial(n):
    if n == 0:               # exit condition
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
# 5! = 5 * 4 * 3 * 2 * 1 = 120
