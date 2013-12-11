#!/usr/bin/env python3

def is_palindrome(string):
    return string == string[::-1]

string = input('enter a string, check whether it is a palindrome\n')
print(string, 'is' if is_palindrome(string) else 'is not', 'a palindrome')
