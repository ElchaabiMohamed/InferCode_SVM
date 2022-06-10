def union(a,b):
  seen = {}

  i = 0
  while i < len(a):
    seen[a[i]] = True
    i = i + 1

  j = 0
  while j < len(b):
    if not (b[j] in seen):
      seen[b[j]] = True
    j = j + 1

    return seen

def intersection(a, b):
  seen = {}

  i = 0
  while i < len(a):
    if a[i] in b and not (a[i] in seen):
      seen[a[i]] = True
    i = i + 1

  return seen 
      
      
