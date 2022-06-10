def reverse_list(a, i=1, newa=[]):
	if i <= len(a):
		newa.append(a[-i])
		i = i + 1
		return reverse_list(a, i, newa)
	else:
		return newa
		newa = []