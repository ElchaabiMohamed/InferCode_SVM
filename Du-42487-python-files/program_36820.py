import sys

def count_letters(s):
	count = 0
	if s == '':
		return count
	elif s != '':
		s = list(s)
		s.pop()
		''.join(s)
		count += 1
		return count_letters(s)	


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()