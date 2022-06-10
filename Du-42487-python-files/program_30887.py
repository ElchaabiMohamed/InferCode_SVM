def count_letters(l):
	return 1 + count_letters(s[1:]) if l else 0
