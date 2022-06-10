def swap(a,x,y):
	tmp=a[x]
	a[x]=a[y]
	a[y]=tmp
	return a
def reverse(a):
	i=0
	j=len(a)-1
	while i<(len(a)/2):
		swap(a,i,j)
		i+=1
		j-=1
	return a
def main():
	a=["apple","orange","pear"]

	print(swap(a,2,1))
	print(reverse(a))

if __name__ == "__main__":
   main()
