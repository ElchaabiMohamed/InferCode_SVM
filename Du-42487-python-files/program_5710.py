from sys import argv

def fibonacci(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

def main():
	print((fibonacci(int(argv[1]))))
if __name__ == '__main__':
	main()


