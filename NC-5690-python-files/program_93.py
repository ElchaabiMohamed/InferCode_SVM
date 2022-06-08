def listeSymetrique(l):
  trouve=True
  i=0
  j=len(l)-1
  while i<len(l) and j<len(l) and trouve:
    if l[i]!=l[j]:
      trouve=False
    i+=1
    j-=1
  return trouve