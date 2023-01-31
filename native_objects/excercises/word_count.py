import re

sonnet = """ This is a test sentence. We are going to count the number of words in a sentence """

# Unique words
uniques = {}
words = re.findall(r"\w+", sonnet)

for word in words:
    if word in uniques:
        uniques[word] += 1
    else:
        uniques[word] = 1

print(uniques)