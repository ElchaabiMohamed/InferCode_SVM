def count_letters(s):
	if s == "":
		return 0

	s = s.replace(s[0],"",1)

	return 1 + count_letters(s)