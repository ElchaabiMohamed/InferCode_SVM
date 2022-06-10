def string_length(s):
	return 1 + string_length(s[1:]) if s else 0

def count_letters(s):
	if not s:
		return 0

	return string_length(s)


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()