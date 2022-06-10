def count_letters(string):
	if string == "":
		return 0
	else:
		return 1 + count_letters(string[1:])