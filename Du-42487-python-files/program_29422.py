def swap(a, i, j):
	a[i], a[j] = a[j], a[i]
	return a
	
def reverse(a):
	i = 0
	while i < (len(a) // 2):
		swap(a, i, len(a) - 1 - i)
		i = i + 1
	return a

def main():
	a = [4, 3, 1, 2]
	print(swap(a, 2, 3))
	print(reverse(a))
	print(reverse([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
   
if __name__ == "__main__":
   main()