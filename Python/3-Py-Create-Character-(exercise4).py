import random

print("\nWelcome to the character generator!")
print("Let's name the brave adventurers:\n")

character_names = []

character_names.append(input("Character 1: "))
character_names.append(input("Character 2: "))
character_names.append(input("Character 3: "))
character_names.append(input("Character 4: "))
character_names.append(input("Character 5: "))

print("\n***ULTIMATE DUNGEON TEAM IS COMPLETE!***\n")

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

## **OPTIONAL BONUS CHALLENGE**
## Make it so that there is a 10% chance that the stats are printed as binary, 
## 10% chance that the states are printed as hex and 80% chance they are printed as decimals

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
    
    num = random.randint(0, 9)
    if num < 1:
        print(f'\tStrength: {bin(character_strength)}')
        print(f'\tMagic: {bin(character_magic)}')
        print(f'\tHealth: {bin(character_health)}\n')
    elif num < 2:
        print(f'\tStrength: {hex(character_strength)}')
        print(f'\tMagic: {hex(character_magic)}')
        print(f'\tHealth: {hex(character_health)}\n')
    else:
        print(f'\tStrength: {character_strength}')
        print(f'\tMagic: {character_magic}')
        print(f'\tHealth: {character_health}\n')

print("HAPPY ADVENTURING!")