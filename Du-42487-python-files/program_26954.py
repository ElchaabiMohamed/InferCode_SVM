def count_letters(s):
	try:
		b = s.index(s[-1]) + 1
	except IndexError:
		return 0
	s = ''
	if s == '':
		return b
	return count_letters(s)