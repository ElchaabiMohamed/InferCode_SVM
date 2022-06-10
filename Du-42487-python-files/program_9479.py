def count_letters(s):
	if s == "":
		return 0

	count = count_letters(s[:-1])
	return len(s) + count