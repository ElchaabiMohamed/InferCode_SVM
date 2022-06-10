def count_letters(s):
	count = 0
	for x in s:
		count += 1
		return count_letters(s)
	return count
