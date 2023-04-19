import random

print("Welcome to the character generator!")
print("Let's name the brave adventurers:")

character_names = []

character_names.append(input("Character 1: "))
character_names.append(input("Character 2: "))
character_names.append(input("Character 3: "))
character_names.append(input("Character 4: "))
character_names.append(input("Character 5: "))

print("\n***ULTIMATE DUNGEON TEAM IS COMPLETE!***")

for i in range(5):
    character_type = random.choice(["Warrior", "Wizard", "Potato"])
    character_health = random.randint(5, 10)
    character_strength = random.randint(5, 10)
    character_magic = random.randint(5, 10)
    
    if character_type == "Warrior":
        character_strength *= 3
    elif character_type == "Wizard":
        character_magic *= 3
    else:
        character_health *= 3
    
    print(f'"{character_names[i]}" is a {character_type}!')
    print(f'\tStrength: {character_strength}')
    print(f'\tMagic: {character_magic}')
    print(f'\tHealth: {character_health}\n')

print("HAPPY ADVENTURING!")