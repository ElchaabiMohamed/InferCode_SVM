def listeSymetrique(l):
  res=True
  i=0
  j=len(l)-1
  while i<len(l) and j<len(l):
    if l[i]!=l[j]:
      res=False
    i+=1
    j-=1
  return res