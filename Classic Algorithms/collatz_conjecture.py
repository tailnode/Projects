#!/usr/bin/env python3

def find_step(n):
    step = 0
    while n != 1:
        step += 1
        if n//2 * 2 == n:
            n /= 2
        else:
            n = n*3 + 1
    return step

number = int(input('enter a positive integer\n'))
print('step: ', str(find_step(number)))
