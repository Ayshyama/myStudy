from datetime import datetime

str_date = "2019-01-01"

date = datetime.strptime(str_date, "%Y-%m-%d")

print(type(date))

str_date = "Monday, January 1, 2019"

date = datetime.strptime(str_date, "%A, %B %d, %Y")

print(date)


dt = datetime(2019, 1, 1, 12, 30, 45)

my_str = dt.strftime("%d.%m.%y %H:%M:%S")

print(my_str)

my_str2 = dt.strftime("%A, %B %d, %Y")

print(my_str2)
