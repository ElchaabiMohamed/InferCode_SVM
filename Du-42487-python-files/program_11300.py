def count_letters(l):
	if l == "":
		return 0

	return count_letters(l[:-1]) + 1