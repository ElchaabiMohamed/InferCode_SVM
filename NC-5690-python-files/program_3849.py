def suiteAri(liste):
  i=0
  res=True
  while i<len(liste)-1 and res==True:
    r=liste[1]-liste[0]
    if liste[i+1]-liste[i]==r:
      res=True
    else:
      res=False
    i+=1
  return res