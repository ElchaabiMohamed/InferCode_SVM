def suiteGeo(liste):
  i=0
  res=True
  if len(liste)==0:
    res=True
  if len(liste)==[1]:
    res=True
  if len(liste)==[]:
    res=False
  while i<len(liste)-1 and res==True:
    q=liste[i+1]/liste[i]
    if liste[i+1]/liste[i]==q:
      res=True
    else:
      res=False
    i+=1
  return res
