def count_letters(s):
	l=0
	for e in s:
		l+=1
	return l

def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
