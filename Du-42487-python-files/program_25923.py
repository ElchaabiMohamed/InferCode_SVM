def count_letters(s):
	if len(s) == 0:
		return 0
	elif len(s) == 1:
		return 1
	else:
		return 1 + count_letters(s[1:])
