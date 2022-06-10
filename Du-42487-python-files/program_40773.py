
def factorial(n):
	if n == 0:
		return 1
	total = 1
	for i in range(0, n):
		total *= i
	return factorial(n-1) * n

