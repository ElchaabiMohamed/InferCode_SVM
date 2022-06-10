count = 0

def count_letters(s):	
	count = 0
	if s == "":
		return count
	return 1 + count_letters(s[1:])
