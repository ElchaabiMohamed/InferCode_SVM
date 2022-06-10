def count_letters(s):
	try:
		if s == '':
			return b
	except IndexError:
		return 0
	b = s.index(s[-1])
	s = ''
	return count_letters(s)