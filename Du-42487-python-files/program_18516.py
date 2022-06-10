def count_letters(l):
	if l == '':
		return 0
	return 1 + count_letters(l[1:])
	#cat at t ''
	#1 + 2
	#1 + 1
	#1 + 0 =1
def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
