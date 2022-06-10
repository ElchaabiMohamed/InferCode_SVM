a = [2,3,6,6,7,8]

def bsearch(a,q):

	low = 0
	high = len(a)
	
	while low < high:
		mid = (low + high) / 2
		if a[mid] < q:
			low = mid + 1
		
		else:
			high = mid

	return low

def main():
	print(bsearch(a,4))

if __name__ == "__main__":
   main()