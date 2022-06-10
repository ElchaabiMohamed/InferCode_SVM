def count_letters(word):
	if word == "":
		return 0
	else:
		return 1 + count_letters(word[1:])
