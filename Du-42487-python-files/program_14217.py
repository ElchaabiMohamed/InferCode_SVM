def count_letters(s):
	count = 0	
	if s == "":
		return count
	count += 1
	return count_letters(s[1:])
