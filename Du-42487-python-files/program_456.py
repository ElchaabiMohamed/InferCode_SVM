
def count_letters(s):
	total = 0
	for c in s[:-1]:
		total += 1
	return count_letters(s[:-1]) + 1