from datetime import datetime
from datetime import timedelta

def is_leap_year(year):
    dt = datetime(year, 2, 1)
    delta = timedelta(days=28)
    dt = dt + delta
    if dt.month == 2:
        return True
    return False

print(is_leap_year(2020))

# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  