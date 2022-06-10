def swap(a, i, j):
	tmp=a[j]
	a[j]=a[i]
	a[i]=tmp
def reverse(a):
	tmp = a[len(a)-1]
	a[len(a)-1]=a[i]
	a[i]=tmp



def main():
	print(swap(a))
	print(reverse(a))

if __name__=="__main__":
	main()