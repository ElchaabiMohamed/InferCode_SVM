def count_letters(s):
	if s == "":
		return 0

	length = count_letters(s[:-1])
	count +=1
	if length == 0:
		return count