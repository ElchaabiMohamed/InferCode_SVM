def suiteGeo(liste):
  i=0
  res=True
  if liste[0]==0:
    res=False
  while i<len(liste)-1 and res==True:
    r=liste[0]/liste[1]
    if liste[i]/liste[i+1]==r:
      res=True
    else:
      res=False
    i+=1
  return res
  