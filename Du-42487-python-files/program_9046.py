total = 0
def count_letters(s):
	if s == '':
		return total
	total += 1
	print(total)
	s = s[:-1]
	print(s)
	return count_letters(s)