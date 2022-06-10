import random

def quicksort(l, p, r):
	if r <= p:
		return l
	q = partition(l, p, r)
	quicksort(l, p, (q - 1))
	quicksort(l, (q + 1), r)

def partition(l, p, r):
	q = j = p
	while j < r:
		if l[j] <= l[r]:
			l[q], l[j] = l[j], l[q]
			q +=1
		j+=1
	l[q], l[r] = l[r], l[q]
	return q



def main():
    A = random.sample(list(range(-99, 100)), 10)

    print(('Unsorted: {}'.format(A)))
    quicksort(A, 0, len(A)-1)
    print(('Sorted: {}'.format(A)))

if __name__ == '__main__':
    main()
