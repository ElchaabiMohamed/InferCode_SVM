def count_letters(s):
	if len(s) == 0:
		return 0
	return count_letters(len(s)-1)