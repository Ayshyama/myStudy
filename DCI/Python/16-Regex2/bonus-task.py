import re

def make_happy(st: str):
    return re.sub(r'([:;8xX])\(', r'\1)', st)

print(make_happy("My current mood: :("))

print(make_happy("My current mood: :("))

print(make_happy("My current mood: :("))

