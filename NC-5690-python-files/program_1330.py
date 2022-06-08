def produitScalaire(vec1,vec2):
  i=0
  ok=True
  res=False
  while i<len(mot)/2 and ok:
    if mot[i]!=mot[-i-1]:
      ok=False
    i+=1
  if ok: 
    res=True
  return res