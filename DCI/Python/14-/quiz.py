zen_python = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# Clean up the string by removing punctuation and converting to lowercase
cleaned_text = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in zen_python).lower()


# Split the cleaned text into individual words
words = cleaned_text.split()
print(words)
# Create a dictionary to store the word occurrences
word_occurrences = {}

# Iterate over each word and record its index
for index, word in enumerate(words):
    if word not in word_occurrences:
        word_occurrences[word] = []
    word_occurrences[word].append(index)

print('-----------------------------------------')
# Print the word occurrences
for word, occurrences in word_occurrences.items():
    print(f"{word}: {occurrences}")