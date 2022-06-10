def count_letters(s="", i=0):
	print((s, i))
	
	if s == "":
		return i

	i += 1
	return count_letters(s.replace[s[0], "", 1], i)