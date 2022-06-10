def count_letters(s):
	b = s.index(s[-1])
	s = ''
	try:
		if s == '':
			return b
	except IndexError:
		return 0
	return count_letters(s)