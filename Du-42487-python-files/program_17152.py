def fibonacci(n):

	if n == 0 or n==1 or n==2:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print((fibonacci(0)))
print((fibonacci(1)))
print((fibonacci(2)))
print((fibonacci(3)))
print((fibonacci(4)))
print((fibonacci(5)))
print((fibonacci(6)))

