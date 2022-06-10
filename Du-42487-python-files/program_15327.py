def count_letters(s):
	total = 0
	if s == "":
		return 0

	return total + count_letters(s[0:])

