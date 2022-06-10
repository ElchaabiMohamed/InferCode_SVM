def fibonacci(n):
	a = 0
	b = 1

	l = []

	while a < n:
		a += b
		a,b = b,a
		l.append(a)

	return l(len.l()-1)	
		



