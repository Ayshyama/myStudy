my_str = """
day: 3, month: 1, year: 2012↵
day:1, month:12, year:2012↵
day:  3, month: 11, year: 2012↵
day:  10, month: 2, year: 2022↵
day:  1, month: 10, year: 20123453
"""
import re

my_matches = re.findall(r'day:\s*\d,\smonth:\s*\d,\syear:\s*\d{4}', my_str)
my_matches = re.findall(r'day:\s*(\d+),\smonth:\s*(\d+),\syear:\s*(\d{2,4})', my_str)
# print(my_matches)

for day, month, year in my_matches:
    print(f'day: {day}, month: {month}, year: {year}')


from datetime import datetime

my_dates = []
for day, month, year in my_matches:
    dt = datetime(int(year), int(month), int(day))
    my_dates.append(dt)

print(my_dates)
