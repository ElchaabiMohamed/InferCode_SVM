def power(base, power2):
	if base == 0:
		return "invalid"
	if power2 == 0:
		return 1
	elif power2 == 1:
		return base
	else:
		return base * power(base, (power2 - 1))

def main():
    print((power(2,3)))
    print((power(4,4)))
    print((power(2,32)))
    print((power(10,3)))
    print((power(8,0)))

if __name__ == '__main__':
    main()