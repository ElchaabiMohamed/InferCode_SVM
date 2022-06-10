a = []

def reverse(a):
  i = len(a) -1 
  b = []
  while i >= 0:
    b.append(a[i])
    i -= 1
  return b
