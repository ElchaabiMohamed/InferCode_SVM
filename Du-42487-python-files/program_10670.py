def count_letters(n):
	if n == '':
		return 0
	else:
		return 1+ count_letters(n[1:])
