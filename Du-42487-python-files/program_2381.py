def swap(a,x,y):
	tmp=a[x]
	a[x]=a[y]
	a[y]=tmp
	return a
def reverse(a):
	return a[::-1]
def main():
	a=[4,2,3,1]
	print(swap(a,2,3))

	print(reverse(a))

if __name__ == "__main__":
   main()
