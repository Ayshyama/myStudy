# 09.05.2023
# Task - Convert keys between cases

def convert_to_snake(natural_case):
    snake_case = {}
    for key in natural_case:
        # convert key to lower
        key_lower = key.lower()

        # replace spaces to with underscore
        key_snake_case = key_lower.replace(' ', '_')

        # add key-value pairs to new dict
        snake_case[key_snake_case] = natural_case[key]

    return snake_case



natural_case_A = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}

natural_case_B = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

print(convert_to_snake(natural_case_A))
print('---------------------------')
print(convert_to_snake(natural_case_B))
