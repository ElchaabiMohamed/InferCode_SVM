def suiteGeo(liste):
  i=0
  res=True
  while i<len(liste) and res==True:
    if liste[i]!=0:
      listetest=[liste[0]]
      q=liste[1]/liste[0]
      u=liste[0]*q**i
      listetest=listetest+u
    else:
      res=False
    if liste[i]==listetest[i]:
      res=True
    else:
      res=False
  return res