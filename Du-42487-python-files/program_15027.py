def count_letters(s):
	if len(s) == 0:
		return 0
	if len(s) == 1:
		return 1
	return count_letters(s[1:]) + 1