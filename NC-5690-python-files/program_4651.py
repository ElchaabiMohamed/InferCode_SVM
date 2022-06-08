def suiteGeo(liste):
  i=0
  res=True
  while i<len(liste)-1 and res==True:
    if liste[i]==0:
      res=False
    q=liste[i+1]/liste[i]
    if liste[i+1]/liste[i]==q:
      res=True
    else:
      res=False
    i+=1
  return res
