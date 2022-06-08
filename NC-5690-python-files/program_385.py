def indiceOccurrence(n,x,l):
  cpt=0
  i=0
  while i<len(l) and cpt<n:
    if l[i]==x:
       cpt=cpt+1
    i=i+1
  return [cpt]