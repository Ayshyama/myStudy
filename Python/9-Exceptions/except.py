
## TASK 1 ##


# while 1:
#     try:
#         1/int(input('Enter a number: '))
#         print('Ok')
#         break
#     except ZeroDivisionError:
#         print('Must be not 0')



## TASK 2 ##


# while 1:
#     try:
#         num1 = float(input('Enter the first number: '))
#         num2 = float(input('Enter the second number: '))
#         if num2 == 0:
#             print('Error: Division by zero')
#             continue
#         result = num1/num2
#         print(f"The result of {num1} divide by {num2} is {result}")
#         break
#     except ValueError:
#         print('Invalid input. Please enter a numeric value')


# try:
#     numbers = input('Enter a list of int separeted by commas: ')
#     numbers_list = [int(num) for num in numbers.split(',')]
#     average = sum(numbers_list) / len(numbers_list)
#     print(f'the avarage: {average}')
# except ValueError:
#     print("Invalid input. Please enter a list of integers separated by commas.")





# def func(*args, **kwargs):
#     print(type(kwargs))
#     print(kwargs.get('a', 'empty'))

# func()



from datetime import datetime, timedelta
from dateutil import tz

def add_days(d: datetime, n: int, timezone:str):
    tz_obj = tz.gettz(timezone)
    if tz_obj:
        return d.astimezone(tz_obj) + timedelta(days=n)
    raise ValueError('Incorrect timezone')

d = add_days(datetime(2024, 12, 12), 45, 'Europe/Berlin')

print(d)





