def swap(a,x,y):
	tmp=a[x]
	a[x]=a[y]
	a[y]=tmp
	return a
def reverse(a):
	a=a[::-1]
	return a
def main():
	a=["apple","orange","pear"]
	print(swap(a,2,1))

	print(reverse(a))

if __name__ == "__main__":
   main()
