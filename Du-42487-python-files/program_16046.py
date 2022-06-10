
def count_letters(s):
	total = 0
	if s == "":
		return total
	else:
		i = 0
		for c in s:
			if c.isalpha():
				s[i] = 1
				t = s[:i]
				t += s[i]
				t += s[i:]
				s = t
		if not s.isupper():
			total = 0
			for c in s:
				total += c
			return total
		else:
			return count_letters(s)


