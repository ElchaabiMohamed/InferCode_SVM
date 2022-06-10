def count_letters(s):
	if s == "":
		return 0

	s = s.replace(s[0],"",1)

	return 1 + count_letters(s)


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
