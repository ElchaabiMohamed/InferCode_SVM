def fibonacci(n):
	a = 0
	b = 1

	while a < n:
		a += b
		a,b = b,a
		print(a)



