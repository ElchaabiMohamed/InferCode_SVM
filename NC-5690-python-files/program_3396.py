def suiteGeo(liste):
  i=0
  while i<len(liste)-1 and res==True:
    if liste[0]==0:
      res=False
    else:
      r=liste[1]/liste[0]
      if liste[i+1]/liste[i]==r:
        res=True
      else:
        res=False
    i+=1
  return res