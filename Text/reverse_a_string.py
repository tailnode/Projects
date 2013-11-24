#!/usr/bin/python3

def reverse_string1(string):
    output = list(original)
    output.reverse()
    return ''.join(output)

#a better way
def reverse_string(string):
    return string[::-1]

def test():
    original = input('Enter a string and the program will reverse it and print it out.\n')
    print(reverse_string(original))

test()
