

def count_letters(a):
	if a == '':
		return 0
	a=a[:-1]
	n=1
	return n + count_letters(a)

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()