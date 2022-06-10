def maximum(l):
	if len(l) == 1:
		return l[0]
	elif len(l) == 0:
		return 0

	m = maximum(l[1:])
	if m < l[0]:
		return l[0]
	return m

def main():
    max = None
    print((maximum([6,5,1,3,4])))
    print((maximum([6,5,11,3,4])))
    print((maximum([6,15,11,13,14])))
    print((maximum([6,15,11,13,4])))

if __name__ == '__main__':
    main()