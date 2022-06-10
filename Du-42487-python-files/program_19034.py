
def count_letters(s):
	total = 0
	if s == "":
		return 0
	else:
		for c in s[:-1]:
			total += 1
			s = s[c:-1]
		return count_letters(s) + 1

