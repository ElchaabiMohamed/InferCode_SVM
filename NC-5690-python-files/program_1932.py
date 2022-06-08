def indiceOccurrence(n,x,l):
  prec=0
  res=0
  i=0
  while i<len(l) and prec<n:
    if l[i]==x:
      prec=prec+1
    i=i+1
    if prec==n:
      return i
    if prec<n:
      return none