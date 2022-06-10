a = [1, 2, 3, 1, 2, 3]

def increasing_order(a, i):
  p = i
  j = i + 1
  while j < len(a):
    if a[j] < a[p]:
      p = j
    j = j + 1
  return p
