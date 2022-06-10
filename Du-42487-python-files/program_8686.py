def power(n, t):
	if t == 0:
		return 1
	t -= 1
	return n * power(n, t)

def main():
    print((power(2,3)))
    print((power(4,4)))
    print((power(2,32)))
    print((power(10,3)))
    print((power(8,0)))

if __name__ == '__main__':
    main()