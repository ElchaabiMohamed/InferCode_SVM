def fibonacci(num):
	if num == 0 or num == 1:
		return 1
	return fibonacci(num - 1) + fibonacci(num - 2)

def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()