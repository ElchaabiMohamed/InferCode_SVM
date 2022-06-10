
def count_letters(s):
	total = 0
	if not s:
		return total
	else:
		for c in s[:-1]:
			total += 1
	return count_letters(s) + 1