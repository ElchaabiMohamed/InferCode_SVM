def swap(a,i,j):
	a[i],a[j] = a[j],a[i]
	return a
def reverse(lst):
	i = 0
	while i < len(lst)/2:
		swap(lst,i,len(lst)-1-i)
		i += 1
	return lst

def main():
	nums = [1,2,3,4,5,6,7,8,9]
	print((swap(nums,1,2)))
	print((reverse(nums)))

if __name__ == "__main__":
	main()