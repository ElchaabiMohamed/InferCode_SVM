#swap elements at positions i and j in list a
def swap(a,i,j):
  tmp = a[i]
  a[i] = a[j]
  a[j] = tmp
  return a

def reverse(a):
  i = 0
  j = len(a)-1
  while i < j:
    swap(a,i,j)
    i = i + 1
    j = j - 1
  return a
