def count_letters(s):
	count = 0
	if s == "":
		return 0

	length = count_letters(s[:-1])
	count += 1
	if length == 0:
		return count