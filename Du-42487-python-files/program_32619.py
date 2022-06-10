j=0
def sumup(n):
	#j+=n
	if n==0:
		return n
	return n+ sumup(n-1)
