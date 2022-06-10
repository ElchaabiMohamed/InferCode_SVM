def count_letters(s):
	count = 0
	if s == "":
		return count
	count + 1
	s = s - s[0]
	return count_letters(s)