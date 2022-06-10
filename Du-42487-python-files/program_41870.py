def sumup(n):
	if n == 0:
		return 0
	return sumup(n - 1) + n

def main():
    print((sumup(0)))
    print((sumup(1)))
    print((sumup(12)))

if __name__ == '__main__':
    main()