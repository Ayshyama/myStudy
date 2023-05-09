# 09.05.2023
# Task - Maths with dictionary elements

dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}

## Output: 73

total = 0

for key in dict1:
    total += dict1[key] * dict2[key]

print(total)