def power(m,n):
	if m==1:
		return m

	return power(n**m,m-1)