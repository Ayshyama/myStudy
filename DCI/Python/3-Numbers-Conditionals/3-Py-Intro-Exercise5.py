
### Task 1

numbers = []
numbers.append(int(input("\nEnter Number 1: ")))
numbers.append(int(input("Enter Number 2: ")))
numbers.append(int(input("Enter Number 3: ")))
print('\nSum of the numbers: {}\n'.format(sum(numbers)))


### Task 2

number1 = input('Please enter first number: ')
number2 = input('Please enter second number: ')

number1_int = int(number1)
number2_int = int(number2)


if number1_int > 10000 and number2_int > 10000:
    print('Numbers are beeeeg!')
    if number1 > number2:
        print('First number is greater!')
    elif number2 > number1:
        print('Second number is greater!')
    else:
        print('Numbers are equal!')

### Task 3

number1 = int(input('Enter number 1: '))
number2 = int(input('Enter number 2: '))
number3 = int(input('Enter number 3: '))
number4 = int(input('Enter number 4: '))
number5 = int(input('Enter number 5: '))

max_number = max(number1, number2, number3, number4, number5)
print("Maximum of the numbers: ", max_number)

### Task 4

month = input('Input the name of Month: ').lower()

if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
    days = 31
elif month in ["april", "june", "september", "november"]:
    days = 30
elif month == "february":
    days = 28
else:
    print("Don't know this month :(")

print(f'Number of days: {days} days')

### Task 5

number = int(input('Enter a number: '))

if number % 2 == 0 and number % 3 == 0:
    print(f'{number} is even and divisible by 3')

elif number % 2 != 0 and number % 3 == 0:
    print(f'{number} is not even but it is divisible by 3')

elif number % 2 == 0 and number % 3 != 0:
    print(f'{number} is even but it is not divisible by 3')

else:
    print(f'{number} is not even and not divisible by 3')


