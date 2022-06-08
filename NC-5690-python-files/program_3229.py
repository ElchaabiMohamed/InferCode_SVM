def indiceOccurrence(n,x,l):
    if l==[] or x not in l:
      cpt=None
    else:
      trouve=False
      cpt=-1
      i=0
      while i<len(l) and not trouve:
        if x==l[i] and n!=0:
          n-=1
        if n==0:
          trouve=True
        cpt+=1
        i+=1
      if n!=0:
        cpt=None
    return cpt