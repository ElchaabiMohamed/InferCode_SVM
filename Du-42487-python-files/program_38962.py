a = []

def swap(a,i,j):
	tmp = a[j]
	a[j]=a[i]
	a[i]= tmp
	return a
def reverse(a):
	i = 0 
	t = []
	while i < len(a):
		t = t + a[len(a)-i - 1]
		i = i + 1

	
	return t 
	