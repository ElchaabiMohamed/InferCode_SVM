def quatrePlus100(liste):
  i=0
  res=[]
  while i<len(liste) and i<6:
    if liste[i]>100:
      res.append(liste[i])
    i=i+1
  return res
