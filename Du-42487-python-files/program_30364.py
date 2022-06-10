
def count_letters(s):
	total = 0
	if s == "":
		return total
	else:
		i = 0
		for c in s:
			if c.isalpha():
				t = s[:i]
				t +=  "1"
				t += s[i:]
				s = t
			i += 1
		if not s.isupper():
			total = 0
			for c in s:
				total += int(c)
			return total
		else:
			return count_letters(s)


