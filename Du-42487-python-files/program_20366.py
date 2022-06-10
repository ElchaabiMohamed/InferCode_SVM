def power(m,n):
	if  m == 1:
		return 1
	if n == 1 :
		return m
	if n == 0 :
		return 1
	return m * (m  + power(m,n - 1))
