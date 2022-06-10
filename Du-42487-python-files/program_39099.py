def fibonacci(x):
	if x == 0:
		return 1
	elif x == 1:
		return 1
	return fibonacci(x-1) + fibonacci(x-2)

def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()