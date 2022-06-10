import sys
a=[1,2,3,4,5,6,7,8,9]
q=6

def bsearch(a,q):
	low=0
	high=len(a)
	while low<high:
		mid=(low+high)/2
		if a[mid]<q:
			low=mid+1
		else:
			high=mid
	return low
