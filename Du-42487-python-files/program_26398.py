def union(a,b):
  c = []

  i = 0
  while i < len(a):
    c.append(a[i])
    i = i + 1
  
  k = 0
  while k < len(b):
    if not (b[k] in a):
      c.append(b[k])
    k = k + 1
  
  return c

def intersection(a,b):
  c = []
  
  while i < len(a):
    if a[i] in b:
      c.append(a[i])
    i = i + 1

  return c
