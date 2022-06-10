def fibonacci(n):
	try:
		a = 0
		b = 1

		l = []
		c = 0
		while c != n:
			a += b
			a,b = b,a
			l.append(a)
			c += 1

		return l[int(len(l)-1)]
	except:
		return 1

a = fibonacci(0)
print(a)


		



