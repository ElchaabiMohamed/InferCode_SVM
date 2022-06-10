def swap(a,i,j):
	tmp=a[i]
	a[i]=a[j]
	a[j]=tmp
	return a

def reverse(a):
	i=0
	j=len(a)-1
	while i<len(a)/2:
		tmp=a[i]
		a[i]=a[j]
		a[j]=tmp
		i=i+1
		j=j-1
		



