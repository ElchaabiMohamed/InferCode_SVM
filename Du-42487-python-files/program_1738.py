def count_letters(s):
	count = 0
	i = 0
	while s[i] != "":
		count += 1
		i += 1
		return count_letters(s)
	return count
