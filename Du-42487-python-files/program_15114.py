a = [4,3,1,2]

tmp = 0
def swap(a,i,j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp
	return a
def reverse(a):
	i = 0
	j = len(a) - 1
	while i < 2 % len(a):
		swap(a,i,j)
		j = j - 1
		i = i + 1
	return a
	
	

def main():
   print(swap(a,2,3))
   print(reverse(a))

if __name__ == "__main__":
   main()