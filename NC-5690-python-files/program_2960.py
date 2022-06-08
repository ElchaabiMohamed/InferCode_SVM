def listeSymetrique(l):
  ok=True
  i=0
  j=-1
  while i<(len(l)/2) and ok :
    if l[i]!=l[j] :
      ok=False
    i+=1
    j-=1
  
  return ok