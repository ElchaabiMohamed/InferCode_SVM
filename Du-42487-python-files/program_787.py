 

def count_letters(s):
	if s == "":
		return 0
	else:
		return count_letters(s[:-1]) + 1
		