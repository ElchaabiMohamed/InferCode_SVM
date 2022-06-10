# A recursive function is one that calls itself

def sumup(n):
	if n == 1:
		return 1
	
	sum_to_n_1 = sumup(n-1)
	return n + sum_to_n_1

x = sumup(n)
print(x)