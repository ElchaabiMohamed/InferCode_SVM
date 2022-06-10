def count_letters(s):
	if s == '':
		return 0

	count = 0
	for ch in s:
		count += 1
	return count


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
