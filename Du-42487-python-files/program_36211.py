a = [4,3,1,2]

def swap(a,i,j):
 	tmp = a[j]
 	a[j] = a[i]
 	a[i] = tmp
 	return a

def reverse(a):
	a = a[::-1]
	return a


def main():
	print(swap(a,2,3))
	print(reverse(a))
	

if __name__ == "__main__":
   main()