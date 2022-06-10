def factorial(n):
	if n < 1:
		return 1
	if n == 1:
		return 1
	return n * factorial(n-1)

from sys import argv
if __name__ == "__main__":
	print((factorial(int(argv[1]))))