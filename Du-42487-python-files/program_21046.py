import sys

def count_letters(s):
	count = 0
	if s == '':
		return 0
	elif s != '':
		s = list(s)
		s.pop()
		count += 1
		count_letters(''.join(s))
	else:
		return count_letters(s)	