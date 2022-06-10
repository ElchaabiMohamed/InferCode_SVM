def swap(a, i, j):
	tmp=a[j]
	a[j]=a[i]
	a[i]=tmp
i = 0
def reverse(a):
	tmp = a[len(a)-i-1]
	a[len(a)-i-1]=a[i]
	a[i]=tmp
	i = i + 1

def main():
	print(swap(a))
	print(reverse(a))

if __name__=="__main__":
	main()