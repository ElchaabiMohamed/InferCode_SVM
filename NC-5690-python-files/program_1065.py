def suiteGeo(liste):
  i=0
  res=True
  if len(liste)==0:
    res=True
  while i<len(liste)-1 and res==True:
    if liste[i]==0:
      res=True
    if liste[i]!=0:
      q=liste[1]/liste[0]
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q:
        res=False
    i+=1
  return res
