import time

s=time.time()
t=time.time()
print(s==t)

print('------------------')

import datetime
dr_1 = datetime.datetime.today()
dr_2 = datetime.datetime.now()

print(dr_1)
print(dr_2)

print('------------------')
import datetime
given_date = datetime.datetime(2020, 7, 26)
print(given_date.strftime('%A'))
print('------------------')


a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')