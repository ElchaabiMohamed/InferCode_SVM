def suiteGeo(liste):
  i=0
  c=True
  if liste[0]==0:
    c=False
  while i<(len(liste)-2) and c:
    if liste[i]!=0 and liste[i+1]!=0:
      if liste[i+2]/liste[i+1]!=liste[i+1]/liste[i]:
        c=False
    i=i+1
  return c