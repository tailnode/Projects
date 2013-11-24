#!/usr/bin/python3


def generate_fibonacci(n):
	fibonacci = [1]
	for i in range(n - 1):
		fibonacci.append(sum(fibonacci[-2:]))
	return fibonacci if n > 0 else []

if __name__ == '__main__':
	for i in range(10):
		print(generate_fibonacci(i))
		print('\n')
