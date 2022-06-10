def maximum(n):
	if len(n) == 1:
		return n[0]

	m = maximum(n[1:])
	return n[0] if n[0] > m else m


def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()