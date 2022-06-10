def swap(a, i, j):
	tmp = a[i]
	a[i] = a[j]
	a[j] = tmp

def reverse(a):
	for i in range(len(a) / 2):
		swap(a, i, len(a)-i-1)

def selection_sort(a):
	for i in range(len(a)):
		smallest = i
		for j in range(i, len(a)):
			if a[j] < a[smallest]:
				smallest = j
		swap(a, i, smallest)
	return a

def main():
	a = [3, 6, 423, 45, 87, 2, 4]

	selection_sort(a)
	print(a)

if __name__ == '__main__':
	main()

