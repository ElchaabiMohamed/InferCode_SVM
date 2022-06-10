def count_letters(l):
	return 1 + count_letters(l[1:]) if l else 0
