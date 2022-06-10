def count_letters(s):
	total = 0
	if s == '':
		return total
	for t in s:
		total += 1 
	s = ''
	return count_letters(s)