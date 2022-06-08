def listeSymetrique(l):
  res=True
  i=0
  j=-1
  while i<len(l) and j<len(l) and res==True:
    if l[i]==l[j]:
      i=i+1
      j=j-1
    else:
      res=False
  return res