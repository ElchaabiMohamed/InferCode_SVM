def quatrePlus100(liste):
  res=[]
  i=0
  n=0
  while i<len(liste) and n<4:
    if liste[i]>100:
      res.append(liste[i])
      n=n+1
    i=i+1
  return res