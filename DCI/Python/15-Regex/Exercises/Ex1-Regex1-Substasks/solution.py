### 11.05.2023



import re

### Task 1
print('-----------### Task 1-------------')

text = "Berlin is a world city of culture, politics, media and science."
print(re.search(r'\s', text).span()[0])


### Task 2
print('-----------### Task 2-------------')


text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
print(re.search('Frankfurt', text))


### Task 3
print('-----------### Task 3-------------')

text = 'Berlin is a city of culture.'
print(re.sub(r' ', '-', text))


### Task 4
print('-----------### Task 4-------------')

test = 'Berlin is a city of culture.'
print(re.search(r'in', text))


### Task 5
print('-----------### Task 5-------------')

text = 'Berlin is a city of culture.'
print(re.search(r'\bB\w*', text).span())



### Task 6
print('-----------### Task 6-------------')

text = 'The rain in Spain.'
print(len(re.findall(r'ai', text)))


