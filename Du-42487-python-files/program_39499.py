import sys

def count_letters(s):
	s = list(s)
	if s == []:
		return 0 
	else:
		count = 0
		for c in s:
			count += 1
		return count		
		


def main():
    len = None
    print((count_letters('cat')))
    print((count_letters('catastrophe')))
    print((count_letters('')))

if __name__ == '__main__':
    main()