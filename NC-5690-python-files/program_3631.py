def suiteAri(liste):
  res=True
  i=0
  while i<len(liste)-1 and res==True:
    r=liste[0]-liste[1]
    if liste[i]-liste[i+1]==r:
      res=True
    else:
      res=False
  return res