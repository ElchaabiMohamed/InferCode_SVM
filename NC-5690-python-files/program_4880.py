def suiteAri(liste):
  res=0
  i=1
  for i in liste:
    if liste[i]%liste[i+1]==0:
      res=False
    elif liste[i]%liste[i+1]!=liste[i+1]%liste[i+2]:
      res=False
    else:
      res=True
  return res