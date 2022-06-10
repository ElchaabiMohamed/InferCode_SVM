import sys

def count_letters(s):
	count = 0
	if s == '':
		return count
	elif s != '':
		s = list(s)
		s.pop()
		''.join(s)
		count += 0 
		return count_letters(s)	