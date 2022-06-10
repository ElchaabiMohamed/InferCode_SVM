def power(num, ter):
	
	if ter == 0:
		return 1

	ter = ter - 1

	return num * power(num, ter)