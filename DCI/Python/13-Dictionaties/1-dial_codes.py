dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {code[1]: code[0] for code in dial_codes}
print(country_dial)

my_country_code = {country.upper(): code for country, code in country_dial.items() if code < 70}
print(my_country_code)

print(list(zip([1, 2], 'ABC')))





# list(enumerate('ABC'))

# list(enumerate('ABC', start=1))

# my_fruits = ['apple', 'banana', 'melon']

# for integer, value in enumerate(my_fruits, start=1):
#     print(f"{integer}. {value}")