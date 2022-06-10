
def factorial(n):
	if n == 0:
		return 0
	total = 1
	for i in range(n):
		total *= i
	return factorial(n-1) * n

