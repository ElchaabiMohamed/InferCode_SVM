def count_letters(s):
	if theString == "": 
		return 0
	return 1 + count_letters(s[1:])