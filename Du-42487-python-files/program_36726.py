a=[]
def bsearch(a,q):
	low =0
	high= len(a)
	while low<high:
		mid = (high+low)/2
		if a[mid]<q:
			low =mid
		else:
			high = mid
	return low


bsearch(a,q)
