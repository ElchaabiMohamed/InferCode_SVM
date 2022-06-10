def union(a,b):
  i = 0 
  dic = {}
  while i < len(a):
    dic[a[i]] = True 
    i = i + 1

    j = 0 
    while j < len(b):
      if not (b[j] in dic):
        dic[b[j]] = True 
      j = j + 1

  return dic  
     
def intersection(a,b):
  seen = {}

  i= 0
  while i < len(a):
    if a[i] in b and not (a[i] in seen):
      seen[a[i]] = True
    i = i + 1
  return seen




