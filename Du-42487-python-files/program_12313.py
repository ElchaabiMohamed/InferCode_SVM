a = []

tmp = 0
def swap(a,i,j):
	if a!= []:
		tmp = a[i]
		a[i] = a[j]
		a[j] = tmp
		return a
	else:
		return a
def reverse(a):
	i = 0
	j = len(a) - 1
	if a != []:		
		while i < 2 % len(a):
			swap(a,i,j)
			j = j - 1
			i = i + 1
		return a
	else:
		return a
	
	

def main():
   print(swap(a,2,3))
   print(reverse(a))

if __name__ == "__main__":
   main()