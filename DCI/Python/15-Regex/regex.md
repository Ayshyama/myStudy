## Regex

- Regular expressions (regex) are a powerful tool for pattern matching and string manipulation in Python.
- In regex:

1. characters are used to match literal characters in a string
2. metacharacters and special sequences are used to match more complex patterns

### Regex methods

| Method       | Description                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| re.search()  | Searches the string for a match to the regex pattern and returns the first match found.                                              |
| re.findall() | Returns a list of all non-overlapping matches of the regex pattern in the string.                                                    |
| re.match()   | Returns a match object if the pattern is found at the beginning of the string. If the pattern is not found, the method returns None. |
| re.sub()     | Substitutes all occurrences of the regex pattern in the string with a replacement string.                                            |
| re.split()   | Splits the string at each occurrence of the regex pattern and returns a list of the resulting substrings.  

*Characters**: These are literal characters that match themselves.
For example, the regex **a** matches the character "a" in a string.

**Metacharacters**: These are special characters that have a special meaning in regex.
Some common metacharacters include:

| Character          | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| . (dot):           | Matches any character except newline.                           |
| ^ (caret):         | Matches the beginning of a string.                              |
| $ (dollar sign):   | Matches the end of a string.                                    |
| \* (asterisk):     | Matches zero or more occurrences of the preceding character.    |
| + (plus sign):     | Matches one or more occurrences of the preceding character.     |
| ? (question mark): | Matches zero or one occurrence of the preceding character.      |
| {m}:               | Matches exactly m occurrences of the preceding character.       |
| {m,n}:             | Matches between m and n occurrences of the preceding character. |

**Special sequences**: These are shorthand codes for commonly used patterns. Some common special sequences include:

[image.png](character_classes.png)