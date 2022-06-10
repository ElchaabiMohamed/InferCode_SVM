def swap(a,i,j):
	tmp = a[j]
	a[j] = a[i]
	a[i] = tmp
	return
def reverse(a):
	return swap(a,2,3)
def main():
	a = [4,3,1,2]
	print(swap(a,i,j))
	return
if __name__ == "__main__":
	main()
