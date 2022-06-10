def power(n,mult):
	if mult == 0:
		return 0
	return n**mult
	power(n,mult-1)