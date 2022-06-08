def suiteAri(liste):
  res=True
  while i<len(liste) and res:
    if liste[i]%liste[i+1]==0:
      res=False
    elif liste[i+1]%liste[i+2]!=liste[i]%liste[i+1]:
      res=False
    else:
      res=True
  return res