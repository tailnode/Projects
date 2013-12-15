#!/usr/bin/env python3

string = input('enter a string\n')

words = string.split()
word_dict = {}

for word in words:
    try:
        word_dict[word] += 1
    except:
        word_dict[word] = 1

print('word'.ljust(10) + 'counts')
for k, v in word_dict.items():
    print(k.ljust(10) + str(v))

