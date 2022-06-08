def indiceOccurrence(n,x,l):
  i=0
  j=0
  res = -1
  while j <3 and i < len(l):
    if l[i] == x:
      j+=1
      if j == 3:
        res = l[i+1]
    i+=1
    if res == -1: res = None
  return(res)