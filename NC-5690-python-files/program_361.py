def indiceOccurrence(n,x,l):
  i=0
  j=0
  res = -1
  while j <n and i < len(l):
    if l[i] == x:
      j+=1
      if j == n:
        res = i
    i+=1
    if res == -1: res = None
  return(res)