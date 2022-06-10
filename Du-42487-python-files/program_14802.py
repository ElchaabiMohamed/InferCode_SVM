def selectionsort(A):
	i = 0
	while i < len(A):
		p = i
		j = i + 1
		while j < len(A):
			if A[j] < A[p]:
				p = j
			j = j + 1

		tmp = A[p]
		A[p] = A[i]
		A[i] = tmp

		i = i + 1


import random

def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    selectionsort(A)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
