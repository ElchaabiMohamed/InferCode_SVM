def count_letters(string_):
	counter = 0
	for i in string:
		counter += 1
	return counter


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()