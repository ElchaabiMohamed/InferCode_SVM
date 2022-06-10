def count_letters(s):
	if len(s) == 0:
		return 0
	s = list(s)
	s.remove(s[0])
	return 1 + count_letters(s)

