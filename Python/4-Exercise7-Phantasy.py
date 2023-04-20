import random

def generate_stats_value():
    return random.randint(3, 15)

def generate_character(name):
    character_class = random.choice(['Barbarian', 'Cleric', 'Druid'])
    health = generate_stats_value()
    strength = generate_stats_value()
    magic = generate_stats_value()
    initiative = generate_stats_value()

    if character_class == 'Barbarian':
        health *= 3
        strength *= 3
    elif character_class == 'Cleric':
        magic *= 3
        initiative *= 3
    else:
        health *= 2
        magic *= 2
        initiative *= 2

    return f'{name} is a {character_class}!\nStrength: {strength}\nMagic: {magic}\nHealth: {health}\nInitiative: {initiative}\n'

print("\nWelcome to the character generator!\n")
num_characters = int(input("How many characters are we creating: "))
print("\nLet's name the brave adventurers:\n")
      
names = []
for i in range(num_characters):
    name = input(f"Character {i+1}: ")
    names.append(name)

print("\n******YOUR CHARACTERS ARE COMPLETE******")
for name in names:
    print(generate_character(name))

print("Happy adventuring!")