#!/usr/bin/env python3

import random

random.seed()

def generate_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randrange(2*n))
    return numbers

def bubble_sort(numbers):
    for j in range(1,len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

def merge(l1, l2):
    sum_list = []
    while l1 and l2:
        if l1[0] > l2[0]:
            sum_list.append(l2.pop(0))
        else:
            sum_list.append(l1.pop(0))
    return sum_list + l1 + l2

def merge_sort(numbers):
    if len(numbers) <= 1: return numbers
    mid = len(numbers)//2
    return merge(merge_sort(numbers[:mid]), merge_sort(numbers[mid:]))
    
numbers = generate_numbers(100)
print(numbers)
#bubble_sort(numbers)
print(merge_sort(numbers))
