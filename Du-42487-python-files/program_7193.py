total = 0
def count_letters(s):
	if s == '':
		return total
	total += 1
	s = s[:-1]
	return count_letters(s)