import random

print('Welcome')
print("Let's name the brave adventurers")

name1 = input('Character 1: ')
name2 = input('Character 2: ')
name3 = input('Character 3: ')
name4 = input('Character 4: ')
name5 = input('Character 5: ')

# CHARACTER 1
luck = random.randint(1, 3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if luck == 1:
    print(name1 + " is a Warrior")
    strength = strength * 3
elif luck == 2:
    print(name1 + " is a Wizard")
    magic = magic * 3
else:
    print(name1 + " is a Potato")
    health = health * 3

print('Strength: ', strength)
print('Magic: ', strength)
print('Health: ', strength)

# CHARACTER 2
luck = random.randint(1, 3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if luck == 1:
    print(name2 + " is a Warrior")
    strength = strength * 3
elif luck == 2:
    print(name2 + " is a Wizard")
    magic = magic * 3
else:
    print(name2 + " is a Potato")
    health = health * 3

print('Strength: ', strength)
print('Magic: ', strength)
print('Health: ', strength)

# CHARACTER 3
luck = random.randint(1, 3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if luck == 1:
    print(name3 + " is a Warrior")
    strength = strength * 3
elif luck == 2:
    print(name3 + " is a Wizard")
    magic = magic * 3
else:
    print(name3 + " is a Potato")
    health = health * 3

print('Strength: ', strength)
print('Magic: ', strength)
print('Health: ', strength)

# CHARACTER 4
luck = random.randint(1, 3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if luck == 1:
    print(name4 + " is a Warrior")
    strength = strength * 3
elif luck == 2:
    print(name4 + " is a Wizard")
    magic = magic * 3
else:
    print(name4 + " is a Potato")
    health = health * 3

print('Strength: ', strength)
print('Magic: ', strength)
print('Health: ', strength)

# CHARACTER 5
luck = random.randint(1, 3)
strength = random.randint(5,10)
magic = random.randint(5,10)
health = random.randint(5,10)

if luck == 1:
    print(name5 + " is a Warrior")
    strength = strength * 3
elif luck == 2:
    print(name5 + " is a Wizard")
    magic = magic * 3
else:
    print(name5 + " is a Potato")
    health = health * 3

print('Strength: ', strength)
print('Magic: ', strength)
print('Health: ', strength)