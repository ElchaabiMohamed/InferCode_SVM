
def fibonacci(a):
	if a == 0 or a == 1:
		return 1
	return fibonacci(a-1) + fibonacci(a-2)
def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()