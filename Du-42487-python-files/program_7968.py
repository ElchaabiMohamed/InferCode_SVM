count = 0

def count_letters(s):	
	if s == "":
		return count
	else:
		count += 1
	return count_letters(s[1:])
