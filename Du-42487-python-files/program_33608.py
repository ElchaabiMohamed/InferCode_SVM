import sys

def factorial(n):
	if n == 0:
		return 0
	return n * factorila(n-1)	


def main():
    print((factorial(0)))
    print((factorial(1)))
    print((factorial(12)))

if __name__ == '__main__':
    main()	