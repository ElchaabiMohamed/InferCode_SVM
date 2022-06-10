def count_letters(s):
	count = 0
	if s == "":
		return count
	return count + 1 , count_letters(s)