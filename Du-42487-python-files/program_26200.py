def count_letters(a):
	if a =='':
		return 0
	return count_letters(a[1:]) + 1