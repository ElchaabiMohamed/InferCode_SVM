def indiceOccurrence(n,x,l):
    if l==[]:
      cpt=None
    else:
      trouve=False
      cpt=0
      i=0
      while i<len(l) and not trouve:
        if x==l[i] and n!=0:
          n-=1
        if n==0:
          trouve=True
        cpt+=1
        i+=1
      if n!=0:
        cpt=-1
    return cpt