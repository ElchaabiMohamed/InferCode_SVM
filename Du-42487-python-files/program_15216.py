def factorial(x):
	if x==1 or x==0:
		return 1
	return x * factorial(x-1)	


def main():
    print((factorial(0)))
    print((factorial(1)))
    print((factorial(12)))

if __name__ == '__main__':
    main()
