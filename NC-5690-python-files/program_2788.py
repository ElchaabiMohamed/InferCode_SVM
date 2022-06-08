def indiceOccurrence(n,x,l):
    cpt=0
    res=0
    i=0
    while i<len(l) and cpt<n:
      if l[i]==x:
        cpt+=1
      i+=1
    if cpt==n:
      res=i-1
    else:
      res=None
    return res
        