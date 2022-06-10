def fibonacci(n):
	a,b = 1,1
	for i in range(n):
		a,b = b,a+b
	return a


def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()
