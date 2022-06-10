import sys

def count(s):
	length = 0
	for i in s:
		length += 1
	return length


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()
