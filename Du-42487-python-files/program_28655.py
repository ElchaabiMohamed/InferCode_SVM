def count_letters(s):

	if s == "":
		return 0
	else:
		i = 1
		f = s[i:]
	return i + count_letters(f)

