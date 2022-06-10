def fibonacci(int):
	if int == 0 or int == 1:
		return 1
	return fibonacci(int-1)+fibonacci(int-2)

def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()
