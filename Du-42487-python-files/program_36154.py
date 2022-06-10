def count_letters(s,c=0):
	if s == "":
		return c
	s = s[1:]
	c=c+1
	return count_letters(s)