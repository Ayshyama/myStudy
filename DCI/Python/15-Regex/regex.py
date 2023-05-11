import re

my_search = re.search('a', 'Ha')
print(my_search)

# dot (.)

match_obj = re.match('a.', 'abc')
# The regex 'a.' matches the first 'a' character and any character after it
# so the match object contains 'ab'.
print('a. --> abc', match_obj)

match_obj = re.match('a.', 'aaa')
# The regex 'a.' requires at least two characters in the string to match
# so none is returned
print('a. --> a', match_obj)

#^ caret
match_obj = re.match('^a', 'abc')
# The regex '^a' matches the first character of the string 'abc'
print('^a --> abc', match_obj)

match_obj = re.match('^b', 'abc')
# The regex '^b' does not match the beginning of the string 'abc'
print('^b --> abc', match_obj)

#$ Dollar Sign
match_obj = re.search('c$', 'abc')  
# The regex 'c$' matches the last character of the string 'abc'
print('c$---> abc',match_obj)

match_obj = re.search('a$', 'abc') 
 # The regex 'a$' does not match the end of the string 'abc'
print('a$---> abc',match_obj)

# Asterisk (*)
match_obj = re.match('a*', 'aaa')
#The regex 'a*' matches zero or more 'a' characters at the beginning of the string 'aaa'
print('a*---> aaa',match_obj)

match_obj = re.match('a*', 'bbb')
# The regex 'a*' matches zero 'a' characters in the string 'bbb'
print('a*---> bbb',match_obj)

# Plus Sign (+)
match_obj = re.match('a+', 'aaaaabaaa')
# match_obj = re.match('a{1,}', 'aaa')
print('a+--> aaa',match_obj)

match_obj = re.match('a+', 'bbb')
print('a+--> bbb',match_obj)

# {m}
match_obj = re.match('a{2}', 'aaa')
print(f'a{2}--> aaa',match_obj)

# {m , n}
# match_obj = re.match('a{2,4}', 'abaaaa')
match_obj = re.search('a{2,4}', 'aabaaaa')
print(f'a{2,3}--> aaaaa',match_obj)


# Character classes

# \d
match_obj = re.match('\d', '123')
print('\d--> 123',match_obj)

match_obj = re.match('\d', 'abc')
print('\d--> abc',match_obj)

match_obj = re.match('\s', ' hello')
print('\s--> hello',match_obj)

match_obj = re.match('\w', 'hello')
print('\w--> hello',match_obj)

match_obj = re.match('[abc]', 'alpha')
print('[abc]-> alpha',match_obj)

match_obj = re.match('[abc]', 'lalpha')
print('[abc]-> lalpha',match_obj)


match_obj = re.match('[a-zP]+', 'alPha1')
print('[a-zP]+-> alPha1',match_obj)

match_obj = re.match('[a-zA-Z]+', 'alPha1')
print('[a-zA-Z]+-> alPha1',match_obj)

match_obj = re.match('[^P]+', 'alPha1')
print('[^P]+-> alPha1',match_obj)

#findall

pattern = '[xyz]'
text1 = 'hello xyz world'
matches = re.findall(pattern, text1)
print('[xyz] --> hello xyz world: ', matches)

pattern='xyz'
matches = re.findall(pattern, text1)
matches = re.findall('xyz', 'hello xyz world')
print('xyz --> hello xyz world: ', matches)

pattern='l+'
matches = re.findall(pattern, text1)
print('l+ --> hello xyz world: ', matches)

pattern='l?'
matches = re.findall(pattern, text1)
print('l? --> hello xyz world: ', matches)


input_str = "John Smith, 25 years old"
pattern = "([^0-9]+)\s([^0-9]+)"
output_str = re.findall(pattern, input_str)
print('(\w+\s(\w+)) --> : John Smith, 25 years old', output_str)






