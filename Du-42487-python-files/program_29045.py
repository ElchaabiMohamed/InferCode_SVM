def parition(a, p, r):
  q = j = p

  while j < r:
    if A[j] <= A[r]:
      A[q], A[j] = A[j], A[q]
      q += 1
    j += 1

  A[q], A[r] = A[r], A[q]

def quicksort(a, p, r):
  if r <= p:
    return
  else:
    q = parition(a, p, r)
    quicksort(a, p, q - 1)
    quicksort(a, q + 1, r)

def main():
  quicksort()

if __name__ == "__main__":
  main()
