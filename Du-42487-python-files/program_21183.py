
def count_letters(s):
	total = 0
	if s == "":
		return total
	else:
		i = 0
		for c in s[:-1]:
			total += 1
			i += 1
			s = s[i:-1]
		return count_letters(s) + 1

