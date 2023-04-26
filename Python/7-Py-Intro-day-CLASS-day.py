### Teacher Piet
### 26.04.2023
### Py Intro day 7


                        ### CLASSES DAY ###

class Car:
    def __init__(self, doors, model, year):
        self.doors = doors
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, speed_delta):
        self.speed += speed_delta

    def brake(self, speed_delta):
        if self.speed - speed_delta < 0:
            self.speed = 0
        else :
            self.speed -= speed_delta

    def info(self):
        print(f"Car with {self.doors} doors from {self.model} has a current speed of {self.speed}.")


car_obj = Car(4, "BMW", 2014)

car_obj.doors
car_obj.model
car_obj.year

print(car_obj.speed)
car_obj.accelerate(50)
print(car_obj.speed)
car_obj.brake(25)
print(car_obj.speed)
car_obj.brake(30)
print(car_obj.speed)
car_obj.info()



# Py Modules
'''

- A module is a file containing Python definitions and statements that can be used in other Python programs.
- Can define functions, classes, and variables, and can be imported into other Py programs to provide additional functionality.

'''

import math
print(math.sin(1))
print(math.sqrt)
print(math.pi)
math.inf > 1000

from math import pi
from math import sqrt, sin
import math as BLA

print(sqrt(25))
print(sin(pi))
print(BLA.e)



import time

print(time.time())

# The Datetime Module

'''
- the 'Unix epoch' is a time reference commonly used in programming
- this 'Unix' timestamp started 12 AM on Jan 1, 1970 Coordinated Universal Time (UTC)
- 'time.time()' function returns the seconds since that moment
- this moment is called the 'epoch timestamp'
'''
import datetime
print(datetime.datetime.now)

# make it human-readable
# 'time.ctime()' function returns a string description of the current time

print(time.ctime(time.time())) # c stands for current time

print(time.ctime(0))

'Thu Jan'

## The time.sleep() Function

# for i in range(5):
#     print('tick')
#     time.sleep(1)
#     print('tock')
#     time.sleep(1)

def calcProd():
    product = 1
    for i in range(1, 1_000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
delta = endTime - startTime

print(f'Took {delta} seconds')



print('----------------------')
# get the datetime object of the current time and of a given time:
import datetime
print(datetime.datetime.now())
# or 
from datetime import datetime
print(datetime.now())




print('----------------------')
# Get date entities:
dt = datetime.now()
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.weekday())

datetime.fromtimestamp(time.time())



print('----------------------')
# Converting datetime Objects into Strings
# use strftime() to make datetime objects human-readable
oct21st = datetime(2019, 10, 21, 16, 29, 0)
print(oct21st.strftime('%y-%m-%d %H:%M:%S %A'))


print('----------------------')
# Converting Strings into datetime Objects
# The strptime() function is the inverse of the strftime() method:

dt = datetime.strptime('October 21, 2019', '%B %d, %Y')
print(dt)


#
datetime.strptime('10.04.2023', '%d.%m.%Y')




