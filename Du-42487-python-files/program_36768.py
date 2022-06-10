def count_letters(s):
	if len(s) == 0:
		return 0
	return count_letters(s[1:])