def indiceOccurrence(n,x,l):
  
  while i<len(l) and i<n:
    if x==l[i]:
      n=n+1
    i=i+1
  return i