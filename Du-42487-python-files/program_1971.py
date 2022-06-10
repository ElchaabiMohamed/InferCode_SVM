import sys

count = 0

def count_letters(s):
	if s == '':
		return 0
	elif s != '':
		s = list(s)
		s.pop()
		count += 1
		count_letters(s.join())
	else:
		return count_letters(s)	