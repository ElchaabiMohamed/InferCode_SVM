def count_letters(s):
	total = 0
	if s == '':
		return total
	total += 1
	s = s[:-1]
	print(s)
	return count_letters(s)