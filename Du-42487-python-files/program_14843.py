def swap(a, i, j):
  for k in a:
    a[i], a[j] = a[j], a[i]
  return a

def reverse(a):
  return [i for i in range(len(a), 0, -1)] 

