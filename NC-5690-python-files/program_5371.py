def suiteGeo(liste):
  i=0
  res=True
  if len(liste)==0:
    res=True
  while i<len(liste)-1 and res==True:
    if liste[i]==0:
      res=False
    if liste[i]!=0:
      q=liste[1]/liste[0]
    if liste[i]!=0:
      if liste[i+1]/liste[i]!=q:
        res=False
    if liste[i] and liste[i+1]==0:
      res=True
    if liste[i]==0 and liste[i+1]==0:
      res=True
    i+=1
  return res