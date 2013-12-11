#!/usr/bin/env python3

def square(n):
    m = 0;
    while n != 0:
        digit = n % 10
        n = n // 10
        m += digit ** 2
    return m

def is_happy_number(number):
    numbers = []
    while number != 1 and not number in numbers:
        numbers.append(number)
        number = square(number)
    return number == 1

def find_happy_number():
    i = 0
    count = 0
    print('first 8 happy numbers are:')
    while count < 8:
        i += 1
        if is_happy_number(i):
            count += 1
            print(i, '\t', end='')
    print('')

find_happy_number()
