def suiteGeo(liste):
  i=0
  res=True
  listetest=[]
  while i<len(liste) and res==True:
    if liste[i]!=0 and len(liste)>=2:
      listetest=[liste[0]]
      q=liste[1]/liste[0]
      u=liste[0]*q**i
      listetest.append(u)
      if liste[i]==listetest[i]:
        res=True
      else:
        res=False
    else:
      res=False
    i=i+1
  return res