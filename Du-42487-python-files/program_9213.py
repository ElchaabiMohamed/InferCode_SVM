def count_letters(word):
	i = 0
	try:
		i = i + 1
		return count_letters(word[1:])
	except:
		return i
