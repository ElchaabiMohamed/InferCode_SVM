def factorial(x):
	if x==1:
		return 1
	if x==0:
		return 0	
	return x * factorial(x-1)	


def main():
    print((factorial(0)))
    print((factorial(1)))
    print((factorial(12)))

if __name__ == '__main__':
    main()
