a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

tmp = []
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
	if a != [] and len(a) > 2:		
		while i < len(a) / 2:
			swap(a,i,j)
			j = j - 1
			i = i + 1
		return a
	elif len(a) <= 2 and len(a) > 0:
		swap(a,i,j)
		return a
	else:
		return a
	
	

def main():
   print(reverse(a))

if __name__ == "__main__":
   main()