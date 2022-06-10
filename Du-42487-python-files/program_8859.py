def fibonacci(n):
	if n == 0:
		return 1
	a = 0
	b = 1

	l = []
	c = 0
	while c != n:
		a += b
		a,b = b,a
		l.append(a)
		c += 1
	
	return l[-1]


		



