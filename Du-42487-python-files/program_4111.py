def fibonacci(N):
	if N == 0 or N == 1:
	   return(1)
	return(fibonacci(N-1) + fibonacci(N-2))

def main():
    print((fibonacci(0)))
    print((fibonacci(1)))
    print((fibonacci(5)))
    print((fibonacci(8)))

if __name__ == '__main__':
    main()
