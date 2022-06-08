def indiceOccurrence(n,x,l):
  trouve=0
  i=0
  while i<len(l) and trouve!=n:
    if x==l[i]:
      trouve=trouve+1
    i=i+1
  i=i-1
  if trouve!=n:
    i=None
  return i
