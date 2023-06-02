def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n-1)


print(countdown(5))


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


print(power(2, 3))

