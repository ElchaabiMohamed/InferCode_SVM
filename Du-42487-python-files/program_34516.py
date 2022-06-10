def union(a,b):
  c = []

  i = 0
  while i < len(a):
    c.append(a[i])
    i = i + 1
  
  j = 0
  while j < len(b):
    if b[i] not in a:
      c.append(b[i])
  
  return c

def intersection():
  c = []
  
  while i < len(a):
    if a[i] in b:
      c.append(a[i])
    i = i + 1

  return c
