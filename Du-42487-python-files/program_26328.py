def fibonacci(i, n=1):
	#print (i)
	if i==1 or i==0:
		return 1
	return fibonacci(i-1) + fibonacci(i-2)
