def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp



def reverse(a):
	i = 0
	while i < len(a)/2:
		swap(a,a[i],a[len(a)-i-1])
		i=i+1

		




