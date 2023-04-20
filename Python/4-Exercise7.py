import random

def generate_stats():
    return random.randint(3, 15)

def generate_character(name):
    character_class = random.choice(['Barbarian', 'Cleric', 'Druid'])
    health = generate_stats()
    strength = generate_stats()
    magic = generate_stats()
    initiative = generate_stats()

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

print("Welcome to the character generator!")
num_characters = int(input("How many characters are we creating: "))

names = []
for i in range(num_characters):
    name = input(f"Character {i+1}: ")
    names.append(name)

print("\n***YOUR CHARACTERS ARE COMPLETE***")
for name in names:
    print(generate_character(name))

print("Happy adventuring!")